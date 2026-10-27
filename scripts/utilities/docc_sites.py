"""The DocC sites other than Apple's (site.DOCC_SITES), as the Apple process scrapes them.

Each site's roots (its allow-list) are jobs of the Apple run (scrape.py),
next to the Apple technologies, with its own namespace, hash files and
local links. Before its jobs, its index root is loaded (load_site, rule 7(f)
of todo-4's D6 design):
- a 200 whose body lists pages: its first segments are the site's index
  roots, persisted as metadata.index_roots in .hashes/<namespace>/_site.json
  (not a *_hashes.json name: no per-root step, dirmap or count sees it);
- a 404/410: index_root_gone; the persisted index roots stand in (with none
  persisted yet, it is a failure, as below);
- anything else (5xx, timeout, challenge, a body that isn't the index): our
  failure; the site's jobs are skipped this run, which exits 1.
The site's top-level set is its allow-list, its excludes and its index roots,
so a page of a top-level segment it doesn't crawl (e.g. docs.swift.org's 14
private stdlib modules) is never crawled, as a root or as a module. Each of
its excluded paths that is a collection (a package's proposals) is fetched
too: the pages it lists that no crawl reached (DocCSite.excluded_pages) are
linked by URL, as the collection is; a failed fetch uses those its last
successful one listed (persisted in _site.json), and is no error.

A site whose index is a navigator index (a Swift Package Index package's
index/index.json, DocCSite.roots_from_index) has no allow-list: the first
segments of the documentation paths it lists are its roots, each a job, and
its top-level set. They are persisted as index_roots too, and its loads
differ (load_site, row 3):
- a 404/410 index is the package's removal: on the 1st such run the
  persisted roots run normally (metadata.root_gone_runs = 1 in _site.json,
  reset by a 200); on the 2nd the package goes whole and runs nothing; with
  no roots persisted (its first run, or after that removal) a 404/410 runs
  nothing, writes nothing and is no error;
- a root its index stops listing is counted in its hash file's
  metadata.unlisted_runs on each successful load (reset once listed again),
  and goes with its dir on the 2nd (unlisted_removals): SPI keeps serving a
  removed target's JSON, so its root never 404s;
- any other failure is ours, as above, and counts nothing.

Its removals are automatic (rule 7): a top-level hash file whose root left
the allow-list goes with its dir, at the end of the next run that covers the
site (config_removals), and a site that left the config goes whole, its
namespace's docs dir and hash dir (gone_sites). A root that answers 404/410
on 2 consecutive runs goes as an Apple root does (root_gone_runs); other
failures follow the 2.1 policy. A page we have that answers 404/410 goes at
once, as an Apple page does, except on a site whose page_gone_runs is over 1
(a package's, 2: SPI answers 404 while it rebuilds its docs), where it goes
on that many consecutive 404/410 runs (consecutive_gone). Module sinks under
a namespace (D6) are only ever removed by the module rules.
"""

import dataclasses
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Final, List, Optional, Sequence, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scraper.base import NOT_MODIFIED, BaseAppleScraper, FetchFailed
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper, SiteRemoval
from scraper.sink import CHILD_MODULES_KEY, HASH_FILE_SUFFIX, MODULE_KEY, Sink, apple_top_level, metadata_ids
from scraper.site import DocCSite
from scraper.utils.hash_manager import HashManager, read_hash_file
from scraper.utils.logger import get_logger
from scraper.utils.naming import dirmap
from scraper.utils.rate_limiter import AdaptiveRateLimiter
from cleanup_orphans_at_end import INDEX_GONE, NOT_CONFIGURED, ROOT_GONE_REMOVAL_RUNS, UNLISTED
from cleanup_removed_frameworks import UNLISTED_REMOVAL_RUNS

logger = get_logger(__name__)

