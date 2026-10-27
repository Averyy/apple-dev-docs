#!/usr/bin/env python3
"""MLX scraper: Sphinx link normalization, failure policy, sources and cleanup, over consecutive runs.

Each test runs the real scraper (wafer for the Sphinx pages, aiohttp for
GitHub) against a local fake upstream (fake_upstream.py), in a temporary
docs dir and hash file. wafer needs Python 3.12 and requirements-scrape.txt
(the scrape workflow's environment); elsewhere these tests are skipped.

The config: Sphinx "Lib" (output Lib), "Lib-Data" (Lib/lib-data, nested in
Lib) and "tools" (its own top-level dir, like coremltools); GitHub "lib-lm"
(two configured files, Lib/lib-lm) and "lib-swift" (a README plus the Docs
directory, Lib-Swift/lib-swift); web pages "site" (three configured pages,
its own top-level dir Web, like App-Store).
"""

import dataclasses
import errno
import json
from pathlib import Path
from typing import Any, AsyncIterator, Dict, List, Set

import pytest

pytest.importorskip("wafer", reason="needs wafer-py: Python 3.12 + requirements-scrape.txt (CLAUDE.md, .venv-scrape)")

import scrape_mlx_docs  # noqa: E402
import utilities.source_policy as source_policy  # noqa: E402
from fake_upstream import DROP, FakeUpstream, case_sensitive  # noqa: E402
from scrape_mlx_docs import GitHubDocSource, SphinxDocSource, WebPageSource  # noqa: E402

# Lib: every way of spelling a page (directory, fragment, query, extensionless)
LIB_PAGES = {
    "index.html": ("./", "index.html#top", "guide.html", "api/", "ops", "ops.html#x", "Printer.html",
                   "printer.html", "logo.png", "https://example.com/x.html", "genindex.html"),
    "guide.html": ("index.html",),
    "api/index.html": ("funcs.html?highlight=a", "../ops.html"),
    "api/funcs.html": (),
    "ops.html": ("nested/deep.html",),
    "nested/deep.html": (),
    "Printer.html": (),
    "printer.html": (),
}
DATA_PAGES = {"index.html": ("x.html",), "x.html": ()}
TOOLS_PAGES = {"index.html": ("a.html", "b.html", "c.html"), "a.html": (), "b.html": (), "c.html": ()}
GITHUB_FILES = {
    ("org/lib-lm", "README.md"): "Lib/lib-lm/README.md",
    ("org/lib-lm", "pkg/LORA.md"): "Lib/lib-lm/pkg/LORA.md",
    ("org/lib-swift", "README.md"): "Lib-Swift/lib-swift/README.md",
    ("org/lib-swift", "Docs/Intro.md"): "Lib-Swift/lib-swift/Docs/Intro.md",
    ("org/lib-swift", "Docs/Guides/Usage.md"): "Lib-Swift/lib-swift/Docs/Guides/Usage.md",
    ("org/lib-swift", "Docs/Guides/More.md"): "Lib-Swift/lib-swift/Docs/Guides/More.md",
}


def printer_names() -> Set[str]:
    """The case-colliding pair, each with its own deterministic suffix."""
    import hashlib
    return {f"Lib/{stem}-{hashlib.sha1(f'{stem}.md'.encode()).hexdigest()[:5]}.md" for stem in ("Printer", "printer")}


LIB_DOCS = {"Lib/index.md", "Lib/guide.md", "Lib/api/index.md", "Lib/api/funcs.md", "Lib/ops.md",
            "Lib/nested/deep.md"} | printer_names()
DATA_DOCS = {"Lib/lib-data/index.md", "Lib/lib-data/x.md"}
TOOLS_DOCS = {"tools/index.md", "tools/a.md", "tools/b.md", "tools/c.md"}
GITHUB_DOCS = set(GITHUB_FILES.values())
# The configured web pages (each links to another page of the site, never crawled)
WEB_PAGES = {"guide/rules/": "Web/guide/rules.md", "privacy/": "Web/privacy.md", "data-use/": "Web/data-use.md"}
WEB_DOCS = set(WEB_PAGES.values())
ALL = LIB_DOCS | DATA_DOCS | TOOLS_DOCS | GITHUB_DOCS | WEB_DOCS


def sphinx_sources(site: FakeUpstream) -> List[SphinxDocSource]:
    return [
        SphinxDocSource(name="Lib", base_url=site.sphinx_url("lib/"), output_dir="Lib", framework="Lib",
                        skip_paths=["genindex.html", "search.html"]),
        SphinxDocSource(name="Lib-Data", base_url=site.sphinx_url("libdata/"), output_dir="Lib/lib-data",
                        framework="Lib"),
        SphinxDocSource(name="tools", base_url=site.sphinx_url("tools/"), output_dir="tools", framework="tools"),
    ]


GITHUB = [
    GitHubDocSource(name="lib-lm", repo="org/lib-lm", branch="main", output_dir="Lib/lib-lm", framework="Lib",
                    files=["README.md", "pkg/LORA.md"]),
    GitHubDocSource(name="lib-swift", repo="org/lib-swift", branch="main", output_dir="Lib-Swift/lib-swift",
                    framework="Lib-Swift", files=["README.md"], directories=["Docs"]),
]


def web_sources(site: FakeUpstream) -> List[WebPageSource]:
    return [WebPageSource(name="site", base_url=site.web_url(), output_dir="Web", framework="Web",
                          pages=list(WEB_PAGES))]


def web_html(title: str, body: str = "") -> str:
    """A web page: its content in main, between the site's nav and footer;
    by default a paragraph linking to another page of the site."""
    content = body or f'<p>{title} text, see <a href="/web/other/">other</a>.</p>'
    return (f'<html><body><nav><a href="/web/other/">Other</a></nav><main><h1>{title}</h1>{content}</main>'
            '<footer>Footer</footer></body></html>')


def web_key(site: FakeUpstream, path: str) -> str:
    return f"site:{site.web_url(path)}"


