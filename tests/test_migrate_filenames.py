"""The filename migration (scripts/utilities/migrate_filenames.py), on a small git repo.

One framework, TestKit, with every case the migration handles: files that
move (also into a "-page" folder, leaving an empty dir), files that stay,
files two pages wrote (the footer names the owner; the other page gets no
file, and may take over the path the owner leaves), a file-less live page,
a pending removal (a tracked file no live entry records) and
metadata.pending_orphans. Then the idempotence run, the checks that
stop it before anything changes, and its refusals to run elsewhere.
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts', 'utilities')))

import migrate_filenames
from scraper.config import Config

FW = "TestKit"
JSON = "https://developer.apple.com/tutorials/data/documentation"
DOC = "https://developer.apple.com/documentation"
DOCS = Path("documentation") / FW


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def case_sensitive(path: Path) -> bool:
    """Whether the filesystem holding path tells names apart by case."""
    probe = path / "CaseProbe"
    probe.write_text("")
    try:
        return not (path / "caseprobe").exists()
    finally:
        probe.unlink()


class Repo:
    """A git repo (cwd) holding TestKit's docs and hash file."""

    def __init__(self) -> None:
        self.hashes: Dict[str, Dict[str, Any]] = {}
        self.metadata: Dict[str, Any] = {}

    def page(self, path: str, file: Optional[str], footer: Optional[str] = None, live: bool = True,
             write: bool = True) -> None:
        """A page's two keys, recording DOCS/file; the file, with its footer (path's doc URL by default)."""
        json_key = f"{JSON}/{path}.json"
        doc_key = f"{DOC}/{path}"
        recorded = str(DOCS / file) if file else None
        entry: Dict[str, Any] = {"hash": f"h-{path}"}
        if recorded:
            entry["file_path"] = recorded
        self.hashes[json_key] = dict(entry) if live else {"status": "error", "error": "HTTP 404"}
        self.hashes[doc_key] = dict(entry)
        if recorded and write:
            self.write(recorded, footer or doc_key)

    @staticmethod
    def write(recorded: str, footer: str) -> None:
        Path(recorded).parent.mkdir(parents=True, exist_ok=True)
        Path(recorded).write_text(f"# page\n\nText.\n\n---\n\n*[View on Apple Developer]({footer})*\n")

    def save(self) -> None:
        data = {"metadata": {"total_pages": len(self.hashes), **self.metadata}, "hashes": self.hashes}
        Path(".hashes").mkdir(exist_ok=True)
        Path(f".hashes/{FW}_hashes.json").write_text(json.dumps(data, indent=2, sort_keys=True))

    def commit(self, message: str) -> None:
        git("add", "-A")
        git("commit", "-qm", message)

    @staticmethod
    def saved() -> Dict[str, Any]:
        data: Dict[str, Any] = json.loads(Path(f".hashes/{FW}_hashes.json").read_text())
        return data

    @staticmethod
    def files() -> List[str]:
        return sorted(str(p) for p in Path("documentation").rglob("*") if p.is_file())


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[Repo]:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(Config, "OUTPUT_DIR", Path("documentation"))
    monkeypatch.setattr(Config, "CACHE_DIR", Path(".hashes"))
    git("init", "-q")
    git("config", "user.email", "test@example.com")
    git("config", "user.name", "Test")
    # Leave the tests' structlog setup alone (capture_logs needs uncached loggers)
    monkeypatch.setattr(migrate_filenames, "setup_logging", lambda log_level: None)
    yield Repo()


def standard(repo: Repo) -> None:
    """Every case the migration handles, committed."""
    repo.page(FW, f"{FW}.md")  # the root: stays
    repo.page("testkit/alpha", "alpha.md")  # stays
    # Two overloads wrote one file; its footer names (_:): it moves, () gets no file
    repo.page("testkit/setneedsdisplay(_:)", "setneedsdisplay.md")
    repo.page("testkit/setneedsdisplay()", "setneedsdisplay.md", write=False)
    # The struct lost its file to the method; the method moves away, and the
    # struct takes the path back
    repo.page("testkit/font/weight(_:)", "font/weight.md")
    repo.page("testkit/font/weight", "font/weight.md", write=False)
    # Named like the framework: into "-page" folders; testkit/ is left empty
    repo.page("testkit/testkit", "testkit-class.md")
    repo.page("testkit/testkit/init(_:)", "testkit/init.md")
    # A live page whose file is gone: only its recorded path changes
    repo.page("testkit/lost(_:)", "lost.md", write=False)
    # Apple removed it; the valve holds its file for the next cleanup
    repo.page("testkit/stale(_:)", "stale.md", live=False)
    repo.metadata["pending_orphans"] = [str(DOCS / "stale.md"), str(DOCS / "TestKit" / "init.md")]
    repo.save()
    repo.commit("A")