# A site's own file in its hash dir: metadata.site (its name) and, for a site
# with an index root, metadata.index_roots
SITE_FILE: Final = "_site.json"
SITE_KEY: Final = "site"
INDEX_ROOTS_KEY: Final = "index_roots"
# A navigator-index site's consecutive runs whose index answered 404/410 (in
# _site.json), and a root's consecutive loads of it that didn't list the
# root (in the root's hash file); each present only while > 0
ROOT_GONE_KEY: Final = "root_gone_runs"
UNLISTED_KEY: Final = "unlisted_runs"
GONE_STATUSES: Final = (404, 410)
# The pages each excluded collection listed on its last successful fetch (in
# _site.json), {exclude: [paths]}: what a run whose fetch of it fails excludes
EXCLUDED_PAGES_KEY: Final = "excluded_pages"


def site_file(site: DocCSite) -> Path:
    """A site's _site.json: .hashes/<namespace>/_site.json."""
    return Config.get_hash_dir(site.namespace) / SITE_FILE


def persisted_index_roots(site: DocCSite) -> List[str]:
    """The index roots the site's last successful index load persisted (cased; [] if none)."""
    try:
        _, metadata = read_hash_file(site_file(site))
    except (OSError, ValueError):
        return []
    roots = metadata.get(INDEX_ROOTS_KEY)
    return [root for root in roots if isinstance(root, str) and root] if isinstance(roots, list) else []


def index_roots(site: DocCSite, body: str) -> List[str]:
    """The first segments of the documentation pages an index root's references list.

    Each as its identifier cases it (doc://…/documentation/MigrationGuide ->
    MigrationGuide), else as its URL does. Raises ValueError for a body that
    isn't such a page (no JSON, or no reference to a documentation page).
    """
    data = json.loads(body)
    references = data.get("references") if isinstance(data, dict) else None
    if not isinstance(references, dict):
        raise ValueError("no references")
    roots: Dict[str, str] = {}
    for identifier, reference in references.items():
        url = reference.get("url") if isinstance(reference, dict) else None
        if not (isinstance(url, str) and reference.get("type") == "topic" and url.startswith(site.doc_path)):
            continue
        segment = url[len(site.doc_path):].split("/", 1)[0].split("#", 1)[0]
        if not segment:
            continue
        identifier_path = str(identifier).partition("/documentation/")[2]
        cased = identifier_path.split("/", 1)[0].split("#", 1)[0]
        roots.setdefault(segment.lower(), cased if cased.lower() == segment.lower() else segment)
    if not roots:
        raise ValueError("no documentation page in its references")
    return sorted(roots.values(), key=str.lower)


def collection_pages(site: DocCSite, collection: str, body: str) -> List[str]:
    """The pages an excluded collection's JSON curates (its topicSections): their paths, lowercased.

    Each through its reference's URL, as the crawl resolves a link
    ("/documentation/logging/slg-nnnn" -> logging/slg-nnnn), without its
    #fragment. The collection itself and a top-level page (a root, never
    excluded this way) are none. Raises ValueError for a body that isn't a
    page (no JSON, or no references).
    """
    data = json.loads(body)
    references = data.get("references") if isinstance(data, dict) else None
    if not isinstance(references, dict):
        raise ValueError("no references")
    sections = data.get("topicSections")
    pages: Set[str] = set()
    for section in sections if isinstance(sections, list) else []:
        identifiers = section.get("identifiers") if isinstance(section, dict) else None
        for identifier in identifiers if isinstance(identifiers, list) else []:
            reference = references.get(identifier) if isinstance(identifier, str) else None
            if not isinstance(reference, dict) or reference.get("type") != "topic":
                continue
            url = reference.get("url")
            if not (isinstance(url, str) and url.startswith(site.doc_path)):
                continue
            path = url[len(site.doc_path):].split("#", 1)[0].strip("/").lower()
            if "/" in path and path != collection:
                pages.add(path)
    return sorted(pages)


