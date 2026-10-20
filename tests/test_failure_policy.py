"""The scraper's failure policy across consecutive framework runs.

Each test runs whole framework scrapes (scrape_framework inside the scraper's
context, so the hash file is saved and reloaded between runs, as in CI)
against a fake Apple served through an httpx.MockTransport, and checks what
each run decides: the per-entry counters (consecutive_failures,
consecutive_local_errors), the root_gone_runs/failure_storm_runs metadata, the
FrameworkOutcome (blocked, persistent failures, root flags), and which files
scrape.py's end-of-run cleanup would delete after the run (would_delete),
also for a page we have whose entry was lost (a hash file that failed to load
or save, or was deleted). Some tests drive scrape_everything end to end, to
check that the orphan cleanup honours a blocked framework (or one whose hash
file couldn't be saved or loaded) and that --frameworks names one of which
matches no framework scrape nothing.
"""

import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Set

import httpx
import pytest
from structlog.testing import capture_logs
from structlog.typing import EventDict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import cleanup_orphans_at_end
import scrape_all_frameworks
from cleanup_orphans_at_end import CleanupReport
from scraper.config import Config
from scraper.json_scraper import PERSISTENT_FAILURE_RUNS, AppleJSONDocumentationScraper, FrameworkOutcome
from scraper.utils.hash_manager import HashManager
from scraper.utils.rate_limiter import AdaptiveRateLimiter
from tests.test_fetch_results import TIMEOUT, FakeApple, Spec, doc_url, json_url, ok, page, status

FW = "testkit"
ROOT = FW
ALPHA = "testkit/alpha"
ALPHA_CHILD = "testkit/alpha/child"
BETA = "testkit/beta"
GAMMA = "testkit/gamma"
NEW = "testkit/zeta"
MAX_RETRIES = 3

Site = Dict[str, List[str]]

# root -> alpha (-> alpha/child), beta, gamma: 5 files, so 2 orphans stay under the valve
SITE: Site = {ROOT: [ALPHA, BETA, GAMMA], ALPHA: [ALPHA_CHILD], ALPHA_CHILD: [], BETA: [], GAMMA: []}


class Apple(FakeApple):
    """FakeApple that 404s (and records) any URL the test didn't route."""

    def __init__(self, routes: Dict[str, List[Spec]]) -> None:
        super().__init__(routes)
        self.unrouted: List[str] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        if str(request.url) not in self.routes:
            self.unrouted.append(str(request.url))
            return httpx.Response(404, text="unrouted", request=request)
        return super().__call__(request)


def routes_for(site: Site, overrides: Optional[Dict[str, List[Spec]]] = None, version: int = 1) -> Dict[str, List[Spec]]:
    """Each page answers 200 with an etag of its body (304 on a match), unless overridden."""
    routes: Dict[str, List[Spec]] = {}
    for path, children in site.items():
        body = page(path, children)
        if version > 1:
            body = body.replace("page.", f"page, v{version}.")
        etag = "E-" + hashlib.sha256(body.encode()).hexdigest()[:12]
        routes[json_url(path)] = [ok(body, etag)]
    for path, specs in (overrides or {}).items():
        routes[json_url(path)] = specs
    return routes


def file_of(path: str) -> Path:
    """The .md file a page of SITE is saved to (relative, as in production)."""
    if path == ROOT:
        return Path("documentation") / FW / f"{FW}.md"
    return Path("documentation") / f"{path}.md"


class Runs:
    """Consecutive framework runs over one sandbox (cwd = tmp_path, relative dirs)."""

    def __init__(self, monkeypatch: pytest.MonkeyPatch) -> None:
        self.monkeypatch = monkeypatch
        self.events: List[EventDict] = []
        self.last: Optional[AppleJSONDocumentationScraper] = None  # the last run's scraper

    async def run(self, routes: Dict[str, List[Spec]], fw: str = FW) -> AppleJSONDocumentationScraper:
        apple = Apple(routes)
        scraper = AppleJSONDocumentationScraper(fw, fw.title())
        with capture_logs() as events:
            async with scraper:
                assert scraper.session is not None
                await scraper.session.aclose()
                scraper.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
                await scraper.scrape_framework()
        self.events = events
        assert apple.unrouted == []
        self.last = scraper
        return scraper

    def logged(self, event: str) -> List[EventDict]:
        return [e for e in self.events if e["event"] == event]

    @staticmethod
    def saved(fw: str = FW) -> Dict[str, Any]:
        """The framework's hash file as saved."""
        data: Dict[str, Any] = json.loads(Config.get_hash_file(fw).read_text())
        return data

    @staticmethod
    def entry(path: str, fw: str = FW) -> Dict[str, Any]:
        entry: Dict[str, Any] = Runs.saved(fw)["hashes"][json_url(path)]
        return entry

    def orphans(self, fw: str = FW) -> Set[Path]:
        """Orphan detection for the framework, from the last run's in-memory touched set."""
        scraper = self.last
        assert scraper is not None and scraper.framework_id == fw
        return set(scraper.hash_manager.get_untouched_files(Config.get_framework_output_dir(fw)))

    @staticmethod
    def cleanup(*scrapers: AppleJSONDocumentationScraper, interactive: bool = False) -> CleanupReport:
        """scrape.py's end-of-run cleanup (--cleanup-orphans --auto-cleanup) after these runs.

        Each framework's result as scrape_single_framework computes it right
        after the framework's save.
        """
        for scraper in scrapers:
            scraper.scan_orphans()
        return cleanup_orphans_at_end.cleanup_after_scrape([s.outcome for s in scrapers], interactive)


def would_delete(scraper: AppleJSONDocumentationScraper) -> Dict[str, List[Path]]:
    """What scrape.py's end-of-run cleanup would delete after this run, deleting nothing.

    The framework's result as scrape_single_framework computes it right after
    the save, then confirm-then-delete's decision (plan_cleanup).
    """
    scraper.scan_orphans()
    outcome = scraper.outcome
    if outcome.skip_cleanup or outcome.orphan_scan is None:
        return {}
    cleanup = cleanup_orphans_at_end.plan_cleanup(outcome.framework_id, outcome.orphan_scan)
    return {outcome.framework_id: cleanup.delete} if cleanup.delete else {}