def migrate(*args: str) -> int:
    sys.argv = ["migrate_filenames.py", *args]
    code: int = migrate_filenames.main()
    return code


MOVED = {
    "setneedsdisplay.md": "setneedsdisplay(_).md",
    "font/weight.md": "font/weight(_).md",
    "testkit-class.md": "testkit-page.md",
    "testkit/init.md": "testkit-page/init(_).md",
}


class TestMigration:
    def test_dry_run_changes_nothing(self, repo: Repo, capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None:
        standard(repo)
        before = (repo.files(), Path(f".hashes/{FW}_hashes.json").read_bytes())
        assert migrate("--dry-run", "--plan", str(tmp_path / "plan.tsv")) == 0
        assert (repo.files(), Path(f".hashes/{FW}_hashes.json").read_bytes()) == before
        out = capsys.readouterr().out
        assert "renames: 4 (3 within their dir); staying: 2" in out
        assert "new paths shared by several pages (case-insensitive): 0" in out
        assert "non-owners (no file; the next scrape writes it): 2 (1 take over a path" in out
        assert "file-less live pages (only the recorded path changes): 1" in out
        assert "tracked .md no live entry records (the next scrape's cleanup removes them): 1" in out
        assert f"- {DOCS / 'stale.md'}" in out
        assert "✓ All checks passed; nothing changed (dry run)" in out
        plan = [line.split("\t") for line in (tmp_path / "plan.tsv").read_text().splitlines()]
        assert sorted((row[0], row[3], row[4]) for row in plan if row[0] == "rename") == sorted(
            ("rename", str(DOCS / old), str(DOCS / new)) for old, new in MOVED.items()
        )
        assert sorted(row[2] for row in plan if row[0] == "non-owner") == [
            f"{JSON}/testkit/font/weight.json", f"{JSON}/testkit/setneedsdisplay().json",
        ]
        assert [row[3] for row in plan if row[0] == "orphan"] == [str(DOCS / "stale.md")]

    def test_migrate_then_rerun(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        # A second framework, without a render version (TestKit has one): its file moves too
        other = Path("documentation") / "OtherKit"
        other_entry = {"hash": "h-run", "file_path": str(other / "run.md")}
        repo.write(str(other / "run.md"), f"{DOC}/otherkit/run(_:)")
        Path(".hashes").mkdir(exist_ok=True)
        Path(".hashes/OtherKit_hashes.json").write_text(json.dumps({"metadata": {"total_pages": 2}, "hashes": {
            f"{JSON}/otherkit/run(_:).json": other_entry, f"{DOC}/otherkit/run(_:)": other_entry,
        }}, indent=2, sort_keys=True))
        repo.metadata["render"] = {"version": 0}
        standard(repo)
        before = repo.saved()
        assert migrate() == 0
        out = capsys.readouterr().out
        assert "removed 1 empty dirs" in out
        for old, new in MOVED.items():
            assert not (DOCS / old).exists() and (DOCS / new).exists()
        assert not (DOCS / "testkit").exists()
        for kept in (f"{FW}.md", "alpha.md", "stale.md"):
            assert (DOCS / kept).exists()
        # Nothing is written for a non-owner, or for the file-less page
        for missing in ("setneedsdisplay().md", "font/weight.md", "lost(_).md"):
            assert not (DOCS / missing).exists()
        saved = repo.saved()
        new_paths = {
            FW: f"{FW}.md", "testkit/alpha": "alpha.md",
            "testkit/setneedsdisplay(_:)": "setneedsdisplay(_).md",
            "testkit/setneedsdisplay()": "setneedsdisplay().md",
            "testkit/font/weight(_:)": "font/weight(_).md", "testkit/font/weight": "font/weight.md",
            "testkit/testkit": "testkit-page.md", "testkit/testkit/init(_:)": "testkit-page/init(_).md",
            "testkit/lost(_:)": "lost(_).md",
        }
        for path, file in new_paths.items():
            for key in (f"{JSON}/{path}.json", f"{DOC}/{path}"):
                # Only the recorded path changes
                assert saved["hashes"][key] == {**before["hashes"][key], "file_path": str(DOCS / file)}
        # A page that isn't live keeps its keys as they are
        assert saved["hashes"][f"{DOC}/testkit/stale(_:)"] == before["hashes"][f"{DOC}/testkit/stale(_:)"]
        # pending_orphans follows the renames (any casing), sorted
        assert saved["metadata"]["pending_orphans"] == sorted(
            [str(DOCS / "stale.md"), str(DOCS / "testkit-page" / "init(_).md")]
        )
        # metadata.render stays as loaded, in both saved hash files: the rename renders nothing
        other_saved = json.loads(Path(".hashes/OtherKit_hashes.json").read_text())
        assert saved["metadata"]["render"] == {"version": 0} and "render" not in other_saved["metadata"]
        assert other_saved["hashes"][f"{JSON}/otherkit/run(_:).json"] == {
            **other_entry, "file_path": str(other / "run(_).md")}
        # git sees renames
        git("add", "-A")
        status = git("status", "--porcelain").splitlines()
        assert sorted(line[:2] for line in status) == ["M ", "M ", "R ", "R ", "R ", "R ", "R "]
        git("commit", "-qm", "rename")

        hashes_after = Path(f".hashes/{FW}_hashes.json").read_bytes()
        files_after = repo.files()
        assert migrate() == 0
        out = capsys.readouterr().out
        assert "renames: 0 (0 within their dir)" in out
        assert "hash keys to rewrite: 0 in 0 hash files" in out
        # The non-owners are file-less now, with the page that already was
        assert "file-less live pages (only the recorded path changes): 3" in out
        assert "renamed 0 files" in out and "rewrote 0 hash keys; saved 0 hash files" in out
        assert Path(f".hashes/{FW}_hashes.json").read_bytes() == hashes_after
        assert repo.files() == files_after
        assert git("status", "--porcelain") == ""


class TestChecks:
    """A failed check changes nothing."""

    @staticmethod
    def unchanged(repo: Repo, capsys: pytest.CaptureFixture[str], failure: str) -> None:
        before = (repo.files(), Path(f".hashes/{FW}_hashes.json").read_bytes())
        assert migrate() == 1
        out = capsys.readouterr().out
        assert f"❌ {failure}: 1" in out and "❌ Nothing changed" in out
        assert (repo.files(), Path(f".hashes/{FW}_hashes.json").read_bytes()) == before

    def test_case_duplicate_keys(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        standard(repo)
        repo.hashes[f"{JSON}/testkit.json"] = dict(repo.hashes[f"{JSON}/{FW}.json"])
        repo.save()
        self.unchanged(repo, capsys, "case-duplicate keys (the D5 normalization drops them)")

    def test_a_shared_file_whose_footer_names_none_of_its_pages(
        self, repo: Repo, capsys: pytest.CaptureFixture[str]
    ) -> None:
        standard(repo)
        repo.write(str(DOCS / "setneedsdisplay.md"), f"{DOC}/testkit/somethingelse")
        self.unchanged(repo, capsys, "shared files whose footer names no single page")

    def test_a_rename_onto_a_file_that_stays(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        standard(repo)
        # A pending removal's file sits where a page moves to
        repo.page("testkit/old", "font/weight(_).md", live=False)
        repo.save()
        self.unchanged(repo, capsys, "renames onto a file that stays")

    def test_a_rename_onto_another_moved_file(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        standard(repo)
        # foo.md moves to foo(_).md, and bar.md onto foo.md: a chain
        repo.page("testkit/foo(_:)", "foo.md")
        repo.page("testkit/foo", "bar.md")
        repo.save()
        self.unchanged(repo, capsys, "renames onto another moved file (a chain)")

    def test_a_non_owner_onto_a_file_that_stays(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        standard(repo)
        repo.page("testkit/old", "setneedsdisplay().md", live=False)
        repo.save()
        self.unchanged(repo, capsys, "non-owners whose new path is a file that stays")

    def test_a_non_owner_onto_a_single_pages_file_that_moves_away(
        self, repo: Repo, capsys: pytest.CaptureFixture[str]
    ) -> None:
        standard(repo)
        # It lost alpha.md to alpha; its new path is the file testkit/testkit leaves
        repo.page("testkit/testkit-class", "alpha.md", write=False)
        repo.save()
        self.unchanged(
            repo, capsys, "non-owners whose new path is a single page's file that moves away (not a shared file's)"
        )

    def test_a_file_less_page_onto_a_file_that_stays(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        standard(repo)
        # A file-less page may take the path a file moves away from
        repo.page("testkit/testkit-class", "gone.md", write=False)
        repo.save()
        assert migrate("--dry-run") == 0
        capsys.readouterr()
        # Not a pending removal's file: lost(_:) would record it as its own
        repo.page("testkit/old", "lost(_).md", live=False)
        repo.save()
        self.unchanged(repo, capsys, "file-less pages whose new path is a file that stays")

    def test_a_page_in_two_hash_files(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        standard(repo)
        entry = {"hash": "h", "file_path": "documentation/OtherKit/alpha.md"}
        data = {"metadata": {"total_pages": 1}, "hashes": {f"{JSON}/testkit/alpha.json": entry}}
        Path(".hashes/OtherKit_hashes.json").write_text(json.dumps(data))
        self.unchanged(repo, capsys, "pages in two hash files")

    def test_files_differing_only_in_case(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        if not case_sensitive(Path.cwd()):
            pytest.skip("case-insensitive filesystem: two such files can't exist")
        standard(repo)
        repo.write(str(DOCS / "Alpha.md"), f"{DOC}/testkit/alpha")
        self.unchanged(repo, capsys, "files differing only in case")

    def test_a_hash_file_that_cant_be_read(self, repo: Repo, capsys: pytest.CaptureFixture[str]) -> None:
        standard(repo)
        # Not even dirmap can read it: it might be a framework's
        Path(".hashes/Broken_hashes.json").write_text("{")
        self.unchanged(repo, capsys, "hash files that can't be read")

    def test_a_file_no_live_entry_records_names_a_live_page(
        self, repo: Repo, capsys: pytest.CaptureFixture[str]
    ) -> None:
        standard(repo)
        repo.write(str(DOCS / "copy.md"), f"{DOC}/testkit/alpha")
        repo.commit("copy")
        self.unchanged(repo, capsys, "files no live entry records whose footer names a live page")


class TestRefusals:
    """It runs only from the repo root, on the repo's docs and hash files."""

    @staticmethod
    def refused(capsys: pytest.CaptureFixture[str], message: str, root: Path) -> None:
        def state() -> Tuple[List[str], bytes]:
            files = sorted(str(p) for p in (root / "documentation").rglob("*"))
            return files, (root / f".hashes/{FW}_hashes.json").read_bytes()

        before = state()
        assert migrate() == 1
        assert f"❌ {message}" in capsys.readouterr().out
        assert state() == before

    def test_outside_the_repo_root(
        self, repo: Repo, capsys: pytest.CaptureFixture[str], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        standard(repo)
        monkeypatch.chdir(tmp_path / "documentation")
        self.refused(capsys, "Run it from the repo root; nothing changed", tmp_path)

    @pytest.mark.parametrize("setting", ["OUTPUT_DIR", "CACHE_DIR"])
    def test_another_output_or_cache_dir(
        self, repo: Repo, capsys: pytest.CaptureFixture[str], tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
        setting: str,
    ) -> None:
        standard(repo)
        monkeypatch.setattr(Config, setting, Path("sandbox"))
        self.refused(capsys, "OUTPUT_DIR/CACHE_DIR must be the repo's", tmp_path)


@pytest.mark.parametrize("written", ["init%28a:b-30cwy", "init(a:b-30cwy"])
def test_footer_url_names_the_page_of_an_encoded_footer(tmp_path: Path, written: str) -> None:
    """A footer whose URL the site cut has its "(" encoded (markdown_url; an older rendering
    has it as it is): either names the page by its URL, as its hash keys record it."""
    page = tmp_path / "init.md"
    Repo.write(str(page), f"{DOC}/testkit/{written}")
    assert migrate_filenames.footer_url(str(page)) == f"{DOC}/testkit/init(a:b-30cwy"