def page_json_url(site: DocCSite, path: str) -> str:
    """A documentation path's JSON URL, as the crawl keys its hash entry (dot segments escaped with "'")."""
    escaped = "/".join(f"'{segment}" if segment.startswith(".") else segment for segment in path.split("/"))
    return f"{site.json_prefix}{escaped}.json"


def live_json_urls(hash_dir: Path, site: DocCSite) -> Set[str]:
    """The JSON URLs of the site's pages its hash files record live (a file, no error); unreadable files skipped."""
    live: Set[str] = set()
    for path in sorted(hash_dir.glob(f"*{HASH_FILE_SUFFIX}")) if hash_dir.is_dir() else []:
        try:
            hashes, _ = read_hash_file(path)
        except (OSError, ValueError):
            continue
        live |= {url for url, entry in hashes.items()
                 if url.startswith(site.json_prefix) and isinstance(entry, dict)
                 and entry.get("file_path") and entry.get("status") != "error"}
    return live


def navigator_roots(site: DocCSite, body: str) -> List[str]:
    """The roots a navigator index (DocC's index/index.json) lists: the first segments of its documentation paths.

    Each as its root node's title cases it when that is the segment in
    another casing (/documentation/carekitstore, "CareKitStore"), else as
    the path does. A path outside the site's documentation (a /tutorials/
    page, OD5) is none. Raises ValueError for a body that isn't such an
    index (no JSON, no interfaceLanguages, or no documentation path).
    """
    data = json.loads(body)
    languages = data.get("interfaceLanguages") if isinstance(data, dict) else None
    if not isinstance(languages, dict):
        raise ValueError("no interfaceLanguages")
    roots: Dict[str, str] = {}
    stack: List[Any] = list(languages.values())
    while stack:
        node = stack.pop()
        if isinstance(node, list):
            stack.extend(node)
            continue
        if not isinstance(node, dict):
            continue
        children = node.get("children")
        if isinstance(children, list):
            stack.extend(children)
        path = node.get("path")
        if not (isinstance(path, str) and path.startswith(site.doc_path)):
            continue
        rest = path[len(site.doc_path):].split("#", 1)[0].strip("/")
        segment = rest.split("/", 1)[0]
        if not segment:
            continue
        title = node.get("title")
        if "/" not in rest and isinstance(title, str) and title.lower() == segment.lower():
            roots[segment.lower()] = title
        else:
            roots.setdefault(segment.lower(), segment)
    if not roots:
        raise ValueError("no documentation path")
    return sorted(roots.values(), key=str.lower)


