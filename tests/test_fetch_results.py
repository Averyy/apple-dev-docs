"""fetch_page_with_etag's result sentinels and how each caller handles them.

fetch_page_with_etag returns (content, etag), NOT_MODIFIED or FetchFailed and
never writes a hash entry; its callers apply the failure policy. These tests
pin every caller's outcome for one call (return value, mark_error calls, hash
entries, queued children, the failure recorded for the end-of-run count) for
each response kind: 200, 304, 4xx, 429 and 5xx after all retries, timeout, a
200 whose body is not JSON, and a convert/save error of ours. How those
failures are counted across runs is in test_failure_policy.py. They run
offline against an httpx.MockTransport.
"""

import dataclasses
import errno
import hashlib
import json
import os
import sys
from collections import deque
from pathlib import Path
from typing import Any, Callable, Deque, Dict, List, Optional, Sequence, Tuple

import httpx
import pytest
from structlog.testing import capture_logs
from structlog.typing import EventDict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper.base import NOT_MODIFIED, FetchFailed, NotModified
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper

FW = "testkit"
JSON_BASE = AppleJSONDocumentationScraper.JSON_BASE_URL
DOC_BASE = "https://developer.apple.com/documentation"
OLD_TS = "2026-01-01T00:00:00"
OLD_SESSION = "2026-01-01T00:00:00.000001"
MAX_RETRIES = 3

Spec = Dict[str, Any]


def json_url(path: str) -> str:
    return f"{JSON_BASE}/{path}.json"


def doc_url(path: str) -> str:
    return f"{DOC_BASE}/{path}"


def page(path: str, children: Sequence[str] = ()) -> str:
    """A minimal Apple JSON page body that links to `children`."""
    return json.dumps({
        "identifier": {"url": f"doc://com.apple.{FW}/documentation/{path}", "interfaceLanguage": "swift"},
        "metadata": {"title": path.split("/")[-1], "symbolKind": "class", "roleHeading": "Class"},
        "abstract": [{"type": "text", "text": f"The {path} page."}],
        "topicSections": [{
            "title": "Topics",
            "identifiers": [f"doc://com.apple.{FW}/documentation/{c}" for c in children],
        }],
    })


def ok(body: str, etag: str) -> Spec:
    """200 with an ETag, or 304 when the request's If-None-Match matches it."""
    return {"kind": "ok", "body": body, "etag": etag}


def status(code: int) -> Spec:
    return {"kind": "status", "code": code}


TIMEOUT: Spec = {"kind": "timeout"}
CONNECT_ERROR: Spec = {"kind": "connect"}


class FakeApple:
    """MockTransport handler: a response sequence per URL (the last repeats)."""

    def __init__(self, routes: Dict[str, List[Spec]]) -> None:
        self.routes = routes
        self.calls: Dict[str, int] = {}
        self.requests: List[Tuple[str, Optional[str]]] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        url = str(request.url)
        if_none_match = request.headers.get("If-None-Match")
        self.requests.append((url, if_none_match))
        seq = self.routes[url]
        i = self.calls.get(url, 0)
        self.calls[url] = i + 1
        spec = seq[min(i, len(seq) - 1)]
        if spec["kind"] == "timeout":
            raise httpx.ReadTimeout("timed out", request=request)
        if spec["kind"] == "connect":
            raise httpx.ConnectError("connection refused", request=request)
        if spec["kind"] == "status":
            return httpx.Response(spec["code"], text="error", request=request)
        if if_none_match is not None and if_none_match == spec["etag"]:
            return httpx.Response(304, headers={"ETag": spec["etag"]}, request=request)
        return httpx.Response(200, text=spec["body"], headers={"ETag": spec["etag"]}, request=request)


class Rig:
    """A scraper wired to FakeApple, with mark_error calls recorded."""

    def __init__(self, routes: Dict[str, List[Spec]], monkeypatch: pytest.MonkeyPatch) -> None:
        self.fake = FakeApple(routes)
        self.scraper = AppleJSONDocumentationScraper(FW, "TestKit")
        self.scraper.session = httpx.AsyncClient(
            transport=httpx.MockTransport(self.fake), follow_redirects=True
        )

        async def no_wait() -> None:
            return None

        monkeypatch.setattr(self.scraper.rate_limiter, "acquire", no_wait)
        self.mark_error_calls: List[Tuple[str, str]] = []
        real_mark_error = self.scraper.hash_manager.mark_error

        def spy(url: str, error: str) -> None:
            self.mark_error_calls.append((url, error))
            real_mark_error(url, error)

        monkeypatch.setattr(self.scraper.hash_manager, "mark_error", spy)
        self.events: List[EventDict] = []

    def logged(self, event: str) -> List[EventDict]:
        """The captured structlog events named `event`."""
        return [e for e in self.events if e["event"] == event]

    @property
    def hashes(self) -> Dict[str, Dict[str, Any]]:
        return self.scraper.hash_manager.hashes

    @property
    def session_id(self) -> str:
        return self.scraper.hash_manager.session_id

    def seed_good(self, path: str, body: str, etag: str) -> Path:
        """Record `path` as a previously good page (both keys, file on disk)."""
        url = doc_url(path)
        file_path = self.scraper._get_organized_file_path(url, {})
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(f"# {path}\n", encoding="utf-8")
        entry = {
            "hash": hashlib.sha256(body.encode("utf-8")).hexdigest(),
            "last_checked": OLD_TS,
            "status": "unchanged",
            "session_id": OLD_SESSION,
            "etag": etag,
            "file_path": str(file_path),
        }
        self.hashes[json_url(path)] = dict(entry)
        self.hashes[url] = dict(entry)
        return file_path


