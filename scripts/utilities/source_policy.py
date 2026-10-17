"""
Failure policy and orphan cleanup shared by the MLX, HIG and Swift scrapers.

They get the same protection as the Apple scraper: a page that was removed
upstream (404/410, or no longer linked or listed) is removed automatically,
while our own failed requests never delete live docs.

- A configured root, directory or file that returns 404/410 keeps every file
  under its output location for that run (source_gone_pending; not an error,
  the scraper's other cleanup still runs). On SOURCE_GONE_RUNS consecutive
  runs it is a removal (source_gone): nothing under it is expected any more,
  so the normal cleanup deletes its files and its keys are pruned.
- Any other failure of a configured root, directory or file keeps every file
  under its output location and its keys, every run until it recovers
  (source_fetch_failed, exit 1). It never reaches D8: only 404/410 x2
  removes a configured source. A directory found by a listing that we have
  files under follows the same rule (directory_fetch_failed), except that
  its 404/410 is a removal at once; one we have no files under (new this
  run) has nothing to keep, so its failure follows the never-good page rule
  below (a file moved into it would otherwise be orphaned).
- A 404/410 on any other page (a HIG or Sphinx page, a file found by a
  directory listing) is a removal at once; it never blocks.
- Any other failure (5xx, 403, timeout, challenge) on a previously good page
  keeps its file and blocks the scraper's cleanup. On the
  PERSISTENT_FAILURE_RUNS-th consecutive failed run (D8) it stops blocking
  and the page is treated as removed (persistent_fetch_failure, exit 1). A
  page is previously good when its key is in the hash file or its file is
  on disk under exactly its name (has_file_named): a hash file that was lost
  or couldn't be read loses keys, not files.
- A transient failure (5xx, 429, timeout, network, challenge) on a page we
  never had blocks too (a page moved under a new parent would otherwise be
  orphaned by our own failed request), lifted the same way. A 4xx on such a
  page doesn't block.
- A page that fails to convert or save keeps its file and blocks, until the
  PERSISTENT_FAILURE_RUNS-th run in a row (persistent_local_error, exit 1).
  A local error never deletes anything.
- Orphans go through confirm-then-delete, per scanned dir: when a dir's
  orphans are at least half of its .md files, or more than
  VALVE_MAX_ORPHANS, nothing of them is deleted that run; they wait in
  metadata.pending_orphans, and the next clean run deletes the ones it finds
  orphaned again (the rest wait only if they trip the valve themselves). A
  run that keeps their location (its source or directory failed) leaves
  them waiting.
- A file is expected when a page of this run names it exactly, else in any
  casing (as the Apple scraper matches recorded paths): on a case-sensitive
  filesystem a file renamed upstream in casing only leaves the old-cased
  file an orphan.

The counters live in the hash file's metadata.failure_counts,
{key: {"gone": n, "fail": n, "local": n}} with an entry only while a count is
above 0 (MLX/Swift hash values are bare digests that can't carry fields),
next to metadata.pending_orphans (only while non-empty). A gone or fail count
belongs to consecutive runs that meet the key: a key not met this run loses
it, also when its location was kept this run (its source or directory
failed, so the key wasn't fetched), as the Apple scraper ends a URL's
consecutive_failures on any run that doesn't fetch it, a failed root's
included. So D8 needs PERSISTENT_FAILURE_RUNS failed fetches in a row. A
location this run keeps carries its files, its hash keys and its
pending_orphans entries, not its counts. A local count ends only when the
page saves (as the Apple scraper's consecutive_local_errors) or goes: a run
that doesn't reach the page leaves it as it is, and a run whose cleanup ran
and that saves no hash key for the page (its file deleted, its key pruned)
drops it, unless the page failed locally again in that run or its location
was kept.
"""

import asyncio
import json
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import (
    Any,
    Awaitable,
    Callable,
    Container,
    Dict,
    Final,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)

import aiohttp

logger = logging.getLogger(__name__)

# A configured root, directory or file that returns 404/410 on this many
# consecutive runs is removed (source_gone)
SOURCE_GONE_RUNS: Final = 2
# A page that fails (fetch or local error) on this many consecutive runs
# stops blocking cleanup (D8 for a fetch failure on a page we had)
PERSISTENT_FAILURE_RUNS: Final = 3
# The mass-removal valve, as for Apple frameworks (scraper/utils/hash_manager.py
# valve_trips): more orphans than this in one scanned dir, or at least half
# of its .md files, are confirmed on the next clean run first
VALVE_MAX_ORPHANS: Final = 1000

GONE_STATUSES: Final = frozenset({404, 410})

# Retry transient failures (502s are common on api.github.com)
MAX_ATTEMPTS = 4
RETRY_BASE_DELAY = 2.0  # seconds; doubles per retry
RETRY_AFTER_CAP = 120.0  # seconds; upper bound on honoring a server Retry-After
RETRYABLE_STATUSES = frozenset({429, 500, 502, 503, 504})