def sandbox_runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Runs:
    """A sandbox for consecutive framework runs: relative dirs under tmp_path, no waits."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(Config, "OUTPUT_DIR", Path("documentation"))
    monkeypatch.setattr(Config, "CACHE_DIR", Path(".hashes"))
    monkeypatch.setattr(Config, "MAX_RETRIES", MAX_RETRIES)
    monkeypatch.setattr(Config, "RETRY_BACKOFF_FACTOR", 0.0)

    async def no_wait(self: AdaptiveRateLimiter) -> None:
        return None

    monkeypatch.setattr(AdaptiveRateLimiter, "acquire", no_wait)
    return Runs(monkeypatch)


@pytest.fixture
def runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Runs]:
    yield sandbox_runs(tmp_path, monkeypatch)


async def seeded(runs: Runs, site: Site = SITE) -> None:
    """A first, clean run that saves every page."""
    scraper = await runs.run(routes_for(site))
    assert not scraper.outcome.skip_cleanup
    for path in site:
        assert file_of(path).exists(), path


def counters(entry: Dict[str, Any]) -> Dict[str, int]:
    return {k: v for k, v in entry.items() if k.startswith("consecutive_")}


def fail_convert(monkeypatch: pytest.MonkeyPatch, path: str) -> None:
    """Make the markdown converter raise for one page (a local error of ours)."""
    real_init = AppleJSONDocumentationScraper.__init__

    def init(self: AppleJSONDocumentationScraper, *args: Any, **kwargs: Any) -> None:
        real_init(self, *args, **kwargs)
        convert = self.markdown_converter.convert_page

        def convert_page(data: Dict[str, Any]) -> str:
            if data["source_url"] == doc_url(path):
                raise ValueError("unsupported block")
            return convert(data)

        monkeypatch.setattr(self.markdown_converter, "convert_page", convert_page)

    monkeypatch.setattr(AppleJSONDocumentationScraper, "__init__", init)


class TestCleanRuns:
    async def test_clean_runs_dont_block_or_write_counters(self, runs: Runs) -> None:
        await seeded(runs)
        scraper = await runs.run(routes_for(SITE))
        outcome = scraper.outcome
        assert outcome == FrameworkOutcome(framework_id=FW, stats=outcome.stats)
        assert not outcome.skip_cleanup
        saved = runs.saved()
        assert saved["metadata"] == {"total_pages": len(saved["hashes"]),
                                     "render": {"version": AppleJSONDocumentationScraper.RENDER_VERSION}}
        assert all(not counters(e) for e in saved["hashes"].values())
        assert runs.orphans() == set()
        assert not (Path("documentation") / FW / "scraping_progress.txt").exists()
        # No unconditional root fetch before scrape_page (the old topic-hierarchy fetch)
        assert not hasattr(scraper, "topic_hierarchy")

    async def test_a_304_only_run_saves_nothing(self, runs: Runs) -> None:
        """Every page answers 304: its entries are only touched, so the hash file isn't rewritten."""
        await seeded(runs)
        hash_file = Config.get_hash_file(FW)
        before = hash_file.read_bytes()
        mtime = hash_file.stat().st_mtime_ns
        scraper = await runs.run(routes_for(SITE))
        assert scraper.hash_manager.touched >= {json_url(path) for path in SITE}
        assert hash_file.read_bytes() == before and hash_file.stat().st_mtime_ns == mtime
        assert runs.orphans() == set() and would_delete(scraper) == {}

    async def test_an_etag_rotation_changes_only_the_etags(self, runs: Runs) -> None:
        """The same content under new etags (e.g. a CDN redeploy): only the etag values change."""
        await seeded(runs)
        before = runs.saved()
        rotated = {url: [ok(spec["body"], f"{spec['etag']}-r") for spec in specs]
                   for url, specs in routes_for(SITE).items()}
        await runs.run(rotated)
        after = runs.saved()
        assert after["metadata"] == before["metadata"]
        assert set(after["hashes"]) == set(before["hashes"])
        for url, entry in before["hashes"].items():
            assert after["hashes"][url] == {**entry, "etag": f"{entry['etag']}-r"}, url

    async def test_metadata_and_local_error_counts_survive_a_quiet_run(self, runs: Runs) -> None:
        await seeded(runs)
        hash_file = Config.get_hash_file(FW)
        data = json.loads(hash_file.read_text())
        data["metadata"]["pending_orphans"] = ["documentation/testkit/old.md"]
        data["metadata"]["module"] = {"parent": "other"}
        unlinked = json_url("testkit/unlinked")
        data["hashes"][unlinked] = {
            "status": "error", "error": "HTTP 502", "consecutive_failures": 2, "consecutive_local_errors": 2,
        }
        hash_file.write_text(json.dumps(data, indent=2))
        await runs.run(routes_for(SITE))
        saved = runs.saved()
        assert saved["metadata"]["pending_orphans"] == ["documentation/testkit/old.md"]
        assert saved["metadata"]["module"] == {"parent": "other"}
        assert list(saved["metadata"]) == ["module", "pending_orphans", "render", "total_pages"]
        # A local-error count resets only on a successful save; a run that
        # never fetched the URL ends its D8 streak
        assert counters(saved["hashes"][unlinked]) == {"consecutive_local_errors": 2}


class TestD8:
    """A previously good page that keeps failing (anything but 404/410)."""

    @pytest.mark.parametrize("fault", [
        [status(502)],
        [status(403)],
        [TIMEOUT],
        [status(429)],
        [ok("not json {", "E-BAD")],
    ], ids=["502", "403", "timeout", "429", "invalid-json"])
    async def test_blocks_two_runs_then_d8_removes_it(self, runs: Runs, fault: List[Spec]) -> None:
        await seeded(runs)
        for run in (1, 2):
            scraper = await runs.run(routes_for(SITE, {ALPHA: fault}))
            outcome = scraper.outcome
            assert outcome.blocks == {"fetch_failed": [json_url(ALPHA)]}
            assert outcome.skip_cleanup and outcome.persistent_fetch_failures == []
            entry = runs.entry(ALPHA)
            assert entry["consecutive_failures"] == run
            assert entry.get("status") != "error" and entry["file_path"] == str(file_of(ALPHA))
            # The kept page isn't an orphan; its unreached child would be, but cleanup is blocked
            assert runs.orphans() == {file_of(ALPHA_CHILD)}
            assert would_delete(scraper) == {}

        scraper = await runs.run(routes_for(SITE, {ALPHA: fault}))
        outcome = scraper.outcome
        assert outcome.blocks == {}
        assert not outcome.skip_cleanup
        assert outcome.persistent_fetch_failures == [json_url(ALPHA)]
        assert [e["url"] for e in runs.logged("persistent_fetch_failure")] == [json_url(ALPHA)]
        saved = runs.saved()["hashes"]
        assert saved[json_url(ALPHA)]["status"] == "error"
        assert saved[json_url(ALPHA)]["consecutive_failures"] == 3
        assert saved[doc_url(ALPHA)]["status"] == "error"
        assert "file_path" not in saved[doc_url(ALPHA)]
        # Treated as removed: the cleanup deletes the page and its unreachable subtree
        assert runs.orphans() == {file_of(ALPHA), file_of(ALPHA_CHILD)}
        assert would_delete(scraper) == {FW: sorted([file_of(ALPHA), file_of(ALPHA_CHILD)])}

        # Run 4, still linked and still failing: never-good at 3+, not blocked again
        scraper = await runs.run(routes_for(SITE, {ALPHA: fault}))
        if fault == [status(403)]:
            # A never-good 4xx neither blocks nor counts
            assert runs.entry(ALPHA)["consecutive_failures"] == 3
            assert scraper.outcome.persistent_fetch_failures == []
        else:
            assert runs.entry(ALPHA)["consecutive_failures"] == 4
            assert scraper.outcome.persistent_fetch_failures == [json_url(ALPHA)]
        assert scraper.outcome.blocks == {}

        # The page comes back: saved again, counter dropped
        scraper = await runs.run(routes_for(SITE))
        assert not scraper.outcome.skip_cleanup
        assert counters(runs.entry(ALPHA)) == {}
        assert file_of(ALPHA).exists()

    async def test_a_200_resets_the_count(self, runs: Runs) -> None:
        await seeded(runs)
        await runs.run(routes_for(SITE, {ALPHA: [status(502)]}))
        assert runs.entry(ALPHA)["consecutive_failures"] == 1
        scraper = await runs.run(routes_for(SITE, version=2))
        assert not scraper.outcome.skip_cleanup
        assert counters(runs.entry(ALPHA)) == {}

    async def test_a_304_whose_refetch_succeeds_resets_the_count(self, runs: Runs) -> None:
        await seeded(runs)
        await runs.run(routes_for(SITE, {ALPHA: [status(502)]}))
        await runs.run(routes_for(SITE))
        assert counters(runs.entry(ALPHA)) == {}

    async def test_304_then_failed_refetch_x3_keeps_the_file(self, runs: Runs) -> None:
        await seeded(runs)
        good = routes_for(SITE)[json_url(ALPHA)][0]
        fault = [good] + [status(502)] * (MAX_RETRIES + 1)
        for run in (1, 2):
            scraper = await runs.run(routes_for(SITE, {ALPHA: fault}))
            assert scraper.outcome.blocks == {"fetch_failed": [json_url(ALPHA)]}
            assert runs.entry(ALPHA)["consecutive_failures"] == run
        scraper = await runs.run(routes_for(SITE, {ALPHA: fault}))
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_fetch_failures == [json_url(ALPHA)]
        entry = runs.entry(ALPHA)
        # The 304 proved it live: no mark_error, still touched, file kept
        assert entry.get("status") != "error" and entry["consecutive_failures"] == 3
        assert runs.orphans() == {file_of(ALPHA_CHILD)}

    async def test_404_on_a_good_page_is_removed_in_the_same_run(self, runs: Runs) -> None:
        await seeded(runs)
        scraper = await runs.run(routes_for(SITE, {ALPHA: [status(404)]}))
        assert not scraper.outcome.skip_cleanup
        assert [e["url"] for e in runs.logged("page_gone")] == [json_url(ALPHA)]
        assert counters(runs.entry(ALPHA)) == {}
        assert runs.orphans() == {file_of(ALPHA), file_of(ALPHA_CHILD)}

    async def test_a_404_ends_the_streak(self, runs: Runs) -> None:
        await seeded(runs)
        for _ in (1, 2):
            await runs.run(routes_for(SITE, {ALPHA: [status(502)]}))
        assert runs.entry(ALPHA)["consecutive_failures"] == 2
        scraper = await runs.run(routes_for(SITE, {ALPHA: [status(404)]}))
        assert not scraper.outcome.skip_cleanup
        assert counters(runs.entry(ALPHA)) == {}
        assert runs.orphans() == {file_of(ALPHA), file_of(ALPHA_CHILD)}