class SiteIndexLoader(BaseAppleScraper):
    """Loads a DocC site's index root through the scraper's HTTP client (its retries and rate limit).

    Its hash manager is the site's _site.json, saved on exit.
    """

    def __init__(self, site: DocCSite, rate_limiter: Optional[AdaptiveRateLimiter] = None) -> None:
        self.site = site
        self._site_file = HashManager(site_file(site), Config.get_docs_dir(site.namespace))
        super().__init__(
            framework_id=site.name,
            framework_name=site.label,
            base_url=site.index_url,
            hash_dir=Config.get_hash_dir(site.namespace),
            rate_limiter=rate_limiter,
            max_retries=site.max_retries,
            retry_backoff=site.retry_backoff,
        )

    @property
    def hash_manager(self) -> HashManager:
        """The site's _site.json."""
        return self._site_file

    async def save_page_data(self, sink: Sink, url: str, data: Dict[str, Any]) -> bool:
        raise NotImplementedError("the index root is never saved as a page")

    async def load(self) -> Tuple[str, List[str], Optional[str]]:
        """Fetch the index root.

        Returns:
            ("ok", its index roots, None), persisted in _site.json;
            ("gone", [], why) for a 404/410; ("failed", [], why) otherwise
        """
        assert self.site.index_url is not None
        result = await self.fetch_page(self.site.index_url)
        if isinstance(result, FetchFailed):
            state = "gone" if result.status in GONE_STATUSES else "failed"
            return state, [], f"{self.site.index_url}: {result.error}"
        if result is NOT_MODIFIED:
            return "failed", [], f"{self.site.index_url}: HTTP 304 without a conditional request"
        try:
            roots = (navigator_roots if self.site.roots_from_index else index_roots)(self.site, result)
        except ValueError as e:
            return "failed", [], f"{self.site.index_url}: not the site's index ({e})"
        self._site_file.set_metadata(INDEX_ROOTS_KEY, roots)
        return "ok", roots, None

    async def load_excluded_pages(self) -> List[str]:
        """The pages the site's excluded collections list (collection_pages), one request each.

        An excluded path below a root (a package's proposals collection) is
        a collection; an excluded root id (docs.swift.org's "swift") is a
        whole top-level segment, never fetched. Each collection's pages are
        persisted in _site.json; a collection whose fetch fails (any status,
        404/410 too: a package's host answers 404 while it rebuilds its
        docs) or isn't a page gives the pages its last successful fetch
        persisted, logged, and is no error of the run; so does one that
        lists no page while pages are persisted (a package's host may serve
        a collection empty while it rebuilds its docs), so that its pages'
        renderings (sink.render_inputs) don't flip and back.
        """
        stored = self._site_file.get_metadata(EXCLUDED_PAGES_KEY)
        persisted: Dict[str, Any] = stored if isinstance(stored, dict) else {}
        loaded: Dict[str, List[str]] = {}
        for collection in (exclude for exclude in self.site.excludes if "/" in exclude):
            url = f"{self.site.json_prefix}{collection}.json"
            result = await self.fetch_page(url)
            error: Optional[str] = None
            if isinstance(result, FetchFailed):
                error = result.error
            elif result is NOT_MODIFIED:
                error = "HTTP 304 without a conditional request"
            else:
                try:
                    loaded[collection] = collection_pages(self.site, collection, result)
                except ValueError as e:
                    error = f"not a page ({e})"
                else:
                    if not loaded[collection] and persisted.get(collection):
                        error = "lists no page"
            if error is not None:
                previous = persisted.get(collection)
                loaded[collection] = ([page for page in previous if isinstance(page, str)]
                                      if isinstance(previous, list) else [])
                logger.warning("excluded_collection_failed", site=self.site.name, url=url, error=error,
                               persisted=len(loaded[collection]))
        self._site_file.set_metadata(
            EXCLUDED_PAGES_KEY, {collection: pages for collection, pages in loaded.items() if pages} or None)
        return sorted({page for pages in loaded.values() for page in pages})


@dataclass
class SiteRun:
    """A DocC site's share of a run, from its config and its index root (load_site).

    Attributes:
        site: The site, with the pages its excluded collections list this
            run (DocCSite.excluded_pages): its jobs' site
        jobs: Its roots to crawl this run, (root id, docs dir as cased):
            none when error is set
        top_level: Its top-level set (lowercased): its allow-list, its
            excludes' first segments and its index roots
        known_dirs: Its docs dirs linked locally, {name.lower(): name}: those
            its hash dir shows (naming.dirmap) and its jobs'
        listed: The roots its config or index lists this run (lowercased):
            its allow-list, or a navigator-index site's index roots (none
            when its index failed or is gone for good)
        removals: A navigator-index site's removals this run (rule 7(a)):
            its roots unlisted on UNLISTED_REMOVAL_RUNS loads, or the whole
            package once its index is gone on ROOT_GONE_REMOVAL_RUNS runs
        error: Why its jobs are skipped this run (7(f)): an error for the run
    """

    site: DocCSite
    jobs: List[Tuple[str, str]] = field(default_factory=list)
    top_level: Set[str] = field(default_factory=set)
    known_dirs: Dict[str, str] = field(default_factory=dict)
    listed: Set[str] = field(default_factory=set)
    removals: List[SiteRemoval] = field(default_factory=list)
    error: Optional[str] = None


