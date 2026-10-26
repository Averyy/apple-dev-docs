"""A fake upstream for the MLX, HIG and Swift scraper tests.

One local aiohttp server serves everything those scrapers fetch, so the tests
drive their real HTTP clients (aiohttp, httpx and wafer):

- Sphinx pages under /sphinx/... (HTML with links);
- web pages under /web/... (HTML, the MLX scraper's configured pages);
- GitHub raw files under /raw/<repo>/<branch>/<path>, and contents-API
  listings under /api/repos/<repo>/contents/<dir>, built from those files;
- HIG JSON pages under /hig/tutorials/data/design/human-interface-guidelines/...

A test changes the site between runs (add or remove pages) and injects
faults by path: an HTTP status, a dropped connection (DROP), or a status for
the first N requests only (flaky).
"""

import asyncio
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from aiohttp import web

# A fault that drops the connection without an answer (a network error)
DROP = -1
# A fault that answers 200 with a body that isn't JSON (HIG/GitHub API only)
BAD_JSON = -2

HIG_PREFIX = "/hig/tutorials/data/design"
HIG_ROOT = "human-interface-guidelines"


def case_sensitive(directory: Path) -> bool:
    """Whether the filesystem under directory tells names apart by casing
    (Linux, as on CI; not macOS): a case-only rename upstream leaves a stale
    old-cased file only there."""
    probe = directory / "CaseProbe"
    probe.write_text("")
    try:
        return not (directory / "caseprobe").exists()
    finally:
        probe.unlink()


class FakeUpstream:
    """The fake upstream server and its content."""

    def __init__(self) -> None:
        self.files: Dict[str, Tuple[str, str]] = {}  # path -> (content type, body)
        self.faults: Dict[str, int] = {}  # path -> fault on every request
        self.flaky: Dict[str, List[int]] = {}  # path -> faults for the next requests, then normal
        self.requests: List[str] = []
        self.arrivals: List[Tuple[str, float]] = []  # (path, time.monotonic()) per request
        self.base_url = ""
        self._runner: Optional[web.AppRunner] = None

    async def start(self) -> str:
        app = web.Application()
        app.router.add_route("GET", "/{tail:.*}", self._handle)
        self._runner = web.AppRunner(app)
        await self._runner.setup()
        site = web.TCPSite(self._runner, "127.0.0.1", 0)
        await site.start()
        port = self._runner.addresses[0][1]
        self.base_url = f"http://127.0.0.1:{port}"
        return self.base_url

    async def stop(self) -> None:
        if self._runner is not None:
            await self._runner.cleanup()

    def count(self, path: str) -> int:
        """How many requests a path got."""
        return self.requests.count(path)

    async def _handle(self, request: web.Request) -> web.StreamResponse:
        path = request.path
        self.requests.append(path)
        self.arrivals.append((path, time.monotonic()))
        fault: Optional[int] = None
        if self.flaky.get(path):
            fault = self.flaky[path].pop(0)
        elif path in self.faults:
            fault = self.faults[path]
        if fault == DROP:
            assert request.transport is not None
            request.transport.close()
            await asyncio.sleep(0.05)
            return web.Response(status=500)
        if fault == BAD_JSON:
            return web.Response(status=200, text="{not json", content_type="application/json")
        if fault is not None:
            return web.Response(status=fault, text=f"fault {fault}")
        if path.startswith("/api/repos/"):
            return self._listing(path)
        if path in self.files:
            content_type, body = self.files[path]
            return web.Response(status=200, text=body, content_type=content_type)
        return web.Response(status=404, text="not found")

    # -- Sphinx -------------------------------------------------------------

    def sphinx_page(self, path: str, title: str, links: Tuple[str, ...] = (), body: str = "") -> None:
        """A Sphinx page at /sphinx/<path>, linking to links (hrefs as written)."""
        anchors = "".join(f'<li><a href="{href}">{href}</a></li>' for href in links)
        html = (f"<html><body><main><h1>{title}</h1><p>{body or title} text.</p>"
                f"<ul>{anchors}</ul></main></body></html>")
        self.files[f"/sphinx/{path}"] = ("text/html", html)

    def sphinx_url(self, path: str = "") -> str:
        return f"{self.base_url}/sphinx/{path}"

    # -- Web pages ----------------------------------------------------------

    def web_page(self, path: str, html: str) -> None:
        """A web page at /web/<path> (path as configured, e.g. "guide/rules/")."""
        self.files[f"/web/{path}"] = ("text/html", html)

    def web_url(self, path: str = "") -> str:
        return f"{self.base_url}/web/{path}"

    # -- GitHub -------------------------------------------------------------

    def github_file(self, repo: str, path: str, content: str, branch: str = "main") -> None:
        self.files[f"/raw/{repo}/{branch}/{path}"] = ("text/plain", content)

    def raw_path(self, repo: str, path: str, branch: str = "main") -> str:
        return f"/raw/{repo}/{branch}/{path}"

    def api_path(self, repo: str, path: str) -> str:
        return f"/api/repos/{repo}/contents/{path}"

    def _listing(self, path: str) -> web.Response:
        rest = path[len("/api/repos/"):]
        owner, name, _, directory = rest.split("/", 3)
        repo = f"{owner}/{name}"
        prefix = f"/raw/{repo}/main/"
        entries: Dict[str, Dict[str, Any]] = {}
        for file_path in self.files:
            if not file_path.startswith(prefix + directory + "/"):
                continue
            repo_path = file_path[len(prefix):]
            child = repo_path[len(directory) + 1:].split("/", 1)[0]
            child_path = f"{directory}/{child}"
            if "/" in repo_path[len(directory) + 1:]:
                entries[child_path] = {"name": child, "path": child_path, "type": "dir"}
            else:
                entries[child_path] = {"name": child, "path": child_path, "type": "file"}
        if not entries:
            return web.Response(status=404, text='{"message": "Not Found"}', content_type="application/json")
        return web.Response(status=200, text=json.dumps(sorted(entries.values(), key=lambda e: e["path"])),
                            content_type="application/json")

    # -- HIG ----------------------------------------------------------------

    def hig_page(self, name: str, title: str, children: Tuple[str, ...] = (), abstract: str = "") -> None:
        """A HIG page ("" is the root), with topic links to children (page names)."""
        identifiers = [f"doc://com.apple.HIG/design/Human-Interface-Guidelines/{child}" for child in children]
        references = {
            identifier: {"title": child.title(), "url": f"/design/human-interface-guidelines/{child}"}
            for identifier, child in zip(identifiers, children, strict=True)
        }
        data = {
            "metadata": {"title": title, "role": "article"},
            "abstract": [{"type": "text", "text": abstract or f"About {title}."}],
            "primaryContentSections": [{"kind": "content", "content": [
                {"type": "paragraph", "inlineContent": [{"type": "text", "text": f"{title} body."}]}
            ]}],
            "topicSections": [{"title": "Topics", "identifiers": identifiers}] if identifiers else [],
            "references": references,
        }
        self.files[self.hig_path(name)] = ("application/json", json.dumps(data))

    def hig_path(self, name: str) -> str:
        return f"{HIG_PREFIX}/{HIG_ROOT}.json" if not name else f"{HIG_PREFIX}/{HIG_ROOT}/{name}.json"

    def hig_base(self) -> str:
        return f"{self.base_url}{HIG_PREFIX}"