class TestNeverGood:
    """A URL with no live entry (e.g. a newly linked page)."""

    @pytest.mark.parametrize("fault", [[status(502)], [TIMEOUT], [status(429)], [ok("not json {", "E")]],
                             ids=["502", "timeout", "429", "invalid-json"])
    async def test_transient_failure_blocks_until_3(self, runs: Runs, fault: List[Spec]) -> None:
        await seeded(runs)
        site: Site = {**SITE, ROOT: [ALPHA, BETA, GAMMA, NEW], NEW: []}
        for run in (1, 2):
            scraper = await runs.run(routes_for(site, {NEW: fault}))
            assert scraper.outcome.blocks == {"fetch_failed": [json_url(NEW)]}
            entry = runs.entry(NEW)
            assert entry["status"] == "error" and entry["consecutive_failures"] == run
        scraper = await runs.run(routes_for(site, {NEW: fault}))
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_fetch_failures == [json_url(NEW)]
        assert runs.entry(NEW)["consecutive_failures"] == 3

    @pytest.mark.parametrize("code", [403, 404, 410])
    async def test_4xx_doesnt_block(self, runs: Runs, code: int) -> None:
        await seeded(runs)
        site: Site = {**SITE, ROOT: [ALPHA, BETA, GAMMA, NEW], NEW: []}
        scraper = await runs.run(routes_for(site, {NEW: [status(code)]}))
        assert not scraper.outcome.skip_cleanup
        assert runs.entry(NEW) == {"status": "error", "error": f"HTTP {code}"}

    async def test_pages_reachable_only_through_it_go_when_it_stops_blocking(self, runs: Runs) -> None:
        await seeded(runs)
        # Apple moves gamma under a new page whose fetch keeps failing
        moved: Site = {**SITE, ROOT: [ALPHA, BETA, NEW], NEW: [GAMMA]}
        for _ in (1, 2):
            scraper = await runs.run(routes_for(moved, {NEW: [status(502)]}))
            assert scraper.outcome.blocks == {"fetch_failed": [json_url(NEW)]}
            assert runs.orphans() == {file_of(GAMMA)}
        scraper = await runs.run(routes_for(moved, {NEW: [status(502)]}))
        assert not scraper.outcome.skip_cleanup
        assert would_delete(scraper) == {FW: [file_of(GAMMA)]}

    async def test_a_4xx_never_protects_the_pages_reachable_only_through_it(self, runs: Runs) -> None:
        await seeded(runs)
        moved: Site = {**SITE, ROOT: [ALPHA, BETA, NEW], NEW: [GAMMA]}
        scraper = await runs.run(routes_for(moved, {NEW: [status(403)]}))
        assert not scraper.outcome.skip_cleanup
        assert would_delete(scraper) == {FW: [file_of(GAMMA)]}

    @pytest.mark.parametrize("between", ["404", "unlinked"])
    async def test_a_404_or_an_unfetched_run_ends_the_streak(self, runs: Runs, between: str) -> None:
        """A stale count must not lift the block on our first new failure."""
        await seeded(runs)
        site: Site = {**SITE, ROOT: [ALPHA, BETA, GAMMA, NEW], NEW: []}
        for _ in (1, 2, 3):
            await runs.run(routes_for(site, {NEW: [status(502)]}))
        assert runs.entry(NEW)["consecutive_failures"] == 3
        for _ in (4, 5):
            if between == "404":
                scraper = await runs.run(routes_for(site, {NEW: [status(404)]}))
            else:
                scraper = await runs.run(routes_for(SITE))  # nothing links to it
            assert not scraper.outcome.skip_cleanup
            assert counters(runs.entry(NEW)) == {}
        # Apple moves gamma under it, and our fetch of it fails once: blocked, gamma kept
        moved: Site = {**SITE, ROOT: [ALPHA, BETA, NEW], NEW: [GAMMA]}
        scraper = await runs.run(routes_for(moved, {NEW: [status(502)]}))
        assert scraper.outcome.blocks == {"fetch_failed": [json_url(NEW)]}
        assert scraper.outcome.persistent_fetch_failures == []
        assert runs.entry(NEW)["consecutive_failures"] == 1
        assert runs.orphans() == {file_of(GAMMA)}


