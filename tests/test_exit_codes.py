"""scrape.py's exit code (2.2), through scrape_everything.

- 0: a clean run, also when a root returned 404/410 (removed at 2 runs) or
  the valve holds a mass removal for confirmation;
- 1: an error of ours: a framework raised, its cleanup was blocked (a failed
  request, a local error, zero touched), a page failed persistently (no
  longer blocking), the orphan cleanup failed, or the re-indexing failed;
- 2: aborted before scraping: the list guard, a --frameworks name that is no
  framework, a --resume target that isn't listed (or missing);
- 130: interrupted.

Consecutive runs over the test_failure_policy sandbox, against a fake Apple.
"""

import asyncio
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterator, List, Sequence, Type

import httpx
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import scrape_all_frameworks
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.hash_manager import HashManager
from tests.test_failure_policy import (
    ALPHA, BETA, FW, GAMMA, ROOT, SITE, Apple, FrameworkList, Runs, Site, fail_convert, file_of,
    routes_for, sandbox_runs, seeded,
)
from tests.test_fetch_results import Spec, status

CI = ["--yes", "--cleanup-orphans", "--auto-cleanup"]
OTHER = "otherkit"
OTHER_SITE: Site = {OTHER: [f"{OTHER}/one", f"{OTHER}/two"], f"{OTHER}/one": [], f"{OTHER}/two": []}


@pytest.fixture
def runs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Runs]:
    yield sandbox_runs(tmp_path, monkeypatch)


def mocked(apple: Apple) -> Type[AppleJSONDocumentationScraper]:
    class MockedScraper(AppleJSONDocumentationScraper):
        async def __aenter__(self) -> "MockedScraper":
            self.session = httpx.AsyncClient(transport=httpx.MockTransport(apple), follow_redirects=True)
            return self

    return MockedScraper


async def scrape(monkeypatch: pytest.MonkeyPatch, routes: Dict[str, List[Spec]], *args: str,
                 listing: Type[Any] = FrameworkList) -> int:
    """One scrape.py run (scrape_everything) against a fake Apple; its exit code."""
    monkeypatch.setattr(scrape_all_frameworks, "AppleJSONDocumentationScraper", mocked(Apple(routes)))
    monkeypatch.setattr(scrape_all_frameworks, "AppleFrameworkListScraper", listing)
    monkeypatch.setattr(sys, "argv", ["scrape.py", *args])
    code: int = await scrape_all_frameworks.scrape_everything()
    return code


def stray() -> Path:
    """An unlinked .md file in testkit: an orphan a clean run's cleanup deletes."""
    path = Config.OUTPUT_DIR / FW / "stray.md"
    path.write_text("# stray\n")
    return path