GITHUB_RAW = "https://raw.githubusercontent.com"
GITHUB_API = "https://api.github.com"

# Hash-file metadata keys this policy owns (scrapers may add their own, e.g. MLX's sources)
FAILURE_COUNTS_KEY: Final = "failure_counts"
PENDING_ORPHANS_KEY: Final = "pending_orphans"
COUNT_FIELDS: Final = ("gone", "fail", "local")


# =============================================================================
# FETCHING
# =============================================================================

@dataclass(frozen=True)
class FetchFailed:
    """A fetch that produced no usable response, after all retries.

    Attributes:
        status: HTTP status of the last response, or None if none arrived
            (timeout, connection or other network error)
        error: What failed, for logs
        transient: True for a failure of ours or a server's that a later run
            may not repeat (5xx, a 429 that outlasted its retries, a network
            error, a timeout, a challenge, an unusable body); False for any
            other 4xx
    """

    status: Optional[int]
    error: str
    transient: bool

    @property
    def gone(self) -> bool:
        """The server says the resource was removed (404/410)."""
        return self.status in GONE_STATUSES


def status_failure(status: int) -> FetchFailed:
    """The failure for a final non-2xx HTTP status."""
    return FetchFailed(status=status, error=f"HTTP {status}", transient=status >= 500 or status == 429)


# One request: (status, Retry-After header or None, body text)
Attempt = Callable[[], Awaitable[Tuple[int, Optional[str], str]]]


async def fetch_with_retry(
    attempt: Attempt,
    url: str,
    network_errors: Tuple[Type[BaseException], ...],
) -> Union[str, FetchFailed]:
    """Run a request, retrying transient failures (5xx/429/network errors) with backoff.

    Args:
        attempt: Makes one request
        url: For logs
        network_errors: Exceptions attempt raises for a request that got no
            usable response; each is retried

    Returns:
        The body on a 2xx; FetchFailed for any other final status (404 and
        other 4xx are not retried) or once MAX_ATTEMPTS are used up
    """
    last: Optional[FetchFailed] = None
    retry_after: Optional[float] = None
    for attempt_number in range(MAX_ATTEMPTS):
        if attempt_number:
            delay = RETRY_BASE_DELAY * (2 ** (attempt_number - 1))
            if retry_after is not None:
                # Rate-limit responses say how long to wait; honor that (capped)
                delay = max(delay, min(retry_after, RETRY_AFTER_CAP))
            logger.warning(
                f"Retrying {url} in {delay:.0f}s "
                f"(attempt {attempt_number + 1}/{MAX_ATTEMPTS}): {last.error if last else ''}"
            )
            await asyncio.sleep(delay)
        retry_after = None
        try:
            status, retry_after_header, body = await attempt()
        except network_errors as e:
            last = FetchFailed(status=None, error=f"{type(e).__name__}: {e}", transient=True)
            continue
        if 200 <= status < 300:
            return body
        if status in RETRYABLE_STATUSES:
            if retry_after_header and retry_after_header.isdigit():
                retry_after = float(retry_after_header)
            last = status_failure(status)
            continue
        return status_failure(status)
    assert last is not None  # the loop only falls through after a failure
    logger.warning(f"Giving up on {url} after {MAX_ATTEMPTS} attempts: {last.error}")
    return last


async def http_get(
    session: aiohttp.ClientSession,
    url: str,
    headers: Optional[Mapping[str, str]] = None,
    timeout: Optional[aiohttp.ClientTimeout] = None,
) -> Union[str, FetchFailed]:
    """GET a URL with aiohttp, retrying transient failures (fetch_with_retry)."""

    async def attempt() -> Tuple[int, Optional[str], str]:
        kwargs: Dict[str, Any] = {"headers": headers}
        if timeout is not None:
            kwargs["timeout"] = timeout
        async with session.get(url, **kwargs) as response:
            body = await response.text() if 200 <= response.status < 300 else ""
            return response.status, response.headers.get("Retry-After"), body

    return await fetch_with_retry(attempt, url, (aiohttp.ClientError, asyncio.TimeoutError, UnicodeDecodeError))


def github_api_headers() -> Dict[str, str]:
    """Headers for the GitHub contents API, with GITHUB_TOKEN when set (higher rate limits)."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"
    return headers


async def fetch_github_raw(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str,
    timeout: Optional[aiohttp.ClientTimeout] = None,
) -> Union[str, FetchFailed]:
    """Fetch a file's raw content from GitHub."""
    return await http_get(session, f"{GITHUB_RAW}/{repo}/{branch}/{path}", timeout=timeout)