class TestLocalErrors:
    async def test_blocks_two_runs_then_keeps_the_file(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        await seeded(runs)
        fail_convert(monkeypatch, ALPHA)
        # Alpha changed (so it is re-converted) and beta is no longer linked (a real removal)
        site = {**SITE, ROOT: [ALPHA, GAMMA]}
        changed = {ALPHA: routes_for(site, version=2)[json_url(ALPHA)]}
        alpha_before = runs.entry(ALPHA)
        for run in (1, 2):
            scraper = await runs.run(routes_for(site, changed))
            assert scraper.outcome.blocks == {"local_error": [json_url(ALPHA)]}
            entry = runs.entry(ALPHA)
            assert entry["consecutive_local_errors"] == run
            # Write before hash: the old etag stays, so the next run refetches
            assert entry["etag"] == alpha_before["etag"] and entry["hash"] == alpha_before["hash"]
            assert "consecutive_failures" not in entry
            # Links first: the child was reached and stays touched; beta waits for a clean run
            assert runs.orphans() == {file_of(BETA)}
        scraper = await runs.run(routes_for(site, changed))
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_local_errors == [json_url(ALPHA)]
        assert [e["url"] for e in runs.logged("persistent_local_error")] == [json_url(ALPHA)]
        # Never deleted on a local error; the other removal in the framework goes through
        assert runs.orphans() == {file_of(BETA)}
        assert would_delete(scraper) == {FW: [file_of(BETA)]}

    async def test_a_new_page_whose_path_is_too_long_blocks_until_3(self, runs: Runs) -> None:
        """Its save fails every run (a path over the filesystem's PATH_MAX; names are capped): counted like any local error."""
        await seeded(runs)
        long = f"{FW}/" + "/".join(["a" * 200] * 25)
        # Apple adds the page and stops linking beta (a real removal)
        site: Site = {**SITE, ROOT: [ALPHA, GAMMA, long], long: []}
        for run in (1, 2):
            scraper = await runs.run(routes_for(site))
            assert scraper.outcome.blocks == {"local_error": [json_url(long)]}
            assert runs.logged("error_processing_url") == []
            entry = runs.entry(long)
            assert entry["status"] == "error" and entry["error"].startswith("local error: ")
            assert entry["consecutive_local_errors"] == run
            assert runs.orphans() == {file_of(BETA)}
        scraper = await runs.run(routes_for(site))
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_local_errors == [json_url(long)]
        assert would_delete(scraper) == {FW: [file_of(BETA)]}

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    async def test_a_dir_we_may_not_search(self, runs: Runs) -> None:
        """No permission on alpha's dir: alpha/child's file can't be checked or written.

        Unchanged, the page is kept (its etag is still sent) and nothing
        blocks. Changed, it fails to save every run: it blocks until 3, and
        its entry and count survive scrape.py's cleanup, which prunes only
        the entries of files known to be gone.
        """
        await seeded(runs)
        locked = file_of(ALPHA_CHILD).parent
        locked.chmod(0)
        try:
            scraper = await runs.run(routes_for(SITE))
            assert scraper.outcome.blocks == {}
            assert json_url(ALPHA_CHILD) in scraper.hash_manager.touched
            # Alpha/child changes; beta is no longer linked, then gamma (real removals)
            site: Site = {**SITE, ROOT: [ALPHA, GAMMA]}
            removed = {3: [file_of(BETA)], 4: [file_of(GAMMA)]}
            for run in (1, 2, 3, 4):
                if run == 4:
                    site = {**SITE, ROOT: [ALPHA]}
                changed = {ALPHA_CHILD: routes_for(site, version=2)[json_url(ALPHA_CHILD)]}
                scraper = await runs.run(routes_for(site, changed))
                assert runs.logged("error_processing_url") == []
                assert runs.entry(ALPHA_CHILD)["consecutive_local_errors"] == run
                assert scraper.outcome.blocks == ({"local_error": [json_url(ALPHA_CHILD)]} if run < 3 else {})
                # scrape.py's --auto-cleanup: delete the orphans, then prune the entries of deleted files
                report = runs.cleanup(scraper)
                assert report.deleted == ({FW: len(removed[run])} if run in removed else {})
                assert report.failures == []
                for path in removed.get(run, []):
                    assert not path.exists()
            assert scraper.outcome.persistent_local_errors == [json_url(ALPHA_CHILD)]
        finally:
            locked.chmod(0o755)
        assert file_of(ALPHA_CHILD).exists()

    async def test_a_page_back_after_a_404_keeps_its_file(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        await seeded(runs)
        # Alpha 404s in a run that beta's 502 blocks, so alpha's file stays on disk
        # while only its doc-URL key still records it
        await runs.run(routes_for(SITE, {ALPHA: [status(404)], BETA: [status(502)]}))
        assert runs.entry(ALPHA)["status"] == "error" and file_of(ALPHA).exists()
        # Apple serves alpha again, and our converter fails on it
        fail_convert(monkeypatch, ALPHA)
        for run in (1, 2, 3):
            scraper = await runs.run(routes_for(SITE))
            assert runs.entry(ALPHA)["consecutive_local_errors"] == run
            assert runs.orphans() == set()
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_local_errors == [json_url(ALPHA)]

    @pytest.mark.parametrize("held_by", ["block", "valve"])
    async def test_a_page_back_after_d8_keeps_its_file(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, held_by: str
    ) -> None:
        """D8 marked both keys, but that run's cleanup didn't delete the page's file."""
        if held_by == "valve":
            # Alpha and its 5 children are 6 of 9 files: today's >50% valve holds the D8 removal
            kids = [f"{ALPHA}/c{i}" for i in range(5)]
            site: Site = {ROOT: [ALPHA, BETA, GAMMA], ALPHA: kids, BETA: [], GAMMA: [], **{k: [] for k in kids}}
        else:
            site = SITE
        await seeded(runs, site)
        for _ in (1, 2):
            await runs.run(routes_for(site, {ALPHA: [status(502)]}))
        faults = {ALPHA: [status(502)]}
        if held_by == "block":
            faults[BETA] = [status(502)]  # another page's first failure blocks this run
        scraper = await runs.run(routes_for(site, faults))
        assert scraper.outcome.persistent_fetch_failures == [json_url(ALPHA)]
        assert scraper.outcome.skip_cleanup == (held_by == "block")
        # Held: blocked, or the valve holds it for a second clean run
        assert would_delete(scraper) == {}
        saved = runs.saved()["hashes"]
        assert saved[json_url(ALPHA)]["status"] == "error" and saved[doc_url(ALPHA)]["status"] == "error"
        assert file_of(ALPHA) in runs.orphans()

        # Apple serves alpha again (changed), and our converter fails on it
        real_init = AppleJSONDocumentationScraper.__init__
        fail_convert(monkeypatch, ALPHA)
        changed = {ALPHA: routes_for(site, version=2)[json_url(ALPHA)]}
        for run in (1, 2, 3):
            scraper = await runs.run(routes_for(site, changed))
            entry = runs.entry(ALPHA)
            assert entry["consecutive_local_errors"] == run
            # Its JSON-URL key records the file again, with no etag and an unknown hash
            assert entry.get("status") != "error" and entry["file_path"] == str(file_of(ALPHA))
            assert entry["hash"] == "" and "etag" not in entry and "consecutive_failures" not in entry
            assert runs.orphans() == set()
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_local_errors == [json_url(ALPHA)]
        # Never deleted on a local error
        assert would_delete(scraper) == {}

        # The converter is fixed: refetched without an etag, converted and saved again
        monkeypatch.setattr(AppleJSONDocumentationScraper, "__init__", real_init)
        scraper = await runs.run(routes_for(site, changed))
        assert not scraper.outcome.skip_cleanup
        entry = runs.entry(ALPHA)
        assert counters(entry) == {} and entry["hash"] and entry["etag"]
        assert "v2" in file_of(ALPHA).read_text(encoding="utf-8")


class TestRoot:
    async def test_root_404_counts_root_gone_runs(self, runs: Runs) -> None:
        await seeded(runs)
        for run in (1, 2):
            scraper = await runs.run(routes_for(SITE, {ROOT: [status(404)]}))
            outcome = scraper.outcome
            assert outcome.root_gone_runs == run
            assert outcome.skip_cleanup and not outcome.blocked
            assert not outcome.root_fetch_failed
            assert runs.saved()["metadata"]["root_gone_runs"] == run
            event = "root_gone_pending" if run == 1 else "root_gone"
            assert len(runs.logged(event)) == 1
            assert all(not counters(e) for e in runs.saved()["hashes"].values())
            assert would_delete(scraper) == {}
        scraper = await runs.run(routes_for(SITE))
        assert scraper.outcome.root_gone_runs == 0
        assert "root_gone_runs" not in runs.saved()["metadata"]

    @pytest.mark.parametrize("fault", [
        [status(503)], [TIMEOUT], [ok("not json {", "E")], [status(403)], [status(429)],
    ], ids=["503", "timeout", "invalid-json", "403", "429"])
    async def test_root_failure_keeps_everything_and_never_reaches_d8(self, runs: Runs, fault: List[Spec]) -> None:
        await seeded(runs)
        hash_file = Config.get_hash_file(FW)
        data = json.loads(hash_file.read_text())
        data["metadata"]["root_gone_runs"] = 1
        hash_file.write_text(json.dumps(data))
        for _ in range(4):
            scraper = await runs.run(routes_for(SITE, {ROOT: fault}))
            outcome = scraper.outcome
            assert outcome.root_fetch_failed
            assert outcome.blocks == {"root_fetch_failed": [json_url(ROOT)]}
            assert outcome.persistent_fetch_failures == []
            assert counters(runs.entry(ROOT)) == {}
            assert runs.entry(ROOT)["file_path"] == str(file_of(ROOT))
            # Not a 404: root_gone_runs neither counts nor resets
            assert runs.saved()["metadata"]["root_gone_runs"] == 1
            assert file_of(ROOT) not in runs.orphans()

    async def test_root_304_then_failed_refetch_never_reaches_d8(self, runs: Runs) -> None:
        await seeded(runs)
        good = routes_for(SITE)[json_url(ROOT)][0]
        # scrape_page and the queued fetch get a 304; the discovery refetch fails
        fault = [good, good] + [status(502)] * (MAX_RETRIES + 1)
        for _ in range(4):
            scraper = await runs.run(routes_for(SITE, {ROOT: fault}))
            outcome = scraper.outcome
            assert outcome.root_fetch_failed
            assert outcome.blocks == {"root_fetch_failed": [json_url(ROOT)]}
            assert outcome.persistent_fetch_failures == []
            assert counters(runs.entry(ROOT)) == {}
            # The root's links were never read, so only its own file stays touched
            assert runs.orphans() == {file_of(path) for path in SITE if path != ROOT}

    async def test_root_404_then_200_is_live_and_doesnt_block(self, runs: Runs) -> None:
        await seeded(runs)
        await runs.run(routes_for(SITE, {ROOT: [status(404)]}))
        assert runs.saved()["metadata"]["root_gone_runs"] == 1
        # scrape_page gets a 404, then the queued fetch a 200 that no longer links beta
        site = {**SITE, ROOT: [ALPHA, GAMMA]}
        good = routes_for(site)[json_url(ROOT)][0]
        scraper = await runs.run(routes_for(site, {ROOT: [status(404), good]}))
        outcome = scraper.outcome
        assert outcome.blocks == {} and not outcome.skip_cleanup
        assert not outcome.root_fetch_failed and outcome.root_gone_runs == 0
        assert "root_gone_runs" not in runs.saved()["metadata"]
        assert len(runs.logged("root_fetch_conflict")) == 1
        assert runs.entry(ROOT)["file_path"] == str(file_of(ROOT))
        # The whole framework was read: the real removal goes through
        assert would_delete(scraper) == {FW: [file_of(BETA)]}
        # A later 404 run starts the count again
        scraper = await runs.run(routes_for(site, {ROOT: [status(404)]}))
        assert scraper.outcome.root_gone_runs == 1

    @pytest.mark.parametrize("answers", ["200-then-404", "304-then-404", "304-then-refetch-404"])
    async def test_root_404_after_a_200_or_304_blocks_and_resets(self, runs: Runs, answers: str) -> None:
        await seeded(runs)
        hash_file = Config.get_hash_file(FW)
        data = json.loads(hash_file.read_text())
        data["metadata"]["root_gone_runs"] = 1
        hash_file.write_text(json.dumps(data))
        good = routes_for(SITE)[json_url(ROOT)][0]
        changed = routes_for(SITE, version=2)[json_url(ROOT)][0]
        fault = {
            "200-then-404": [changed, status(404)],
            "304-then-404": [good, status(404)],
            "304-then-refetch-404": [good, good, status(404)],
        }[answers]
        scraper = await runs.run(routes_for(SITE, {ROOT: fault}))
        outcome = scraper.outcome
        # The root is live, but the fetch that reads its links failed
        assert outcome.root_fetch_failed
        assert outcome.blocks == {"root_fetch_failed": [json_url(ROOT)]}
        assert outcome.root_gone_runs == 0
        assert "root_gone_runs" not in runs.saved()["metadata"]
        assert len(runs.logged("root_fetch_conflict")) == 1 and runs.logged("page_gone") == []
        entry = runs.entry(ROOT)
        assert entry.get("status") != "error" and entry["file_path"] == str(file_of(ROOT)) and entry["etag"]
        assert counters(entry) == {}
        assert runs.orphans() == {file_of(path) for path in SITE if path != ROOT}

    async def test_root_404_then_200_with_a_local_error_keeps_its_file(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        await seeded(runs)
        fail_convert(monkeypatch, ROOT)
        good = routes_for(SITE)[json_url(ROOT)][0]
        for run in (1, 2, 3):
            scraper = await runs.run(routes_for(SITE, {ROOT: [status(404), good]}))
            assert runs.entry(ROOT)["consecutive_local_errors"] == run
            assert runs.orphans() == set()
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_local_errors == [json_url(ROOT)]

    async def test_new_framework_whose_root_404s_writes_nothing(self, runs: Runs) -> None:
        for _ in range(2):
            scraper = await runs.run({json_url(ROOT): [status(404)]})
            assert scraper.outcome.root_gone_runs == 1
            assert not Path("documentation", FW).exists()
            assert not Config.get_hash_file(FW).exists()
            assert len(runs.logged("skipped_empty_hash_cache")) == 1

    async def test_a_lost_hash_file_next_to_its_docs_still_reaches_2(self, runs: Runs) -> None:
        """With no hash file but the framework's docs on disk, the root-gone count is written."""
        await seeded(runs)
        Config.get_hash_file(FW).unlink()
        for run in (1, 2):
            scraper = await runs.run(routes_for(SITE, {ROOT: [status(404)]}))
            assert scraper.outcome.root_gone_runs == run
            assert runs.saved()["metadata"]["root_gone_runs"] == run
            assert runs.logged("skipped_empty_hash_cache") == []
        for path in SITE:
            assert file_of(path).exists(), path


class TestFailureStorm:
    async def test_storm_isnt_counted_until_its_third_run(self, runs: Runs) -> None:
        leaves = [f"testkit/leaf{i}" for i in range(10)]
        site: Site = {ROOT: leaves, **{leaf: [] for leaf in leaves}}
        await seeded(runs, site)
        failing = {leaf: [status(502)] for leaf in leaves[:6]}  # 6 > max(5, 1% of 11)
        for run in (1, 2):
            scraper = await runs.run(routes_for(site, failing))
            assert scraper.outcome.failure_storm
            assert scraper.outcome.blocks["fetch_failed"] == [json_url(leaf) for leaf in leaves[:6]]
            assert runs.saved()["metadata"]["failure_storm_runs"] == run
            assert all(not counters(runs.entry(leaf)) for leaf in leaves)
            assert runs.logged("failure_storm")[0]["counting"] is False
        scraper = await runs.run(routes_for(site, failing))
        assert runs.saved()["metadata"]["failure_storm_runs"] == 3
        assert runs.logged("failure_storm")[0]["counting"] is True
        assert [runs.entry(leaf).get("consecutive_failures") for leaf in leaves[:6]] == [1] * 6
        # A run under the threshold isn't a storm: the metadata is dropped
        scraper = await runs.run(routes_for(site, {leaves[0]: [status(502)]}))
        assert not scraper.outcome.failure_storm
        assert "failure_storm_runs" not in runs.saved()["metadata"]
        assert runs.entry(leaves[0])["consecutive_failures"] == 2
        assert counters(runs.entry(leaves[1])) == {}

    async def test_a_storm_run_pauses_a_count_without_resetting_it(self, runs: Runs) -> None:
        leaves = [f"testkit/leaf{i}" for i in range(10)]
        site: Site = {ROOT: leaves, **{leaf: [] for leaf in leaves}}
        await seeded(runs, site)
        await runs.run(routes_for(site, {leaves[0]: [status(502)]}))
        assert runs.entry(leaves[0])["consecutive_failures"] == 1
        scraper = await runs.run(routes_for(site, {leaf: [status(502)] for leaf in leaves[:6]}))
        assert scraper.outcome.failure_storm
        assert runs.entry(leaves[0])["consecutive_failures"] == 1
        assert all(not counters(runs.entry(leaf)) for leaf in leaves[1:])


class FrameworkList:
    """Stands in for AppleFrameworkListScraper: technologies.json lists testkit and otherkit."""

    async def __aenter__(self) -> "FrameworkList":
        return self

    async def __aexit__(self, *exc: Any) -> None:
        return None

    async def fetch_all_frameworks(self) -> List[Dict[str, str]]:
        return [{"id": FW, "title": "TestKit"}, {"id": "otherkit", "title": "OtherKit"}]


class TestScrapeEverything:
    """scrape.py's flow: the orphan cleanup leaves blocked frameworks alone, and
    --frameworks never falls back to every framework or to some of the names."""

    async def test_cleanup_skips_a_blocked_framework_and_cleans_the_others(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        other = "otherkit"
        other_site: Site = {other: ["otherkit/one", "otherkit/two", "otherkit/three"],
                            "otherkit/one": [], "otherkit/two": [], "otherkit/three": []}
        await seeded(runs)
        await runs.run(routes_for(other_site), fw=other)
        # testkit: alpha 502 (blocked) and beta unlinked; otherkit: "three" unlinked
        routes = {
            **routes_for({**SITE, ROOT: [ALPHA, GAMMA]}, {ALPHA: [status(502)]}),
            **routes_for({**other_site, other: ["otherkit/one", "otherkit/two"]}),
        }
        apple = Apple(routes)

        class MockedScraper(AppleJSONDocumentationScraper):
            async def __aenter__(self) -> "MockedScraper":
                self.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
                return self

        monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", MockedScraper)
        monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", FrameworkList)
        monkeypatch.setattr(sys, "argv", [
            "scrape.py", "--frameworks", FW, other, "--yes", "--cleanup-orphans", "--auto-cleanup",
        ])
        await scrape_all_frameworks.scrape_everything()
        # Blocked: nothing deleted in testkit (not even the really unlinked beta)
        for path in SITE:
            assert file_of(path).exists(), path
        # Clean: otherkit's unlinked page was deleted
        assert not (Path("documentation") / "otherkit/three.md").exists()
        assert (Path("documentation") / "otherkit/two.md").exists()

    @pytest.mark.parametrize(
        "names",
        [["nosuchkit"], [f"{FW} otherkit"], [], [FW, "Other Kit"]],
        ids=["unknown", "one-unsplit-string", "no-name", "one-unknown"],
    )
    async def test_frameworks_matching_none_scrape_nothing(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], names: List[str]
    ) -> None:
        """Never every framework, and never a partial run: exit code 2, before any scrape or cleanup."""
        await seeded(runs)
        stray = Path("documentation") / FW / "stray.md"
        stray.write_text("# stray\n")
        assert runs.orphans() == {stray}
        scraped: List[Dict[str, Any]] = []

        async def scrape_frameworks(**kwargs: Any) -> Dict[str, Any]:
            scraped.append(kwargs)
            return {"framework_outcomes": []}

        monkeypatch.setattr(scrape_all_frameworks, "scrape_frameworks", scrape_frameworks)
        monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", FrameworkList)
        monkeypatch.setattr(sys, "argv", [
            "scrape.py", "--frameworks", *names, "--yes", "--cleanup-orphans", "--auto-cleanup",
        ])
        capsys.readouterr()
        assert await scrape_all_frameworks.scrape_everything() == 2
        assert scraped == []
        assert stray.exists()
        out = capsys.readouterr().out
        if names:
            assert f"Not a framework id or title in technologies.json: {names[-1]}. Nothing scraped." in out
        else:
            assert "--frameworks needs at least one framework name. Nothing scraped." in out

        # Every name an id or a title, in any casing (Apple flips a
        # framework's URL casing; "OtherKit" is its title and "TESTKIT" its
        # id, "otherkit" both): only those frameworks, each once, exit code 0
        monkeypatch.setattr(sys, "argv", ["scrape.py", "--frameworks", "TESTKIT", "OtherKit", "otherkit", "--yes"])
        assert await scrape_all_frameworks.scrape_everything() == 0
        [call] = scraped
        assert call["framework_list"] == await FrameworkList().fetch_all_frameworks()
        assert "Not a framework id or title" not in capsys.readouterr().out

    async def test_an_empty_framework_list_scrapes_nothing(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        class EveryFramework(FrameworkList):
            async def fetch_all_frameworks(self) -> List[Dict[str, str]]:
                raise AssertionError("fell back to every framework")

        monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", EveryFramework)
        stats = await scrape_all_frameworks.scrape_frameworks(framework_list=[])
        assert stats is not None
        assert stats["total_frameworks"] == 0 and stats["framework_outcomes"] == []

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    async def test_a_failed_hash_save_fails_the_framework_and_keeps_its_files(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """No permission to write the hash dir: the run's entries never reach the hash file.

        Against the previous run's file, zeta (added and saved this run) would
        be an orphan, so the framework fails and its cleanup is skipped.
        """
        await seeded(runs)
        hash_file = Config.get_hash_file(FW)
        saved = hash_file.read_text()
        apple = Apple(routes_for({**SITE, ROOT: [*SITE[ROOT], NEW], NEW: []}))

        class MockedScraper(AppleJSONDocumentationScraper):
            async def __aenter__(self) -> "MockedScraper":
                self.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
                return self

        monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", MockedScraper)
        monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", FrameworkList)
        monkeypatch.setattr(sys, "argv", [
            "scrape.py", "--frameworks", FW, "--yes", "--cleanup-orphans", "--auto-cleanup",
        ])
        capsys.readouterr()
        hash_file.parent.chmod(0o555)
        try:
            await scrape_all_frameworks.scrape_everything()
        finally:
            hash_file.parent.chmod(0o755)
        out = capsys.readouterr().out
        assert f"Failed: TestKit - failed to save hash file {hash_file}" in out
        assert f"Cleanup skipped this run for 1 frameworks: {FW} (raised)" in out
        assert hash_file.read_text() == saved
        for path in [*SITE, NEW]:
            assert file_of(path).exists(), path

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    async def test_prune_counts_only_entries_it_saved(self, runs: Runs) -> None:
        """No permission to write the hash dir after the scrape's save: the prune is lost, and reported."""
        await seeded(runs)
        scraper = await runs.run(routes_for({**SITE, ROOT: [ALPHA, GAMMA]}))  # beta is unlinked
        hash_dir = Config.get_hash_file(FW).parent
        hash_dir.chmod(0o555)
        try:
            report = runs.cleanup(scraper)
        finally:
            hash_dir.chmod(0o755)
        assert report.deleted == {FW: 1} and not file_of(BETA).exists()
        assert report.pruned == 0
        assert report.failures == [f"{FW}: hash file save failed ({Config.get_hash_file(FW)})"]
        assert json_url(BETA) in runs.saved()["hashes"]
        # The next deletion in the framework (gamma, unlinked too) prunes them,
        # with gamma's: each page's JSON-URL and doc-URL keys
        scraper = await runs.run(routes_for({**SITE, ROOT: [ALPHA]}))
        report = runs.cleanup(scraper)
        assert report.deleted == {FW: 1} and report.failures == [] and report.pruned == 4
        assert json_url(BETA) not in runs.saved()["hashes"] and json_url(GAMMA) not in runs.saved()["hashes"]

    async def test_framework_exception_is_an_outcome(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        async def boom(self: AppleJSONDocumentationScraper) -> Dict[str, Any]:
            raise RuntimeError("bug")

        monkeypatch.setattr(AppleJSONDocumentationScraper, "scrape_framework", boom)
        stats = await scrape_all_frameworks.scrape_frameworks(framework_list=[{"id": FW, "title": "TestKit"}])
        assert stats is not None
        [outcome] = stats["framework_outcomes"]
        assert outcome.framework_id == FW and outcome.raised == "bug"
        assert outcome.blocked and outcome.skip_cleanup
        assert stats["failed_frameworks"] == 1

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    async def test_a_failed_hash_save_doesnt_hide_the_scrape_exception(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        await seeded(runs)

        async def boom(self: AppleJSONDocumentationScraper) -> Dict[str, Any]:
            self.hash_manager.set_counter(json_url(ROOT), "consecutive_failures", 1)
            raise RuntimeError("bug")

        monkeypatch.setattr(AppleJSONDocumentationScraper, "scrape_framework", boom)
        hash_dir = Config.get_hash_file(FW).parent
        hash_dir.chmod(0o555)
        try:
            stats = await scrape_all_frameworks.scrape_frameworks(framework_list=[{"id": FW, "title": "TestKit"}])
        finally:
            hash_dir.chmod(0o755)
        assert stats is not None
        [outcome] = stats["framework_outcomes"]
        assert outcome.raised == "bug" and outcome.skip_cleanup


class TestHashFileThatFailsToLoad:
    """A hash file that exists but loads nothing (e.g. a hand edit, a merge
    conflict marker, a truncated copy): the run can't tell the pages we have
    from new ones, so it blocks, and its save replaces the file."""

    @staticmethod
    def break_hash_file(how: str) -> Path:
        hash_file = Config.get_hash_file(FW)
        text = hash_file.read_text()
        broken = {
            "truncated": text[: len(text) // 2].encode(),
            "not-utf8": b"\xff" + text.encode(),
            "not-a-hash-file": b"[]",
        }[how]
        hash_file.write_bytes(broken)
        return hash_file

    @pytest.mark.parametrize("how", ["truncated", "not-utf8", "not-a-hash-file"])
    async def test_a_failing_page_we_have_still_takes_3_runs(self, runs: Runs, how: str) -> None:
        """Beta, a page we have, answers 403: its file on disk shows it is ours."""
        await seeded(runs)
        hash_file = self.break_hash_file(how)
        scraper = await runs.run(routes_for(SITE, {BETA: [status(403)]}))
        assert scraper.hash_manager.load_error is not None
        outcome = scraper.outcome
        assert outcome.blocks == {"hash_load_failed": [str(hash_file)], "fetch_failed": [json_url(BETA)]}
        assert outcome.skip_cleanup and outcome.persistent_fetch_failures == []
        # The file was replaced, and records beta as a page we have
        assert HashManager(hash_file).load_error is None
        entry = runs.entry(BETA)
        assert entry.get("status") != "error" and entry["file_path"] == str(file_of(BETA))
        assert entry["consecutive_failures"] == 1
        assert runs.orphans() == set()

        scraper = await runs.run(routes_for(SITE, {BETA: [status(403)]}))
        assert scraper.outcome.blocks == {"fetch_failed": [json_url(BETA)]}
        assert runs.entry(BETA)["consecutive_failures"] == 2
        scraper = await runs.run(routes_for(SITE, {BETA: [status(403)]}))
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_fetch_failures == [json_url(BETA)]
        assert would_delete(scraper) == {FW: [file_of(BETA)]}

    async def test_cleanup_waits_one_run(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        """scrape.py's flow: beta is really unlinked; it goes on the next run."""
        await seeded(runs)
        hash_file = self.break_hash_file("truncated")
        apple = Apple(routes_for({**SITE, ROOT: [ALPHA, GAMMA]}))

        class MockedScraper(AppleJSONDocumentationScraper):
            async def __aenter__(self) -> "MockedScraper":
                self.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
                return self

        monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", MockedScraper)
        monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", FrameworkList)
        monkeypatch.setattr(sys, "argv", [
            "scrape.py", "--frameworks", FW, "--yes", "--cleanup-orphans", "--auto-cleanup",
        ])
        capsys.readouterr()
        await scrape_all_frameworks.scrape_everything()
        assert f"Cleanup skipped this run for 1 frameworks: {FW} (hash_load_failed x1)" in capsys.readouterr().out
        assert file_of(BETA).exists()
        assert HashManager(hash_file).load_error is None

        await scrape_all_frameworks.scrape_everything()
        assert "Cleanup skipped" not in capsys.readouterr().out
        assert not file_of(BETA).exists()
        for path in (ROOT, ALPHA, ALPHA_CHILD, GAMMA):
            assert file_of(path).exists(), path

    async def test_a_gone_root_still_reaches_2(self, runs: Runs) -> None:
        """Holding nothing worth saving, the run still replaces the file, so the count goes on."""
        await seeded(runs)
        hash_file = self.break_hash_file("truncated")
        scraper = await runs.run(routes_for(SITE, {ROOT: [status(404)]}))
        assert scraper.outcome.blocks == {"hash_load_failed": [str(hash_file)]}
        assert scraper.outcome.root_gone_runs == 1
        assert runs.saved()["metadata"]["root_gone_runs"] == 1
        assert runs.logged("skipped_empty_hash_cache") == []

        scraper = await runs.run(routes_for(SITE, {ROOT: [status(404)]}))
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.root_gone_runs == 2
        assert runs.saved()["metadata"]["root_gone_runs"] == 2

    async def test_a_failing_root_then_a_gone_root_reaches_2(self, runs: Runs) -> None:
        """The failed-load run records only the root's JSON-URL key, which the root's
        404s then mark as an error: no entry has a file_path, yet the count is written."""
        await seeded(runs)
        self.break_hash_file("truncated")
        await runs.run(routes_for(SITE, {ROOT: [status(503)]}))
        assert list(runs.saved()["hashes"]) == [json_url(ROOT)]
        for run in (1, 2):
            scraper = await runs.run(routes_for(SITE, {ROOT: [status(404)]}))
            assert scraper.outcome.root_gone_runs == run
            assert runs.saved()["metadata"]["root_gone_runs"] == run
            assert all(not entry.get("file_path") for entry in runs.saved()["hashes"].values())
        for path in SITE:
            assert file_of(path).exists(), path


class TestLostEntries:
    """A page we have whose entry was lost: no entry records its URL, but its
    file is on disk. A hash file that failed to load or save leaves that state
    for later runs, as does a deleted one, so a failure on the page must still
    take D8's 3 runs, as it does with its entry."""

    @staticmethod
    async def fails_3_runs_then_d8(runs: Runs, victim: str, site: Site = SITE) -> None:
        """The victim answers 403 three runs in a row: kept and blocking twice, then D8."""
        for run in (1, 2):
            scraper = await runs.run(routes_for(site, {victim: [status(403)]}))
            assert scraper.outcome.blocks == {"fetch_failed": [json_url(victim)]}
            entry = runs.entry(victim)
            assert entry.get("status") != "error" and entry["file_path"] == str(file_of(victim))
            assert entry["consecutive_failures"] == run
            assert runs.orphans() == set()
        scraper = await runs.run(routes_for(site, {victim: [status(403)]}))
        assert scraper.outcome.blocks == {}
        assert scraper.outcome.persistent_fetch_failures == [json_url(victim)]
        assert would_delete(scraper) == {FW: [file_of(victim)]}

    @pytest.mark.parametrize("cut", ["parent-502", "root-503"])
    async def test_a_page_a_failed_load_run_never_reached(self, runs: Runs, cut: str) -> None:
        """That run's save records only the pages it reached: alpha's 502 (or
        the root's 503) cut the victim off, so its entry is gone."""
        await seeded(runs)
        TestHashFileThatFailsToLoad.break_hash_file("truncated")
        if cut == "parent-502":
            victim, fault = ALPHA_CHILD, {ALPHA: [status(502)]}
        else:
            victim, fault = BETA, {ROOT: [status(503)]}
        scraper = await runs.run(routes_for(SITE, fault))
        assert "hash_load_failed" in scraper.outcome.blocks
        assert json_url(victim) not in runs.saved()["hashes"]
        await self.fails_3_runs_then_d8(runs, victim)

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    async def test_a_page_saved_in_a_run_whose_hash_save_failed(self, runs: Runs) -> None:
        """The failed save keeps the previous file, which lacks zeta, added and saved that run."""
        await seeded(runs)
        site: Site = {**SITE, ROOT: [*SITE[ROOT], NEW], NEW: []}
        hash_dir = Config.get_hash_file(FW).parent
        hash_dir.chmod(0o555)
        try:
            with pytest.raises(OSError, match="failed to save hash file"):
                await runs.run(routes_for(site))
        finally:
            hash_dir.chmod(0o755)
        assert file_of(NEW).exists()
        assert json_url(NEW) not in runs.saved()["hashes"]
        await self.fails_3_runs_then_d8(runs, NEW, site)

    async def test_a_deleted_hash_file(self, runs: Runs) -> None:
        await seeded(runs)
        Config.get_hash_file(FW).unlink()
        await self.fails_3_runs_then_d8(runs, BETA)

    async def test_an_error_entry_is_judged_by_it(self, runs: Runs) -> None:
        """Beta answered 404 in a blocked run, so its file is still on disk. A
        403 next run is a never-good 4xx: it neither blocks nor keeps the file."""
        await seeded(runs)
        scraper = await runs.run(routes_for(SITE, {ALPHA: [status(502)], BETA: [status(404)]}))
        assert scraper.outcome.blocks == {"fetch_failed": [json_url(ALPHA)]}
        assert file_of(BETA).exists()
        scraper = await runs.run(routes_for(SITE, {BETA: [status(403)]}))
        assert not scraper.outcome.skip_cleanup
        assert runs.entry(BETA)["status"] == "error"
        assert would_delete(scraper) == {FW: [file_of(BETA)]}


class TestRenderVersion:
    """4.13: a framework rendered by another RENDER_VERSION is rendered again whole (every page
    fetched without its etag and written), and the new version is stored only after a clean run."""

    @staticmethod
    def bump(monkeypatch: pytest.MonkeyPatch, version: int = 2) -> None:
        monkeypatch.setattr(AppleJSONDocumentationScraper, "RENDER_VERSION", version)

    @staticmethod
    def stored() -> Any:
        return Runs.saved()["metadata"].get("render")

    async def test_a_stale_framework_is_rendered_again_then_answers_304(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        await seeded(runs)
        assert self.stored() == {"version": AppleJSONDocumentationScraper.RENDER_VERSION}
        for path in SITE:
            file_of(path).write_text("# an older rendering\n", encoding="utf-8")
        hashes_before = runs.saved()["hashes"]
        self.bump(monkeypatch)
        scraper = await runs.run(routes_for(SITE))
        assert scraper.stats["pages_skipped"] == 0 and scraper.stats["pages_scraped"] >= len(SITE)
        for path in SITE:
            assert f"The {path} page." in file_of(path).read_text(encoding="utf-8"), path
        assert runs.logged("render_version_stale") and runs.logged("render_version_stored")
        saved = runs.saved()
        assert saved["metadata"]["render"] == {"version": 2}
        assert saved["hashes"] == hashes_before  # same JSON, same etags and files
        # The next run of the same version: every page answers 304, nothing is written
        hash_file = Config.get_hash_file(FW)
        before = hash_file.read_bytes()
        scraper = await runs.run(routes_for(SITE))
        assert scraper.stats["pages_scraped"] == 0 and scraper.stats["pages_skipped"] >= len(SITE)
        assert hash_file.read_bytes() == before and not runs.logged("render_version_stale")

    async def test_pages_the_storing_run_didnt_reach_are_rendered_when_back(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Their files keep the old rendering (here held by the valve): the run that stores the
        version drops their hash and etag, so they are rendered when Apple links them again unchanged."""
        await seeded(runs)
        for path in SITE:
            file_of(path).write_text("# an older rendering\n", encoding="utf-8")
        unreached = (ALPHA, ALPHA_CHILD, BETA, GAMMA)
        root_only = routes_for({**SITE, ROOT: []})
        # A run of the stored version that doesn't reach them leaves their entries alone
        entries = {path: runs.entry(path) for path in unreached}
        await runs.run(root_only)
        assert {path: runs.entry(path) for path in unreached} == entries
        hash_file = Config.get_hash_file(FW)
        data = runs.saved()
        data["hashes"][json_url(GAMMA)]["consecutive_local_errors"] = 1
        hash_file.write_text(json.dumps(data, indent=2, sort_keys=True))
        self.bump(monkeypatch)
        scraper = await runs.run(root_only)  # clean, 4 of 5 files unreached
        assert self.stored() == {"version": 2}
        for path in unreached:
            entry = runs.entry(path)
            assert entry["hash"] == "" and "etag" not in entry and entry["file_path"] == str(file_of(path)), path
        assert counters(runs.entry(GAMMA)) == {"consecutive_local_errors": 1}
        assert runs.entry(ROOT)["hash"] and runs.entry(ROOT)["etag"]
        report = runs.cleanup(scraper)
        assert report.deleted == {} and report.held == {FW: (4, 5)}
        assert runs.saved()["metadata"]["pending_orphans"] == sorted(str(file_of(path)) for path in unreached)
        # A run of the stored version that still doesn't reach them writes nothing
        before = hash_file.read_bytes()
        await runs.run(root_only)
        assert hash_file.read_bytes() == before and not runs.logged("render_version_stale")
        # Linked again, JSON unchanged: fetched without an etag and rendered; nothing is orphaned
        scraper = await runs.run(routes_for(SITE))
        for path in SITE:
            assert f"The {path} page." in file_of(path).read_text(encoding="utf-8"), path
        report = runs.cleanup(scraper)
        assert report.deleted == {} and report.held == {} and "pending_orphans" not in runs.saved()["metadata"]
        assert all(runs.entry(path)["hash"] and runs.entry(path)["etag"] for path in unreached)
        # Then every page answers 304 and nothing is written
        before = hash_file.read_bytes()
        scraper = await runs.run(routes_for(SITE))
        assert scraper.stats["pages_scraped"] == 0 and hash_file.read_bytes() == before

    async def test_a_blocked_run_keeps_the_stored_version(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        await seeded(runs)
        self.bump(monkeypatch)
        scraper = await runs.run(routes_for(SITE, {BETA: [status(502)]}))
        assert scraper.outcome.blocked
        assert self.stored() == {"version": 1}
        # Still stale: the next (clean) run renders every page again and stores it
        scraper = await runs.run(routes_for(SITE))
        assert scraper.stats["pages_skipped"] == 0 and self.stored() == {"version": 2}

    async def test_a_root_gone_run_stores_nothing(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        await seeded(runs)
        self.bump(monkeypatch)
        scraper = await runs.run(routes_for(SITE, {ROOT: [status(404)]}))
        assert scraper.outcome.root_gone_runs == 1 and not scraper.outcome.blocked
        assert self.stored() == {"version": 1}

    async def test_a_persistent_local_error_keeps_the_version_unstored(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """The page's old file is kept and its etag still matches: only an unstored version renders it again."""
        await seeded(runs)
        self.bump(monkeypatch)
        fail_convert(monkeypatch, ALPHA)
        for run in range(1, PERSISTENT_FAILURE_RUNS + 1):
            scraper = await runs.run(routes_for(SITE))
            assert scraper.outcome.blocked == (run < PERSISTENT_FAILURE_RUNS), run
            assert self.stored() == {"version": 1}, run
        assert scraper.outcome.persistent_local_errors == [json_url(ALPHA)]

    async def test_a_filename_clash_doesnt_keep_the_framework_stale(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        await seeded(runs)
        self.bump(monkeypatch)
        clashing = "testkit/alpha-"  # seg_name strips the "-"
        site: Site = {**SITE, ROOT: [*SITE[ROOT], clashing], clashing: []}
        scraper = await runs.run(routes_for(site))
        assert scraper.outcome.filename_clashes == [json_url(clashing)] and not scraper.outcome.skip_cleanup
        assert self.stored() == {"version": 2}

    async def test_the_end_of_run_prune_keeps_the_stored_version(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """cleanup_orphans_at_end's manager passes no version: its prune-save keeps render."""
        await seeded(runs)
        stray = Config.OUTPUT_DIR / FW / "stray.md"
        stray.write_text("# stray\n")
        scraper = await runs.run(routes_for({**SITE, ROOT: [ALPHA, BETA]}))
        report = runs.cleanup(scraper)
        assert report.failures == [] and report.pruned > 0
        assert not stray.exists() and not file_of(GAMMA).exists()
        assert self.stored() == {"version": 1}