class TestExit0:
    async def test_a_clean_run(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                               capsys: pytest.CaptureFixture[str]) -> None:
        await seeded(runs)
        orphan = stray()
        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(SITE), "--frameworks", FW, *CI) == 0
        out = capsys.readouterr().out
        assert "🎉 SCRAPING COMPLETED SUCCESSFULLY!" in out and "Errors of ours" not in out
        assert not orphan.exists()

    async def test_every_framework(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """--all, as CI runs it: the list (here testkit and otherkit) is fetched and checked."""
        await seeded(runs)
        assert await scrape(monkeypatch, {**routes_for(SITE), **routes_for(OTHER_SITE)}, "--all", *CI) == 0
        assert all(file_of(path).exists() for path in SITE)
        assert (Config.OUTPUT_DIR / OTHER / "one.md").exists()

    async def test_a_root_gone_twice_is_a_removal_not_an_error(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        await seeded(runs)
        routes = routes_for(SITE, {ROOT: [status(404)]})
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 0
        assert file_of(ROOT).exists()
        capsys.readouterr()
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 0
        assert "Removed 1 frameworks whose root returned 404/410" in capsys.readouterr().out
        assert not (Config.OUTPUT_DIR / FW).exists() and not Config.get_hash_file(FW).exists()

    async def test_a_valve_hold_is_not_an_error(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                                capsys: pytest.CaptureFixture[str]) -> None:
        """3 of 5 files unlinked: held in pending_orphans, then confirmed and deleted."""
        await seeded(runs)
        routes = routes_for({**SITE, ROOT: [GAMMA]})
        capsys.readouterr()
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 0
        assert "Held by the valve" in capsys.readouterr().out
        assert all(file_of(path).exists() for path in SITE)
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 0
        assert not file_of(ALPHA).exists() and file_of(GAMMA).exists()


class TestExit1:
    @pytest.mark.parametrize("fault", [[status(502)], [status(403)]], ids=["502", "403"])
    async def test_a_blocked_framework_then_a_persistent_failure(
        self, runs: Runs, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], fault: List[Spec]
    ) -> None:
        """Runs 1-2 block (nothing deleted); run 3 no longer blocks (D8 deletes) but still flags the run."""
        await seeded(runs)
        routes = routes_for(SITE, {BETA: fault})
        for run in (1, 2):
            capsys.readouterr()
            assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 1
            out = capsys.readouterr().out
            assert "SCRAPING COMPLETED, WITH ERRORS" in out
            assert f"Errors of ours this run (1), exit code 1:\n   - {FW}: fetch_failed x1\n" in out
            assert file_of(BETA).exists() and Runs.entry(BETA)["consecutive_failures"] == run
        capsys.readouterr()
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 1
        assert f"   - {FW}: persistent_fetch_failure x1\n" in capsys.readouterr().out
        assert not file_of(BETA).exists()

    async def test_a_persistent_local_error(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                            capsys: pytest.CaptureFixture[str]) -> None:
        await seeded(runs)
        fail_convert(monkeypatch, BETA)
        routes = routes_for(SITE, version=2)  # every page changed, so beta is converted again
        for run in (1, 2):
            capsys.readouterr()
            assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 1
            assert f"   - {FW}: local_error x1\n" in capsys.readouterr().out
            assert Runs.entry(BETA)["consecutive_local_errors"] == run
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 1
        assert f"   - {FW}: persistent_local_error x1\n" in capsys.readouterr().out
        assert file_of(BETA).exists()  # never deleted on a local error

    async def test_a_framework_that_raised(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                           capsys: pytest.CaptureFixture[str]) -> None:
        await seeded(runs)
        orphan = stray()

        async def boom(self: AppleJSONDocumentationScraper) -> Dict[str, Any]:
            raise RuntimeError("bug")

        monkeypatch.setattr(AppleJSONDocumentationScraper, "scrape_framework", boom)
        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(SITE), "--frameworks", FW, *CI) == 1
        assert f"   - {FW}: raised: bug\n" in capsys.readouterr().out
        assert orphan.exists()

    async def test_zero_touched(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                capsys: pytest.CaptureFixture[str]) -> None:
        """A session-tracking bug of ours: no entry got this run's session_id."""
        await seeded(runs)
        orphan = stray()
        monkeypatch.setattr(HashManager, "touch", lambda self, url: None)
        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(SITE), "--frameworks", FW, *CI) == 1
        assert f"   - {FW}: zero_touched x1\n" in capsys.readouterr().out
        assert orphan.exists()

    @pytest.mark.skipif(hasattr(os, "geteuid") and os.geteuid() == 0, reason="root ignores file permissions")
    async def test_a_failed_cleanup(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                    capsys: pytest.CaptureFixture[str]) -> None:
        """The root-gone x2 removal can't delete the docs dir: exit 1, and the next run removes it."""
        await seeded(runs)
        routes = routes_for(SITE, {ROOT: [status(404)]})
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 0
        Config.OUTPUT_DIR.chmod(0o555)
        try:
            capsys.readouterr()
            assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 1
        finally:
            Config.OUTPUT_DIR.chmod(0o755)
        out = capsys.readouterr().out
        assert "🎉 SCRAPING COMPLETED SUCCESSFULLY!" in out  # the scrape itself was clean
        assert f"   - cleanup: {FW}: removal failed:" in out
        assert await scrape(monkeypatch, routes, "--frameworks", FW, *CI) == 0
        assert not (Config.OUTPUT_DIR / FW).exists() and not Config.get_hash_file(FW).exists()

    async def test_a_failed_reindex(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                    capsys: pytest.CaptureFixture[str]) -> None:
        await seeded(runs)

        def failed_run(cmd: Sequence[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
            return subprocess.CompletedProcess(cmd, 1, "", "meilisearch unavailable")

        monkeypatch.setattr(subprocess, "run", failed_run)
        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(SITE), "--frameworks", FW, "--yes", "--trigger-reindex") == 1
        assert "   - re-indexing failed with return code 1\n" in capsys.readouterr().out


class TestExit2:
    """Aborted before scraping: nothing is scraped or cleaned."""

    @staticmethod
    def untouched(before: Dict[str, bytes]) -> bool:
        return before == {str(p): p.read_bytes() for p in sorted(Path(".").rglob("*")) if p.is_file()}

    @pytest.mark.parametrize("args", [
        ["--all", *CI],
        ["--frameworks", FW, *CI],
    ], ids=["all", "frameworks"])
    async def test_an_empty_framework_list(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                           capsys: pytest.CaptureFixture[str], args: List[str]) -> None:
        """framework_list_scraper returns [] when the fetch fails."""
        await seeded(runs)
        stray()
        before = {str(p): p.read_bytes() for p in sorted(Path(".").rglob("*")) if p.is_file()}

        class NoFrameworks(FrameworkList):
            async def fetch_all_frameworks(self) -> List[Dict[str, str]]:
                return []

        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(SITE), *args, listing=NoFrameworks) == 2
        assert "technologies.json listed 0 frameworks" in capsys.readouterr().out
        assert self.untouched(before)

    async def test_a_short_framework_list(self, runs: Runs, monkeypatch: pytest.MonkeyPatch) -> None:
        """2 listed for 3 framework hash files; with the 3rd counted as unlisted (2.5), the run goes on."""
        await seeded(runs)
        await runs.run(routes_for(OTHER_SITE), fw=OTHER)
        await runs.run(routes_for({"thirdkit": []}), fw="thirdkit")
        stray()
        before = {str(p): p.read_bytes() for p in sorted(Path(".").rglob("*")) if p.is_file()}
        routes = {**routes_for(SITE), **routes_for(OTHER_SITE)}
        assert await scrape(monkeypatch, routes, "--all", *CI) == 2
        assert self.untouched(before)
        manager = HashManager(Config.get_hash_file("thirdkit"))
        manager.set_metadata("unlisted_runs", 1)
        assert manager.save()
        assert await scrape(monkeypatch, routes, "--all", *CI) == 0

    @pytest.mark.parametrize("args", [
        ["--resume", "nosuchkit"],
        ["--resume"],
        ["--resume", "--yes"],
    ], ids=["not-listed", "no-name", "flag-after"])
    async def test_a_resume_target_not_found(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                             capsys: pytest.CaptureFixture[str], args: List[str]) -> None:
        await seeded(runs)
        stray()
        before = {str(p): p.read_bytes() for p in sorted(Path(".").rglob("*")) if p.is_file()}
        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(SITE), *args, "--all", *CI) == 2
        out = capsys.readouterr().out
        if args[1:] == ["nosuchkit"]:
            assert "Could not find framework 'nosuchkit' to resume from. Nothing scraped." in out
        else:
            assert "--resume needs the framework to resume from" in out
        assert self.untouched(before)

    async def test_resume_from_a_listed_framework_any_casing(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                                                             capsys: pytest.CaptureFixture[str]) -> None:
        """FrameworkList lists testkit then otherkit: resuming from OTHERKIT scrapes otherkit only."""
        await seeded(runs)
        orphan = stray()
        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(OTHER_SITE), "--resume", "OTHERKIT", "--all", *CI) == 0
        assert "Will scrape 1 frameworks" in capsys.readouterr().out
        assert orphan.exists() and (Config.OUTPUT_DIR / OTHER / "one.md").exists()


class TestExit130:
    @pytest.mark.parametrize("interrupt", [KeyboardInterrupt, asyncio.CancelledError],
                             ids=["KeyboardInterrupt", "CancelledError"])
    async def test_interrupted(self, runs: Runs, monkeypatch: pytest.MonkeyPatch,
                               capsys: pytest.CaptureFixture[str], interrupt: Type[BaseException]) -> None:
        """Under asyncio.run, Ctrl-C reaches the coroutine as a cancellation. No cleanup runs."""
        await seeded(runs)
        orphan = stray()

        async def interrupted(**kwargs: Any) -> Dict[str, Any]:
            raise interrupt()

        monkeypatch.setattr(scrape_all_frameworks, "scrape_frameworks", interrupted)
        capsys.readouterr()
        assert await scrape(monkeypatch, routes_for(SITE), "--frameworks", FW, *CI) == 130
        assert "Scraping interrupted by user" in capsys.readouterr().out
        assert orphan.exists()