async def list_github_directory(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str,
    timeout: Optional[aiohttp.ClientTimeout] = None,
) -> Union[List[Dict[str, Any]], FetchFailed]:
    """A directory's entries from the GitHub contents API.

    A body that isn't a JSON list (e.g. the path is a file) is a transient
    failure, never an empty directory: an empty listing would make every
    local file under it an orphan.
    """
    url = f"{GITHUB_API}/repos/{repo}/contents/{path}?ref={branch}"
    body = await http_get(session, url, headers=github_api_headers(), timeout=timeout)
    if isinstance(body, FetchFailed):
        return body
    try:
        data = json.loads(body)
    except ValueError:
        return FetchFailed(status=200, error=f"invalid JSON from {url}", transient=True)
    if not isinstance(data, list):
        return FetchFailed(status=200, error=f"unexpected GitHub API response for {url}: expected a list",
                           transient=True)
    return [item for item in data if isinstance(item, dict)]


async def discover_github_markdown(
    session: aiohttp.ClientSession,
    repo: str,
    branch: str,
    path: str,
    recursive: bool = True,
    skip_dir_suffixes: Tuple[str, ...] = (),
    delay: float = 0.0,
    timeout: Optional[aiohttp.ClientTimeout] = None,
) -> Tuple[List[str], Dict[str, FetchFailed]]:
    """Every markdown file under a GitHub directory, and the listings that failed.

    Args:
        path: The directory (repo-relative)
        recursive: Also list subdirectories (in parallel)
        skip_dir_suffixes: Subdirectory names ending like this are skipped
            (e.g. Xcode bundles, which can't contain docs)
        delay: Seconds to wait after each listing (rate limiting)

    Returns:
        (repo-relative paths of the .md files found, {directory: failure} for
        every listing that failed; a failed directory contributes no files)
    """
    listing = await list_github_directory(session, repo, branch, path, timeout=timeout)
    if delay:
        await asyncio.sleep(delay)
    if isinstance(listing, FetchFailed):
        return [], {path: listing}

    files: List[str] = []
    subdirs: List[str] = []
    for item in listing:
        item_path = item.get("path")
        name = str(item.get("name", ""))
        if not isinstance(item_path, str):
            continue
        if item.get("type") == "file" and name.endswith(".md"):
            files.append(item_path)
        elif item.get("type") == "dir" and recursive and not name.endswith(skip_dir_suffixes):
            subdirs.append(item_path)

    failures: Dict[str, FetchFailed] = {}
    if subdirs:
        results = await asyncio.gather(*(
            discover_github_markdown(session, repo, branch, subdir, True, skip_dir_suffixes, delay, timeout)
            for subdir in subdirs
        ))
        for sub_files, sub_failures in results:
            files.extend(sub_files)
            failures.update(sub_failures)
    return files, failures


# =============================================================================
# FAILURE COUNTERS
# =============================================================================

class FailureCounts:
    """Per-key run counters: the hash file's metadata.failure_counts.

    gone: consecutive runs a configured root/directory/file returned 404/410;
    fail: consecutive runs a page's fetch failed (not 404/410);
    local: runs a page failed to convert or save since it last saved (a run
    that doesn't reach the page neither counts nor ends it).
    Each moves at most once per key per run.
    """

    def __init__(self, stored: Any) -> None:
        self._stored: Dict[str, Dict[str, int]] = {}
        if isinstance(stored, dict):
            for key, entry in stored.items():
                if not isinstance(key, str) or not isinstance(entry, dict):
                    continue
                counts = {
                    name: value for name, value in entry.items()
                    if name in COUNT_FIELDS and isinstance(value, int) and not isinstance(value, bool) and value > 0
                }
                if counts:
                    self._stored[key] = counts
        self._current: Dict[str, Dict[str, int]] = {}
        self._bumped: Set[Tuple[str, str]] = set()

    def get(self, key: str, name: str) -> int:
        """A key's count, as of now in this run."""
        entry = self._current[key] if key in self._current else self._stored.get(key, {})
        return entry.get(name, 0)

    def _entry(self, key: str) -> Dict[str, int]:
        if key not in self._current:
            self._current[key] = dict(self._stored.get(key, {}))
        return self._current[key]

    def touch(self, key: str) -> None:
        """The key was met this run: keep its counts as they are."""
        self._entry(key)

    def bump(self, key: str, name: str, cap: Optional[int] = None) -> int:
        """Count this run for a key (once per run) and return the new count."""
        entry = self._entry(key)
        if (key, name) not in self._bumped:
            self._bumped.add((key, name))
            count = entry.get(name, 0) + 1
            entry[name] = min(count, cap) if cap is not None else count
        return entry[name]

    def reset(self, key: str, *names: str) -> None:
        """Restart a key's counts (the key was met this run)."""
        entry = self._entry(key)
        for name in names:
            entry.pop(name, None)

    def to_metadata(self, kept: Callable[[str], bool], present: Callable[[str], bool]) -> Dict[str, Dict[str, int]]:
        """The counts to save, only those above 0.

        A key met this run keeps its counts as they now are. A stored key not
        met keeps only its local count: fail and gone count consecutive runs
        that met the key, so a run that didn't meet it ends them, also when
        kept() says its location was kept this run (as the Apple scraper's
        consecutive_failures, which a run that never fetched the URL ends),
        while a local error ends only when the page saves. A local count goes
        with its page: it is dropped when present() says the page is gone,
        unless the page failed to convert or save this run, or kept() says
        its location (and so its file) was kept this run.
        """
        merged: Dict[str, Dict[str, int]] = {
            key: {"local": entry["local"]}
            for key, entry in self._stored.items()
            if key not in self._current and "local" in entry
        }
        merged.update(self._current)
        result: Dict[str, Dict[str, int]] = {}
        for key in sorted(merged):
            entry = merged[key]
            if ("local" in entry and (key, "local") not in self._bumped
                    and not kept(key) and not present(key)):
                entry = {name: value for name, value in entry.items() if name != "local"}
            counts = {name: entry[name] for name in COUNT_FIELDS if entry.get(name, 0) > 0}
            if counts:
                result[key] = counts
        return result