async def load_site(site: DocCSite, rate_limiter: Optional[AdaptiveRateLimiter] = None) -> SiteRun:
    """A site's share of the run: its index root loaded (7(f)), its jobs and its top-level set.

    Its _site.json records the site (metadata.site) on every load, so a
    site that later leaves the config is found (gone_sites).

    Args:
        site: The site
        rate_limiter: The limiter its jobs share
    """
    run = SiteRun(site=site, listed={root.lower() for root in site.roots})
    roots: List[str] = []
    state = "ok"
    async with SiteIndexLoader(site, rate_limiter) as index:
        assert isinstance(index, SiteIndexLoader)
        if site.index_url:
            state, roots, why = await index.load()
            if state == "gone":
                logger.warning("index_root_gone", site=site.name, url=site.index_url, error=why)
                roots = persisted_index_roots(site)
                if site.roots_from_index:
                    roots = _index_gone(index, roots, run)
                elif not roots:
                    run.error = f"{site.name}: index root gone (404/410) with no index_roots persisted: {why}"
            elif state == "failed":
                run.error = f"{site.name}: index root failed: {why}"
            elif site.roots_from_index:
                index.hash_manager.set_metadata(ROOT_GONE_KEY, None)
        if not (site.roots_from_index and state == "gone" and not roots):
            # (A navigator-index site whose index is gone with nothing to run writes nothing)
            index.hash_manager.set_metadata(SITE_KEY, site.name)
            if run.error is None and any("/" in exclude for exclude in site.excludes):
                # The pages only its excluded collections list (none of its
                # hash files records them live: no crawl reached them) are
                # linked by URL (DocCSite.excluded_pages); one in-scope
                # curation reaches is crawled and linked locally as ever. An
                # inline link to any of them is never followed (collection_pages)
                live = live_json_urls(Config.get_hash_dir(site.namespace), site)
                listed = await index.load_excluded_pages()
                pages = [page for page in listed if page_json_url(site, page) not in live]
                if pages:
                    logger.info("excluded_pages", site=site.name, pages=len(pages))
                if listed:
                    run.site = site = dataclasses.replace(
                        site, excluded_pages=frozenset(pages), collection_pages=frozenset(listed))
    if run.error is not None:
        logger.error("index_root_failed", site=site.name, url=site.index_url, error=run.error)
        return run

    hash_dir = Config.get_hash_dir(site.namespace)
    cased = {root.lower(): root for root in roots}
    if site.roots_from_index:
        listed = [root for root in sorted(cased) if not site.excluded(root)]
        if state == "ok":
            run.removals += unlisted_removals(site, set(listed))
        run.listed = set(listed)
    else:
        listed = list(site.roots)
    run.top_level = (
        set(listed)
        | {exclude.split("/", 1)[0].lower() for exclude in site.excludes}
        | set(cased)
    )
    if site.roots_from_index and hash_dir.exists():
        # A root its index no longer lists stays top-level (never crawled as a module) until it is removed
        run.top_level |= apple_top_level(hash_dir, site)
    run.known_dirs = dirmap(hash_dir, site.json_prefix) if hash_dir.exists() else {}
    for root in listed:
        dir_name = AppleJSONDocumentationScraper._canonical_framework_id(cased.get(root, root), hash_dir)
        run.jobs.append((root, dir_name))
        run.known_dirs[dir_name.lower()] = dir_name
    return run