@pytest.fixture
async def site(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> AsyncIterator[FakeUpstream]:
    upstream = FakeUpstream()
    base = await upstream.start()
    monkeypatch.setattr(scrape_mlx_docs, "OUTPUT_BASE", tmp_path / "documentation")
    monkeypatch.setattr(scrape_mlx_docs, "HASH_FILE", tmp_path / ".hashes" / "mlx_docs_hashes.json")
    monkeypatch.setattr(scrape_mlx_docs, "REQUEST_DELAY", 0)
    monkeypatch.setattr(scrape_mlx_docs, "SPHINX_MAX_RETRIES", 0)
    monkeypatch.setattr(scrape_mlx_docs, "SPHINX_SOURCES", sphinx_sources(upstream))
    monkeypatch.setattr(scrape_mlx_docs, "GITHUB_SOURCES", list(GITHUB))
    monkeypatch.setattr(scrape_mlx_docs, "WEB_SOURCES", web_sources(upstream))
    monkeypatch.setattr(source_policy, "GITHUB_RAW", f"{base}/raw")
    monkeypatch.setattr(source_policy, "GITHUB_API", f"{base}/api")
    monkeypatch.setattr(source_policy, "RETRY_BASE_DELAY", 0)
    for prefix, pages in (("lib", LIB_PAGES), ("libdata", DATA_PAGES), ("tools", TOOLS_PAGES)):
        for path, links in pages.items():
            upstream.sphinx_page(f"{prefix}/{path}", f"{prefix} {path}", links)
    for (repo, path), _ in GITHUB_FILES.items():
        upstream.github_file(repo, path, f"# {path}\n\nFrom {repo}.\n")
    for path in WEB_PAGES:
        upstream.web_page(path, web_html(f"web {path}"))
    yield upstream
    await upstream.stop()


async def run(**kwargs: Any) -> int:
    stats = await scrape_mlx_docs.scrape_all(**kwargs)
    return int(stats["exit_code"])


def docs() -> Set[str]:
    out = scrape_mlx_docs.OUTPUT_BASE
    return {p.relative_to(out).as_posix() for p in out.rglob("*.md") if p.is_file()}


def hash_file() -> Dict[str, Any]:
    data: Dict[str, Any] = json.loads(scrape_mlx_docs.HASH_FILE.read_text())
    return data


def metadata() -> Dict[str, Any]:
    result: Dict[str, Any] = hash_file()["metadata"]
    return result


def key(site: FakeUpstream, source: str, path: str) -> str:
    prefix = {"Lib": "lib", "Lib-Data": "libdata", "tools": "tools"}[source]
    return f"{source}:{site.sphinx_url(f'{prefix}/{path}')}"


async def test_a_new_render_version_renders_every_page_once(site: FakeUpstream,
                                                             monkeypatch: pytest.MonkeyPatch) -> None:
    """Stale behaves as --force; a blocked run keeps the stored version, a clean one stores it."""
    version = scrape_mlx_docs.RENDER_VERSION
    assert await run() == 0
    assert metadata()["render"] == {"version": version}
    guide = scrape_mlx_docs.OUTPUT_BASE / "Lib" / "guide.md"
    readme = scrape_mlx_docs.OUTPUT_BASE / "Lib" / "lib-lm" / "README.md"
    for path in (guide, readme):
        path.write_text("# an older rendering\n")
    monkeypatch.setattr(scrape_mlx_docs, "RENDER_VERSION", version + 1)
    site.faults["/sphinx/tools/a.html"] = 502
    assert await run() == 1
    assert metadata()["render"] == {"version": version}
    site.faults.clear()
    assert await run() == 0
    assert metadata()["render"] == {"version": version + 1}
    assert all("an older rendering" not in path.read_text() for path in (guide, readme))
    before = scrape_mlx_docs.HASH_FILE.read_text()
    assert await run() == 0 and scrape_mlx_docs.HASH_FILE.read_text() == before


async def test_pages_the_storing_run_didnt_render_are_rendered_when_back(site: FakeUpstream,
                                                                         monkeypatch: pytest.MonkeyPatch) -> None:
    """The run that stores a new render version drops the source hash of the keys it didn't
    produce (here pages whose files the valve holds), so they are rendered when linked again."""
    assert await run() == 0
    keys = set(hash_file()["hashes"])
    for path in ALL:
        (scrape_mlx_docs.OUTPUT_BASE / path).write_text("# an older rendering\n")
    monkeypatch.setattr(scrape_mlx_docs, "RENDER_VERSION", scrape_mlx_docs.RENDER_VERSION + 1)
    site.sphinx_page("lib/index.html", "lib index.html", ("guide.html",))  # 6 of Lib's 12 files unlinked
    assert await run() == 0 and docs() == ALL and len(metadata()["pending_orphans"]) == 6
    assert metadata()["render"] == {"version": scrape_mlx_docs.RENDER_VERSION}
    hashes = hash_file()["hashes"]
    assert set(hashes) == keys and len([key for key in keys if hashes[key] == ""]) == 6
    site.sphinx_page("lib/index.html", "lib index.html", LIB_PAGES["index.html"])  # linked again, unchanged
    assert await run() == 0 and docs() == ALL and "pending_orphans" not in metadata()
    assert not any("an older rendering" in (scrape_mlx_docs.OUTPUT_BASE / path).read_text() for path in ALL)
    assert set(hash_file()["hashes"]) == keys and all(hash_file()["hashes"].values())
    before = scrape_mlx_docs.HASH_FILE.read_text()
    assert await run() == 0 and scrape_mlx_docs.HASH_FILE.read_text() == before


async def test_full_scrape_normalizes_links(site: FakeUpstream) -> None:
    assert await run() == 0
    assert docs() == ALL
    assert not any("-b8d32" in path for path in docs())
    # Each page fetched once: no "./", ".../api/", extensionless or ?query spelling
    for path in LIB_PAGES:
        assert site.count(f"/sphinx/lib/{path}") == 1, path
    assert site.count("/sphinx/lib/") == 0 and site.count("/sphinx/lib/ops") == 0
    assert site.count("/sphinx/lib/genindex.html") == 0 and site.count("/sphinx/lib/logo.png") == 0
    assert metadata()["sources"] == {"Lib": "Lib", "Lib-Data": "Lib/lib-data", "tools": "tools",
                                     "lib-lm": "Lib/lib-lm", "lib-swift": "Lib-Swift/lib-swift", "site": "Web"}
    assert "failure_counts" not in metadata() and "pending_orphans" not in metadata()
    assert len(hash_file()["hashes"]) == len(ALL)


async def test_sphinx_root_5xx_keeps_its_dir_while_others_are_cleaned(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults["/sphinx/tools/index.html"] = 503
    site.sphinx_page("lib/index.html", "lib", ("api/", "ops", "Printer.html", "printer.html"))  # guide unlinked
    for run_number in range(4):
        assert await run() == 1, run_number  # source_fetch_failed
        assert docs() == ALL - {"Lib/guide.md"}
        assert key(site, "tools", "a.html") in hash_file()["hashes"]
    site.faults.clear()
    assert await run() == 0 and docs() == ALL - {"Lib/guide.md"}


async def test_a_nested_sources_root_failure_keeps_only_its_own_dir(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults["/sphinx/lib/index.html"] = 502  # Lib's root: Lib/ is kept, except the nested sources' dirs
    site.sphinx_page("libdata/index.html", "libdata", ())  # x unlinked in Lib-Data
    site.files.pop(site.raw_path("org/lib-lm", "pkg/LORA.md"))  # a configured file 404 (pending)
    assert await run() == 1
    assert docs() == ALL - {"Lib/lib-data/x.md"}


async def test_a_sphinx_page_404_is_removed_at_once(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults["/sphinx/lib/guide.html"] = 404
    assert await run() == 0
    assert docs() == ALL - {"Lib/guide.md"}
    assert key(site, "Lib", "guide.html") not in hash_file()["hashes"]


async def test_a_good_sphinx_page_failing_3_runs_goes_with_its_subtree(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults["/sphinx/lib/ops.html"] = 500  # ops links to nested/deep
    for run_number in (1, 2):
        assert await run() == 1
        assert docs() == ALL
        assert metadata()["failure_counts"] == {key(site, "Lib", "ops.html"): {"fail": run_number}}
    assert await run() == 1  # D8
    assert docs() == ALL - {"Lib/ops.md", "Lib/nested/deep.md"}
    assert key(site, "Lib", "ops.html") not in hash_file()["hashes"]


async def test_d8_needs_3_failed_fetches_in_a_row(site: FakeUpstream) -> None:
    """tools/a fails on odd runs, and its source's root on even runs, when a
    isn't fetched: it never fails 2 runs in a row, so D8 never removes it."""
    assert await run() == 0
    a = key(site, "tools", "a.html")
    for run_number in range(1, 8):
        site.faults.clear()
        site.faults["/sphinx/tools/a.html" if run_number % 2 else "/sphinx/tools/index.html"] = 502
        assert await run() == 1 and docs() == ALL, run_number
        assert metadata().get("failure_counts", {}) == ({a: {"fail": 1}} if run_number % 2 else {}), run_number
    site.faults.clear()
    assert await run() == 0 and docs() == ALL and "failure_counts" not in metadata()


async def test_a_new_sphinx_page_failing_protects_the_page_moved_under_it(site: FakeUpstream) -> None:
    assert await run() == 0
    site.sphinx_page("lib/ops.html", "ops", ("new.html",))
    site.sphinx_page("lib/new.html", "new", ("nested/deep.html",))
    site.faults["/sphinx/lib/new.html"] = DROP  # a connection error, never answered
    for _ in (1, 2):
        assert await run() == 1 and docs() == ALL
    assert await run() == 1  # lifted at 3
    assert docs() == ALL - {"Lib/nested/deep.md"}
    site.faults.clear()
    assert await run() == 0 and docs() == ALL | {"Lib/new.md"}


@pytest.mark.parametrize("twin", [False, True])
async def test_a_new_page_4xx_does_not_block(site: FakeUpstream, twin: bool) -> None:
    """A newly linked Sphinx page and a newly listed GitHub file answering 403
    are pages we never had (no key, no file under exactly their names): they
    don't block, and a real removal in the same run is deleted. As case twins
    (Guide.html of guide.html, Docs/intro.md of Docs/Intro.md), another
    page's file is under another casing of their names, which a
    case-insensitive filesystem also reports under theirs."""
    assert await run() == 0
    page, file = ("Guide.html", "Docs/intro.md") if twin else ("new.html", "Docs/New.md")
    site.sphinx_page("lib/index.html", "lib", (*LIB_PAGES["index.html"], page))
    site.faults[f"/sphinx/lib/{page}"] = 403
    site.github_file("org/lib-swift", file, "# New\n")
    site.faults[site.raw_path("org/lib-swift", file)] = 403
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # c unlinked: a real removal
    assert await run() == 0
    assert docs() == ALL - {"tools/c.md"} and "failure_counts" not in metadata()
    assert key(site, "Lib", page) not in hash_file()["hashes"]
    assert f"github:org/lib-swift:{file}" not in hash_file()["hashes"]


async def test_sphinx_retries(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    assert await run() == 0
    monkeypatch.setattr(scrape_mlx_docs, "SPHINX_MAX_RETRIES", 1)
    site.flaky["/sphinx/lib/guide.html"] = [503]
    assert await run() == 0 and docs() == ALL
    assert site.count("/sphinx/lib/guide.html") == 3


async def test_sphinx_requests_are_spaced_per_host(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    # wafer's rate_limit spaces a request from the previous one to its host
    # only when they don't overlap, so the pages are fetched one at a time
    monkeypatch.setattr(scrape_mlx_docs, "REQUEST_DELAY", 0.05)
    assert await run() == 0 and docs() == ALL
    arrivals = [moment for path, moment in site.arrivals if path.startswith("/sphinx/")]
    assert len(arrivals) == len(LIB_PAGES) + len(DATA_PAGES) + len(TOOLS_PAGES)
    assert min(later - earlier for earlier, later in zip(arrivals, arrivals[1:], strict=False)) >= 0.045


async def test_a_sphinx_convert_error_x3_keeps_the_file(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    assert await run() == 0
    site.sphinx_page("lib/guide.html", "guide changed", ("index.html",))
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # c unlinked
    convert = scrape_mlx_docs.html_to_markdown

    def failing(html: str, source: SphinxDocSource, url: str) -> str:
        if url.endswith("/guide.html"):
            raise AttributeError("converter bug")
        return convert(html, source, url)

    monkeypatch.setattr(scrape_mlx_docs, "html_to_markdown", failing)
    for run_number in (1, 2):
        assert await run() == 1 and docs() == ALL
        assert metadata()["failure_counts"] == {key(site, "Lib", "guide.html"): {"local": run_number}}
    assert await run() == 1  # persistent_local_error: kept, no longer blocking
    assert docs() == ALL - {"tools/c.md"}
    assert "guide changed" not in (scrape_mlx_docs.OUTPUT_BASE / "Lib/guide.md").read_text()


async def test_a_convert_error_count_survives_runs_that_dont_reach_the_page(site: FakeUpstream,
                                                                            monkeypatch: pytest.MonkeyPatch) -> None:
    """deep's converter fails every run, and its only parent ops fails every
    other run: a run that doesn't reach deep neither counts nor ends its local
    errors, so the block still lifts at its 3rd error; the count goes with the page."""
    assert await run() == 0
    site.sphinx_page("lib/nested/deep.html", "deep changed", ())
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # c unlinked
    convert = scrape_mlx_docs.html_to_markdown

    def failing(html: str, source: SphinxDocSource, url: str) -> str:
        if url.endswith("/nested/deep.html"):
            raise AttributeError("converter bug")
        return convert(html, source, url)

    monkeypatch.setattr(scrape_mlx_docs, "html_to_markdown", failing)
    ops, deep = key(site, "Lib", "ops.html"), key(site, "Lib", "nested/deep.html")
    for run_number in range(1, 5):
        site.faults.pop("/sphinx/lib/ops.html", None)
        if run_number % 2 == 0:
            site.faults["/sphinx/lib/ops.html"] = 503
        assert await run() == 1 and docs() == ALL, run_number  # blocked by deep, or by ops
        local = {deep: {"local": (run_number + 1) // 2}}
        assert metadata()["failure_counts"] == (local | {ops: {"fail": 1}} if run_number % 2 == 0 else local)
    site.faults.clear()
    assert await run() == 1 and docs() == ALL - {"tools/c.md"}  # deep's 3rd error: kept, no longer blocking
    assert metadata()["failure_counts"] == {deep: {"local": 3}}
    site.sphinx_page("lib/ops.html", "ops", ())  # deep removed upstream: its file, key and count go
    assert await run() == 0 and docs() == ALL - {"tools/c.md", "Lib/nested/deep.md"}
    assert deep not in hash_file()["hashes"] and "failure_counts" not in metadata()


@pytest.mark.parametrize("partner", ["removed", "added"])
async def test_a_page_failing_to_convert_keeps_its_doc_under_its_old_name(site: FakeUpstream,
                                                                          monkeypatch: pytest.MonkeyPatch,
                                                                          partner: str) -> None:
    """Its collision partner removed (or added) upstream moves Printer.html to
    its name without (or with) its suffix while its converter fails: until it
    is written there, its doc is under the old name, which is kept, never deleted."""
    printer_suffixed, twin_suffixed = sorted(printer_names())  # Printer.html's, printer.html's
    if partner == "added":
        site.files.pop("/sphinx/lib/printer.html")  # a 404: Printer.html is alone at first
    assert await run() == 0
    before = docs()
    if partner == "added":
        site.sphinx_page("lib/printer.html", "printer", ())
        old, new, after = "Lib/Printer.md", printer_suffixed, before | {twin_suffixed}
    else:
        site.files.pop("/sphinx/lib/printer.html")
        old, new, after = printer_suffixed, "Lib/Printer.md", before - {twin_suffixed}
    site.sphinx_page("lib/Printer.html", "Printer changed", ())
    convert = scrape_mlx_docs.html_to_markdown

    def failing(html: str, source: SphinxDocSource, url: str) -> str:
        if url.endswith("/Printer.html"):
            raise RuntimeError("converter bug")
        return convert(html, source, url)

    monkeypatch.setattr(scrape_mlx_docs, "html_to_markdown", failing)
    for _ in (1, 2):
        assert await run() == 1 and docs() == before | after  # blocked
    for _ in (3, 4):  # its 3rd error on: no longer blocking, its doc kept
        assert await run() == 1 and docs() == after
        assert "Printer changed" not in (scrape_mlx_docs.OUTPUT_BASE / old).read_text()
    monkeypatch.setattr(scrape_mlx_docs, "html_to_markdown", convert)
    assert await run() == 0 and docs() == (after - {old}) | {new}
    assert "Printer changed" in (scrape_mlx_docs.OUTPUT_BASE / new).read_text()
    assert "failure_counts" not in metadata()


async def test_a_write_failing_part_way_under_a_new_name_keeps_the_old_one(site: FakeUpstream,
                                                                           monkeypatch: pytest.MonkeyPatch) -> None:
    """A save that fails part way (disk full) under the page's new name leaves
    nothing there (doc writes are atomic: the temp file is removed); its doc
    under the old name is still kept."""
    assert await run() == 0
    printer_suffixed, twin_suffixed = sorted(printer_names())
    site.files.pop("/sphinx/lib/printer.html")
    site.sphinx_page("lib/Printer.html", "Printer changed", ())
    new = scrape_mlx_docs.OUTPUT_BASE / "Lib/Printer.md"
    write_text = Path.write_text

    def disk_full(self: Path, data: str, *args: Any, **kwargs: Any) -> int:
        if self.name.startswith(new.name):  # its temp file
            write_text(self, data[:6], *args, **kwargs)
            raise OSError(errno.ENOSPC, "No space left on device")
        return write_text(self, data, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", disk_full)
    for run_number in range(1, 5):
        assert await run() == 1, run_number
        expected = ALL if run_number < 3 else ALL - {twin_suffixed}
        assert docs() == expected, run_number
        assert not list(scrape_mlx_docs.OUTPUT_BASE.rglob("*.tmp"))
        assert "Printer changed" not in (scrape_mlx_docs.OUTPUT_BASE / printer_suffixed).read_text()
    monkeypatch.setattr(Path, "write_text", write_text)
    assert await run() == 0 and docs() == (ALL - printer_names()) | {"Lib/Printer.md"}
    assert "Printer changed" in new.read_text()


@pytest.mark.parametrize("repo, path", [("org/lib-lm", "pkg/LORA.md"), ("org/lib-swift", "Docs/Intro.md")])
async def test_a_github_write_failing_part_way_keeps_the_old_doc_whole(site: FakeUpstream,
                                                                       monkeypatch: pytest.MonkeyPatch,
                                                                       repo: str, path: str) -> None:
    """A configured or listed GitHub file's write is atomic too: one that
    fails part way (disk full) leaves the old doc as it was (kept as a local
    error), and no temp file."""
    assert await run() == 0
    doc = scrape_mlx_docs.OUTPUT_BASE / GITHUB_FILES[(repo, path)]
    original = doc.read_text()
    site.github_file(repo, path, f"# {path}\n\nChanged.\n")
    write_text = Path.write_text

    def disk_full(self: Path, data: str, *args: Any, **kwargs: Any) -> int:
        if self.name.startswith(doc.name):  # the doc, or its temp file
            write_text(self, data[:10], *args, **kwargs)
            raise OSError(errno.ENOSPC, "No space left on device")
        return write_text(self, data, *args, **kwargs)

    monkeypatch.setattr(Path, "write_text", disk_full)
    assert await run() == 1 and docs() == ALL
    assert doc.read_text() == original
    assert not list(scrape_mlx_docs.OUTPUT_BASE.rglob("*.tmp"))
    assert metadata()["failure_counts"] == {f"github:{repo}:{path}": {"local": 1}}
    monkeypatch.setattr(Path, "write_text", write_text)
    assert await run() == 0 and "Changed" in doc.read_text()


@pytest.mark.parametrize("loss", ["deleted", "unreadable"])
async def test_pages_we_have_are_protected_after_the_hash_file_is_lost(site: FakeUpstream, loss: str) -> None:
    """A lost hash file loses keys, not files: a 403 on a Sphinx page or a
    listed GitHub file on disk still takes D8's 3 runs, as Apple's lost
    entries do (ops with its subtree); a configured file is a source and is
    kept every run."""
    assert await run() == 0
    if loss == "deleted":
        scrape_mlx_docs.HASH_FILE.unlink()
    else:
        scrape_mlx_docs.HASH_FILE.write_text("{not json")
    site.faults["/sphinx/lib/ops.html"] = 403  # ops links to nested/deep
    site.faults[site.raw_path("org/lib-swift", "Docs/Intro.md")] = 403
    site.faults[site.raw_path("org/lib-lm", "pkg/LORA.md")] = 403
    ops, intro = key(site, "Lib", "ops.html"), "github:org/lib-swift:Docs/Intro.md"
    for run_number in (1, 2):
        assert await run() == 1 and docs() == ALL, run_number  # kept and blocking
        assert metadata()["failure_counts"] == {ops: {"fail": run_number}, intro: {"fail": run_number}}
    assert await run() == 1  # D8 for ops (and its subtree) and Intro
    assert docs() == ALL - {"Lib/ops.md", "Lib/nested/deep.md", "Lib-Swift/lib-swift/Docs/Intro.md"}
    assert await run() == 1 and "Lib/lib-lm/pkg/LORA.md" in docs()
    site.faults.clear()
    assert await run() == 0 and docs() == ALL and "failure_counts" not in metadata()


async def test_a_page_we_have_under_its_other_name_is_protected_after_the_hash_file_is_lost(
        site: FakeUpstream) -> None:
    """Printer.html's doc is under its suffixed name when its twin is removed
    upstream (its plain name is planned now), and it answers 403 with the
    hash file lost: its file under its other name shows a page we have."""
    assert await run() == 0
    scrape_mlx_docs.HASH_FILE.unlink()
    site.files.pop("/sphinx/lib/printer.html")  # a 404: removed at once, but the block holds its file
    site.faults["/sphinx/lib/Printer.html"] = 403
    for _ in (1, 2):
        assert await run() == 1 and docs() == ALL  # kept and blocking
    assert await run() == 1  # D8: Printer.html goes, with its twin's file
    assert docs() == ALL - printer_names()
    site.faults.clear()
    assert await run() == 0 and docs() == (ALL - printer_names()) | {"Lib/Printer.md"}


async def test_a_configured_file_failing_is_kept_every_run(site: FakeUpstream) -> None:
    """A configured file is a source, like a configured dir: any failure but
    404/410 keeps it and its key every run (source_fetch_failed, exit 1),
    never reaching D8, while the rest is cleaned. Only 404/410 x2 removes it."""
    assert await run() == 0
    site.faults[site.raw_path("org/lib-lm", "README.md")] = 503
    site.faults[site.raw_path("org/lib-lm", "pkg/LORA.md")] = 403
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # c unlinked: a real removal
    for run_number in range(1, source_policy.PERSISTENT_FAILURE_RUNS + 2):
        assert await run() == 1, run_number
        assert docs() == ALL - {"tools/c.md"}, run_number
        assert "failure_counts" not in metadata()
        assert {"github:org/lib-lm:README.md", "github:org/lib-lm:pkg/LORA.md"} <= set(hash_file()["hashes"])
    site.faults.clear()
    assert await run() == 0 and docs() == ALL - {"tools/c.md"}


async def test_a_page_back_under_its_old_name_is_rewritten_there(site: FakeUpstream) -> None:
    """Printer.html moves to its suffixed name and changes on a blocked run,
    which leaves its older doc under its plain name; when it moves back, unchanged
    since, the stored hash is the newer content's, so the plain name is rewritten."""
    printer_suffixed, twin_suffixed = sorted(printer_names())
    site.files.pop("/sphinx/lib/printer.html")  # Printer.html alone: Lib/Printer.md
    assert await run() == 0
    plain = scrape_mlx_docs.OUTPUT_BASE / "Lib/Printer.md"
    site.sphinx_page("lib/printer.html", "printer", ())
    site.sphinx_page("lib/Printer.html", "Printer changed", ())
    site.faults["/sphinx/lib/guide.html"] = 502  # blocked: nothing deleted
    assert await run() == 1 and docs() == ALL | {"Lib/Printer.md"}
    assert "Printer changed" not in plain.read_text()
    site.files.pop("/sphinx/lib/printer.html")
    site.faults.clear()
    assert await run() == 0 and docs() == (ALL - printer_names()) | {"Lib/Printer.md"}
    assert "Printer changed" in plain.read_text()
    written = plain.stat().st_mtime_ns
    assert await run() == 0 and plain.stat().st_mtime_ns == written  # then skipped as unchanged


async def test_a_case_twins_leftover_never_stands_in_for_the_page(site: FakeUpstream) -> None:
    """q.html gets Q.html's plain name, in another casing, after Q.html is
    removed upstream while its file is still there (a blocked run). On a
    case-insensitive filesystem that file answers for q.html's name: q.html is
    still written under its own name, and the leftover goes."""
    index_links = LIB_PAGES["index.html"]
    site.sphinx_page("lib/Q.html", "Big Q", ())
    site.sphinx_page("lib/index.html", "lib", (*index_links, "Q.html"))
    assert await run() == 0 and docs() == ALL | {"Lib/Q.md"}
    site.sphinx_page("lib/q.html", "small q", ())  # the twin appears: both suffixed
    site.sphinx_page("lib/index.html", "lib", (*index_links, "Q.html", "q.html"))
    site.faults["/sphinx/lib/guide.html"] = 502
    assert await run() == 1
    site.files.pop("/sphinx/lib/Q.html")  # removed; q.html now plain, but fails (kept, blocked)
    site.faults.clear()
    site.faults["/sphinx/lib/q.html"] = 502
    assert await run() == 1 and "Lib/Q.md" in docs()
    site.faults.clear()
    assert await run() == 0 and docs() == ALL | {"Lib/q.md"}
    doc = scrape_mlx_docs.OUTPUT_BASE / "Lib/q.md"
    assert "lib/q.html" in doc.read_text() and "small q" in doc.read_text()
    written = doc.stat().st_mtime_ns
    assert await run() == 0 and doc.stat().st_mtime_ns == written  # then skipped as unchanged


async def test_a_case_twins_file_is_not_kept_as_the_pages_other_name(site: FakeUpstream,
                                                                      monkeypatch: pytest.MonkeyPatch) -> None:
    """q.html, new, fails to convert while its twin Q.html moves from Q.md to
    its suffixed name: Q.md, Q.html's superseded doc, is not q.html's other
    name (q.md) in another casing, so it goes once the block lifts."""
    index_links = LIB_PAGES["index.html"]
    site.sphinx_page("lib/Q.html", "Big Q", ())
    site.sphinx_page("lib/index.html", "lib", (*index_links, "Q.html"))
    assert await run() == 0 and docs() == ALL | {"Lib/Q.md"}
    site.sphinx_page("lib/q.html", "small q", ())
    site.sphinx_page("lib/index.html", "lib", (*index_links, "Q.html", "q.html"))
    convert = scrape_mlx_docs.html_to_markdown

    def failing(html: str, source: SphinxDocSource, url: str) -> str:
        if url.endswith("/lib/q.html"):
            raise RuntimeError("converter bug")
        return convert(html, source, url)

    monkeypatch.setattr(scrape_mlx_docs, "html_to_markdown", failing)
    for _ in (1, 2):
        assert await run() == 1  # blocked by q.html's local error
    big_q = {name for name in docs() if name.startswith("Lib/Q")}
    assert len(big_q) == 2 and "Lib/Q.md" in big_q  # Q.html's suffixed doc, and its old one
    assert await run() == 1  # its 3rd error: no longer blocking
    assert docs() == ALL | (big_q - {"Lib/Q.md"})


async def test_a_link_urllib_rejects_is_skipped(site: FakeUpstream) -> None:
    """A placeholder host in a link (urlparse raises on it) is not a page of the
    source: the run goes on as usual, every other source included."""
    assert await run() == 0
    site.sphinx_page("tools/a.html", "a", ("http://[your-host]:8080/", "//[x/y", "https://[::1"))
    site.github_file("org/lib-lm", "README.md", "# README changed\n")
    site.files.pop(site.raw_path("org/lib-lm", "pkg/LORA.md"))  # a configured file 404: pending, counted
    assert await run() == 0 and docs() == ALL
    assert metadata()["failure_counts"] == {"github:org/lib-lm:pkg/LORA.md": {"gone": 1}}
    assert "README changed" in (scrape_mlx_docs.OUTPUT_BASE / "Lib/lib-lm/README.md").read_text()


async def test_a_page_whose_links_cant_be_read_blocks_uncounted(site: FakeUpstream,
                                                                 monkeypatch: pytest.MonkeyPatch) -> None:
    """A bug of ours raised while reading a page's links (the plan's outer
    except): the page keeps its file as it is, its children are unknown, so
    the cleanup stays blocked (never lifted, never counted); the rest of the
    run goes on."""
    assert await run() == 0
    site.sphinx_page("lib/ops.html", "ops changed", ("nested/deep.html",))
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # c unlinked
    site.github_file("org/lib-lm", "README.md", "# README changed\n")
    extract = scrape_mlx_docs.extract_links

    def failing(html: str, url: str, source: SphinxDocSource) -> List[str]:
        if url.endswith("/ops.html"):
            raise RuntimeError("link bug")
        return extract(html, url, source)

    monkeypatch.setattr(scrape_mlx_docs, "extract_links", failing)
    for _ in range(source_policy.PERSISTENT_FAILURE_RUNS + 1):
        assert await run() == 1 and docs() == ALL  # ops, its child deep, and c kept
        assert "failure_counts" not in metadata()
        assert "ops changed" not in (scrape_mlx_docs.OUTPUT_BASE / "Lib/ops.md").read_text()
        assert "README changed" in (scrape_mlx_docs.OUTPUT_BASE / "Lib/lib-lm/README.md").read_text()
    monkeypatch.setattr(scrape_mlx_docs, "extract_links", extract)
    assert await run() == 0 and docs() == ALL - {"tools/c.md"}
    assert "ops changed" in (scrape_mlx_docs.OUTPUT_BASE / "Lib/ops.md").read_text()


async def test_a_configured_github_dir_404_x2(site: FakeUpstream) -> None:
    assert await run() == 0
    for path in ("Docs/Intro.md", "Docs/Guides/Usage.md", "Docs/Guides/More.md"):
        site.files.pop(site.raw_path("org/lib-swift", path))  # the listing 404s
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # a removal elsewhere
    assert await run() == 0  # source_gone_pending
    assert docs() == ALL - {"tools/c.md"}
    assert metadata()["failure_counts"] == {"github:org/lib-swift:Docs/": {"gone": 1}}
    assert await run() == 0  # source_gone: 3 of 4 files in Lib-Swift is a mass removal: held
    assert len(metadata()["pending_orphans"]) == 3
    assert await run() == 0  # confirmed
    assert docs() == ALL - {"tools/c.md"} - {path for path in GITHUB_DOCS if "/Docs/" in path}
    assert not any(k.startswith("github:org/lib-swift:Docs/") for k in hash_file()["hashes"])


async def test_a_configured_file_404_x2_and_subdirectory_failures(site: FakeUpstream) -> None:
    assert await run() == 0
    site.files.pop(site.raw_path("org/lib-lm", "pkg/LORA.md"))
    site.faults[site.api_path("org/lib-swift", "Docs/Guides")] = 502  # directory_fetch_failed: kept
    assert await run() == 1
    assert docs() == ALL
    assert metadata()["failure_counts"] == {"github:org/lib-lm:pkg/LORA.md": {"gone": 1}}
    site.faults.clear()
    assert await run() == 0  # gone x2
    assert docs() == ALL - {"Lib/lib-lm/pkg/LORA.md"}
    # A listed subdirectory 404 is a removal at once: 2 of Lib-Swift's 4 files, so the valve holds them first
    site.faults[site.api_path("org/lib-swift", "Docs/Guides")] = 404
    assert await run() == 0
    assert docs() == ALL - {"Lib/lib-lm/pkg/LORA.md"}
    assert metadata()["pending_orphans"] == ["Lib-Swift/lib-swift/Docs/Guides/More.md",
                                             "Lib-Swift/lib-swift/Docs/Guides/Usage.md"]
    assert await run() == 0
    assert docs() == ALL - {"Lib/lib-lm/pkg/LORA.md", "Lib-Swift/lib-swift/Docs/Guides/Usage.md",
                            "Lib-Swift/lib-swift/Docs/Guides/More.md"}


async def test_a_file_moved_into_a_new_subdirectory_that_fails_to_list(site: FakeUpstream) -> None:
    """The new subdirectory has nothing of ours to keep: its failure blocks the
    cleanup (never-good rule), so the moved file isn't deleted at its old path."""
    assert await run() == 0
    site.files[site.raw_path("org/lib-swift", "Docs/NewSub/Intro.md")] = site.files.pop(
        site.raw_path("org/lib-swift", "Docs/Intro.md"))
    site.faults[site.api_path("org/lib-swift", "Docs/NewSub")] = 503
    for run_number in (1, 2):
        assert await run() == 1 and docs() == ALL
        assert metadata()["failure_counts"] == {"github:org/lib-swift:Docs/NewSub/": {"fail": run_number}}
    assert await run() == 1  # lifted at 3 (persistent_fetch_failure): the old path goes
    assert docs() == ALL - {"Lib-Swift/lib-swift/Docs/Intro.md"}
    site.faults.clear()
    assert await run() == 0
    assert docs() == (ALL - {"Lib-Swift/lib-swift/Docs/Intro.md"}) | {"Lib-Swift/lib-swift/Docs/NewSub/Intro.md"}
    assert "failure_counts" not in metadata()


async def test_a_held_page_linked_again_is_still_one_we_have(site: FakeUpstream) -> None:
    """The keys of files the valve holds aren't pruned until those files are
    deleted: a held page linked again is still previously good, so a 403 on it
    blocks instead of deleting its file, and nothing is rewritten."""
    assert await run() == 0
    keys = set(hash_file()["hashes"])
    site.sphinx_page("lib/index.html", "lib index.html", ("guide.html",))  # 6 of Lib's 12 files unlinked
    stats = await scrape_mlx_docs.scrape_all()
    assert stats["exit_code"] == 0 and stats["pruned"] == 0 and docs() == ALL
    assert len(metadata()["pending_orphans"]) == 6
    assert set(hash_file()["hashes"]) == keys
    site.sphinx_page("lib/index.html", "lib index.html", LIB_PAGES["index.html"])  # linked again
    site.faults["/sphinx/lib/ops.html"] = 403
    assert await run() == 1 and docs() == ALL  # a page we have: blocks
    assert metadata()["failure_counts"] == {key(site, "Lib", "ops.html"): {"fail": 1}}
    site.faults.clear()
    stats = await scrape_mlx_docs.scrape_all()
    assert stats["exit_code"] == 0 and stats["downloaded"] == 0 and docs() == ALL
    assert set(hash_file()["hashes"]) == keys and "pending_orphans" not in metadata()


async def test_a_configured_github_dir_5xx_keeps_its_files(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults[site.api_path("org/lib-swift", "Docs")] = 503
    site.files.pop(site.raw_path("org/lib-swift", "README.md"))  # configured file 404: pending
    assert await run() == 1
    assert docs() == ALL


async def test_a_source_dropped_from_the_config(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    assert await run() == 0
    monkeypatch.setattr(scrape_mlx_docs, "SPHINX_SOURCES", sphinx_sources(site)[:2])  # tools dropped
    assert await run() == 0  # its own dir is 100% orphaned: held, and it stays in metadata.sources
    assert docs() == ALL
    assert metadata()["sources"]["tools"] == "tools"
    assert sorted(metadata()["pending_orphans"]) == sorted(TOOLS_DOCS)
    assert sum(k.startswith("tools:") for k in hash_file()["hashes"]) == len(TOOLS_DOCS)  # pruned once deleted
    assert await run() == 0  # confirmed: deleted, its dir removed, dropped from metadata.sources
    assert docs() == ALL - TOOLS_DOCS
    assert not (scrape_mlx_docs.OUTPUT_BASE / "tools").exists()
    assert "tools" not in metadata()["sources"] and "pending_orphans" not in metadata()
    assert not any(k.startswith("tools:") for k in hash_file()["hashes"])


async def test_a_nested_source_dropped_from_the_config(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    assert await run() == 0
    monkeypatch.setattr(scrape_mlx_docs, "GITHUB_SOURCES", GITHUB[1:])  # lib-lm (Lib/lib-lm) dropped
    assert await run() == 0  # weighed in its own dir: held
    assert docs() == ALL
    assert await run() == 0
    assert docs() == ALL - {"Lib/lib-lm/README.md", "Lib/lib-lm/pkg/LORA.md"}
    assert "lib-lm" not in metadata()["sources"]


async def test_a_directory_dropped_from_a_source_that_stays(site: FakeUpstream,
                                                            monkeypatch: pytest.MonkeyPatch) -> None:
    """A DocC catalog dropped from a source's directories (row 5 / OD4: mlx-swift's
    Source/MLX and mlx-swift-lm's MLXLMCommon, which the Swift Package Index now
    renders) while the source stays for its README: the catalog's files leave
    through the normal cleanup (3 of Lib-Swift's 4 files: held by the valve,
    then deleted), the README stays, and nothing is missing in between."""
    assert await run() == 0
    catalog = {path for path in GITHUB_DOCS if "/Docs/" in path}
    monkeypatch.setattr(scrape_mlx_docs, "GITHUB_SOURCES", [GITHUB[0], dataclasses.replace(GITHUB[1], directories=[])])
    assert await run() == 0
    assert docs() == ALL
    assert sorted(metadata()["pending_orphans"]) == sorted(catalog)
    assert await run() == 0
    assert docs() == ALL - catalog
    assert "Lib-Swift/lib-swift/README.md" in docs()
    assert not any(k.startswith("github:org/lib-swift:Docs/") for k in hash_file()["hashes"])
    assert "pending_orphans" not in metadata()


def test_the_catalogs_the_swift_package_index_renders_are_not_imported() -> None:
    """Row 5 / OD4 (a): mlx-swift's and mlx-swift-lm's documentation targets come
    from the Swift Package Index (scraper/site.py SPI_PACKAGES), so their
    catalogs aren't imported again; only the READMEs and mlx-swift-lm's two
    libraries that aren't SPI targets are."""
    sources = {source.name: source for source in scrape_mlx_docs.GITHUB_SOURCES}
    assert sources["mlx-swift"].files == ["README.md"] and not sources["mlx-swift"].directories
    assert sources["mlx-swift-lm"].files == ["README.md"]
    assert sources["mlx-swift-lm"].directories == [
        "Libraries/MLXHuggingFace/Documentation.docc", "Libraries/MLXRerankers/Documentation.docc"]


def moved_tools(site: FakeUpstream, output_dir: str) -> List[SphinxDocSource]:
    """The config with the "tools" source (same name) moved to output_dir."""
    sources = sphinx_sources(site)
    sources[2] = SphinxDocSource(name="tools", base_url=site.sphinx_url("tools/"), output_dir=output_dir,
                                 framework="tools")
    return sources


async def test_a_source_moved_to_another_output_dir(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    """Its old dir is no longer configured: removed like a dropped source's
    (its own dir 100% orphaned, so held, then confirmed), recorded until then
    under "tools@tools" since "tools" now records the new dir."""
    assert await run() == 0
    monkeypatch.setattr(scrape_mlx_docs, "SPHINX_SOURCES", moved_tools(site, "Lib/tools"))
    moved = {f"Lib/{path}" for path in TOOLS_DOCS}
    assert await run() == 0
    assert docs() == ALL | moved
    assert metadata()["sources"]["tools"] == "Lib/tools" and metadata()["sources"]["tools@tools"] == "tools"
    assert sorted(metadata()["pending_orphans"]) == sorted(TOOLS_DOCS)
    assert await run() == 0  # confirmed: deleted, its dir removed, dropped from metadata.sources
    assert docs() == (ALL - TOOLS_DOCS) | moved
    assert not (scrape_mlx_docs.OUTPUT_BASE / "tools").exists()
    assert "tools@tools" not in metadata()["sources"] and "pending_orphans" not in metadata()
    before = scrape_mlx_docs.HASH_FILE.read_text()
    assert await run() == 0 and scrape_mlx_docs.HASH_FILE.read_text() == before  # no churn


async def test_a_source_moved_in_casing_only(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    """tools -> Tools. On a case-sensitive filesystem (CI) the old dir is
    another dir: its files are held, kept while the source's root fails (the
    new dir's location doesn't exclude its own case twin), then confirmed.
    Where the filesystem folds case (macOS) it is the same dir: nothing is
    orphaned, and the old entry goes at once."""
    assert await run() == 0
    folds = not case_sensitive(scrape_mlx_docs.OUTPUT_BASE)
    monkeypatch.setattr(scrape_mlx_docs, "SPHINX_SOURCES", moved_tools(site, "Tools"))
    moved = {f"Tools/{path.split('/', 1)[1]}" for path in TOOLS_DOCS}
    assert await run() == 0
    if folds:
        assert docs() == ALL and "tools@tools" not in metadata()["sources"]
        assert "pending_orphans" not in metadata()
    else:
        assert docs() == ALL | moved and metadata()["sources"]["tools@tools"] == "tools"
        assert sorted(metadata()["pending_orphans"]) == sorted(TOOLS_DOCS)
    site.faults["/sphinx/tools/index.html"] = 503  # source_fetch_failed: every tools file kept, in any casing
    for _ in (1, 2):
        assert await run() == 1
        assert docs() == (ALL if folds else ALL | moved)
    site.faults.clear()
    assert await run() == 0
    assert docs() == (ALL if folds else (ALL - TOOLS_DOCS) | moved)
    assert metadata()["sources"]["tools"] == "Tools"
    assert "tools@tools" not in metadata()["sources"] and "pending_orphans" not in metadata()


async def test_a_source_removed_before_metadata_sources_existed(site: FakeUpstream,
                                                                monkeypatch: pytest.MonkeyPatch) -> None:
    """D2a: the hash file predates metadata.sources; the removed source's files
    sit under a configured top-level dir, so that dir's scan removes them."""
    assert await run() == 0
    data = hash_file()
    del data["metadata"]["sources"]
    stale = key(site, "Lib", "")  # the base-URL key the old link handling stored
    data["hashes"][stale] = "0" * 64
    scrape_mlx_docs.HASH_FILE.write_text(json.dumps(data))
    monkeypatch.setattr(scrape_mlx_docs, "GITHUB_SOURCES", GITHUB[1:])
    assert await run() == 0  # 2 of the files under Lib: under the valve, deleted at once
    assert docs() == ALL - {"Lib/lib-lm/README.md", "Lib/lib-lm/pkg/LORA.md"}
    assert not any(k.startswith("github:org/lib-lm:") for k in hash_file()["hashes"])
    assert stale not in hash_file()["hashes"]
    assert "lib-lm" not in metadata()["sources"]


async def test_unsafe_stored_sources_are_never_cleaned(site: FakeUpstream, tmp_path: Path) -> None:
    """Entries pointing outside the docs dir (or at it) are dropped, never scanned: two runs,
    so a held removal would be confirmed. Every target stays inside tmp_path."""
    assert await run() == 0
    loose = tmp_path / "loose.md"
    loose.write_text("not ours")
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    (elsewhere / "keep.md").write_text("not ours")
    # A link inside the docs dir that leads outside it: only resolving the path rejects it
    (scrape_mlx_docs.OUTPUT_BASE / "link").symlink_to(elsewhere, target_is_directory=True)
    data = hash_file()
    data["metadata"]["sources"].update({"evil": "..", "root": "", "abs": str(elsewhere), "dot": ".",
                                        "up": "Lib/../..", "backslash": "Lib\\..\\..", "link": "link"})
    scrape_mlx_docs.HASH_FILE.write_text(json.dumps(data))
    for _ in range(2):
        assert await run() == 0
        assert loose.exists() and (elsewhere / "keep.md").exists() and docs() == ALL
    assert set(metadata()["sources"]) == {"Lib", "Lib-Data", "tools", "lib-lm", "lib-swift", "site"}
    assert "pending_orphans" not in metadata()


async def test_pruning_is_saved_on_a_quiet_run(site: FakeUpstream) -> None:
    assert await run() == 0
    data = hash_file()
    data["hashes"]["MLX:https://example.com/gone.html"] = "1" * 64
    scrape_mlx_docs.HASH_FILE.write_text(json.dumps(data))
    stats = await scrape_mlx_docs.scrape_all()
    assert stats["exit_code"] == 0 and stats["downloaded"] == 0 and stats["pruned"] == 1
    assert "MLX:https://example.com/gone.html" not in hash_file()["hashes"]
    before = scrape_mlx_docs.HASH_FILE.read_text()
    assert await run() == 0
    assert scrape_mlx_docs.HASH_FILE.read_text() == before


async def test_force_keeps_the_failure_policy(site: FakeUpstream) -> None:
    assert await run() == 0
    site.faults["/sphinx/lib/guide.html"] = 403  # a page we have: protected even with --force
    stats = await scrape_mlx_docs.scrape_all(force=True)
    assert stats["exit_code"] == 1 and docs() == ALL
    assert stats["downloaded"] == len(ALL) - 1


def test_main_exit_codes(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.argv", ["scrape_mlx_docs.py"])

    async def returns(code: int) -> Dict[str, Any]:
        return {"exit_code": code}

    for code in (0, 1):
        monkeypatch.setattr(scrape_mlx_docs, "scrape_all", lambda code=code, **_: returns(code))
        assert scrape_mlx_docs.main() == code

    async def raises(error: BaseException) -> Dict[str, Any]:
        raise error

    monkeypatch.setattr(scrape_mlx_docs, "scrape_all", lambda **_: raises(KeyboardInterrupt()))
    assert scrape_mlx_docs.main() == 130
    monkeypatch.setattr(scrape_mlx_docs, "scrape_all", lambda **_: raises(RuntimeError("bug")))
    assert scrape_mlx_docs.main() == 1


async def test_readme_only_takes_the_crawls_readmes(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    """readme_only: the directory crawl takes only README.md files; the
    other .md files it took before go through the normal cleanup."""
    assert await run() == 0
    site.github_file("org/lib-swift", "Docs/Guides/README.md", "# Guides\n")
    readme_only = [GITHUB[0], GitHubDocSource(name="lib-swift", repo="org/lib-swift", branch="main",
                                              output_dir="Lib-Swift/lib-swift", framework="Lib-Swift",
                                              files=["README.md"], directories=["Docs"], readme_only=True)]
    monkeypatch.setattr(scrape_mlx_docs, "GITHUB_SOURCES", readme_only)
    others = {"Lib-Swift/lib-swift/Docs/Intro.md", "Lib-Swift/lib-swift/Docs/Guides/Usage.md",
              "Lib-Swift/lib-swift/Docs/Guides/More.md"}
    assert await run() == 0  # 3 of Lib-Swift's 5 files: held by the valve
    assert docs() == ALL | {"Lib-Swift/lib-swift/Docs/Guides/README.md"}
    assert len(metadata()["pending_orphans"]) == 3
    assert site.count("/raw/org/lib-swift/main/Docs/Intro.md") == 1  # not fetched again
    assert await run() == 0  # confirmed
    assert docs() == (ALL - others) | {"Lib-Swift/lib-swift/Docs/Guides/README.md"}
    assert not any(key.startswith("github:org/lib-swift:Docs/") and not key.endswith("README.md")
                   for key in hash_file()["hashes"])


async def test_doc_links_resolve_in_their_own_catalog(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    """A GitHub file in a DocC catalog (a *.docc dir) has its DocC markup
    converted within its own catalog: <doc:Name> links the catalog's article
    of that name (a name in two catalogs: each links its own), under its
    title, <doc:Name#Anchor> its heading, <doc:#Anchor> a heading of the
    page itself; @Metadata goes. A file outside a catalog is left as it is."""
    catalogs = GitHubDocSource(name="lib-swift", repo="org/lib-swift", branch="main",
                               output_dir="Lib-Swift/lib-swift", framework="Lib-Swift", files=["README.md"],
                               directories=["Sources/One/One.docc", "Sources/Two/Two.docc"])
    monkeypatch.setattr(scrape_mlx_docs, "GITHUB_SOURCES", [GITHUB[0], catalogs])
    site.github_file("org/lib-swift", "README.md", "# Lib\n\nSee <doc:memory>.\n")
    site.github_file("org/lib-swift", "Sources/One/One.docc/One.md",
                     "# ``One``\n\n@Metadata {\n    @PageKind(sampleCode)\n}\n\n## Topics\n\n"
                     "- <doc:memory>\n- <doc:guide#Getting-Started>\n- <doc:#Topics>\n")
    site.github_file("org/lib-swift", "Sources/One/One.docc/Articles/memory.md", "# Memory in One\n")
    site.github_file("org/lib-swift", "Sources/One/One.docc/Articles/guide.md",
                     "# The Guide\n\n## Getting Started\n")
    site.github_file("org/lib-swift", "Sources/Two/Two.docc/Two.md", "# Two\n\nSee <doc:memory>.\n")
    site.github_file("org/lib-swift", "Sources/Two/Two.docc/memory.md",
                     "# Memory in Two\n\nSee <doc:#Wired-Limits>.\n\n## Wired Limits\n")
    assert await run() == 0
    assert await run(force=True) == 0  # every target now has its file
    out = scrape_mlx_docs.OUTPUT_BASE / "Lib-Swift/lib-swift"
    one = (out / "Sources/One/One.docc/One.md").read_text()
    assert ("## Topics\n\n- [Memory in One](Articles/memory.md)\n"
            "- [Getting Started](Articles/guide.md#Getting-Started)\n- [Topics](#Topics)\n") in one
    assert "@Metadata" not in one and "@PageKind" not in one
    assert "See [Memory in Two](memory.md)." in (out / "Sources/Two/Two.docc/Two.md").read_text()
    assert "See [Wired Limits](#Wired-Limits)." in (out / "Sources/Two/Two.docc/memory.md").read_text()
    assert "See <doc:memory>." in (out / "README.md").read_text()


async def test_urls_built_from_file_names_are_percent_encoded(site: FakeUpstream,
                                                                monkeypatch: pytest.MonkeyPatch) -> None:
    """A GitHub file whose name holds spaces (sourcekit-lsp's "Configuration File.md") is
    fetched and saved under its name, its url percent-encoded so a link to it is valid
    markdown; so is a DocC catalog's assets URL."""
    catalog = GitHubDocSource(name="lib-swift", repo="org/lib-swift", branch="main",
                              output_dir="Lib-Swift/lib-swift", framework="Lib-Swift", files=["README.md"],
                              directories=["Docs", "My Lib.docc"])
    monkeypatch.setattr(scrape_mlx_docs, "GITHUB_SOURCES", [GITHUB[0], catalog])
    site.github_file("org/lib-swift", "Docs/Configuration File.md", "# Configuration File\n")
    site.github_file("org/lib-swift", "My Lib.docc/Intro.md", "# Intro\n\n![A chart.](chart)\n")
    assert await run() == 0
    out = scrape_mlx_docs.OUTPUT_BASE / "Lib-Swift/lib-swift"
    assert (out / "Docs/Configuration File.md").read_text().startswith(
        "---\nsource: lib-swift\nframework: Lib-Swift\n"
        "url: https://github.com/org/lib-swift/blob/main/Docs/Configuration%20File.md\n---\n\n# Configuration File\n")
    assert ("![A chart.](https://raw.githubusercontent.com/org/lib-swift/main/My%20Lib.docc/Assets/chart@2x.png)"
            in (out / "My Lib.docc/Intro.md").read_text())


def test_a_page_url_is_written_percent_encoded() -> None:
    """A page's url as front matter and a link can hold it: a space or a non-ASCII letter
    encoded, its delimiters and escapes kept."""
    source = WebPageSource(name="X", base_url="https://h.test/app-store/", output_dir="X", framework="X")
    markdown = scrape_mlx_docs.html_to_markdown(WEB_PAGE, source, "https://h.test/app-store/my page/caf\u00e9%2F?a=b#c")
    assert "\nurl: https://h.test/app-store/my%20page/caf%C3%A9%2F?a=b#c\n" in markdown


async def test_web_pages_are_fetched_one_by_one_never_crawled(site: FakeUpstream) -> None:
    """Each configured page is fetched once and saved under its path without
    the trailing slash, from its main; a link to another page of the site is
    never followed. A page whose markdown is unchanged is skipped (no
    hash-file churn), also when its HTML changed outside its content; a
    changed one is rewritten."""
    assert await run() == 0 and docs() == ALL
    for path in WEB_PAGES:
        assert site.count(f"/web/{path}") == 1, path
    assert site.count("/web/other/") == 0
    rules = (scrape_mlx_docs.OUTPUT_BASE / "Web/guide/rules.md").read_text()
    assert rules.startswith(f"---\nsource: site\nframework: Web\nurl: {site.web_url('guide/rules/')}\n---\n")
    assert "Footer" not in rules and f"[other]({site.web_url('other/')})" in rules  # made absolute
    assert {web_key(site, path) for path in WEB_PAGES} <= set(hash_file()["hashes"])
    before = scrape_mlx_docs.HASH_FILE.read_text()
    site.web_page("data-use/", web_html("web data-use/").replace("<html>", '<html><script src="/x.js?2">'
                                                                          '</script>'))
    stats = await scrape_mlx_docs.scrape_all()
    assert stats["exit_code"] == 0 and stats["downloaded"] == 0 and docs() == ALL
    assert scrape_mlx_docs.HASH_FILE.read_text() == before
    site.web_page("privacy/", web_html("web privacy/", "<p>Changed.</p>"))
    stats = await scrape_mlx_docs.scrape_all()
    assert stats["exit_code"] == 0 and stats["downloaded"] == 1
    assert "Changed." in (scrape_mlx_docs.OUTPUT_BASE / "Web/privacy.md").read_text()


async def test_a_web_page_404_x2_is_removed(site: FakeUpstream) -> None:
    """A configured page is a source: its 1st 404 keeps it (source_gone_pending,
    not an error), its 2nd removes it (source_gone); back, it is written again."""
    assert await run() == 0
    site.faults["/web/privacy/"] = 404
    assert await run() == 0 and docs() == ALL
    assert metadata()["failure_counts"] == {web_key(site, "privacy/"): {"gone": 1}}
    assert await run() == 0  # 1 of Web's 3 files: deleted at once
    assert docs() == ALL - {"Web/privacy.md"}
    assert web_key(site, "privacy/") not in hash_file()["hashes"]
    site.faults.clear()
    assert await run() == 0 and docs() == ALL and "failure_counts" not in metadata()


async def test_a_web_page_failing_is_kept_every_run(site: FakeUpstream) -> None:
    """Any other failure keeps the page and its key every run, never reaching
    D8 (source_fetch_failed, exit 1), while the rest is cleaned."""
    assert await run() == 0
    site.faults["/web/privacy/"] = 503
    site.faults["/web/data-use/"] = DROP  # a connection error, never answered
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # c unlinked: a real removal
    for run_number in range(1, source_policy.PERSISTENT_FAILURE_RUNS + 2):
        assert await run() == 1, run_number
        assert docs() == ALL - {"tools/c.md"}, run_number
        assert {web_key(site, "privacy/"), web_key(site, "data-use/")} <= set(hash_file()["hashes"])
    site.faults.clear()
    assert await run() == 0 and docs() == ALL - {"tools/c.md"}


async def test_a_web_page_failing_to_convert_keeps_its_file(site: FakeUpstream,
                                                           monkeypatch: pytest.MonkeyPatch) -> None:
    """A convert error is ours: the page keeps its file and blocks the cleanup."""
    assert await run() == 0
    site.web_page("privacy/", web_html("web privacy/", "<p>Changed.</p>"))
    site.sphinx_page("tools/index.html", "tools", ("a.html", "b.html"))  # c unlinked: waits for the cleanup
    convert = scrape_mlx_docs.html_to_markdown

    def failing(html: str, source: Any, url: str) -> str:
        if url == site.web_url("privacy/"):
            raise ValueError("conversion bug")
        return convert(html, source, url)

    monkeypatch.setattr(scrape_mlx_docs, "html_to_markdown", failing)
    assert await run() == 1 and docs() == ALL
    assert metadata()["failure_counts"] == {web_key(site, "privacy/"): {"local": 1}}
    monkeypatch.setattr(scrape_mlx_docs, "html_to_markdown", convert)
    assert await run() == 0 and docs() == ALL - {"tools/c.md"} and "failure_counts" not in metadata()
    assert "Changed." in (scrape_mlx_docs.OUTPUT_BASE / "Web/privacy.md").read_text()


async def test_a_web_page_dropped_from_the_config(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    """Its file is an orphan of its source's dir (1 of 3: deleted at once), its key pruned."""
    assert await run() == 0
    sources = web_sources(site)
    sources[0].pages.remove("privacy/")
    monkeypatch.setattr(scrape_mlx_docs, "WEB_SOURCES", sources)
    assert await run() == 0 and docs() == ALL - {"Web/privacy.md"}
    assert web_key(site, "privacy/") not in hash_file()["hashes"]


async def test_a_web_source_dropped_from_the_config(site: FakeUpstream, monkeypatch: pytest.MonkeyPatch) -> None:
    """As any dropped source: its own dir is all orphans, held one clean run,
    deleted on the next with its keys and its metadata.sources entry."""
    assert await run() == 0
    monkeypatch.setattr(scrape_mlx_docs, "WEB_SOURCES", [])
    assert await run() == 0 and docs() == ALL
    assert metadata()["sources"]["site"] == "Web"
    assert sorted(metadata()["pending_orphans"]) == sorted(WEB_DOCS)
    assert await run() == 0 and docs() == ALL - WEB_DOCS
    assert not (scrape_mlx_docs.OUTPUT_BASE / "Web").exists()
    assert "site" not in metadata()["sources"] and "pending_orphans" not in metadata()
    assert not any(k.startswith("site:") for k in hash_file()["hashes"])


def test_web_page_paths(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(scrape_mlx_docs, "OUTPUT_BASE", tmp_path)
    source = WebPageSource(name="X", base_url="https://h.test/app-store/", output_dir="X", framework="X",
                           pages=["review/guidelines/", "app-privacy-details/", "terms.html"])
    assert scrape_mlx_docs.web_page_paths(source) == {
        "https://h.test/app-store/review/guidelines/": tmp_path / "X/review/guidelines.md",
        "https://h.test/app-store/app-privacy-details/": tmp_path / "X/app-privacy-details.md",
        "https://h.test/app-store/terms.html": tmp_path / "X/terms.md",
    }
    # Outside the base URL, the base URL itself, two pages on one file (in any casing)
    for pages in (["../other/"], ["https://elsewhere.test/x/"], ["//elsewhere.test/x/"], [""], ["./"],
                  ["Review/", "review/"]):
        with pytest.raises(ValueError):
            scrape_mlx_docs.web_page_paths(WebPageSource(name="X", base_url=source.base_url, output_dir="X",
                                                         framework="X", pages=pages))


def test_the_configured_sources() -> None:
    """The real config loads (unique names, valid web pages); the App Store pages' files."""
    assert scrape_mlx_docs.configured_sources()["App-Store"] == "App-Store"
    (app_store,) = scrape_mlx_docs.WEB_SOURCES
    assert {path.relative_to(scrape_mlx_docs.OUTPUT_BASE).as_posix()
            for path in scrape_mlx_docs.web_page_paths(app_store).values()} == {
        "App-Store/review/guidelines.md", "App-Store/app-privacy-details.md",
        "App-Store/user-privacy-and-data-use.md"}


WEB_PAGE = """<html><body><nav><a href="/app-store/">App Store</a></nav><main>
<header><h1>Review Rules</h1><p>Read them all.</p></header>
<h3 id="intro">Introduction</h3>
<p>See the <a href="/app-store/privacy/">privacy page</a>, <a href="#safety">safety</a> and
<a href="//cdn.example/x">the CDN</a>.</p>
<h3 id="safety"><span id="1"></span>1.<span><img alt="key" src="/app-store/key.svg"/></span> Safety</h3>
<ul>
<li id="1.1"><strong>1.1 Content</strong>
<p>Apps should not include:</p>
<ul><li><strong>1.1.1</strong> Mean content.</li>
<li><strong>1.1.2</strong> Violence.</li></ul>
Unless it is satire.</li>
<li><strong>1.2 Info</strong>
<p>Include a way to contact you.</p></li>
<li><strong>1.3 Kids</strong><p>First rule.</p><p>Second rule.</p></li>
<li>A plain item, <a href="/help/">help</a>.</li>
</ul>
<h4>Notes</h4>
<p>Last.</p>
</main><footer>Copyright</footer></body></html>"""


def test_web_page_conversion() -> None:
    source = WebPageSource(name="X", base_url="https://h.test/app-store/", output_dir="X", framework="X")
    url = "https://h.test/app-store/review/guidelines/"
    markdown = scrape_mlx_docs.html_to_markdown(WEB_PAGE, source, url)
    assert markdown.startswith(f"---\nsource: X\nframework: X\nurl: {url}\n---\n")
    body = markdown.split("---\n", 2)[2]
    # The main only; the title with a plain space
    assert "App Store" not in body and "Copyright" not in body
    assert body.startswith("\n# Review Rules\n\nRead them all.\n")
    # h3 sections become ## (the indexer splits a large page at ##), the levels below follow;
    # a heading's words kept apart
    assert [line for line in body.split("\n") if line.startswith("#")] == [
        "# Review Rules", "## Introduction", "## 1. Safety", "### Notes"]
    # Links from the host's root made absolute; a fragment kept
    assert ("See the [privacy page](https://h.test/app-store/privacy/), [safety](#safety) and\n"
            "[the CDN](https://cdn.example/x).") in body
    # An item of several blocks: its title, text, nested list and trailing text each a paragraph
    assert ("- **1.1 Content**\n\n  Apps should not include:\n\n  - **1.1.1** Mean content.\n"
            "  - **1.1.2** Violence.\n\n  Unless it is satire.\n\n"
            "- **1.2 Info**\n\n  Include a way to contact you.\n\n"
            "- **1.3 Kids**\n\n  First rule.\n\n  Second rule.\n\n"
            "- A plain item, [help](https://h.test/help/).\n") in body


SPHINX_PAGE = """<html><body><main>
<div class="header"><a href="../_sources/api/page.rst">.rst</a>
<ul><li><button>System Settings</button></li><li><button>Light</button></li></ul></div>
<article><h1>mlx.core.thing<a class="headerlink" href="#thing">#</a></h1>
<p>See <a href="ops.html#mlx.core.abs">abs</a>, <a href="ops.html">ops</a>,
<a href="https://other.example/doc/y.html#frag">y</a> and <a href="https://other.example/z.html">z</a>.</p>
<p><img alt="Inline" src="../_images/inline.png"/>
<a class="reference internal image-reference" href="../_images/big.png"><img alt="Big" src="../_images/big.png"/></a></p>
<a class="image-reference" href="../_images/top.png"><img alt="Top" src="../_images/top.png"/></a>
<a class="reference internal" href="tutorial.html"><img alt="Go" src="../_static/go.png"/></a>
<p>Try it: <a class="reference external" href="https://binder.example/v2/gh/x/HEAD"><img alt="Binder"
src="https://binder.example/badge.svg"/></a></p>
<blockquote><div><img alt="Quoted" src="../_static/q.png"/></div></blockquote>
<table><thead><tr><th><p>Name</p></th><th><p>Description</p></th></tr></thead>
<tbody><tr><td><p><a href="list.html#list"><code>list</code></a></p></td><td><p>Convert to a Python <code>list</code>.
See <a href="concat.html#c"><code>concatenate()</code></a>.</p></td></tr>
<tr><td><p><img alt="Cell" src="cell.png"/></p></td><td><p>An <a href="https://pytorch.example/trace.html">external</a>
page.</p></td></tr></tbody></table>
<ul><li><p>Load it:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span># Load the model
model = load()
</pre></div></div>
</li></ul>
<dl><dt>batch()</dt><dd><p>An example.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre># prints (4, 10)
print(x)</pre></div></div>
</dd></dl>
</article></main></body></html>"""


def test_sphinx_conversion() -> None:
    source = SphinxDocSource(name="X", base_url="https://h.test/doc/html/", output_dir="X", framework="X")
    url = "https://h.test/doc/html/api/page.html"
    markdown = scrape_mlx_docs.html_to_markdown(SPHINX_PAGE, source, url)
    body = markdown.split("---\n", 2)[2]
    # The article only: no theme switcher or source link, the title once
    assert "System Settings" not in body and "_sources" not in body and "Light" not in body
    assert body.startswith("\n# mlx.core.thing\n") and body.count("# mlx.core.thing") == 1
    # Relative page links to .md, with or without a fragment; absolute ones unchanged
    assert ("See [abs](ops.md#mlx.core.abs), [ops](ops.md),\n[y](https://other.example/doc/y.html#frag) and "
            "[z](https://other.example/z.html).") in body
    # Images resolved against the page, in a paragraph, in a link, alone in a link, in a blockquote
    assert ("![Inline](https://h.test/doc/html/_images/inline.png)\n"
            "![Big](https://h.test/doc/html/_images/big.png)") in body
    assert "![Top](https://h.test/doc/html/_images/top.png)" in body
    # An image linked elsewhere (a badge, another page) keeps its link
    assert "[![Go](https://h.test/doc/html/_static/go.png)](tutorial.md)" in body
    assert "Try it: [![Binder](https://binder.example/badge.svg)](https://binder.example/v2/gh/x/HEAD)" in body
    assert "> ![Quoted](https://h.test/doc/html/_static/q.png)" in body
    # Table cells: words kept apart (not "Pythonlist", "Seeconcatenate()"), links and images kept
    assert "| Name | Description |" in body
    assert "| [list](list.md#list) | Convert to a Python `list`. See [concatenate()](concat.md#c). |" in body
    assert ("| ![Cell](https://h.test/doc/html/api/cell.png) | An "
            "[external](https://pytorch.example/trace.html) page. |") in body
    # Code in a list item or a definition is fenced, indented under the item
    assert "- Load it:\n\n  ```\n  # Load the model\n  model = load()\n  ```\n" in body
    assert ": An example.\n\n  ```\n  # prints (4, 10)\n  print(x)\n  ```\n" in body
    assert not [line for line in body.split("\n") if line.startswith("# ") and line != "# mlx.core.thing"]


def test_sphinx_lists_headings_and_links() -> None:
    """A Sphinx item's nested list keeps its items (they ran into the item's
    text before), and a heading's words are kept apart around its code. A
    link that can't point to one of our docs is made absolute (from the
    host's root; a skipped page, a file); a page's [source] link goes."""
    page = """<html><body><article><h1>Guide</h1>
<h2>Using <code class="docutils literal"><span class="pre">nn.average</span></code> well<a class="headerlink"
href="#using">¶</a></h2>
<ol><li><p>Download the assets:</p>
<ul><li><p>The utilities</p></li><li><p>The weights</p></li></ul>
</li><li><p>Install it.</p></li></ol>
<p>See <a href="/doc/html/index.html">the root</a>, <a href="../genindex.html">the index</a>,
<a href="../_downloads/x.py">the script</a> and <a href="ops.html#add">add</a>.</p>
<dl><dt>average(<em>x</em>)<a class="reference internal" href="../_modules/nn.html#average"><span
class="viewcode-link"><span class="pre">[source]</span></span></a></dt><dd><p>Averages.</p></dd></dl>
</article></body></html>"""
    source = SphinxDocSource(name="X", base_url="https://h.test/doc/html/", output_dir="X", framework="X",
                             skip_paths=["genindex.html", "_modules/"])
    markdown = scrape_mlx_docs.html_to_markdown(page, source, "https://h.test/doc/html/usage/guide.html")
    body = markdown.split("---\n", 2)[2]
    assert "\n## Using nn.average well\n" in body
    assert "1. Download the assets:\n\n   - The utilities\n   - The weights\n\n2. Install it.\n" in body
    assert ("See [the root](https://h.test/doc/html/index.html), [the index](https://h.test/doc/html/genindex.html),\n"
            "[the script](https://h.test/doc/html/_downloads/x.py) and [add](ops.md#add).") in body
    assert "\n**average(*x*)**\n: Averages.\n" in body and "[source]" not in body and "_modules" not in body


def test_a_list_item_with_a_table_keeps_the_table() -> None:
    """A list item holding a paragraph and a table is converted block by block:
    inline conversion would run the table's cells into the item's text."""
    page = """<html><body><article><h1>Guide</h1>
<ul><li><p>The options:</p>
<table><thead><tr><th>Name</th><th>Use</th></tr></thead><tbody><tr><td>fast</td><td>speed</td></tr></tbody></table>
</li></ul>
</article></body></html>"""
    source = SphinxDocSource(name="X", base_url="https://h.test/doc/html/", output_dir="X", framework="X")
    body = scrape_mlx_docs.html_to_markdown(page, source, "https://h.test/doc/html/guide.html").split("---\n", 2)[2]
    assert "- The options:\n\n  | Name | Use |" in body
    assert "| fast | speed |" in body


def test_link_normalization() -> None:
    source = SphinxDocSource(name="X", base_url="https://h.test/doc/html/", output_dir="X",
                             skip_paths=["genindex.html"])
    page = "https://h.test/doc/html/api/index.html"
    cases = {
        "funcs.html": "https://h.test/doc/html/api/funcs.html",
        "funcs.html#f": "https://h.test/doc/html/api/funcs.html",
        "funcs.html?highlight=a#f": "https://h.test/doc/html/api/funcs.html",
        "funcs": "https://h.test/doc/html/api/funcs.html",
        "./": "https://h.test/doc/html/api/index.html",
        "../": "https://h.test/doc/html/index.html",
        "../..": None,  # outside the base
        "https://h.test/doc/html": "https://h.test/doc/html/index.html",
        "../genindex.html#A": None,
        "genindex.html": None,  # a skip path matches where a segment starts, at any depth
        "mlx.data.CharTrie.genindex.html": "https://h.test/doc/html/api/mlx.data.CharTrie.genindex.html",
        "#top": None,
        "mailto:a@b.c": None,
        "img.png": None,
        "mlx.core.array": None,  # a dotted name that isn't .html: not a page (as before)
        "https://other.test/doc/html/x.html": None,
        # urllib rejects the host part: not a page of the source, never an exception
        "http://[your-host]:8080/": None,
        "//[x/y": None,
        "https://[::1": None,
        "//h.test＃/doc/html/x.html": None,
    }
    for href, expected in cases.items():
        assert scrape_mlx_docs.normalize_link(page, href, source) == expected, href


def test_a_superseded_catalog_is_crawled_until_its_copy_exists(tmp_path: Path) -> None:
    """mlx-swift's DocC catalog comes from the Swift Package Index once the Apple
    scrape has written it; until then (or if that copy is ever gone) from GitHub."""
    source = GitHubDocSource(name="x", repo="o/x", branch="main", output_dir="X", framework="X",
                             directories=["Docs"], superseded_directories={"Source/X.docc": "SPI/x/X"})
    assert scrape_mlx_docs.active_directories(source, tmp_path) == ["Docs", "Source/X.docc"]
    copy = tmp_path / "SPI" / "x" / "X"
    copy.mkdir(parents=True)
    assert scrape_mlx_docs.active_directories(source, tmp_path) == ["Docs", "Source/X.docc"]
    (copy / "X.md").write_text("# X\n")
    assert scrape_mlx_docs.active_directories(source, tmp_path) == ["Docs"]
    configured = {s.name: s.superseded_directories for s in scrape_mlx_docs.GITHUB_SOURCES}
    assert configured["mlx-swift"] == {"Source/MLX/Documentation.docc": "SPI/mlx-swift/MLX"}
    assert configured["mlx-swift-lm"] == {"Libraries/MLXLMCommon/Documentation.docc": "SPI/mlx-swift-lm/MLXLMCommon"}