# =============================================================================
# THE RUN
# =============================================================================

def valve_trips(orphans: int, files: int) -> bool:
    """Whether a scanned dir's orphans are a mass removal, held for confirmation.

    The same rule as the Apple scraper's (scraper/utils/hash_manager.py
    valve_trips): at least half of the dir's .md files, or more than
    VALVE_MAX_ORPHANS.
    """
    return orphans > 0 and (orphans * 2 >= files or orphans > VALVE_MAX_ORPHANS)


def unmatched(existing: Iterable[str], expected: Iterable[str]) -> Set[str]:
    """The existing paths that no expected path names.

    The same rule as the Apple scraper's (scraper/utils/hash_manager.py
    HashManager._unrecorded): an expected path names its file exactly, else
    in any casing. On a case-insensitive filesystem (macOS) a page written
    under a new casing lands in the old file, which keeps its name, so only
    another casing names it; on a case-sensitive one (CI) the old-cased file
    is a separate, stale file, and the exact match leaves it an orphan. A
    path that matches only other casings, of several files, keeps all of them.
    """
    existing_paths = set(existing)
    by_lower: Dict[str, List[str]] = {}
    for path in existing_paths:
        by_lower.setdefault(path.lower(), []).append(path)
    named: Set[str] = set()
    for path in expected:
        if path in existing_paths:
            named.add(path)
        else:
            named.update(by_lower.get(path.lower(), ()))
    return existing_paths - named


def _folded_parts(path: Path) -> Tuple[str, ...]:
    return tuple(part.lower() for part in path.parts)


def is_under(path: Path, parent: Path) -> bool:
    """path is parent or inside it (case-insensitively, like the other path checks)."""
    path_parts, parent_parts = _folded_parts(path), _folded_parts(parent)
    return path_parts[:len(parent_parts)] == parent_parts


def has_file_named(path: Path) -> bool:
    """A file exists under exactly this name.

    Unlike Path.exists(): on a case-insensitive filesystem (macOS) that also
    answers for a file whose name differs only in casing, which is another
    page's (e.g. an MLX case twin's), while CI's filesystem tells them apart.
    The scrapers write every page under exactly its computed name.
    """
    try:
        return path.is_file() and path.name in os.listdir(path.parent)
    except OSError:
        return False


@dataclass(frozen=True)
class KeptLocation:
    """Files a run keeps whatever the cleanup finds: every .md under path,
    except under excluded (other sources' own dirs nested in it).

    Attributes:
        path: The location (a source's output dir, or a directory in it)
        reason: Why it is kept, for the summary
        excluded: Dirs under path that belong to other sources
    """

    path: Path
    reason: str
    excluded: Tuple[Path, ...] = ()

    def holds(self, file: Path) -> bool:
        return is_under(file, self.path) and not any(is_under(file, excluded) for excluded in self.excluded)


@dataclass
class CleanupResult:
    """What a scraper's orphan cleanup did.

    Attributes:
        skipped: The cleanup was blocked by a failure of ours (nothing deleted,
            pending_orphans untouched)
        deleted: Files deleted (or, in a dry run, that would be), relative to
            the output base
        confirmed: Of those, files an earlier clean run held in pending_orphans
        held: Scanned dir -> (orphans the valve holds this run, the dir's .md
            files once the confirmed ones are gone)
        failures: Deletions that failed
    """

    skipped: bool = False
    deleted: List[str] = field(default_factory=list)
    confirmed: int = 0
    held: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    failures: List[str] = field(default_factory=list)