def _index_gone(index: SiteIndexLoader, roots: List[str], run: SiteRun) -> List[str]:
    """A navigator-index site's index answered 404/410 (row 3): the roots it runs this run.

    With roots persisted, the run is counted in _site.json's root_gone_runs:
    below ROOT_GONE_REMOVAL_RUNS the persisted roots run normally; at it the
    package is removed whole (run.removals) and runs nothing, so a later run
    that still finds it in the config re-creates nothing. With none
    persisted (its first run, or after that removal) it runs nothing.
    """
    site = index.site
    if not roots:
        logger.info("index_gone_nothing_persisted", site=site.name)
        return []
    previous = index.hash_manager.get_metadata(ROOT_GONE_KEY)
    gone_runs = (previous if isinstance(previous, int) and previous > 0 else 0) + 1
    index.hash_manager.set_metadata(ROOT_GONE_KEY, gone_runs)
    if gone_runs < ROOT_GONE_REMOVAL_RUNS:
        logger.warning("index_gone_pending", site=site.name, root_gone_runs=gone_runs)
        return roots
    logger.warning("index_gone_removal", site=site.name, root_gone_runs=gone_runs)
    run.removals.append(SiteRemoval(
        site=site.name,
        namespace=site.namespace,
        framework_id="",
        output_dir=Config.get_docs_dir(site.namespace),
        hash_file=Config.get_hash_dir(site.namespace),
        reason=INDEX_GONE,
    ))
    return []


def unlisted_removals(site: DocCSite, listed: Set[str]) -> List[SiteRemoval]:
    """Rule 7(a) for a navigator-index site whose index loaded: its top-level roots the index no longer lists.

    Each top-level hash file (no metadata.module) of the site counts this
    load in its metadata.unlisted_runs if its root isn't listed, and drops
    the count if it is. One counted to UNLISTED_REMOVAL_RUNS is removed with
    its dir (returned). One that can't be read counts as top-level unless a
    readable file of the site lists it in child_modules, and is replaced by
    a file holding only its count (as the Apple unlisted rule does).

    Args:
        site: The site
        listed: The roots its index lists (lowercased)
    """
    hash_dir = Config.get_hash_dir(site.namespace)
    if not hash_dir.is_dir():
        return []
    candidates: List[Tuple[Path, str, Optional[Dict[str, Any]]]] = []
    children: Set[str] = set()
    for path in sorted(hash_dir.glob(f"*{HASH_FILE_SUFFIX}")):
        name = path.name[: -len(HASH_FILE_SUFFIX)]
        try:
            _, metadata = read_hash_file(path)
        except (OSError, ValueError):
            candidates.append((path, name, None))
            continue
        children |= {str(child).lower() for child in metadata_ids(metadata.get(CHILD_MODULES_KEY))}
        if not metadata.get(MODULE_KEY):
            candidates.append((path, name, metadata))
    removals = []
    for path, name, loaded in candidates:
        if loaded is None and name.lower() in children:
            continue
        previous = loaded.get(UNLISTED_KEY) if loaded is not None else None
        runs = previous if isinstance(previous, int) and previous > 0 else 0
        if name.lower() in listed:
            if runs:
                _write_unlisted(path, 0)
            continue
        runs += 1
        if runs < UNLISTED_REMOVAL_RUNS:
            logger.warning("root_unlisted_pending", site=site.name, root=name, unlisted_runs=runs)
            _write_unlisted(path, runs)
            continue
        logger.warning("root_unlisted", site=site.name, root=name, unlisted_runs=runs)
        _write_unlisted(path, runs)
        removals.append(SiteRemoval(
            site=site.name,
            namespace=site.namespace,
            framework_id=name,
            output_dir=Config.get_framework_output_dir(name, namespace=site.namespace),
            hash_file=Config.get_hash_file(name, namespace=site.namespace),
            reason=UNLISTED,
        ))
    return removals


def _write_unlisted(path: Path, runs: int) -> None:
    """Write a root's unlisted_runs into its hash file (0 drops it), every other key as it is.

    A file that can't be loaded is replaced by one holding only the count.
    A failed save is logged by the save; the count is then counted again
    from the old value on the next load.
    """
    manager = HashManager(path)
    manager.set_metadata(UNLISTED_KEY, runs or None)
    manager.save()