@pytest.fixture
def make_rig(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Callable[[Dict[str, List[Spec]]], Rig]:
    monkeypatch.setattr(Config, "OUTPUT_DIR", tmp_path / "documentation")
    monkeypatch.setattr(Config, "CACHE_DIR", tmp_path / ".hashes")
    monkeypatch.setattr(Config, "MAX_RETRIES", MAX_RETRIES)
    monkeypatch.setattr(Config, "RETRY_BACKOFF_FACTOR", 0.0)
    return lambda routes: Rig(routes, monkeypatch)


def http_status_error(code: int, url: str) -> str:
    """The message mark_error records for a status that outlasted its retries."""
    request = httpx.Request("GET", url)
    response = httpx.Response(code, request=request)
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        return str(e)
    raise AssertionError(f"{code} is not an error status")


def assert_error_entry(entry: Dict[str, Any], error: str) -> None:
    """mark_error's entry: no file_path, session_id or etag survive."""
    assert set(entry) == {"hash", "last_checked", "status", "error"}
    assert entry["hash"] == ""
    assert entry["status"] == "error"
    assert entry["error"] == error
    assert entry["last_checked"] != OLD_TS


ALPHA = "testkit/alpha"
ALPHA_BODY = page(ALPHA, ["testkit/alpha/child"])
ALPHA_CHILD = json_url("testkit/alpha/child")
ROOT_BODY = page(FW, [ALPHA])


class TestSentinels:
    def test_not_modified_is_a_singleton_enum_member(self) -> None:
        assert NOT_MODIFIED is NotModified.NOT_MODIFIED
        assert list(NotModified) == [NOT_MODIFIED]

    def test_fetch_failed_is_an_immutable_value(self) -> None:
        failed = FetchFailed(status=404, error="HTTP 404", transient=False)
        assert failed == FetchFailed(404, "HTTP 404", False)
        with pytest.raises(dataclasses.FrozenInstanceError):
            failed.status = 500  # type: ignore[misc]


class TestFetchPageWithEtag:
    """The fetch itself: what it returns, and that it never writes hashes."""

    async def test_200_returns_content_and_etag(self, make_rig: Callable[..., Rig]) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A")]})
        result = await rig.scraper.fetch_page_with_etag(json_url(ALPHA))
        assert result == (ALPHA_BODY, "E-A")
        assert rig.hashes == {}

    async def test_304_returns_not_modified(self, make_rig: Callable[..., Rig]) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A")]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        before = json.loads(json.dumps(rig.hashes))
        result = await rig.scraper.fetch_page_with_etag(json_url(ALPHA))
        assert result is NOT_MODIFIED
        assert rig.fake.requests == [(json_url(ALPHA), "E-A")]
        assert rig.hashes == before

    async def test_use_etag_false_sends_no_if_none_match(self, make_rig: Callable[..., Rig]) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A")]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        result = await rig.scraper.fetch_page_with_etag(json_url(ALPHA), use_etag=False)
        assert result == (ALPHA_BODY, "E-A")
        assert rig.fake.requests == [(json_url(ALPHA), None)]

    @pytest.mark.parametrize("code", [403, 404, 410])
    async def test_4xx_fails_at_once_without_writing(self, make_rig: Callable[..., Rig], code: int) -> None:
        rig = make_rig({json_url(ALPHA): [status(code)]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        before = json.loads(json.dumps(rig.hashes))
        result = await rig.scraper.fetch_page_with_etag(json_url(ALPHA))
        assert result == FetchFailed(status=code, error=f"HTTP {code}", transient=False)
        assert len(rig.fake.requests) == 1
        assert rig.hashes == before
        assert rig.mark_error_calls == []
        assert rig.scraper.stats["pages_failed"] == 0

    @pytest.mark.parametrize("code", [429, 500, 502, 503])
    async def test_status_exhausting_retries_is_transient(self, make_rig: Callable[..., Rig], code: int) -> None:
        rig = make_rig({json_url(ALPHA): [status(code)]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        before = json.loads(json.dumps(rig.hashes))
        result = await rig.scraper.fetch_page_with_etag(json_url(ALPHA))
        assert result == FetchFailed(
            status=code, error=http_status_error(code, json_url(ALPHA)), transient=True
        )
        assert len(rig.fake.requests) == MAX_RETRIES + 1
        assert rig.hashes == before
        assert rig.mark_error_calls == []
        assert rig.scraper.stats["pages_failed"] == 1

    @pytest.mark.parametrize("spec,error", [(TIMEOUT, "timed out"), (CONNECT_ERROR, "connection refused")])
    async def test_network_error_exhausting_retries_has_no_status(
        self, make_rig: Callable[..., Rig], spec: Spec, error: str
    ) -> None:
        rig = make_rig({json_url(ALPHA): [spec]})
        result = await rig.scraper.fetch_page_with_etag(json_url(ALPHA))
        assert result == FetchFailed(status=None, error=error, transient=True)
        assert len(rig.fake.requests) == MAX_RETRIES + 1
        assert rig.hashes == {}
        assert rig.scraper.stats["pages_failed"] == 1

    async def test_recovers_within_retries(self, make_rig: Callable[..., Rig]) -> None:
        rig = make_rig({json_url(ALPHA): [status(502), TIMEOUT, ok(ALPHA_BODY, "E-A")]})
        result = await rig.scraper.fetch_page_with_etag(json_url(ALPHA))
        assert result == (ALPHA_BODY, "E-A")
        assert len(rig.fake.requests) == 3
        assert rig.scraper.stats["pages_failed"] == 0


def assert_touched_only(entry: Dict[str, Any], before: Dict[str, Any], session_id: str) -> None:
    """The entry was kept: only session_id and last_checked were refreshed."""
    assert entry["session_id"] == session_id
    assert entry["last_checked"] != OLD_TS
    assert {k: v for k, v in entry.items() if k not in ("session_id", "last_checked")} == {
        k: v for k, v in before.items() if k not in ("session_id", "last_checked")
    }


def recorded(rig: Rig) -> Dict[str, Tuple[str, FetchFailed]]:
    """The fetch failures recorded this run for the end-of-run count."""
    return {url: (f.kind, f.failure) for url, f in rig.scraper._fetch_failures.items()}


class TestProcessQueuedUrl:
    """_process_queued_url and its discovery refetch after a 304."""

    @staticmethod
    async def process(rig: Rig, tmp_path: Path) -> List[str]:
        queue: Deque[str] = deque()
        with capture_logs() as events:
            await rig.scraper._process_queued_url(json_url(ALPHA), queue, tmp_path / "progress.txt")
        rig.events = events
        # Every outcome is handled where it happens; none may reach the
        # function's catch-all, which would hide a broken branch.
        assert rig.logged("error_processing_url") == []
        assert "exception" not in rig.scraper.outcome.blocks
        return list(queue)

    async def test_200_saves_and_enqueues(self, make_rig: Callable[..., Rig], tmp_path: Path) -> None:
        body = page(ALPHA, ["testkit/alpha/child", "testkit/alpha/new"])
        rig = make_rig({json_url(ALPHA): [ok(body, "E-A2")]})
        file_path = rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        queue = await self.process(rig, tmp_path)
        assert queue == [ALPHA_CHILD, json_url("testkit/alpha/new")]
        assert rig.mark_error_calls == []
        for key in (json_url(ALPHA), doc_url(ALPHA)):
            assert rig.hashes[key]["etag"] == "E-A2"
            assert rig.hashes[key]["session_id"] == rig.session_id
            assert rig.hashes[key]["file_path"] == str(file_path)
        assert "The testkit/alpha page." in file_path.read_text(encoding="utf-8")
        assert rig.scraper._fetch_ok == {json_url(ALPHA)}
        assert rig.scraper._saved_ok == {json_url(ALPHA)}
        assert recorded(rig) == {}
        assert rig.scraper.stats["pages_scraped"] == 1

    async def test_200_writes_the_file_before_recording_it(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        body = page(ALPHA, ["testkit/alpha/child", "testkit/alpha/new"])
        rig = make_rig({json_url(ALPHA): [ok(body, "E-A2")]})
        file_path = rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        file_path.unlink()
        seen: List[Tuple[str, bool]] = []
        real_update_hash = rig.scraper.hash_manager.update_hash

        def spy(url: str, content: str, etag: Optional[str] = None, file_path: Optional[Path] = None) -> None:
            seen.append((url, file_path is not None and file_path.exists()))
            real_update_hash(url, content, etag, file_path)

        monkeypatch.setattr(rig.scraper.hash_manager, "update_hash", spy)
        await self.process(rig, tmp_path)
        assert seen == [(json_url(ALPHA), True), (doc_url(ALPHA), True)]

    async def test_200_same_content_reuses_the_stored_path(
        self, make_rig: Callable[..., Rig], tmp_path: Path
    ) -> None:
        # A new etag on the same content: the stored file path is kept, not recomputed
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A2")]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        stored = rig.scraper.output_dir / "alpha-stored.md"
        stored.write_text("# stored\n", encoding="utf-8")
        rig.hashes[json_url(ALPHA)]["file_path"] = str(stored)
        queue = await self.process(rig, tmp_path)
        assert queue == [ALPHA_CHILD]
        for key in (json_url(ALPHA), doc_url(ALPHA)):
            assert rig.hashes[key]["file_path"] == str(stored)
            assert rig.hashes[key]["etag"] == "E-A2"
            assert rig.hashes[key]["session_id"] == rig.session_id
        assert stored.read_text(encoding="utf-8") == "# stored\n"
        assert rig.scraper.stats["pages_skipped"] == 1
        assert rig.scraper.stats["pages_scraped"] == 0

    async def test_200_same_content_without_a_stored_path_writes_the_file(
        self, make_rig: Callable[..., Rig], tmp_path: Path
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A2")]})
        file_path = rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        file_path.unlink()
        del rig.hashes[json_url(ALPHA)]["file_path"]
        await self.process(rig, tmp_path)
        assert "The testkit/alpha page." in file_path.read_text(encoding="utf-8")
        for key in (json_url(ALPHA), doc_url(ALPHA)):
            assert rig.hashes[key]["file_path"] == str(file_path)

    async def test_304_refreshes_session_and_rediscovers(self, make_rig: Callable[..., Rig], tmp_path: Path) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A")]})
        file_path = rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        queue = await self.process(rig, tmp_path)
        assert rig.fake.requests == [(json_url(ALPHA), "E-A"), (json_url(ALPHA), None)]
        assert queue == [ALPHA_CHILD]
        assert rig.mark_error_calls == []
        entry = rig.hashes[json_url(ALPHA)]
        assert entry["session_id"] == rig.session_id
        assert entry["file_path"] == str(file_path)
        assert entry["etag"] == "E-A"
        assert rig.scraper.stats["pages_skipped"] == 1
        assert rig.scraper._fetch_ok == {json_url(ALPHA)}
        assert recorded(rig) == {}

    async def test_304_then_refetch_304_is_a_failed_refetch(
        self, make_rig: Callable[..., Rig], tmp_path: Path
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A"), status(304)]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        before = dict(rig.hashes[json_url(ALPHA)])
        queue = await self.process(rig, tmp_path)
        assert queue == []
        assert rig.mark_error_calls == []
        assert_touched_only(rig.hashes[json_url(ALPHA)], before, rig.session_id)
        kind, failure = recorded(rig)[json_url(ALPHA)]
        assert kind == "after_304"
        assert failure.status == 304 and failure.transient
        assert rig.scraper._fetch_ok == set()

    @pytest.mark.parametrize("code", [404, 410])
    async def test_404_410_on_good_page_is_a_removal(
        self, make_rig: Callable[..., Rig], tmp_path: Path, code: int
    ) -> None:
        # One fetch, no refetch: the JSON key becomes an error entry, so the
        # file is orphaned; nothing blocks
        rig = make_rig({json_url(ALPHA): [status(code)]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        doc_entry = dict(rig.hashes[doc_url(ALPHA)])
        queue = await self.process(rig, tmp_path)
        error = f"HTTP {code}"
        assert rig.fake.requests == [(json_url(ALPHA), "E-A")]
        assert rig.mark_error_calls == [(json_url(ALPHA), error)]
        assert_error_entry(rig.hashes[json_url(ALPHA)], error)
        assert rig.hashes[doc_url(ALPHA)] == doc_entry
        assert [(e["url"], e["status"]) for e in rig.logged("page_gone")] == [(json_url(ALPHA), code)]
        assert rig.scraper._gone == {json_url(ALPHA)}
        assert queue == []
        assert recorded(rig) == {}
        assert rig.scraper.outcome.blocks == {}
        assert rig.scraper.stats["pages_skipped"] == 0

    @pytest.mark.parametrize("spec", [status(403), status(429), status(500), status(502), status(503), TIMEOUT])
    async def test_other_failure_keeps_a_good_page(
        self, make_rig: Callable[..., Rig], tmp_path: Path, spec: Spec
    ) -> None:
        rig = make_rig({json_url(ALPHA): [spec]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        json_entry = dict(rig.hashes[json_url(ALPHA)])
        doc_entry = dict(rig.hashes[doc_url(ALPHA)])
        queue = await self.process(rig, tmp_path)
        assert rig.mark_error_calls == []
        # No discovery refetch for a failed URL
        assert {url for url, _ in rig.fake.requests} == {json_url(ALPHA)}
        assert all(etag == "E-A" for _, etag in rig.fake.requests)
        assert_touched_only(rig.hashes[json_url(ALPHA)], json_entry, rig.session_id)
        assert rig.hashes[doc_url(ALPHA)] == doc_entry
        assert queue == []
        kind, failure = recorded(rig)[json_url(ALPHA)]
        assert kind == "previously_good"
        assert failure.transient == (spec != status(403))
        assert rig.scraper.stats["pages_skipped"] == 0

    @pytest.mark.parametrize("code", [403, 404, 410])
    async def test_4xx_on_new_url_marks_error_once_and_doesnt_count(
        self, make_rig: Callable[..., Rig], tmp_path: Path, code: int
    ) -> None:
        rig = make_rig({json_url(ALPHA): [status(code)]})
        queue = await self.process(rig, tmp_path)
        assert rig.mark_error_calls == [(json_url(ALPHA), f"HTTP {code}")]
        assert_error_entry(rig.hashes[json_url(ALPHA)], f"HTTP {code}")
        assert set(rig.hashes) == {json_url(ALPHA)}
        assert queue == []
        assert recorded(rig) == {}

    @pytest.mark.parametrize("spec", [status(429), status(502), TIMEOUT])
    async def test_transient_failure_on_new_url_counts(
        self, make_rig: Callable[..., Rig], tmp_path: Path, spec: Spec
    ) -> None:
        rig = make_rig({json_url(ALPHA): [spec]})
        await self.process(rig, tmp_path)
        assert [url for url, _ in rig.mark_error_calls] == [json_url(ALPHA)]
        assert rig.hashes[json_url(ALPHA)]["status"] == "error"
        assert recorded(rig)[json_url(ALPHA)][0] == "never_good"

    async def test_failure_on_new_url_keeps_its_counters(
        self, make_rig: Callable[..., Rig], tmp_path: Path
    ) -> None:
        rig = make_rig({json_url(ALPHA): [status(502)]})
        rig.hashes[json_url(ALPHA)] = {
            "hash": "", "last_checked": OLD_TS, "status": "error", "error": "old",
            "consecutive_failures": 2, "consecutive_local_errors": 1,
        }
        await self.process(rig, tmp_path)
        entry = rig.hashes[json_url(ALPHA)]
        assert entry["consecutive_failures"] == 2
        assert entry["consecutive_local_errors"] == 1
        assert entry["error"] == http_status_error(502, json_url(ALPHA))

    @pytest.mark.parametrize("refetch,error", [
        (status(403), "HTTP 403"),
        (status(502), None),
        (TIMEOUT, "timed out"),
    ])
    async def test_304_then_failed_refetch_keeps_the_page(
        self, make_rig: Callable[..., Rig], tmp_path: Path, refetch: Spec, error: Optional[str]
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A"), refetch]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        before = dict(rig.hashes[json_url(ALPHA)])
        queue = await self.process(rig, tmp_path)
        assert rig.mark_error_calls == []
        assert_touched_only(rig.hashes[json_url(ALPHA)], before, rig.session_id)
        assert queue == []
        kind, failure = recorded(rig)[json_url(ALPHA)]
        assert kind == "after_304"
        assert failure.error == (error or http_status_error(refetch["code"], json_url(ALPHA)))
        assert rig.scraper._fetch_ok == set()

    @pytest.mark.parametrize("code", [404, 410])
    async def test_304_then_refetch_404_410_is_a_removal(
        self, make_rig: Callable[..., Rig], tmp_path: Path, code: int
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A"), status(code)]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        queue = await self.process(rig, tmp_path)
        assert rig.mark_error_calls == [(json_url(ALPHA), f"HTTP {code}")]
        assert_error_entry(rig.hashes[json_url(ALPHA)], f"HTTP {code}")
        assert queue == []
        assert recorded(rig) == {}

    async def test_304_then_refetch_invalid_json_keeps_the_page(
        self, make_rig: Callable[..., Rig], tmp_path: Path
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A"), ok("not json {", "E-A")]})
        file_path = rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        json_entry = dict(rig.hashes[json_url(ALPHA)])
        doc_entry = dict(rig.hashes[doc_url(ALPHA)])
        queue = await self.process(rig, tmp_path)
        assert rig.fake.requests == [(json_url(ALPHA), "E-A"), (json_url(ALPHA), None)]
        assert rig.mark_error_calls == []
        assert queue == []
        assert [e["url"] for e in rig.logged("failed_to_parse_json_for_rediscovery")] == [json_url(ALPHA)]
        assert rig.logged("rediscovered_child_urls") == []
        assert_touched_only(rig.hashes[json_url(ALPHA)], json_entry, rig.session_id)
        assert rig.hashes[json_url(ALPHA)]["file_path"] == str(file_path)
        assert rig.hashes[doc_url(ALPHA)] == doc_entry
        assert recorded(rig)[json_url(ALPHA)] == (
            "after_304", FetchFailed(status=200, error="invalid json", transient=True)
        )
        assert rig.scraper.stats["pages_skipped"] == 1
        assert rig.scraper.stats["pages_failed"] == 1

    async def test_200_invalid_json_keeps_a_good_page(self, make_rig: Callable[..., Rig], tmp_path: Path) -> None:
        # Treated as FetchFailed(200, 'invalid json', transient=True)
        rig = make_rig({json_url(ALPHA): [ok("not json {", "E-BAD")]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        json_entry = dict(rig.hashes[json_url(ALPHA)])
        doc_entry = dict(rig.hashes[doc_url(ALPHA)])
        queue = await self.process(rig, tmp_path)
        assert rig.mark_error_calls == []
        assert_touched_only(rig.hashes[json_url(ALPHA)], json_entry, rig.session_id)
        assert rig.hashes[doc_url(ALPHA)] == doc_entry
        assert queue == []
        assert [e["url"] for e in rig.logged("failed_to_parse_json")] == [json_url(ALPHA)]
        assert recorded(rig)[json_url(ALPHA)] == (
            "previously_good", FetchFailed(status=200, error="invalid json", transient=True)
        )
        assert rig.scraper._fetch_ok == set()

    async def test_200_invalid_json_on_new_url_counts(self, make_rig: Callable[..., Rig], tmp_path: Path) -> None:
        rig = make_rig({json_url(ALPHA): [ok("not json {", "E-BAD")]})
        await self.process(rig, tmp_path)
        assert_error_entry(rig.hashes[json_url(ALPHA)], "invalid json")
        assert recorded(rig)[json_url(ALPHA)][0] == "never_good"

    @pytest.mark.parametrize("target", ["save", "save-part-way", "convert", "extract", "path"])
    async def test_local_error_keeps_the_page_and_enqueues_links_first(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch, target: str
    ) -> None:
        body = page(ALPHA, ["testkit/alpha/child", "testkit/alpha/new"])
        rig = make_rig({json_url(ALPHA): [ok(body, "E-A2")]})
        file_path = rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        json_entry = dict(rig.hashes[json_url(ALPHA)])
        doc_entry = dict(rig.hashes[doc_url(ALPHA)])
        write_text = Path.write_text

        def boom(*args: Any, **kwargs: Any) -> Any:
            raise OSError("disk full")

        def disk_full_part_way(path: Path, data: str, *args: Any, **kwargs: Any) -> int:
            write_text(path, data[:5], *args, **kwargs)
            raise OSError(errno.ENOSPC, "No space left on device")

        if target == "save":
            monkeypatch.setattr(Path, "write_text", boom)
        elif target == "save-part-way":
            # Doc writes are atomic: the old doc stays whole, no temp file is left
            monkeypatch.setattr(Path, "write_text", disk_full_part_way)
        elif target == "convert":
            monkeypatch.setattr(rig.scraper.markdown_converter, "convert_page", boom)
        elif target == "extract":
            monkeypatch.setattr(rig.scraper, "_extract_from_json", boom)
        else:
            monkeypatch.setattr(rig.scraper, "_get_organized_file_path", boom)
        queue = await self.process(rig, tmp_path)
        # Links first: the children are queued even though the save failed
        assert queue == [ALPHA_CHILD, json_url("testkit/alpha/new")]
        # File first: the old hash/etag/file_path stay, so the next run refetches
        assert_touched_only(rig.hashes[json_url(ALPHA)], json_entry, rig.session_id)
        assert rig.hashes[doc_url(ALPHA)] == doc_entry
        assert file_path.read_text(encoding="utf-8") == f"# {ALPHA}\n"
        assert not list(file_path.parent.glob("*.tmp"))
        assert rig.mark_error_calls == []
        assert list(rig.scraper._local_errors) == [json_url(ALPHA)]
        assert [e["url"] for e in rig.logged("page_save_failed")] == [json_url(ALPHA)]
        assert rig.scraper._saved_ok == set()
        # A 200 still counts as a good fetch (resets consecutive_failures)
        assert rig.scraper._fetch_ok == {json_url(ALPHA)}
        assert recorded(rig) == {}
        assert rig.scraper.stats["pages_scraped"] == 0

    async def test_local_error_on_new_url_writes_an_error_entry(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A")]})

        def boom(data: Dict[str, Any]) -> str:
            raise ValueError("bad table")

        monkeypatch.setattr(rig.scraper.markdown_converter, "convert_page", boom)
        queue = await self.process(rig, tmp_path)
        assert queue == [ALPHA_CHILD]
        assert_error_entry(rig.hashes[json_url(ALPHA)], "local error: bad table")
        assert doc_url(ALPHA) not in rig.hashes
        assert list(rig.scraper._local_errors) == [json_url(ALPHA)]

    @pytest.mark.parametrize("target", ["save", "convert", "extract"])
    @pytest.mark.parametrize("keys", ["both-errors", "doc-live"])
    async def test_local_error_keeps_a_file_no_live_entry_records(
        self,
        make_rig: Callable[..., Rig],
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
        target: str,
        keys: str,
    ) -> None:
        """The file is on disk, but D8 marked both keys (or a 404 the JSON-URL key) in a run that kept it."""
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A2")]})
        file_path = rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        error_entry = {"hash": "", "last_checked": OLD_TS, "status": "error", "error": "HTTP 502"}
        rig.hashes[json_url(ALPHA)] = {**error_entry, "consecutive_failures": 3}
        if keys == "both-errors":
            rig.hashes[doc_url(ALPHA)] = dict(error_entry)
        else:
            # The doc-URL key's recorded path wins over the one computed this run
            file_path = rig.scraper.output_dir / "alpha-stored.md"
            file_path.write_text(f"# {ALPHA}\n", encoding="utf-8")
            rig.hashes[doc_url(ALPHA)]["file_path"] = str(file_path)
        doc_entry = dict(rig.hashes[doc_url(ALPHA)])

        def boom(*args: Any, **kwargs: Any) -> Any:
            raise OSError("disk full")

        if target == "save":
            monkeypatch.setattr(Path, "write_text", boom)
        elif target == "convert":
            monkeypatch.setattr(rig.scraper.markdown_converter, "convert_page", boom)
        else:
            monkeypatch.setattr(rig.scraper, "_extract_from_json", boom)
        queue = await self.process(rig, tmp_path)
        assert queue == [ALPHA_CHILD]
        # The JSON-URL key records the file again and is touched; with no etag
        # and an unknown hash, the next run refetches and converts the page
        entry = rig.hashes[json_url(ALPHA)]
        assert entry == {
            "hash": "", "status": "unchanged", "file_path": str(file_path), "consecutive_failures": 3,
            "session_id": rig.session_id, "last_checked": entry["last_checked"],
        }
        assert entry["last_checked"] != OLD_TS
        assert rig.hashes[doc_url(ALPHA)] == doc_entry
        assert file_path.read_text(encoding="utf-8") == f"# {ALPHA}\n"
        assert rig.mark_error_calls == []
        assert list(rig.scraper._local_errors) == [json_url(ALPHA)]

    async def test_local_error_while_extracting_finds_a_file_named_by_its_kind(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """A page named like its framework gets a kind suffix: the kind is read from its JSON."""
        path = f"{FW}/{FW}"
        rig = make_rig({json_url(path): [ok(page(path), "E-T2")]})
        file_path = rig.scraper.output_dir / f"{FW}-class.md"
        file_path.parent.mkdir(parents=True)
        file_path.write_text("# old\n", encoding="utf-8")
        for key in (json_url(path), doc_url(path)):
            rig.hashes[key] = {"hash": "", "last_checked": OLD_TS, "status": "error", "error": "HTTP 502"}

        def boom(*args: Any, **kwargs: Any) -> Any:
            raise ValueError("unsupported block")

        monkeypatch.setattr(rig.scraper, "_extract_from_json", boom)
        await rig.scraper._process_queued_url(json_url(path), deque(), tmp_path / "progress.txt")
        entry = rig.hashes[json_url(path)]
        assert entry["file_path"] == str(file_path) and entry["session_id"] == rig.session_id
        assert rig.mark_error_calls == []

    async def test_local_error_after_the_path_records_the_path_computed_this_run(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A2")]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        for key in (json_url(ALPHA), doc_url(ALPHA)):
            rig.hashes[key] = {"hash": "", "last_checked": OLD_TS, "status": "error", "error": "HTTP 502"}
        computed = rig.scraper.output_dir / "alpha-computed.md"
        computed.write_text(f"# {ALPHA}\n", encoding="utf-8")
        real_path = rig.scraper._get_organized_file_path

        def path_of(url: str, data: Dict[str, Any]) -> Path:
            # Only the fully extracted data gives this run's path
            return computed if "title" in data else real_path(url, data)

        def boom(data: Dict[str, Any]) -> str:
            raise ValueError("bad table")

        monkeypatch.setattr(rig.scraper, "_get_organized_file_path", path_of)
        monkeypatch.setattr(rig.scraper.markdown_converter, "convert_page", boom)
        await self.process(rig, tmp_path)
        assert rig.hashes[json_url(ALPHA)]["file_path"] == str(computed)

    async def test_local_error_with_no_computable_path_writes_an_error_entry(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A2")]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")
        for key in (json_url(ALPHA), doc_url(ALPHA)):
            rig.hashes[key] = {"hash": "", "last_checked": OLD_TS, "status": "error", "error": "HTTP 502"}

        def boom(*args: Any, **kwargs: Any) -> Any:
            raise ValueError("bad path")

        monkeypatch.setattr(rig.scraper, "_get_organized_file_path", boom)
        # Still a counted local error: the failed lookup doesn't reach the outer except
        queue = await self.process(rig, tmp_path)
        assert queue == [ALPHA_CHILD]
        assert_error_entry(rig.hashes[json_url(ALPHA)], "local error: bad path")
        assert list(rig.scraper._local_errors) == [json_url(ALPHA)]
        assert [e["url"] for e in rig.logged("page_file_path_failed")] == [json_url(ALPHA)]

    async def test_local_error_saving_a_name_too_long_writes_an_error_entry(
        self, make_rig: Callable[..., Rig], tmp_path: Path
    ) -> None:
        """A new page whose file name is over the filesystem's limit (255 bytes).

        The file lookup's existence check fails the same way the save did:
        still a counted local error, never the outer except.
        """
        path = f"{FW}/{'a' * 300}"
        rig = make_rig({json_url(path): [ok(page(path, ["testkit/alpha/child"]), "E-L")]})
        queue: Deque[str] = deque()
        with capture_logs() as events:
            await rig.scraper._process_queued_url(json_url(path), queue, tmp_path / "progress.txt")
        rig.events = events
        assert list(queue) == [ALPHA_CHILD]
        assert rig.logged("error_processing_url") == []
        assert rig.scraper.outcome.blocks == {}
        [(url, error)] = rig.mark_error_calls
        assert url == json_url(path) and error.startswith("local error: ")
        assert_error_entry(rig.hashes[json_url(path)], error)
        assert list(rig.scraper._local_errors) == [json_url(path)]
        assert [e["url"] for e in rig.logged("page_save_failed")] == [json_url(path)]

    async def test_unsafe_path_writes_an_error_entry(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A")]})
        outside = tmp_path / "outside.md"
        monkeypatch.setattr(rig.scraper, "_get_organized_file_path", lambda url, data: outside)
        queue = await self.process(rig, tmp_path)
        assert queue == [ALPHA_CHILD]
        assert not outside.exists()
        assert_error_entry(rig.hashes[json_url(ALPHA)], "unsafe file path")
        assert doc_url(ALPHA) not in rig.hashes
        # Never-good and no block: not a local error, not a fetch failure
        assert rig.scraper._local_errors == {}
        assert recorded(rig) == {}
        assert [e["url"] for e in rig.logged("unsafe_file_path_skipped")] == [doc_url(ALPHA)]

    async def test_exception_before_links_blocks_without_counting(
        self, make_rig: Callable[..., Rig], tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rig = make_rig({json_url(ALPHA): [ok(ALPHA_BODY, "E-A2")]})
        rig.seed_good(ALPHA, ALPHA_BODY, "E-A")

        def boom(data: Dict[str, Any]) -> List[str]:
            raise RuntimeError("parser bug")

        monkeypatch.setattr(rig.scraper, "_extract_urls_from_json_data", boom)
        queue: Deque[str] = deque()
        with capture_logs() as events:
            await rig.scraper._process_queued_url(json_url(ALPHA), queue, tmp_path / "progress.txt")
        assert [e["event"] for e in events if e["event"] == "error_processing_url"] == ["error_processing_url"]
        assert rig.scraper.outcome.blocks == {"exception": [json_url(ALPHA)]}
        assert rig.scraper._local_errors == {}
        assert recorded(rig) == {}


class TestScrapePage:
    """scrape_page, the root page's fetch and save."""

    async def test_200_saves_and_records_both_keys(self, make_rig: Callable[..., Rig]) -> None:
        rig = make_rig({json_url(FW): [ok(ROOT_BODY, "E-ROOT")]})
        data = await rig.scraper.scrape_page(doc_url(FW))
        assert data is not None and data["title"] == FW
        assert rig.mark_error_calls == []
        file_path = rig.scraper.output_dir / f"{FW}.md"
        assert f"# {FW}" in file_path.read_text(encoding="utf-8")
        for key in (json_url(FW), doc_url(FW)):
            assert rig.hashes[key]["etag"] == "E-ROOT"
            assert rig.hashes[key]["session_id"] == rig.session_id
            assert rig.hashes[key]["file_path"] == str(file_path)
        assert rig.scraper._root_ok
        assert rig.scraper.stats["pages_scraped"] == 1

    async def test_304_refreshes_both_keys(self, make_rig: Callable[..., Rig]) -> None:
        rig = make_rig({json_url(FW): [ok(ROOT_BODY, "E-ROOT")]})
        file_path = rig.seed_good(FW, ROOT_BODY, "E-ROOT")
        assert await rig.scraper.scrape_page(doc_url(FW)) is None
        assert rig.mark_error_calls == []
        for key in (json_url(FW), doc_url(FW)):
            entry = rig.hashes[key]
            assert entry["status"] == "unchanged"
            assert entry["session_id"] == rig.session_id
            assert entry["file_path"] == str(file_path)
            assert entry["etag"] == "E-ROOT"
        assert rig.scraper.stats["pages_skipped"] == 1
        assert rig.scraper._root_ok

    @pytest.mark.parametrize("code", [404, 410])
    @pytest.mark.parametrize("stored", [True, False])
    async def test_404_410_marks_the_root_gone(
        self, make_rig: Callable[..., Rig], code: int, stored: bool
    ) -> None:
        rig = make_rig({json_url(FW): [status(code)]})
        if stored:
            rig.seed_good(FW, ROOT_BODY, "E-ROOT")
        doc_entry = rig.hashes.get(doc_url(FW))
        assert await rig.scraper.scrape_page(doc_url(FW)) is None
        assert rig.mark_error_calls == [(json_url(FW), f"HTTP {code}")]
        assert_error_entry(rig.hashes[json_url(FW)], f"HTTP {code}")
        assert rig.hashes.get(doc_url(FW)) == doc_entry
        assert rig.scraper._root_gone and not rig.scraper._root_ok
        assert rig.scraper.outcome.blocks == {}
        assert rig.scraper.stats["pages_skipped"] == 0

    # error None: the HTTPStatusError message of a status that outlasted its retries
    @pytest.mark.parametrize("spec,error", [
        (status(403), "HTTP 403"),
        (status(429), None),
        (status(502), None),
        (TIMEOUT, "timed out"),
        (ok("not json {", "E-BAD"), "invalid json"),
    ])
    async def test_other_failure_keeps_a_good_root_and_blocks(
        self, make_rig: Callable[..., Rig], spec: Spec, error: Optional[str]
    ) -> None:
        rig = make_rig({json_url(FW): [spec]})
        rig.seed_good(FW, ROOT_BODY, "E-ROOT")
        json_entry = dict(rig.hashes[json_url(FW)])
        doc_entry = dict(rig.hashes[doc_url(FW)])
        with capture_logs() as events:
            assert await rig.scraper.scrape_page(doc_url(FW)) is None
        assert rig.mark_error_calls == []
        assert_touched_only(rig.hashes[json_url(FW)], json_entry, rig.session_id)
        assert rig.hashes[doc_url(FW)] == doc_entry
        outcome = rig.scraper.outcome
        assert outcome.root_fetch_failed
        assert outcome.blocks == {"root_fetch_failed": [json_url(FW)]}
        # D8 never applies to the root: nothing is recorded for counting
        assert recorded(rig) == {}
        logged = [e for e in events if e["event"] == "root_fetch_failed"]
        assert [e["error"] for e in logged] == [error or http_status_error(spec["code"], json_url(FW))]
        assert rig.scraper.stats["pages_skipped"] == 0

    @pytest.mark.parametrize("spec", [status(403), status(503), TIMEOUT])
    async def test_failure_of_a_new_root_marks_error_and_blocks(
        self, make_rig: Callable[..., Rig], spec: Spec
    ) -> None:
        rig = make_rig({json_url(FW): [spec]})
        assert await rig.scraper.scrape_page(doc_url(FW)) is None
        assert [url for url, _ in rig.mark_error_calls] == [json_url(FW)]
        assert doc_url(FW) not in rig.hashes
        assert rig.scraper.outcome.blocks == {"root_fetch_failed": [json_url(FW)]}

    async def test_save_failure_is_a_local_error(
        self, make_rig: Callable[..., Rig], monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rig = make_rig({json_url(FW): [ok(page(FW, [ALPHA, "testkit/beta"]), "E-ROOT2")]})
        rig.seed_good(FW, ROOT_BODY, "E-ROOT")
        json_entry = dict(rig.hashes[json_url(FW)])
        doc_entry = dict(rig.hashes[doc_url(FW)])

        def boom(data: Dict[str, Any]) -> str:
            raise ValueError("bad aside")

        monkeypatch.setattr(rig.scraper.markdown_converter, "convert_page", boom)
        assert await rig.scraper.scrape_page(doc_url(FW)) is None
        assert_touched_only(rig.hashes[json_url(FW)], json_entry, rig.session_id)
        assert rig.hashes[doc_url(FW)] == doc_entry
        assert list(rig.scraper._local_errors) == [json_url(FW)]
        assert rig.scraper.outcome.blocks == {}
        assert rig.scraper._root_ok

    async def test_local_error_keeps_a_root_file_no_entry_records(
        self, make_rig: Callable[..., Rig], monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """E.g. a lost hash file: the root's file is on disk, and it fails to convert."""
        rig = make_rig({json_url(FW): [ok(ROOT_BODY, "E-ROOT")]})
        file_path = rig.scraper.output_dir / f"{FW}.md"
        file_path.parent.mkdir(parents=True)
        file_path.write_text("# old\n", encoding="utf-8")

        def boom(*args: Any, **kwargs: Any) -> Any:
            raise ValueError("unsupported block")

        monkeypatch.setattr(rig.scraper, "_extract_from_json", boom)
        assert await rig.scraper.scrape_page(doc_url(FW)) is None
        entry = rig.hashes[json_url(FW)]
        assert entry["file_path"] == str(file_path) and entry["session_id"] == rig.session_id
        assert entry["status"] == "new" and entry["hash"] == "" and "etag" not in entry
        assert doc_url(FW) not in rig.hashes
        assert rig.mark_error_calls == []
        assert list(rig.scraper._local_errors) == [json_url(FW)]

    async def test_scrape_and_save_url_blocks_on_an_unexpected_exception(
        self, make_rig: Callable[..., Rig], monkeypatch: pytest.MonkeyPatch
    ) -> None:
        rig = make_rig({json_url(FW): [ok(ROOT_BODY, "E-ROOT")]})

        async def boom(url: str) -> None:
            raise RuntimeError("bug")

        monkeypatch.setattr(rig.scraper, "scrape_page", boom)
        assert await rig.scraper._scrape_and_save_url(doc_url(FW)) is False
        assert rig.scraper.outcome.blocks == {"exception": [doc_url(FW)]}