class ScrapeRun:
    """One scraper run's failures, kept files and orphan cleanup.

    The scraper reports every key it meets (a page, a configured source, a
    listed directory) through the methods below; each one applies the rule
    in the module docstring, logs it under its event name, and records what
    must be kept, what blocks the cleanup and what makes the run exit 1.
    Paths are compared relative to output_base: an expected file exactly,
    else in any casing (unmatched); a kept location and pending_orphans in
    any casing.
    """

    def __init__(
        self,
        scraper: str,
        output_base: Path,
        metadata: Mapping[str, Any],
        load_error: Optional[str] = None,
    ) -> None:
        """
        Args:
            scraper: Name for logs and the summary (e.g. "MLX")
            output_base: The docs root every path is relative to (documentation/)
            metadata: The hash file's metadata, as loaded
            load_error: Why the hash file couldn't be loaded, if it couldn't:
                every key then looks new, so this run's cleanup is blocked
                (hash_load_failed, exit 1); the run's save replaces the file
        """
        self.scraper = scraper
        self.output_base = output_base
        self.load_error = load_error
        self.counts = FailureCounts(metadata.get(FAILURE_COUNTS_KEY))
        self.pending_orphans = self._stored_pending(metadata.get(PENDING_ORPHANS_KEY))
        self.blocks: Dict[str, List[str]] = {}
        self.errors: List[str] = []
        self.kept: List[KeptLocation] = []
        self.kept_key_prefixes: List[str] = []
        self.produced: Set[str] = set()
        self._expected: Set[str] = set()
        if load_error is not None:
            logger.error(f"hash_load_failed: {scraper}: {load_error}; cleanup blocked this run, "
                         "the file is replaced by this run's save")
            self._block("hash_load_failed", load_error)

    def _stored_pending(self, stored: Any) -> List[str]:
        if stored is None:
            return []
        if not isinstance(stored, list) or not all(isinstance(path, str) for path in stored):
            logger.warning(f"{self.scraper}: ignoring malformed {PENDING_ORPHANS_KEY} in the hash file")
            return []
        return list(stored)

    # -- bookkeeping --------------------------------------------------------

    def rel(self, path: Path) -> str:
        """path relative to the output base, as stored (posix)."""
        try:
            return path.relative_to(self.output_base).as_posix()
        except ValueError:
            return path.as_posix()

    def expect(self, path: Path) -> None:
        """Keep this file: it was produced (or protected) this run."""
        self._expected.add(self.rel(path))

    def is_expected(self, path: Path) -> bool:
        """This run produced or protects exactly this path (the cleanup also
        lets it name a file in another casing when no file has its exact name)."""
        return self.rel(path) in self._expected

    def keep_file(self, key: str, path: Path) -> None:
        """Keep a page's file and its key this run."""
        self.produced.add(key)
        self.expect(path)

    def keep_location(self, location: KeptLocation, key_prefix: Optional[str] = None) -> None:
        """Keep every file under a location this run, and the keys that start
        with key_prefix (with their local counts; their fail and gone counts
        end, since this run doesn't fetch them)."""
        self.kept.append(location)
        if key_prefix is not None:
            self.kept_key_prefixes.append(key_prefix)

    def is_kept(self, path: Path) -> bool:
        return any(location.holds(path) for location in self.kept)

    @staticmethod
    def _holds_files(location: KeptLocation) -> bool:
        """There is a .md file on disk that the location holds."""
        if not location.path.is_dir():
            return False
        return any(path.is_file() and location.holds(path) for path in location.path.rglob("*.md"))

    def keeps_key(self, key: str) -> bool:
        """The key belongs to a location this run keeps."""
        return any(key.startswith(prefix) for prefix in self.kept_key_prefixes)

    def _block(self, reason: str, detail: str) -> None:
        self.blocks.setdefault(reason, []).append(detail)

    @property
    def blocked(self) -> bool:
        """This run's cleanup is blocked by a failure of ours."""
        return bool(self.blocks)

    def exit_code(self) -> int:
        """0 for a clean run; 1 if a failure of ours blocked the cleanup or
        anything else of ours failed (removals and valve holds are not errors)."""
        return 1 if self.blocks or self.errors else 0

    # -- outcomes -----------------------------------------------------------

    def page_ok(self, key: str, path: Path) -> None:
        """A page (or file) loaded: keep it; its fetch count restarts."""
        self.counts.reset(key, "fail", "gone")
        self.keep_file(key, path)

    def page_saved(self, key: str) -> None:
        """The page's file now matches its content (written, or unchanged)."""
        self.counts.reset(key, "local")

    def source_ok(self, key: str) -> None:
        """A configured root or directory answered: its counts restart (a
        configured file that loads restarts them through page_ok)."""
        self.counts.reset(key, "gone", "fail")

    def page_failed(self, key: str, failure: FetchFailed, previously_good: bool) -> bool:
        """A page's fetch failed (after retries).

        Args:
            key: The page's hash key
            failure: The failure
            previously_good: We have the page: its key is in the hash file,
                or its file is on disk under exactly its name
                (has_file_named; a lost or unreadable hash file, whose
                replacement holds only the pages fetched that run, loses
                keys, not files)

        Returns:
            True if the page's file is kept this run (the caller then calls
            keep_file with its path); False if it is treated as removed
        """
        if failure.gone:
            self.counts.reset(key, "fail")
            logger.info(f"page_gone: {key} returned {failure.status}; removed")
            return False
        return self._fetch_failed(key, failure, previously_good, event="page", what="page")

    def _fetch_failed(self, key: str, failure: FetchFailed, previously_good: bool, event: str, what: str) -> bool:
        """The page rule for a failure other than 404/410.

        Args:
            event: Prefix of the log events (page, new_directory)
            what: What failed, for the log text

        Returns:
            True if the file is kept this run
        """
        if not previously_good and not failure.transient:
            self.counts.reset(key, "fail")
            logger.info(f"{event}_failed_never_good: {key}: {failure.error} "
                        f"(not blocking: a 4xx on a {what} we never had)")
            return False
        runs = self.counts.bump(key, "fail")
        if runs < PERSISTENT_FAILURE_RUNS:
            logger.warning(f"{event}_fetch_failed: {key}: {failure.error} (run {runs} of {PERSISTENT_FAILURE_RUNS}); "
                           f"{self.scraper} cleanup blocked this run")
            self._block("fetch_failed", f"{key}: {failure.error} (run {runs})")
            return previously_good
        logger.error(f"persistent_fetch_failure: {key}: {failure.error} on {runs} consecutive runs; no longer "
                     "blocking cleanup" + ("; treated as removed" if previously_good else ""))
        self.errors.append(f"persistent_fetch_failure: {key} ({failure.error}, {runs} runs)")
        return False

    def configured_file_failed(self, key: str, failure: FetchFailed, path: Path) -> bool:
        """A configured file's fetch failed. It is a source, like a configured
        root or directory (it may be all its source has), so it follows
        source_failed and never reaches D8: 404/410 keeps its file at run 1
        (source_gone_pending) and removes it at SOURCE_GONE_RUNS
        (source_gone); anything else keeps its file and key every run until
        it recovers (source_fetch_failed, exit 1).

        Args:
            path: Its output file

        Returns:
            True if its file is kept this run (the caller calls keep_file)
        """
        return self.source_failed(key, failure, KeptLocation(path, reason=""), key_prefix=None)

    def source_failed(
        self,
        key: str,
        failure: FetchFailed,
        location: KeptLocation,
        key_prefix: Optional[str],
    ) -> bool:
        """A configured root, directory or file failed: nothing of it was found this run.

        404/410: at run 1 (of SOURCE_GONE_RUNS) every file under location
        and the keys starting with key_prefix are kept (source_gone_pending);
        at SOURCE_GONE_RUNS it is a removal (source_gone). Anything else:
        everything under it is kept, every run until it recovers
        (source_fetch_failed, exit 1). Neither blocks the rest of the cleanup.

        Returns:
            True if its files are kept this run
        """
        if failure.gone:
            runs = self.counts.bump(key, "gone", cap=SOURCE_GONE_RUNS)
            if runs < SOURCE_GONE_RUNS:
                logger.warning(f"source_gone_pending: {key} returned {failure.status} "
                               f"(run {runs} of {SOURCE_GONE_RUNS}); keeping {self.rel(location.path)} this run")
                self.keep_location(KeptLocation(location.path, "source_gone_pending", location.excluded), key_prefix)
                return True
            logger.warning(f"source_gone: {key} returned {failure.status} on {runs} consecutive runs; "
                           f"removing {self.rel(location.path)}")
            return False
        self.counts.touch(key)
        logger.error(f"source_fetch_failed: {key}: {failure.error}; keeping {self.rel(location.path)} "
                     "until it recovers")
        self.errors.append(f"source_fetch_failed: {key} ({failure.error})")
        self.keep_location(KeptLocation(location.path, "source_fetch_failed", location.excluded), key_prefix)
        return True

    def directory_failed(
        self,
        key: str,
        failure: FetchFailed,
        location: KeptLocation,
        key_prefix: Optional[str],
    ) -> bool:
        """A directory found by a listing failed to list.

        404/410 is a removal at once. Anything else keeps everything under
        it (directory_fetch_failed, exit 1), like a configured directory,
        when we have files under it. When we have none (a directory new this
        run), keeping it protects nothing, while a file moved into it from
        elsewhere would be orphaned by our own failed request: the failure
        follows the never-good page rule instead (a transient one blocks the
        cleanup, counted on key and lifted at PERSISTENT_FAILURE_RUNS; any
        other 4xx doesn't block). Whether we have files is read from the disk,
        not the hash keys: an unreadable hash file loads empty, and its files
        must still be kept.

        Returns:
            True if its files are kept this run
        """
        if failure.gone:
            logger.info(f"directory_gone: {key} returned {failure.status}; removed")
            return False
        if not self._holds_files(location):
            return self._fetch_failed(key, failure, previously_good=False, event="new_directory", what="directory")
        logger.error(f"directory_fetch_failed: {key}: {failure.error}; keeping {self.rel(location.path)} "
                     "until it recovers")
        self.errors.append(f"directory_fetch_failed: {key} ({failure.error})")
        self.keep_location(KeptLocation(location.path, "directory_fetch_failed", location.excluded), key_prefix)
        return True

    def local_error(self, key: str, path: Path, error: str) -> None:
        """A page failed to convert or save: its file (if any) is kept, never
        deleted; it blocks cleanup until PERSISTENT_FAILURE_RUNS runs in a row."""
        self.keep_file(key, path)
        runs = self.counts.bump(key, "local")
        if runs < PERSISTENT_FAILURE_RUNS:
            logger.warning(f"page_local_error: {key}: {error} (run {runs} of {PERSISTENT_FAILURE_RUNS}); "
                           f"{self.scraper} cleanup blocked this run")
            self._block("local_error", f"{key}: {error} (run {runs})")
            return
        logger.error(f"persistent_local_error: {key}: {error} on {runs} consecutive runs; no longer blocking "
                     "cleanup, its file is kept")
        self.errors.append(f"persistent_local_error: {key} ({error}, {runs} runs)")

    def unprocessed(self, key: str, path: Optional[Path], error: str) -> None:
        """A page loaded but raised before its links were read: its file (if
        its path is safe) is kept and the cleanup blocked, uncounted (lifting
        the block would orphan the page's live children)."""
        self.produced.add(key)
        if path is not None:
            self.expect(path)
        self.counts.touch(key)
        logger.error(f"page_processing_failed: {key}: {error}; {self.scraper} cleanup blocked this run")
        self._block("processing_failed", f"{key}: {error}")

    def error(self, message: str) -> None:
        """Any other error of ours this run (exit 1)."""
        logger.error(message)
        self.errors.append(message)

    # -- cleanup ------------------------------------------------------------

    def cleanup(
        self,
        scan_dirs: Iterable[Path],
        removable_dirs: Iterable[Path] = (),
        dry_run: bool = False,
    ) -> CleanupResult:
        """Delete this run's orphans, with confirm-then-delete per scanned dir.

        An orphan is a .md file under a scanned dir that this run neither
        produced nor keeps. Each file is weighed in the deepest scanned dir
        that holds it. Every change to pending_orphans is kept on the run
        (written by the caller's save); a blocked run deletes nothing and
        leaves pending_orphans untouched, and an entry under a location this
        run keeps (not scraped this run) is carried unchanged.

        Args:
            scan_dirs: The dirs to clean
            removable_dirs: Scanned dirs that are themselves removed once
                empty (a dropped source's own dir); the others keep their
                root and lose only the empty dirs inside
            dry_run: Report what would be deleted, delete nothing

        Returns:
            What was deleted and held
        """
        result = CleanupResult()
        if self.blocked:
            result.skipped = True
            logger.warning(f"cleanup_blocked: {self.scraper} orphan cleanup skipped this run: "
                           + "; ".join(f"{reason} x{len(details)}" for reason, details in self.blocks.items()))
            return result

        pending = {path.lower() for path in self.pending_orphans}
        removable = {self.rel(path).lower() for path in removable_dirs}
        dirs = sorted(set(scan_dirs), key=lambda path: len(path.parts), reverse=True)

        # Each file is listed once, in the deepest scanned dir that holds it,
        # identified by its directory entry: on a case-insensitive filesystem
        # two scanned dirs spelled in different casings list one file under
        # two names, and on a case-sensitive one two names are two files
        seen: Set[Tuple[int, int]] = set()
        listed: List[Tuple[Path, List[Path]]] = []
        for scan_dir in dirs:
            if not scan_dir.is_dir():
                continue
            files: List[Path] = []
            for path in sorted(scan_dir.rglob("*.md")):
                if not path.is_file():
                    continue
                entry = path.lstat()
                if (entry.st_dev, entry.st_ino) not in seen:
                    seen.add((entry.st_dev, entry.st_ino))
                    files.append(path)
            listed.append((scan_dir, files))
        unexpected = unmatched((self.rel(path) for _, files in listed for path in files), self._expected)

        new_pending: List[str] = []
        plan: List[Tuple[Path, List[Path]]] = []
        for scan_dir, files in listed:
            orphans = [path for path in files if self.rel(path) in unexpected and not self.is_kept(path)]
            if not orphans:
                plan.append((scan_dir, []))
                continue
            confirmed = [path for path in orphans if self.rel(path).lower() in pending]
            remainder = [path for path in orphans if self.rel(path).lower() not in pending]
            result.confirmed += len(confirmed)
            if valve_trips(len(remainder), len(files) - len(confirmed)):
                result.held[self.rel(scan_dir)] = (len(remainder), len(files) - len(confirmed))
                new_pending.extend(self.rel(path) for path in remainder)
                logger.warning(f"orphan_valve_held: {self.rel(scan_dir)}: {len(remainder)} of "
                               f"{len(files) - len(confirmed)} files orphaned; kept in {PENDING_ORPHANS_KEY}, "
                               f"deleted on the next clean run if still orphaned ({len(confirmed)} confirmed)")
                plan.append((scan_dir, confirmed))
            else:
                plan.append((scan_dir, confirmed + remainder))

        for scan_dir, delete in plan:
            for path in delete:
                if dry_run:
                    logger.info(f"Would delete orphan: {self.rel(path)}")
                    result.deleted.append(self.rel(path))
                    continue
                try:
                    path.unlink()
                except FileNotFoundError:
                    continue
                except OSError as e:
                    message = f"orphan_delete_failed: {self.rel(path)}: {e}"
                    logger.error(message)
                    result.failures.append(message)
                    self.errors.append(message)
                    continue
                logger.info(f"orphan_deleted: {self.rel(path)}"
                            + (" (confirmed from pending_orphans)" if self.rel(path).lower() in pending else ""))
                result.deleted.append(self.rel(path))
            if not dry_run:
                self._remove_empty_dirs(scan_dir, self.rel(scan_dir).lower() in removable)

        # A held file under a location this run keeps (its source or directory
        # failed, so nothing under it was scraped) waits, unchanged, for the
        # next run that scrapes it: an unscraped run leaves its entry untouched
        carried = [path for path in self.pending_orphans if self.is_kept(self.output_base / path)]
        self.pending_orphans = sorted(set(new_pending).union(carried))
        return result

    @staticmethod
    def _remove_empty_dirs(scan_dir: Path, remove_root: bool) -> None:
        """Remove the empty dirs under scan_dir, deepest first (and scan_dir itself if remove_root)."""
        if not scan_dir.is_dir():
            return
        for path in sorted(scan_dir.rglob("*"), key=lambda p: len(p.parts), reverse=True):
            if path.is_dir():
                try:
                    path.rmdir()  # only an empty dir
                except OSError:
                    pass
        if remove_root:
            try:
                scan_dir.rmdir()
            except OSError:
                pass

    # -- saving and reporting -----------------------------------------------

    def metadata(self, hash_keys: Container[str]) -> Dict[str, Any]:
        """This policy's hash-file metadata after the run: failure_counts and
        pending_orphans, each only while non-empty.

        Args:
            hash_keys: The keys of the hash file this run saves, after its
                pruning. A page's local count is dropped when the page is
                gone: this run's cleanup ran (a blocked run removes nothing,
                so a page it didn't reach may still be live) and saves no key
                for it
        """
        result: Dict[str, Any] = {}
        counts = self.counts.to_metadata(kept=self.keeps_key,
                                         present=lambda key: self.blocked or key in hash_keys)
        if counts:
            result[FAILURE_COUNTS_KEY] = counts
        if self.pending_orphans:
            result[PENDING_ORPHANS_KEY] = self.pending_orphans
        return result

    def summary_lines(self, cleanup: Optional[CleanupResult]) -> List[str]:
        """The end-of-run summary of failures, kept files, holds and errors."""
        lines: List[str] = []
        for location in self.kept:
            lines.append(f"Kept this run ({location.reason}): {self.rel(location.path)}")
        if cleanup is not None:
            if cleanup.skipped:
                lines.append("Orphan cleanup skipped this run (a failure of ours): "
                             + "; ".join(f"{reason} x{len(details)}" for reason, details in self.blocks.items()))
            for scan_dir, (held, files) in sorted(cleanup.held.items()):
                lines.append(f"Held by the valve ({PENDING_ORPHANS_KEY} set, deleted on the next clean run if "
                             f"still orphaned): {scan_dir}: {held} of {files} files")
        problems = [detail for details in self.blocks.values() for detail in details] + self.errors
        if problems:
            lines.append(f"Errors of ours this run ({len(problems)}), exit code 1:")
            lines.extend(f"  - {problem}" for problem in problems)
        return lines


def policy_metadata(metadata: Mapping[str, Any], keys: Sequence[str]) -> Dict[str, Any]:
    """The given metadata keys of a hash file (those present), for change detection."""
    return {key: metadata[key] for key in keys if key in metadata}