def config_removals(site: DocCSite) -> List[SiteRemoval]:
    """Rule 7(a): the site's top-level hash files whose root left its allow-list, each with its dir.

    A module's hash file (metadata.module) is never one: modules leave only
    through the module rules. One that can't be read counts as top-level,
    unless a readable file of the site lists it in child_modules (it may be
    a module's).
    """
    hash_dir = Config.get_hash_dir(site.namespace)
    if not hash_dir.is_dir():
        return []
    roots = {root.lower() for root in site.roots}
    candidates: List[Tuple[str, bool]] = []
    children: Set[str] = set()
    for path in sorted(hash_dir.glob(f"*{HASH_FILE_SUFFIX}")):
        name = path.name[: -len(HASH_FILE_SUFFIX)]
        try:
            _, metadata = read_hash_file(path)
        except (OSError, ValueError):
            candidates.append((name, False))
            continue
        children |= {str(child).lower() for child in metadata_ids(metadata.get(CHILD_MODULES_KEY))}
        candidates.append((name, bool(metadata.get(MODULE_KEY))))
    removals = []
    for name, module in candidates:
        if module or name.lower() in roots or name.lower() in children:
            continue
        logger.warning("root_not_configured", site=site.name, root=name)
        removals.append(SiteRemoval(
            site=site.name,
            namespace=site.namespace,
            framework_id=name,
            output_dir=Config.get_framework_output_dir(name, namespace=site.namespace),
            hash_file=Config.get_hash_file(name, namespace=site.namespace),
            reason=NOT_CONFIGURED,
        ))
    return removals


def gone_sites(configured: Sequence[DocCSite]) -> List[SiteRemoval]:
    """Rule 7(a): the namespaces whose site left the config, each whole.

    A dir under .hashes holding a _site.json (at any depth: SPI's are
    .hashes/SPI/<repo>/) that is no configured site's hash dir.
    """
    if not Config.CACHE_DIR.is_dir():
        return []
    configured_dirs = {str(Config.get_hash_dir(site.namespace)).lower() for site in configured}
    removals = []
    for path in sorted(Config.CACHE_DIR.rglob(SITE_FILE)):
        hash_dir = path.parent
        if hash_dir == Config.CACHE_DIR or str(hash_dir).lower() in configured_dirs:
            continue
        namespace = hash_dir.relative_to(Config.CACHE_DIR).as_posix()
        try:
            _, metadata = read_hash_file(path)
        except (OSError, ValueError):
            metadata = {}
        name = metadata.get(SITE_KEY) if isinstance(metadata.get(SITE_KEY), str) else namespace
        logger.warning("site_not_configured", site=name, namespace=namespace)
        removals.append(SiteRemoval(
            site=str(name),
            namespace=namespace,
            framework_id="",
            output_dir=Config.get_docs_dir(namespace),
            hash_file=hash_dir,
        ))
    return removals


def check_namespaces(sites: Sequence[DocCSite], reserved: Dict[str, str], apple_ids: Set[str]) -> None:
    """The startup assertion: no DocC namespace's top-level dir is another's.

    Not, case-insensitively, a top-level dir of the MLX, Swift or HIG
    scrapers (their orphan scans cover their whole dirs, so they would
    delete the site's pages every run), nor an Apple hash file's id; and no
    two sites share a namespace.

    Raises:
        ValueError: A namespace collides (the run aborts before scraping)
    """
    seen: Dict[str, str] = {}
    for site in sites:
        if not site.namespace:
            raise ValueError(f"DocC site {site.name} has no namespace")
        top = site.namespace_top.lower()
        if top in reserved:
            raise ValueError(f"DocC site {site.name}'s namespace {site.namespace} is another scraper's dir "
                             f"({reserved[top]})")
        if top in apple_ids:
            raise ValueError(f"DocC site {site.name}'s namespace {site.namespace} is an Apple framework's dir")
        if site.namespace.lower() in seen:
            raise ValueError(f"DocC sites {seen[site.namespace.lower()]} and {site.name} share the namespace "
                             f"{site.namespace}")
        seen[site.namespace.lower()] = site.name
