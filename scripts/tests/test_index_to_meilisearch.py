#!/usr/bin/env python3
"""Indexer: every Meilisearch task's outcome is checked, documents are validated before
they are sent, and the live index keeps serving through every run (an update adds before
it deletes, a rebuild is built beside the live index and swapped in).

Each test runs the real indexer (DocumentProcessor included) on a temporary docs dir and
hash file, against FakeClient: an in-memory stand-in for the Meilisearch client that
records every task it enqueues and every task the indexer waits for, and fails the tasks
a test names, as Meilisearch does (wait_for_task returns a failed task without raising).
Its filter deletes, swaps, settings and createdAt behave as verified on v1.49.
"""

import contextlib
import hashlib
import io
import json
import os
import re
import time
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable, Dict, List, Optional, Tuple, cast
from unittest import mock

import pytest
import requests
from meilisearch.errors import (
    MeilisearchApiError,
    MeilisearchCommunicationError,
    MeilisearchTimeoutError,
)
from rich.console import Console

import index_to_meilisearch
from index_to_meilisearch import (
    INDEX_SETTINGS,
    INDEX_STATE_KEY,
    MAX_DOCUMENT_ID_BYTES,
    MAX_FILTER_VALUE_BYTES,
    MAX_FILTER_VALUES,
    PENDING_HASH,
    PROCESSOR_VERSION,
    MeilisearchIndexer,
    TaskFailedError,
    filter_value_bytes,
    find_invalid_document,
    printable_path,
    quote_filter_value,
    settings_to_update,
)

LIVE = "apple-docs"
BUILD = "apple-docs-build"
META = "apple-docs-meta"

# The only filter the indexer deletes by (values double-quoted, \ and " escaped)
DELETE_FILTER = re.compile(r'file_path IN \[(?P<values>.*)\] AND index_gen != (?P<gen>"(?:[^"\\]|\\.)*")', re.S)
QUOTED = re.compile(r'"((?:[^"\\]|\\.)*)"')


def unquote(value: str) -> str:
    return re.sub(r'\\(.)', r'\1', value)


def meili_normalized(value: str) -> str:
    """How Meilisearch compares filter values (trimmed, NFKD, lowercased; v1.49)"""
    return unicodedata.normalize("NFKD", value.strip()).lower()


def api_error(code: str, status: int = 404) -> MeilisearchApiError:
    """The error the client raises for an API error response"""
    response = requests.models.Response()
    response.status_code = status
    response._content = json.dumps({"message": code, "code": code, "type": "invalid_request"}).encode()
    return MeilisearchApiError(code, response)


class FakeTaskError(Exception):
    """Makes the task being applied fail with this error code"""


def default_settings() -> Dict[str, Any]:
    return {
        "filterableAttributes": [],
        "sortableAttributes": [],
        "searchableAttributes": ["*"],
        "faceting": {"maxValuesPerFacet": 100, "sortFacetValuesBy": {"*": "alpha"}},
        "rankingRules": ["words", "typo"],
    }


class FakeIndex:
    def __init__(self, client: "FakeClient", uid: str) -> None:
        self.client = client
        self.uid = uid

    def add_documents(self, documents: List[Dict[str, Any]]) -> SimpleNamespace:
        return self.client.enqueue("documentAdditionOrUpdate", self.uid, [dict(d) for d in documents])

    def update_settings(self, body: Dict[str, Any]) -> SimpleNamespace:
        return self.client.enqueue("settingsUpdate", self.uid, json.loads(json.dumps(body)))

    def delete_documents(self, ids: Any = None, *, filter: Optional[str] = None) -> SimpleNamespace:
        assert ids is None and isinstance(filter, str)
        self.client.filters.append((self.uid, filter))
        return self.client.enqueue("documentDeletion", self.uid, filter)

    def get_settings(self) -> Dict[str, Any]:
        self.client.check_up()
        if self.uid not in self.client.indexes:
            raise api_error("index_not_found")
        settings: Dict[str, Any] = json.loads(json.dumps(self.client.settings[self.uid]))
        settings["sortableAttributes"] = sorted(settings["sortableAttributes"])  # as Meilisearch returns it
        return settings

    def get_stats(self) -> SimpleNamespace:
        self.client.check_up()
        if self.uid not in self.client.indexes:
            raise api_error("index_not_found")
        return SimpleNamespace(number_of_documents=len(self.client.indexes[self.uid]), is_indexing=False)

    def get_document(self, doc_id: str) -> Dict[str, Any]:
        if self.uid not in self.client.indexes:
            raise api_error("index_not_found")
        if self.client.get_document_error is not None:
            raise self.client.get_document_error
        docs = self.client.indexes[self.uid]
        if doc_id not in docs:
            raise api_error("document_not_found")
        return dict(docs[doc_id])

    def get_documents(self, parameters: Dict[str, Any]) -> SimpleNamespace:
        """The documents fetch (POST /documents/fetch), for the only filter the indexer uses"""
        self.client.check_up()
        assert parameters["filter"] == "index_gen NOT EXISTS", parameters
        if "index_gen" not in self.client.settings[self.uid]["filterableAttributes"]:
            raise api_error("invalid_document_filter", 400)
        self.client.older_fetches += 1
        matching = [doc for doc in self.client.indexes[self.uid].values() if "index_gen" not in doc]
        offset, limit = parameters.get("offset", 0), parameters.get("limit", 20)
        page = [{field: doc[field] for field in parameters["fields"] if field in doc}
                for doc in matching[offset:offset + limit]]
        return SimpleNamespace(results=page, total=len(matching), offset=offset, limit=limit)


class FakeClient:
    """
    In-memory Meilisearch client.

    `fail` maps a task type to the 1-based occurrence of that type that fails (or 0 for
    every one), with its status ("failed" or "canceled"); `always_fail` holds (task type,
    index uid) pairs whose every task fails (e.g. no disk for a build index's documents).
    A failed task changes nothing.
    """

    def __init__(self, indexes: Optional[Dict[str, Dict[str, Dict[str, Any]]]] = None,
                 fail: Optional[Dict[str, Tuple[int, str]]] = None) -> None:
        self.indexes: Dict[str, Dict[str, Dict[str, Any]]] = {}
        self.settings: Dict[str, Dict[str, Any]] = {}
        self.created: Dict[str, str] = {}
        self.clock = datetime(2026, 10, 17, 7, 0, tzinfo=timezone.utc)
        for uid, docs in (indexes or {}).items():
            self.make_index(uid)
            self.indexes[uid] = docs
        self.fail = fail or {}
        self.tasks: Dict[int, SimpleNamespace] = {}
        self.enqueued: List[Tuple[str, str]] = []
        self.payloads: List[Any] = []
        self.filters: List[Tuple[str, str]] = []
        self.waited: List[int] = []
        self.counts: Dict[str, int] = {}
        self.get_document_error: Optional[Exception] = None
        self.raw_index_error: Optional[Exception] = None
        self.add_error: Optional[Exception] = None
        self.timeout_types: set = set()
        self.always_fail: set = set()
        # Meilisearch down (restarting): every request fails until `outage` health checks
        # have failed. `crash_on` (a task type and index uid) makes the first such request
        # fail as a crash would, starting an outage of `crash_outage` health checks
        self.outage = 0
        self.crash_on: Optional[Tuple[str, str]] = None
        self.crash_outage = 3
        self.health_checks = 0
        self.older_fetches = 0

    def check_up(self) -> None:
        if self.outage:
            raise MeilisearchCommunicationError("Connection refused")

    def health(self) -> Dict[str, str]:
        self.health_checks += 1
        if self.outage:
            self.outage -= 1
            raise MeilisearchCommunicationError("Connection refused")
        return {"status": "available"}

    def make_index(self, uid: str) -> None:
        self.clock += timedelta(seconds=1)
        self.indexes[uid] = {}
        self.settings[uid] = default_settings()
        # Meilisearch's format: nanoseconds, Z
        self.created[uid] = self.clock.strftime("%Y-%m-%dT%H:%M:%S.%f") + "123Z"

    def enqueue(self, kind: str, uid: str, payload: Any = None) -> SimpleNamespace:
        self.check_up()
        if self.crash_on == (kind, uid):
            self.crash_on = None
            self.outage = self.crash_outage
            raise MeilisearchCommunicationError("Connection reset by peer")
        if kind == "documentAdditionOrUpdate" and self.add_error is not None:
            raise self.add_error
        self.counts[kind] = self.counts.get(kind, 0) + 1
        task_uid = len(self.tasks)
        self.enqueued.append((kind, uid))
        self.payloads.append(payload)
        status, error, details = "succeeded", None, None
        if kind in self.fail:
            nth, fail_status = self.fail[kind]
            if nth in (0, self.counts[kind]):
                status = fail_status
                error = {"code": "forced_failure", "message": f"forced {kind} failure"} if fail_status == "failed" else None
        if (kind, uid) in self.always_fail:
            status, error = "failed", {"code": "forced_failure", "message": f"forced {kind} failure on {uid}"}
        if status == "succeeded":
            try:
                details = self.apply(kind, uid, payload)
            except FakeTaskError as e:
                status, error = "failed", {"code": str(e), "message": str(e)}
        self.tasks[task_uid] = SimpleNamespace(uid=task_uid, status=status, error=error, type=kind,
                                               index_uid=uid, details=details)
        return SimpleNamespace(task_uid=task_uid)

    def apply(self, kind: str, uid: str, payload: Any) -> Optional[Dict[str, Any]]:
        if kind == "indexCreation":
            if uid in self.indexes:
                raise FakeTaskError("index_already_exists")
            self.make_index(uid)
        elif kind == "indexDeletion":
            if uid not in self.indexes:
                raise FakeTaskError("index_not_found")
            del self.indexes[uid], self.settings[uid], self.created[uid]
        elif kind == "documentAdditionOrUpdate":
            if uid not in self.indexes:
                self.make_index(uid)  # Meilisearch creates a missing index on add
            docs = self.indexes[uid]
            for doc in payload:
                docs[doc["id"]] = doc
        elif kind == "settingsUpdate":
            self.settings[uid].update(payload)
        elif kind == "documentDeletion":
            return self.delete_by_filter(uid, payload)
        elif kind == "indexSwap":
            self.swap(payload)
        return None

    def delete_by_filter(self, uid: str, flt: str) -> Dict[str, Any]:
        if "index_gen" not in self.settings[uid]["filterableAttributes"]:
            raise FakeTaskError("invalid_document_filter")
        match = DELETE_FILTER.fullmatch(flt)
        assert match, f"unexpected filter {flt!r}"
        values = {meili_normalized(unquote(v)) for v in QUOTED.findall(match.group("values"))}
        gen = unquote(match.group("gen")[1:-1])
        docs = self.indexes[uid]
        doomed = [doc_id for doc_id, doc in docs.items()
                  if meili_normalized(doc["file_path"]) in values and doc.get("index_gen") != gen]
        for doc_id in doomed:
            del docs[doc_id]
        return {"deletedDocuments": len(doomed), "originalFilter": flt}

    def swap(self, swaps: List[Dict[str, Any]]) -> None:
        for swap in swaps:
            first, second = swap["indexes"]
            tables: List[Dict[str, Any]] = [self.indexes, self.settings, self.created]
            if swap.get("rename"):
                # Renames the first to the second, which must be missing (v1.49)
                if first not in self.indexes:
                    raise FakeTaskError("index_not_found")
                if second in self.indexes:
                    raise FakeTaskError("index_already_exists")
                for table in tables:
                    table[second] = table.pop(first)
            else:
                if first not in self.indexes or second not in self.indexes:
                    raise FakeTaskError("index_not_found")
                for table in tables:
                    table[first], table[second] = table[second], table[first]

    def index(self, uid: str) -> FakeIndex:
        return FakeIndex(self, uid)

    def get_raw_index(self, uid: str) -> Dict[str, Any]:
        self.check_up()
        if self.raw_index_error is not None:
            raise self.raw_index_error
        if uid not in self.indexes:
            raise api_error("index_not_found")
        return {"uid": uid, "primaryKey": "id", "createdAt": self.created[uid]}

    def create_index(self, uid: str, options: Dict[str, Any]) -> SimpleNamespace:
        return self.enqueue("indexCreation", uid)

    def delete_index(self, uid: str) -> SimpleNamespace:
        return self.enqueue("indexDeletion", uid)

    def swap_indexes(self, parameters: List[Dict[str, Any]]) -> SimpleNamespace:
        return self.enqueue("indexSwap", "*", parameters)

    def wait_for_task(self, uid: int, timeout_in_ms: int = 5000, interval_in_ms: int = 50) -> SimpleNamespace:
        self.waited.append(uid)
        task = self.tasks[uid]
        if task.type in self.timeout_types:
            raise MeilisearchTimeoutError("timeout")
        return task

    def kinds(self) -> List[str]:
        return [kind for kind, _ in self.enqueued]

    def docs(self, uid: str = LIVE) -> Dict[str, Dict[str, Any]]:
        return self.indexes.get(uid, {})

    def paths(self, uid: str = LIVE) -> Dict[str, int]:
        """Documents per file_path"""
        counts: Dict[str, int] = {}
        for doc in self.docs(uid).values():
            counts[doc["file_path"]] = counts.get(doc["file_path"], 0) + 1
        return counts

    def reset_log(self) -> int:
        """Forget the enqueued tasks so far; returns the next task uid"""
        self.enqueued.clear()
        self.payloads.clear()
        self.filters.clear()
        self.waited.clear()
        self.counts.clear()
        return len(self.tasks)


@pytest.fixture(autouse=True)
def no_doc_file_count(monkeypatch: pytest.MonkeyPatch) -> None:
    """As a local build: no DOC_FILE_COUNT unless a test sets one"""
    monkeypatch.delenv("DOC_FILE_COUNT", raising=False)


@pytest.fixture(autouse=True)
def no_meilisearch_db(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """As a run outside the image: no Meilisearch database here, so no disk check, unless
    a test gives it one (meili_disk); no real waiting for Meilisearch"""
    monkeypatch.setenv("MEILI_DB_PATH", str(tmp_path / "no-meilisearch-db"))
    monkeypatch.setattr(index_to_meilisearch.time, "sleep", lambda seconds: None)


@pytest.fixture
def docs_root(tmp_path: Path) -> Path:
    root = tmp_path / "documentation"
    for name in ("SwiftUI/view.md", "SwiftUI/text.md", "UIKit/uiview.md"):
        write_doc(root, name)
    return root


@pytest.fixture
def corpus(tmp_path: Path) -> Path:
    """40 docs: enough for an update to change a few without reaching 25%"""
    root = tmp_path / "documentation"
    for n in range(20):
        write_doc(root, f"SwiftUI/item{n}.md")
        write_doc(root, f"UIKit/thing{n}.md")
    return root


def write_doc(root: Path, name: str, body: str = "") -> Path:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {path.stem}\n\n**Framework**: {path.parts[-2]}\n\n{body or 'Some text.'}\n",
                    encoding="utf-8")
    return path


def id_of(name: str) -> str:
    """The id of <docs root>/<name> as one document: the SHA-1 of its file_path"""
    return hashlib.sha1(f"documentation/{name}".encode("utf-8")).hexdigest()


class ClockedIndexer(MeilisearchIndexer):
    """The indexer with the test's clock"""

    clock: Callable[[], datetime]

    def now(self) -> datetime:
        return self.clock()


def make_indexer(docs_root: Path, client: FakeClient, batch_size: int = 10000,
                 now: Optional[datetime] = None) -> MeilisearchIndexer:
    indexer = ClockedIndexer(
        meilisearch_url="http://127.0.0.1:1",
        api_key="test",
        docs_path=str(docs_root),
        batch_size=batch_size,
        hash_file=str(docs_root.parent / "meilisearch_hashes.json"),
    )
    indexer.client = cast(Any, client)
    # By default a start right after the last one: no weekly rebuild due
    indexer.clock = (lambda: now) if now is not None else (lambda: client.clock + timedelta(hours=1))
    return indexer


def run(docs_root: Path, client: FakeClient, **kwargs: Any) -> int:
    """One indexer run; a new indexer each time, as each container start is"""
    batch_size = kwargs.pop("batch_size", 10000)
    now = kwargs.pop("now", None)
    exit_code: int = make_indexer(docs_root, client, batch_size=batch_size, now=now).run(**kwargs)
    return exit_code


def hash_file_data(docs_root: Path) -> Optional[Dict[str, Any]]:
    hash_file = docs_root.parent / "meilisearch_hashes.json"
    return json.loads(hash_file.read_text()) if hash_file.exists() else None


def saved_hashes(docs_root: Path) -> Optional[Dict[str, str]]:
    """The saved file hashes (without the index state)"""
    data = hash_file_data(docs_root)
    if data is None:
        return None
    data.pop(INDEX_STATE_KEY, None)
    return data


def saved_state(docs_root: Path) -> Optional[Dict[str, Any]]:
    data = hash_file_data(docs_root)
    return None if data is None else data.get(INDEX_STATE_KEY)


def hash_file_text(docs_root: Path) -> Optional[str]:
    hash_file = docs_root.parent / "meilisearch_hashes.json"
    return hash_file.read_text() if hash_file.exists() else None


def assert_every_task_waited(client: FakeClient) -> None:
    assert sorted(set(client.waited)) == sorted(client.tasks), (client.waited, client.enqueued)


def gens(client: FakeClient, uid: str = LIVE) -> set:
    return {doc.get("index_gen") for doc in client.docs(uid).values()}


def big_body(sections: int) -> str:
    """Over the 50 KB chunk size: one document per section"""
    return "\n\n".join(f"## Part {n}\n\n" + "word " * 4000 for n in range(sections))

# ---------------------------------------------------------------------------
# Validation before sending
# ---------------------------------------------------------------------------

def doc(doc_id: Any = "swiftui_view", file_path: Any = "documentation/SwiftUI/view.md") -> Dict[str, Any]:
    return {"id": doc_id, "file_path": file_path, "content": "x"}


def test_valid_documents_pass() -> None:
    assert find_invalid_document([doc(), doc("a_chunk_1"), doc("Az09_-")]) is None
    assert find_invalid_document([doc("x" * MAX_DOCUMENT_ID_BYTES)]) is None


@pytest.mark.parametrize("bad_id", ["x" * (MAX_DOCUMENT_ID_BYTES + 1), "a.b", "a b", "a/b", "é", "", None, 12])
def test_invalid_document_ids_are_caught(bad_id: Any) -> None:
    problem = find_invalid_document([doc(), doc(bad_id)])
    assert problem is not None and "document id" in problem


def test_file_path_limit_is_468_bytes() -> None:
    ok = "documentation/" + "a" * (MAX_FILTER_VALUE_BYTES - len("documentation/"))
    assert len(ok.encode()) == 468
    assert find_invalid_document([doc(file_path=ok)]) is None
    problem = find_invalid_document([doc(file_path=ok + "b")])
    assert problem is not None and "469 bytes" in problem


@pytest.mark.parametrize("bad_path", [None, "", 5])
def test_missing_file_path_is_caught(bad_path: Any) -> None:
    assert find_invalid_document([doc(file_path=bad_path)]) == "document has no file_path"


def test_file_path_limit_counts_the_normalized_value() -> None:
    # Meilisearch measures NFKD + lowercase: 'é' is 2 bytes raw, 3 normalized; the 'ﬁ'
    # ligature is 3 bytes raw, 2 normalized ('fi'). Both verified on v1.49.
    stem = "documentation/U/"
    accented = stem + "é" * ((468 - len(stem)) // 3 + 1)
    assert len(accented.encode()) <= 468 < filter_value_bytes(accented)
    assert find_invalid_document([doc(file_path=accented)]) is not None
    ligature = stem + "ﬁ" * ((468 - len(stem)) // 2)
    assert filter_value_bytes(ligature) <= 468 < len(ligature.encode())
    assert find_invalid_document([doc(file_path=ligature)]) is None
    assert filter_value_bytes("documentation/SwiftUI/View.md") == len("documentation/SwiftUI/View.md")


def test_a_file_name_that_is_not_utf8_is_caught() -> None:
    # On Linux a name with invalid bytes reaches Python surrogate-escaped; Meilisearch
    # fails a whole batch on it (lone surrogate in the JSON, verified on v1.49)
    assert find_invalid_document([doc(), doc("zz_a_", "documentation/Zz/a\udcff.md")]) == \
        "file name is not valid UTF-8"
    assert printable_path(Path("Zz/a\udcff.md")) == "Zz/a\\xff.md"
    assert printable_path(Path("SwiftUI/view.md")) == "SwiftUI/view.md"


# ---------------------------------------------------------------------------
# wait_for_task
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("status", ["failed", "canceled"])
def test_a_task_that_did_not_succeed_raises(docs_root: Path, status: str) -> None:
    client = FakeClient(fail={"documentAdditionOrUpdate": (1, status)})
    indexer = make_indexer(docs_root, client)
    with pytest.raises(TaskFailedError, match=status):
        indexer.wait_for_task(client.index(LIVE).add_documents([doc()]), "add")


def test_a_timeout_raises_task_failed(docs_root: Path) -> None:
    client = FakeClient()
    client.timeout_types = {"documentAdditionOrUpdate"}
    indexer = make_indexer(docs_root, client)
    with pytest.raises(TaskFailedError, match="didn't finish"):
        indexer.wait_for_task(client.index(LIVE).add_documents([doc()]), "add")


# ---------------------------------------------------------------------------
# Fresh volume, rebuild by swap, ordinary starts: every task checked
# ---------------------------------------------------------------------------

def test_fresh_volume_builds_beside_and_renames(docs_root: Path) -> None:
    client = FakeClient()
    assert run(docs_root, client) == 0
    assert client.enqueued == [
        ("indexCreation", BUILD), ("settingsUpdate", BUILD), ("documentAdditionOrUpdate", BUILD),
        ("indexSwap", "*"), ("indexCreation", META), ("documentAdditionOrUpdate", META),
    ]
    # rename: the build's name first, the missing live index second (v1.49)
    assert client.payloads[3] == [{"indexes": [BUILD, LIVE], "rename": True}]
    assert client.payloads[1] == INDEX_SETTINGS
    assert_every_task_waited(client)
    assert BUILD not in client.indexes
    assert len(client.docs()) == 3 and gens(client) == {client.docs()[id_of("SwiftUI/view.md")]["index_gen"]}
    assert set(saved_hashes(docs_root) or {}) == {"SwiftUI/view.md", "SwiftUI/text.md", "UIKit/uiview.md"}
    assert saved_state(docs_root) == {"processor_version": PROCESSOR_VERSION, "created_at": client.created[LIVE]}
    meta = client.docs(META)["index_metadata"]
    assert meta["documents_indexed"] == 3 and meta["last_index_full"] is not None


def test_the_hash_file_stays_a_flat_map_older_indexers_can_read(docs_root: Path) -> None:
    # An older image started on this volume (a rollback) reads every key as a file path:
    # all values but the state are hashes, and the state key is no .md path
    client = FakeClient()
    run(docs_root, client)
    data = hash_file_data(docs_root) or {}
    assert not INDEX_STATE_KEY.endswith(".md")
    assert all(isinstance(value, str) for key, value in data.items() if key != INDEX_STATE_KEY)


def test_a_start_over_an_unchanged_index_queues_no_task_on_it(docs_root: Path) -> None:
    # No settings task, no add, no delete: /health stays 200 through an ordinary restart
    client = FakeClient()
    run(docs_root, client)
    before = hash_file_text(docs_root)
    client.reset_log()
    assert run(docs_root, client) == 0
    assert client.enqueued == [("documentAdditionOrUpdate", META)]
    assert hash_file_text(docs_root) == before


def test_incremental_run_waits_for_every_batch(corpus: Path) -> None:
    client = FakeClient()
    assert run(corpus, client) == 0
    for name in ("SwiftUI/item1.md", "SwiftUI/item2.md", "UIKit/thing3.md"):
        write_doc(corpus, name, "Changed text.")
    write_doc(corpus, "UIKit/uibutton.md")
    first_new_task = client.reset_log()

    assert run(corpus, client, batch_size=2) == 0
    # existing indexes: no creation, no settings; 4 files in batches of 2: 2 add tasks,
    # then one delete of their old documents, then the meta write
    assert client.kinds() == ["documentAdditionOrUpdate"] * 2 + ["documentDeletion", "documentAdditionOrUpdate"]
    assert sorted(client.waited) == list(range(first_new_task, len(client.tasks)))
    assert len(saved_hashes(corpus) or {}) == 41


@pytest.mark.parametrize("failing", [
    ("indexCreation", 1),              # the build index
    ("settingsUpdate", 1),
    ("documentAdditionOrUpdate", 1),   # the first batch
    ("documentAdditionOrUpdate", 2),   # a later batch
    ("indexSwap", 1),                  # the rename
    ("indexCreation", 2),              # the meta index
    ("documentAdditionOrUpdate", 3),   # the meta write
])
def test_a_failed_task_aborts_without_saving_hashes(docs_root: Path, failing: Tuple[str, int]) -> None:
    kind, nth = failing
    client = FakeClient(fail={kind: (nth, "failed")})
    # batch size 2: the 3 files make 2 add tasks, then the meta write is the 3rd
    assert run(docs_root, client, batch_size=2) == 1
    assert saved_hashes(docs_root) is None
    assert_every_task_waited(client)
    # nothing is enqueued after the failed task but the unfinished build's deletion
    failed = next(uid for uid, task in client.tasks.items() if task.status != "succeeded")
    assert client.enqueued[failed + 1:] in ([], [("indexDeletion", BUILD)])
    assert BUILD not in client.indexes


def test_a_failed_add_in_incremental_mode_saves_no_new_hash(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    before = saved_hashes(corpus)
    write_doc(corpus, "SwiftUI/item0.md", "Changed text.")
    client.fail = {"documentAdditionOrUpdate": (0, "failed")}

    assert run(corpus, client) == 1
    # the file it was sending stays pending, so the next run sends it again
    assert saved_hashes(corpus) == {**(before or {}), "SwiftUI/item0.md": PENDING_HASH}
    # no delete and no meta write: last_indexed doesn't move on a failed run
    assert client.enqueued[-1] == ("documentAdditionOrUpdate", LIVE)


def test_a_canceled_task_aborts_like_a_failed_one(docs_root: Path) -> None:
    client = FakeClient(fail={"documentAdditionOrUpdate": (1, "canceled")})
    assert run(docs_root, client) == 1
    assert saved_hashes(docs_root) is None


def test_force_rebuilds_by_swap(docs_root: Path) -> None:
    client = FakeClient(indexes={LIVE: {"old": {"id": "old", "file_path": "documentation/Old/old.md"}}})
    old_created = client.created[LIVE]
    assert run(docs_root, client, force=True) == 0
    assert client.enqueued == [
        ("indexCreation", BUILD), ("settingsUpdate", BUILD), ("documentAdditionOrUpdate", BUILD),
        ("indexSwap", "*"), ("indexDeletion", BUILD),
        ("indexCreation", META), ("documentAdditionOrUpdate", META),
    ]
    assert client.payloads[3] == [{"indexes": [LIVE, BUILD]}]
    assert "old" not in client.docs() and len(client.docs()) == 3
    assert BUILD not in client.indexes
    assert client.created[LIVE] != old_created
    assert saved_state(docs_root) == {"processor_version": PROCESSOR_VERSION, "created_at": client.created[LIVE]}
    assert_every_task_waited(client)
    assert client.docs(META)["index_metadata"]["last_index_full"] is not None


def test_a_leftover_build_index_is_deleted_first(docs_root: Path) -> None:
    client = FakeClient()
    run(docs_root, client)
    client.make_index(BUILD)
    client.indexes[BUILD]["half"] = {"id": "half", "file_path": "documentation/X/half.md"}
    client.reset_log()
    assert run(docs_root, client, force=True) == 0
    assert client.enqueued[:2] == [("indexDeletion", BUILD), ("indexCreation", BUILD)]
    assert "half" not in client.docs()


def test_a_failed_leftover_deletion_aborts_with_the_live_index_untouched(docs_root: Path) -> None:
    client = FakeClient()
    run(docs_root, client)
    live_before = json.dumps(client.docs(), sort_keys=True)
    client.make_index(BUILD)
    client.fail = {"indexDeletion": (1, "failed")}
    assert run(docs_root, client, force=True) == 1
    assert json.dumps(client.docs(), sort_keys=True) == live_before


def test_force_rebuild_on_a_fresh_volume_queues_no_failing_deletion(docs_root: Path) -> None:
    client = FakeClient()
    assert run(docs_root, client, force=True) == 0
    assert "indexDeletion" not in client.kinds()
    assert all(task.status == "succeeded" for task in client.tasks.values())


def test_existing_meta_index_is_not_created_again(docs_root: Path) -> None:
    client = FakeClient()
    run(docs_root, client, force=True)
    full = client.docs(META)["index_metadata"]["last_index_full"]
    client.reset_log()
    assert run(docs_root, client) == 0
    assert ("indexCreation", META) not in client.enqueued
    assert all(task.status == "succeeded" for task in client.tasks.values())
    # an incremental run keeps the full rebuild's timestamp
    assert client.docs(META)["index_metadata"]["last_index_full"] == full


def test_meta_read_error_other_than_not_found_aborts(docs_root: Path) -> None:
    client = FakeClient()
    client.get_document_error = api_error("internal", status=500)
    assert run(docs_root, client) == 1
    assert saved_hashes(docs_root) is None


@pytest.mark.parametrize("error", [
    MeilisearchCommunicationError("connection refused"),
    api_error("payload_too_large", status=413),
])
def test_an_add_request_error_aborts(docs_root: Path, error: Exception) -> None:
    client = FakeClient()
    client.add_error = error
    assert run(docs_root, client) == 1
    assert saved_hashes(docs_root) is None


def test_the_abort_cause_is_printed_last_and_verbatim(docs_root: Path, capsys: pytest.CaptureFixture[str]) -> None:
    # Last, after the summary table, where a reader (or a log tail) looks first. Shown as
    # is: an error text that looks like rich markup must neither vanish nor crash the run
    client = FakeClient()
    client.add_error = MeilisearchCommunicationError("bad [/x] [bold]y")
    assert run(docs_root, client) == 1
    out = capsys.readouterr().out
    assert out.index("Indexing Summary") < out.index("Indexing aborted")
    assert "Indexing aborted: MeilisearchCommunicationError, bad [/x] [bold]y" in out
    assert out.rstrip().splitlines()[-1].strip().startswith("No hashes saved")


def test_an_index_lookup_error_aborts(docs_root: Path) -> None:
    client = FakeClient()
    client.raw_index_error = api_error("invalid_api_key", status=403)
    assert run(docs_root, client) == 1
    assert client.enqueued == []


def test_a_failed_hash_save_exits_1_and_keeps_the_old_file(docs_root: Path) -> None:
    client = FakeClient()
    run(docs_root, client)
    before = hash_file_text(docs_root)
    live_before = json.dumps(client.docs(), sort_keys=True)
    write_doc(docs_root, "UIKit/uibutton.md")
    client.reset_log()
    with mock.patch("os.replace", side_effect=OSError(28, "No space left on device")):
        assert run(docs_root, client) == 1
    assert hash_file_text(docs_root) == before
    assert [p.name for p in docs_root.parent.iterdir() if p.suffix == ".tmp"] == []
    # the save before the first add failed: nothing was sent
    assert client.enqueued == [] and json.dumps(client.docs(), sort_keys=True) == live_before


# ---------------------------------------------------------------------------
# Rebuild by swap: the live index serves until the swap
# ---------------------------------------------------------------------------

def test_a_build_with_too_few_documents_is_not_swapped_in(corpus: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DOC_FILE_COUNT", "40")  # a complete image: only the 90%-of-files gate applies
    client = FakeClient()
    run(corpus, client)
    live_before = json.dumps(client.docs(), sort_keys=True)
    hashes_before = hash_file_text(corpus)
    real_process: Callable[..., List[Dict[str, Any]]] = index_to_meilisearch.DocumentProcessor.process_document

    def process(self: Any, file_path: str) -> List[Dict[str, Any]]:
        if "/UIKit/" in file_path:  # half the files fail
            raise ValueError("converter bug")
        return real_process(self, file_path)

    client.reset_log()
    with mock.patch.object(index_to_meilisearch.DocumentProcessor, "process_document", process):
        assert run(corpus, client, force=True) == 1
    assert "indexSwap" not in client.kinds()
    assert json.dumps(client.docs(), sort_keys=True) == live_before
    assert BUILD not in client.indexes          # its disk freed at once
    assert hash_file_text(corpus) == hashes_before


def test_without_doc_file_count_a_build_far_smaller_than_the_live_index_is_not_swapped_in(corpus: Path) -> None:
    # The old 0.9 x live-count rule, kept for local builds only: 40 files pass the
    # up-front check against 44 live documents, and 37 built documents pass the 90%-of-
    # files gate, but 37 is under 90% of 44
    client = FakeClient()
    run(corpus, client)
    for n in range(4):
        client.indexes[LIVE][f"extra{n}"] = {"id": f"extra{n}", "file_path": f"documentation/Old/x{n}.md"}
    live_before = json.dumps(client.docs(), sort_keys=True)
    real_process: Callable[..., List[Dict[str, Any]]] = index_to_meilisearch.DocumentProcessor.process_document

    def process(self: Any, file_path: str) -> List[Dict[str, Any]]:
        if file_path.endswith(("/thing0.md", "/thing1.md", "/thing2.md")):
            raise ValueError("converter bug")
        return real_process(self, file_path)

    client.reset_log()
    with mock.patch.object(index_to_meilisearch.DocumentProcessor, "process_document", process):
        assert run(corpus, client, force=True) == 1
    assert "indexSwap" not in client.kinds() and BUILD not in client.indexes
    assert json.dumps(client.docs(), sort_keys=True) == live_before


@pytest.mark.parametrize("failing", [
    ("indexDeletion", 1),               # a leftover build index
    ("indexCreation", 1),
    ("settingsUpdate", 1),
    ("documentAdditionOrUpdate", 1),
    ("indexSwap", 1),
])
def test_a_failed_rebuild_leaves_the_live_index_serving(corpus: Path, failing: Tuple[str, int]) -> None:
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", "Changed text.")
    if failing[0] == "indexDeletion":
        client.make_index(BUILD)
    live_before = json.dumps(client.docs(), sort_keys=True)
    created_before = client.created[LIVE]
    hashes_before = hash_file_text(corpus)
    client.reset_log()
    client.fail = {failing[0]: (failing[1], "failed")}

    assert run(corpus, client, force=True) == 1
    assert json.dumps(client.docs(), sort_keys=True) == live_before
    assert client.created[LIVE] == created_before
    assert hash_file_text(corpus) == hashes_before
    # --force asked for a rebuild only: no update follows it
    assert "documentDeletion" not in client.kinds() and ("documentAdditionOrUpdate", LIVE) not in client.enqueued


def test_a_failure_after_the_swap_rebuilds_again_on_the_next_start(corpus: Path) -> None:
    # The old index's deletion fails after the swap of a due rebuild: the new index
    # serves, the hashes aren't saved, so the next start finds a hash file of another
    # index and rebuilds. No update follows the failure: the hash file doesn't describe
    # the new index
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", "Changed text.")
    client.reset_log()
    client.fail = {"indexDeletion": (1, "failed")}
    assert run(corpus, client, now=client.clock + timedelta(days=7)) == 1
    assert saved_state(corpus)["created_at"] != client.created[LIVE]  # type: ignore[index]
    assert ("documentAdditionOrUpdate", LIVE) not in client.enqueued and "documentDeletion" not in client.kinds()
    client.fail = {}
    client.reset_log()
    assert run(corpus, client) == 0
    assert "indexSwap" in client.kinds()
    assert saved_state(corpus)["created_at"] == client.created[LIVE]  # type: ignore[index]


def test_settings_go_only_to_the_build_index_in_a_rebuild(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    client.reset_log()
    assert run(corpus, client, force=True) == 0
    assert [uid for kind, uid in client.enqueued if kind == "settingsUpdate"] == [BUILD]


# ---------------------------------------------------------------------------
# When to rebuild (D10): processor version, createdAt, weekly, >25% changed
# ---------------------------------------------------------------------------

def rebuilt(client: FakeClient) -> bool:
    return ("indexSwap", "*") in client.enqueued


def test_a_hash_file_without_processor_version_rebuilds_by_swap(corpus: Path) -> None:
    # An older indexer's hash file: a flat map with no state
    client = FakeClient()
    run(corpus, client)
    hash_file = corpus.parent / "meilisearch_hashes.json"
    hash_file.write_text(json.dumps(saved_hashes(corpus)))
    client.reset_log()
    assert run(corpus, client) == 0
    assert rebuilt(client) and client.payloads[client.kinds().index("indexSwap")] == [{"indexes": [LIVE, BUILD]}]
    assert saved_state(corpus) == {"processor_version": PROCESSOR_VERSION, "created_at": client.created[LIVE]}


def test_another_processor_version_rebuilds(corpus: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    client = FakeClient()
    run(corpus, client)
    monkeypatch.setattr(index_to_meilisearch, "PROCESSOR_VERSION", PROCESSOR_VERSION + 1)
    client.reset_log()
    assert run(corpus, client) == 0
    assert rebuilt(client)
    assert saved_state(corpus)["processor_version"] == PROCESSOR_VERSION + 1  # type: ignore[index]
    client.reset_log()
    assert run(corpus, client) == 0 and not rebuilt(client)


def test_a_hash_file_of_another_index_rebuilds(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    client.created[LIVE] = "2026-10-17T08:00:00.5Z"  # e.g. a volume replaced by another
    client.reset_log()
    assert run(corpus, client) == 0
    assert rebuilt(client)


@pytest.mark.parametrize("tz", ["UTC", "America/New_York", "Pacific/Kiritimati"])
def test_weekly_rebuild_after_six_and_a_half_days_in_utc(corpus: Path, monkeypatch: pytest.MonkeyPatch, tz: str) -> None:
    # Counted in UTC from the live index's createdAt: the local timezone (the image runs
    # with TZ=America/New_York) and DST don't move it, and 6.5 days isn't floored
    monkeypatch.setenv("TZ", tz)
    time.tzset()
    try:
        client = FakeClient()
        run(corpus, client)
        built = datetime.strptime(client.created[LIVE][:26], "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=timezone.utc)
        client.reset_log()
        assert run(corpus, client, now=built + timedelta(days=6.5) - timedelta(seconds=1)) == 0
        assert not rebuilt(client)
        client.reset_log()
        assert run(corpus, client, now=built + timedelta(days=6.5)) == 0
        assert rebuilt(client)
    finally:
        monkeypatch.delenv("TZ")
        time.tzset()


def test_the_rebuild_age_comes_from_an_aware_utc_clock(corpus: Path) -> None:
    indexer = make_indexer(corpus, FakeClient())
    assert MeilisearchIndexer.now(indexer).utcoffset() == timedelta(0)  # the real clock
    assert index_to_meilisearch.parse_meilisearch_time("2026-10-17T04:34:32.123456789Z") == \
        datetime(2026, 10, 17, 4, 34, 32, 123456, tzinfo=timezone.utc)


@pytest.mark.parametrize("changed,expect_rebuild", [(10, False), (11, True)])
def test_more_than_a_quarter_of_the_files_changed_rebuilds(corpus: Path, changed: int, expect_rebuild: bool) -> None:
    client = FakeClient()
    run(corpus, client)
    for n in range(changed):  # of 40 files: 10 is 25%, 11 is more
        write_doc(corpus, f"SwiftUI/item{n}.md", "Changed text.")
    client.reset_log()
    assert run(corpus, client) == 0
    assert rebuilt(client) is expect_rebuild


def test_removed_files_count_as_changed(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    for n in range(8):
        write_doc(corpus, f"SwiftUI/item{n}.md", "Changed text.")
    for n in range(3):
        (corpus / "UIKit" / f"thing{n}.md").unlink()
    client.reset_log()
    assert run(corpus, client) == 0  # 8 + 3 of 37 files
    assert rebuilt(client)


def test_new_files_under_a_quarter_are_added_in_place(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    for n in range(10):  # +25%
        write_doc(corpus, f"Zz/new{n}.md")
    client.reset_log()
    assert run(corpus, client) == 0
    assert not rebuilt(client) and len(client.docs()) == 50


def normalized_output(capsys: pytest.CaptureFixture[str]) -> str:
    """The captured output with the console's line wrapping undone"""
    return " ".join(capsys.readouterr().out.split())


# ---------------------------------------------------------------------------
# An older indexer ran on the live index (a rollback): rebuilt by swap
# ---------------------------------------------------------------------------

def run_older_indexer(docs_root: Path, client: FakeClient, changed: List[str]) -> None:
    """
    What a start of an older indexer (before add-then-sweep: merge A's, on a rollback)
    does to the live index and the hash file: it resets the filterable attributes without
    index_gen, adds the changed files' documents (with no index_gen) and deletes nothing,
    and saves {**stored, **new}, which keeps the state key as it was. createdAt stays.
    """
    client.settings[LIVE]["filterableAttributes"] = [
        "framework", "platforms", "kind", "is_framework_main", "file_path", "api_name", "is_chunk"]
    hash_file = docs_root.parent / "meilisearch_hashes.json"
    data = json.loads(hash_file.read_text())
    for name in changed:
        for document in index_to_meilisearch.DocumentProcessor().process_document(str(docs_root / name)):
            # its ids were made from the path (e.g. swiftui_big_chunk_1), not sha1s
            document["id"] = "legacy_" + re.sub(r"\W", "_", name) + f"_{document.get('chunk_index', 0)}"
            client.indexes[LIVE][document["id"]] = document
        data[name] = index_to_meilisearch.compute_file_hash(docs_root / name)
    hash_file.write_text(json.dumps(data, indent=2))


def test_a_rollback_to_an_older_indexer_is_rebuilt_by_swap(corpus: Path, capsys: pytest.CaptureFixture[str]) -> None:
    # Merge B's rollback rehearsal: the older image indexed a file that shrank (3 chunks to
    # 1 document) and kept its old chunks. Its hash and the state say the file is indexed,
    # so an update would keep them: the next start rebuilds by swap instead
    write_doc(corpus, "SwiftUI/big.md", big_body(3))
    client = FakeClient()
    run(corpus, client)
    state = saved_state(corpus)
    assert state is not None
    write_doc(corpus, "SwiftUI/big.md", "Now small.")
    run_older_indexer(corpus, client, ["SwiftUI/big.md"])
    assert client.paths()["documentation/SwiftUI/big.md"] == 4
    assert saved_state(corpus) == state and client.created[LIVE] == state["created_at"]

    client.reset_log()
    capsys.readouterr()
    assert run(corpus, client) == 0
    assert "Mode: Rebuild by swap (an older indexer has run on the live index" in normalized_output(capsys)
    assert rebuilt(client) and client.paths()["documentation/SwiftUI/big.md"] == 1
    assert len(gens(client)) == 1
    assert client.settings[LIVE]["filterableAttributes"] == INDEX_SETTINGS["filterableAttributes"]
    assert saved_state(corpus) == {"processor_version": PROCESSOR_VERSION, "created_at": client.created[LIVE]}
    client.reset_log()
    assert run(corpus, client) == 0 and client.enqueued == [("documentAdditionOrUpdate", META)]


def test_a_rollback_rebuild_that_fails_updates_in_place_and_stays_due(corpus: Path) -> None:
    write_doc(corpus, "SwiftUI/big.md", big_body(3))
    client = FakeClient()
    run(corpus, client)
    created = client.created[LIVE]
    write_doc(corpus, "SwiftUI/big.md", "Now small.")
    run_older_indexer(corpus, client, ["SwiftUI/big.md"])
    write_doc(corpus, "SwiftUI/item1.md", "Scraped since.")     # in this image
    (corpus / "UIKit" / "thing0.md").unlink()
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}  # e.g. no disk for a second index

    assert run(corpus, client) == 1
    # the update after the failed rebuild: the change and the removal reach search
    assert "Scraped since" in client.docs()[id_of("SwiftUI/item1.md")]["content"]
    assert "documentation/UIKit/thing0.md" not in client.paths()
    assert client.created[LIVE] == created and BUILD not in client.indexes
    # the file the older indexer re-indexed is indexed again: its stale chunks and the
    # older indexer's document are both swept
    assert client.paths()["documentation/SwiftUI/big.md"] == 1
    assert "Now small" in client.docs()[id_of("SwiftUI/big.md")]["content"]
    assert all("index_gen" in doc for doc in client.docs().values())
    state = saved_state(corpus) or {}
    assert state["created_at"] == created and state["rebuild_due"].startswith("an older indexer has run")

    # still due, though the update made index_gen filterable again
    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client) == 0
    assert rebuilt(client) and client.paths()["documentation/SwiftUI/big.md"] == 1
    assert saved_state(corpus) == {"processor_version": PROCESSOR_VERSION, "created_at": client.created[LIVE]}


def test_a_failed_rollback_rebuild_stays_due_with_nothing_to_update(corpus: Path) -> None:
    # The update re-applies index_gen, which hides the older indexer's run: the hash file
    # is saved anyway, recording the rebuild as due
    write_doc(corpus, "SwiftUI/big.md", big_body(3))
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/big.md", "Now small.")
    run_older_indexer(corpus, client, ["SwiftUI/big.md"])
    client.always_fail = {("indexCreation", BUILD)}
    assert run(corpus, client) == 1
    assert "index_gen" in client.settings[LIVE]["filterableAttributes"]
    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client) == 0
    assert rebuilt(client) and client.paths()["documentation/SwiftUI/big.md"] == 1


def test_a_failed_rollback_rebuild_reindexes_every_file_the_older_indexer_touched(
        corpus: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    # While rolled back, the older indexer re-indexed changed files (same chunk count, and
    # fewer) and a new file that was removed again before the return (its key dropped from
    # the hash file). On the return the rebuild fails: the update indexes those files again
    # and deletes the older indexer's documents, so search and expand_result (the newest
    # index_gen of a file) serve the files as they are
    write_doc(corpus, "SwiftUI/big.md", big_body(5))
    client = FakeClient()
    run(corpus, client)
    stale = client.paths()["documentation/SwiftUI/big.md"]
    write_doc(corpus, "SwiftUI/item2.md", "Changed while rolled back.")
    write_doc(corpus, "SwiftUI/big.md", big_body(3))
    now = len(index_to_meilisearch.DocumentProcessor().process_document(str(corpus / "SwiftUI/big.md")))
    assert 1 < now < stale
    write_doc(corpus, "Zz/brief.md", "Added and removed while rolled back.")
    run_older_indexer(corpus, client, ["SwiftUI/item2.md", "SwiftUI/big.md", "Zz/brief.md"])
    (corpus / "Zz" / "brief.md").unlink()
    monkeypatch.setenv("DOC_FILE_COUNT", "41")  # as docker-build sets it (the documents outnumber the files)
    data = hash_file_data(corpus) or {}
    del data["Zz/brief.md"]
    (corpus.parent / "meilisearch_hashes.json").write_text(json.dumps(data))
    assert client.paths()["documentation/SwiftUI/big.md"] == stale + now
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}
    client.reset_log()
    capsys.readouterr()

    assert run(corpus, client) == 1
    out = normalized_output(capsys)
    assert ("Also re-indexing 2 file(s), and deleting the documents of 1 file(s) no longer here, "
            "that an older indexer added documents for (a rollback)") in out
    assert all("index_gen" in doc for doc in client.docs().values())
    assert len(gens(client)) == 2           # the first build's, and this run's on the files it sent
    assert client.paths()["documentation/SwiftUI/big.md"] == now
    assert "documentation/Zz/brief.md" not in client.paths()
    assert "Changed while rolled back" in client.docs()[id_of("SwiftUI/item2.md")]["content"]
    assert not any(doc_id.startswith("legacy_") for doc_id in client.docs())
    hashes = saved_hashes(corpus) or {}
    assert PENDING_HASH not in hashes.values() and len(hashes) == 41
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("an older indexer has run")
    # the next update finds nothing more to do
    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client) == 0 and rebuilt(client)


def test_an_older_indexers_own_index_is_not_reindexed_file_by_file(corpus: Path) -> None:
    # Merge B's first deploy over merge A's index: no document has index_gen and the hash
    # file records no processor version. When the rebuild fails, the update sends only the
    # changed files (merge A's hashes describe its index)
    client = FakeClient()
    run(corpus, client)
    for document in client.docs().values():
        del document["index_gen"]
    client.settings[LIVE]["filterableAttributes"] = [
        "framework", "platforms", "kind", "is_framework_main", "file_path", "api_name", "is_chunk"]
    (corpus.parent / "meilisearch_hashes.json").write_text(json.dumps(saved_hashes(corpus)))
    write_doc(corpus, "SwiftUI/item0.md", "Scraped change.")
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}
    client.reset_log()
    indexer = make_indexer(corpus, client)
    assert indexer.run() == 1
    assert client.older_fetches == 0 and indexer.stats["processed"] == 1
    assert sum("index_gen" in doc for doc in client.docs().values()) == 1


def test_a_start_over_an_index_this_indexer_built_finds_no_older_documents(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    client.reset_log()
    indexer = make_indexer(corpus, client)
    assert indexer.run() == 0
    assert client.older_fetches == 1 and indexer.stats["processed"] == 0
    assert client.enqueued == [("documentAdditionOrUpdate", META)]


def test_older_documents_are_listed_past_one_fetch(corpus: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    write_doc(corpus, "SwiftUI/big.md", big_body(3))
    client = FakeClient()
    run(corpus, client)
    changed = [f"SwiftUI/item{n}.md" for n in range(5)]
    for name in changed:
        write_doc(corpus, name, "Changed while rolled back.")
    run_older_indexer(corpus, client, changed)
    monkeypatch.setattr(index_to_meilisearch, "UNSTAMPED_FETCH_LIMIT", 2)
    monkeypatch.setenv("DOC_FILE_COUNT", "41")
    client.always_fail = {("indexCreation", BUILD)}
    indexer = make_indexer(corpus, client)
    assert indexer.run() == 1
    assert client.older_fetches == 3 and indexer.stats["processed"] == 5
    assert all("index_gen" in doc for doc in client.docs().values())


# ---------------------------------------------------------------------------
# A due rebuild that fails before its swap: the update is applied instead
# ---------------------------------------------------------------------------

def test_a_due_rebuild_that_keeps_failing_still_updates_the_live_index(
        corpus: Path, capsys: pytest.CaptureFixture[str]) -> None:
    # Every start retries the rebuild and then applies the update, so new and changed docs
    # and Apple's removals keep reaching search while the rebuild can't be done
    client = FakeClient()
    run(corpus, client)
    created = client.created[LIVE]
    week = client.clock + timedelta(days=7)
    write_doc(corpus, "SwiftUI/item0.md", "Scraped change.")
    write_doc(corpus, "SwiftUI/brandnew.md")
    (corpus / "UIKit" / "thing0.md").unlink()
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}  # e.g. no disk for a second index

    for day in range(3):
        client.reset_log()
        capsys.readouterr()
        indexer = make_indexer(corpus, client, now=week + timedelta(days=day))
        assert indexer.run() == 1
        out = normalized_output(capsys)
        assert "Mode: Rebuild by swap (" in out and "weekly rebuild" in out
        assert ("indexCreation", BUILD) in client.enqueued and BUILD not in client.indexes
        assert "Scraped change" in client.docs()[id_of("SwiftUI/item0.md")]["content"]
        assert id_of("SwiftUI/brandnew.md") in client.docs() and "documentation/UIKit/thing0.md" not in client.paths()
        assert client.created[LIVE] == created
        assert (saved_state(corpus) or {})["rebuild_due"].startswith("weekly rebuild")
        if day == 0:
            # the update's counts, not the abandoned build's; the cause comes last
            assert indexer.stats["processed"] == 2 and indexer.stats["removed"] == 1
            assert out.index("Indexing Summary") < out.index("✗ Rebuild failed: add 40 documents: task")
            assert out.endswith("The live index was updated in place instead; the next run retries the rebuild")

    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client, now=week + timedelta(days=3)) == 0
    assert rebuilt(client) and client.created[LIVE] != created and len(client.docs()) == 40
    assert saved_state(corpus) == {"processor_version": PROCESSOR_VERSION, "created_at": client.created[LIVE]}


@pytest.mark.parametrize("recorded", [None, PROCESSOR_VERSION - 1])
def test_a_failed_rebuild_for_another_processor_version_keeps_that_version(corpus: Path, recorded: Optional[int]) -> None:
    # The update leaves the unchanged files' documents at the recorded version (none: an
    # older indexer's flat hash file, merge B's first deploy), so the state keeps it
    client = FakeClient()
    run(corpus, client)
    data = hash_file_data(corpus) or {}
    if recorded is None:
        del data[INDEX_STATE_KEY]
    else:
        data[INDEX_STATE_KEY]["processor_version"] = recorded
    (corpus.parent / "meilisearch_hashes.json").write_text(json.dumps(data))
    write_doc(corpus, "SwiftUI/item0.md", "Scraped change.")
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}

    assert run(corpus, client) == 1
    assert "Scraped change" in client.docs()[id_of("SwiftUI/item0.md")]["content"]
    state = saved_state(corpus) or {}
    assert state["processor_version"] == recorded and state["created_at"] == client.created[LIVE]
    assert state["rebuild_due"]
    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client) == 0 and rebuilt(client)
    assert saved_state(corpus) == {"processor_version": PROCESSOR_VERSION, "created_at": client.created[LIVE]}


def test_a_failed_rebuild_for_a_hash_file_of_another_index_stays_due(corpus: Path) -> None:
    # The update never deletes a current file's documents, so it is safe even on a hash
    # file that may not describe the live index; the rebuild stays due until it succeeds
    client = FakeClient()
    run(corpus, client)
    client.created[LIVE] = "2026-10-17T08:00:00.5Z"
    (corpus / "UIKit" / "thing0.md").unlink()
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}
    assert run(corpus, client) == 1
    assert "documentation/UIKit/thing0.md" not in client.paths() and len(client.docs()) == 39
    state = saved_state(corpus) or {}
    assert state["created_at"] == client.created[LIVE]
    assert state["rebuild_due"].startswith("the hash file belongs to another index")
    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client) == 0 and rebuilt(client)


def test_a_failed_rebuild_for_many_changes_applies_them_in_place(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    for n in range(11):
        write_doc(corpus, f"SwiftUI/item{n}.md", "Changed text.")
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}
    assert run(corpus, client) == 1
    assert all("Changed text" in client.docs()[id_of(f"SwiftUI/item{n}.md")]["content"] for n in range(11))
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("11 of 40 files changed")
    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client) == 0 and rebuilt(client)


def test_a_failed_update_after_a_failed_rebuild_keeps_the_hashes(corpus: Path, capsys: pytest.CaptureFixture[str]) -> None:
    client = FakeClient()
    run(corpus, client)
    before = saved_hashes(corpus)
    write_doc(corpus, "SwiftUI/item0.md", "Changed text.")
    client.always_fail = {("documentAdditionOrUpdate", BUILD), ("documentAdditionOrUpdate", LIVE)}
    capsys.readouterr()
    assert run(corpus, client, now=client.clock + timedelta(days=7)) == 1
    assert saved_hashes(corpus) == {**(before or {}), "SwiftUI/item0.md": PENDING_HASH}
    out = normalized_output(capsys)
    assert "Rebuild failed before its swap" in out
    assert out.endswith("No hashes saved: the next run indexes these files again")


def test_a_rollback_rebuild_stays_due_when_the_update_after_it_stops(corpus: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # The update made index_gen filterable again, then a delete failed: the rebuild was
    # recorded as due before the update changed anything
    write_doc(corpus, "SwiftUI/big.md", big_body(3))
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/big.md", "Now small.")
    run_older_indexer(corpus, client, ["SwiftUI/big.md"])
    (corpus / "UIKit" / "thing0.md").unlink()
    monkeypatch.setenv("DOC_FILE_COUNT", "40")  # as docker-build sets it (the documents outnumber the files)
    client.always_fail = {("documentAdditionOrUpdate", BUILD), ("documentDeletion", LIVE)}
    assert run(corpus, client) == 1
    assert "index_gen" in client.settings[LIVE]["filterableAttributes"]
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("an older indexer has run")
    client.always_fail = set()
    client.reset_log()
    assert run(corpus, client) == 0
    assert rebuilt(client) and client.paths()["documentation/SwiftUI/big.md"] == 1
    assert "documentation/UIKit/thing0.md" not in client.paths()


# ---------------------------------------------------------------------------
# Disk for the second index, and Meilisearch restarting mid-rebuild
# ---------------------------------------------------------------------------

GiB = 1024 ** 3


def meili_disk(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, used: int,
               free: Callable[[], int]) -> Path:
    """Give the run a Meilisearch database directory taking `used` bytes on a disk with
    free() bytes free"""
    db = tmp_path / "meili-db"
    db.mkdir(exist_ok=True)
    monkeypatch.setenv("MEILI_DB_PATH", str(db))
    monkeypatch.setattr(index_to_meilisearch, "size_on_disk", lambda path: used)
    monkeypatch.setattr(index_to_meilisearch, "free_disk_bytes", lambda path: free())
    return db


def test_a_rebuild_without_disk_for_a_second_index_is_not_started(
        corpus: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    # A build that filled the disk would kill Meilisearch (SIGBUS) and keep it from
    # starting again: the rebuild isn't started, and the update is applied instead
    client = FakeClient()
    run(corpus, client)
    created = client.created[LIVE]
    write_doc(corpus, "SwiftUI/item0.md", "Scraped change.")
    (corpus / "UIKit" / "thing0.md").unlink()
    free = 5 * GiB
    meili_disk(monkeypatch, tmp_path, used=4 * GiB, free=lambda: free)   # needs 4.8 + 1 GiB
    week = client.clock + timedelta(days=7)
    client.reset_log()
    capsys.readouterr()

    assert run(corpus, client, now=week) == 1
    out = normalized_output(capsys)
    # (the path may be wrapped)
    assert "✗ Rebuild failed before its swap: not enough disk for a second index: 5.0 GiB free on " in out
    assert ("and a rebuild needs 5.8 GiB (1.2x the 4.0 GiB the database takes, plus 1.0 GiB). "
            "Nothing was built; the live index keeps serving") in out
    assert all(uid != BUILD for _, uid in client.enqueued) and BUILD not in client.indexes
    assert "Scraped change" in client.docs()[id_of("SwiftUI/item0.md")]["content"]
    assert "documentation/UIKit/thing0.md" not in client.paths() and client.created[LIVE] == created
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("weekly rebuild")

    free = 6 * GiB
    client.reset_log()
    capsys.readouterr()
    assert run(corpus, client, now=week) == 0
    assert "✓ Disk: 6.0 GiB free on" in normalized_output(capsys)
    assert rebuilt(client) and client.created[LIVE] != created


def test_a_forced_rebuild_without_disk_changes_nothing(corpus: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    client = FakeClient()
    run(corpus, client)
    live_before = json.dumps(client.docs(), sort_keys=True)
    hashes_before = hash_file_text(corpus)
    meili_disk(monkeypatch, tmp_path, used=4 * GiB, free=lambda: 2 * GiB)
    client.reset_log()
    assert run(corpus, client, force=True) == 1
    assert client.enqueued == [] and json.dumps(client.docs(), sort_keys=True) == live_before
    assert hash_file_text(corpus) == hashes_before


def test_a_build_is_stopped_when_the_disk_fills_up(
        corpus: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    # Something else takes the room the check saw: the build stops between two batches,
    # before the disk is full, and its index is deleted; the update is applied instead
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", "Scraped change.")
    readings = iter([10 * GiB, 3 * GiB, GiB - 1])   # the check, then after each batch
    meili_disk(monkeypatch, tmp_path, used=GiB, free=lambda: next(readings, 10 * GiB))
    client.reset_log()
    capsys.readouterr()
    assert run(corpus, client, now=client.clock + timedelta(days=7), batch_size=15) == 1
    out = normalized_output(capsys)
    assert "the disk is filling up during the build: 1.0 GiB free" in out
    assert [kind for kind, uid in client.enqueued if uid == BUILD] == [
        "indexCreation", "settingsUpdate", "documentAdditionOrUpdate", "documentAdditionOrUpdate", "indexDeletion"]
    assert BUILD not in client.indexes and len(client.docs()) == 40
    assert "Scraped change" in client.docs()[id_of("SwiftUI/item0.md")]["content"]
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("weekly rebuild")


def test_the_update_after_a_rebuild_without_disk_stops_at_the_floor(
        corpus: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    # The update applied instead re-indexes more than 25% of the files in place: it stops
    # before a batch when the free space is under the floor, and saves no hash for the
    # files it didn't index
    client = FakeClient()
    run(corpus, client)
    before = saved_hashes(corpus) or {}
    for n in range(11):
        write_doc(corpus, f"SwiftUI/item{n}.md", "Changed text.")
    changed = {f"SwiftUI/item{n}.md": PENDING_HASH for n in range(11)}
    readings: List[int] = []
    meili_disk(monkeypatch, tmp_path, used=4 * GiB, free=lambda: readings.pop(0) if readings else 10 * GiB)

    # Under the floor from the start (the rebuild check, then the update's): nothing is sent
    readings[:] = [5 * GiB, GiB - 1]
    hashes_before = hash_file_text(corpus)
    client.reset_log()
    capsys.readouterr()
    assert run(corpus, client, batch_size=5) == 1
    out = normalized_output(capsys)
    assert "not enough disk for a second index: 5.0 GiB free" in out
    assert ("the disk is filling up during the update: 1.0 GiB free on" in out
            and "The update was stopped before its next batch; the live index keeps serving" in out)
    assert client.enqueued == [] and hash_file_text(corpus) == hashes_before

    # Under it after the first batch: the files sent stay pending, nothing is deleted
    readings[:] = [5 * GiB, 2 * GiB, GiB - 1]
    client.reset_log()
    capsys.readouterr()
    assert run(corpus, client, batch_size=5) == 1
    assert "the disk is filling up during the update: 1.0 GiB free" in normalized_output(capsys)
    assert [kind for kind, uid in client.enqueued if uid == LIVE] == ["documentAdditionOrUpdate"]
    assert all(uid != BUILD for _, uid in client.enqueued) and len(client.docs()) == 40
    assert saved_hashes(corpus) == {**before, **changed}
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("11 of 40 files changed")

    # With room again, the rebuild runs
    client.reset_log()
    assert run(corpus, client, batch_size=5) == 0 and rebuilt(client)
    assert all("Changed text" in client.docs()[id_of(f"SwiftUI/item{n}.md")]["content"] for n in range(11))


def test_the_disk_is_not_checked_for_a_fresh_volumes_first_build(
        corpus: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    # There is no live index to keep serving, and nothing else to build
    meili_disk(monkeypatch, tmp_path, used=0, free=lambda: 0)
    client = FakeClient()
    assert run(corpus, client, batch_size=15) == 0
    assert len(client.docs()) == 40


def test_meilisearch_db_path_and_size_on_disk(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MEILI_DB_PATH", str(tmp_path / "missing"))
    assert index_to_meilisearch.meilisearch_db_path() is None
    db = tmp_path / "db"
    (db / "indexes" / "uuid").mkdir(parents=True)
    monkeypatch.setenv("MEILI_DB_PATH", str(db))
    assert index_to_meilisearch.meilisearch_db_path() == db
    # LMDB's data.mdb is a sparse file as large as its map: only written blocks count
    with open(db / "indexes" / "uuid" / "data.mdb", "wb") as sparse:
        sparse.write(b"x" * 1_000_000)
        sparse.truncate(2 ** 40)
    (db / "VERSION").write_text("1.49.0")
    size = index_to_meilisearch.size_on_disk(db)
    assert 1_000_000 <= size < 2_000_000


def test_after_meilisearch_crashes_mid_build_the_update_waits_for_it(
        corpus: Path, capsys: pytest.CaptureFixture[str]) -> None:
    # Killed (OOM, a crash) during the build, Meilisearch is restarted by supervisord:
    # the build index is deleted and the update applied once it answers again
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", "Scraped change.")
    client.crash_on = ("documentAdditionOrUpdate", BUILD)
    client.reset_log()
    capsys.readouterr()
    assert run(corpus, client, now=client.clock + timedelta(days=7)) == 1
    out = normalized_output(capsys)
    assert "Waiting for Meilisearch to answer again..." in out and "✓ Meilisearch is answering again" in out
    assert client.health_checks == 5 and BUILD not in client.indexes  # 3 failed, then 2 answered
    assert "Scraped change" in client.docs()[id_of("SwiftUI/item0.md")]["content"]
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("weekly rebuild")
    assert out.endswith("The live index was updated in place instead; the next run retries the rebuild")


def test_a_meilisearch_that_stays_down_fails_the_run(
        corpus: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", "Scraped change.")
    monkeypatch.setattr(index_to_meilisearch, "MEILISEARCH_RECOVERY_SECONDS", 0)
    client.crash_on = ("documentAdditionOrUpdate", BUILD)
    client.crash_outage = 10 ** 6
    capsys.readouterr()
    assert run(corpus, client, now=client.clock + timedelta(days=7)) == 1
    out = normalized_output(capsys)
    assert "Meilisearch didn't answer within 0 s" in out
    assert "✗ Indexing aborted: MeilisearchCommunicationError, Connection refused" in out
    assert "Scraped change" not in client.docs()[id_of("SwiftUI/item0.md")]["content"]


# ---------------------------------------------------------------------------
# --limit (for testing)
# ---------------------------------------------------------------------------

def test_limit_builds_a_fresh_index_of_that_many_files(corpus: Path) -> None:
    client = FakeClient()
    assert run(corpus, client, limit=5) == 0
    assert len(client.docs()) == 5 and len(saved_hashes(corpus) or {}) == 5


def test_limit_never_swaps_a_partial_index_in_for_the_live_one(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    live_before = json.dumps(client.docs(), sort_keys=True)
    hashes_before = hash_file_text(corpus)
    for force, now in ((True, None), (False, client.clock + timedelta(days=7))):
        client.reset_log()
        assert run(corpus, client, limit=5, force=force, now=now) == 1
        assert client.enqueued == []
        assert json.dumps(client.docs(), sort_keys=True) == live_before
        assert hash_file_text(corpus) == hashes_before


def test_limit_updates_only_its_files_when_no_rebuild_is_due(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", "Changed text.")   # among the first 5 files
    write_doc(corpus, "UIKit/thing5.md", "Changed text.")    # not
    client.reset_log()
    assert run(corpus, client, limit=5) == 0
    assert "Changed text" in client.docs()[id_of("SwiftUI/item0.md")]["content"]
    assert "Changed text" not in client.docs()[id_of("UIKit/thing5.md")]["content"]


# ---------------------------------------------------------------------------
# Image completeness (DOC_FILE_COUNT)
# ---------------------------------------------------------------------------

def test_a_matching_doc_file_count_lets_the_build_and_the_deletes_happen(corpus: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DOC_FILE_COUNT", "40")
    client = FakeClient()
    assert run(corpus, client) == 0 and len(client.docs()) == 40
    # a real removal of 5 docs (12.5%), with a matching count: deleted
    for n in range(5):
        (corpus / "UIKit" / f"thing{n}.md").unlink()
    monkeypatch.setenv("DOC_FILE_COUNT", "35")
    client.reset_log()
    assert run(corpus, client) == 0
    assert client.kinds() == ["documentDeletion", "documentAdditionOrUpdate"]
    assert len(client.docs()) == 35


@pytest.mark.parametrize("mode", ["fresh volume", "update", "forced rebuild"])
def test_an_incomplete_image_changes_nothing(corpus: Path, monkeypatch: pytest.MonkeyPatch, mode: str) -> None:
    client = FakeClient()
    if mode != "fresh volume":
        run(corpus, client)
    live_before = json.dumps(client.docs(), sort_keys=True)
    hashes_before = hash_file_text(corpus)
    (corpus / "UIKit" / "thing0.md").unlink()           # missing from the image
    write_doc(corpus, "SwiftUI/item0.md", "Changed.")   # and a change
    monkeypatch.setenv("DOC_FILE_COUNT", "40")          # the checkout had 40
    client.reset_log()
    assert run(corpus, client, force=(mode == "forced rebuild")) == 1
    assert client.enqueued == []                        # no swap, no add, no delete
    assert json.dumps(client.docs(), sort_keys=True) == live_before
    assert hash_file_text(corpus) == hashes_before


def test_an_incomplete_image_says_why(corpus: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setenv("DOC_FILE_COUNT", "41")
    assert run(corpus, FakeClient()) == 1
    out = " ".join(capsys.readouterr().out.split())
    assert "the image holds 40 .md files, but its build counted 41 (DOC_FILE_COUNT)" in out


@pytest.mark.parametrize("value", ["", "  "])
def test_an_empty_doc_file_count_falls_back_to_the_live_count(corpus: Path, monkeypatch: pytest.MonkeyPatch, value: str) -> None:
    monkeypatch.setenv("DOC_FILE_COUNT", value)
    client = FakeClient()
    run(corpus, client)
    live_before = json.dumps(client.docs(), sort_keys=True)
    for n in range(5):  # 35 files for 40 live documents: under 90%
        (corpus / "UIKit" / f"thing{n}.md").unlink()
    client.reset_log()
    assert run(corpus, client) == 1
    assert client.enqueued == [] and json.dumps(client.docs(), sort_keys=True) == live_before
    # 4 removed (36 >= 90% of 40): an ordinary update, its deletes included
    write_doc(corpus, "UIKit/thing0.md")
    client.reset_log()
    assert run(corpus, client) == 0
    assert "documentDeletion" in client.kinds() and len(client.docs()) == 36


def test_a_doc_file_count_that_is_not_a_number_changes_nothing(corpus: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DOC_FILE_COUNT", "forty")
    client = FakeClient()
    assert run(corpus, client) == 1
    assert client.enqueued == []


# ---------------------------------------------------------------------------
# Incremental updates: add, then delete what the run didn't send (3.6a)
# ---------------------------------------------------------------------------

def test_a_chunked_file_that_shrinks_loses_its_old_chunks(corpus: Path) -> None:
    write_doc(corpus, "SwiftUI/big.md", big_body(3))
    client = FakeClient()
    run(corpus, client)
    assert client.paths()["documentation/SwiftUI/big.md"] == 3
    write_doc(corpus, "SwiftUI/big.md", "Now small.")
    client.reset_log()
    indexer = make_indexer(corpus, client)

    assert indexer.run() == 0
    # the add comes first, so the file is never missing from search
    assert client.kinds() == ["documentAdditionOrUpdate", "documentDeletion", "documentAdditionOrUpdate"]
    assert client.filters == [(LIVE, f'file_path IN ["documentation/SwiftUI/big.md"] AND index_gen != "{indexer.index_gen}"')]
    assert client.paths()["documentation/SwiftUI/big.md"] == 1
    assert client.docs()[id_of("SwiftUI/big.md")]["index_gen"] == indexer.index_gen
    assert len(client.docs()) == 41
    assert indexer.stats["documents_deleted"] == 3


def test_a_file_that_grows_into_chunks_loses_its_single_document(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", big_body(4))
    client.reset_log()
    assert run(corpus, client) == 0
    assert client.paths()["documentation/SwiftUI/item0.md"] == 4
    assert id_of("SwiftUI/item0.md") not in client.docs()


def test_every_chunk_of_a_file_reaches_the_index(corpus: Path) -> None:
    # A section over the chunk size, split among whole ones: each chunk has its own id, so
    # none replaces another in the index, and the chunks in order are the file
    body = ("## Small\n\nShort.\n\n## Huge\n\n" + "\n\n".join("word " * 2000 for _ in range(15))
            + "\n\n## Tail\n\nEnd.")
    path = write_doc(corpus, "SwiftUI/huge.md", body)
    client = FakeClient()
    indexer = make_indexer(corpus, client)
    assert indexer.run() == 0
    chunks = sorted((d for d in client.docs().values() if d["file_path"] == "documentation/SwiftUI/huge.md"),
                    key=lambda d: d["chunk_index"])
    assert len(chunks) > 3 and indexer.stats["chunks_created"] == len(client.docs())
    assert [d["id"] for d in chunks] == [f"{id_of('SwiftUI/huge.md')}_chunk_{n}" for n in range(len(chunks))]
    assert all(d["total_chunks"] == len(chunks) for d in chunks)
    assert "\n".join(d["content"] for d in chunks) == path.read_text(encoding="utf-8")


def test_a_removed_file_is_deleted_by_file_path_and_dropped_from_the_hash_file(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    state_before = saved_state(corpus)
    (corpus / "UIKit" / "thing7.md").unlink()
    client.reset_log()
    indexer = make_indexer(corpus, client)

    assert indexer.run() == 0
    # the value is the documents' file_path (documentation/ prefix), not the hash key
    assert client.filters == [(LIVE, f'file_path IN ["documentation/UIKit/thing7.md"] AND index_gen != "{indexer.index_gen}"')]
    assert "documentation/UIKit/thing7.md" not in client.paths()
    assert "UIKit/thing7.md" not in (saved_hashes(corpus) or {})
    assert saved_state(corpus) == state_before
    assert indexer.stats["removed"] == 1
    # deleted once: the next start sends nothing
    client.reset_log()
    assert run(corpus, client) == 0 and client.enqueued == [("documentAdditionOrUpdate", META)]


def test_a_failed_delete_aborts_and_is_retried(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    hashes_before = hash_file_text(corpus)
    (corpus / "UIKit" / "thing7.md").unlink()
    client.reset_log()
    client.fail = {"documentDeletion": (1, "failed")}
    assert run(corpus, client) == 1
    assert hash_file_text(corpus) == hashes_before
    assert ("documentAdditionOrUpdate", META) not in client.enqueued
    client.fail = {}
    assert run(corpus, client) == 0
    assert "documentation/UIKit/thing7.md" not in client.paths()


def test_deletes_send_at_most_2000_values_each(corpus: Path) -> None:
    assert MAX_FILTER_VALUES == 2000
    client = FakeClient()
    run(corpus, client)
    indexer = make_indexer(corpus, client)
    values = [f"documentation/Gone/page{n}.md" for n in range(4500)]
    for n, value in enumerate(values):
        client.indexes[LIVE][f"gone{n}"] = {"id": f"gone{n}", "file_path": value, "index_gen": "old"}
    first = client.reset_log()

    indexer.delete_old_documents(cast(Any, client.index(LIVE)), values)
    sent = [QUOTED.findall(DELETE_FILTER.fullmatch(flt).group("values")) for _, flt in client.filters]  # type: ignore[union-attr]
    assert [len(chunk) for chunk in sent] == [2000, 2000, 500]
    assert [unquote(v) for chunk in sent for v in chunk] == values
    assert not any(doc_id.startswith("gone") for doc_id in client.docs())
    assert client.waited == list(range(first, len(client.tasks)))


def test_filter_values_are_escaped_backslash_first() -> None:
    assert quote_filter_value('a\\b"c') == '"a\\\\b\\"c"'
    assert quote_filter_value("documentation/X/plain.md") == '"documentation/X/plain.md"'


def test_a_path_with_a_quote_or_backslash_is_deleted_exactly(corpus: Path) -> None:
    write_doc(corpus, 'Zz/q"x.md')
    write_doc(corpus, "Zz/back\\slash.md")
    client = FakeClient()
    run(corpus, client)
    for name in ('Zz/q"x.md', "Zz/back\\slash.md"):
        (corpus / name).unlink()
    assert run(corpus, client) == 0
    assert not any(path.startswith("documentation/Zz/") for path in client.paths())
    assert len(client.docs()) == 40


def test_the_delete_waits_for_index_gen_to_be_filterable(corpus: Path) -> None:
    # A live index whose settings lack index_gen (an older indexer ran) is rebuilt; when
    # that rebuild fails, the update after it makes index_gen filterable before any delete
    # (the delete would otherwise fail: filtering on a non-filterable attribute)
    client = FakeClient()
    run(corpus, client)
    client.settings[LIVE]["filterableAttributes"].remove("index_gen")
    (corpus / "UIKit" / "thing7.md").unlink()
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}
    client.reset_log()
    assert run(corpus, client) == 1
    update = client.enqueued[client.enqueued.index(("indexDeletion", BUILD)) + 1:]
    assert update == [("settingsUpdate", LIVE), ("documentDeletion", LIVE), ("documentAdditionOrUpdate", META)]
    assert client.payloads[client.enqueued.index(("settingsUpdate", LIVE))] == \
        {"filterableAttributes": INDEX_SETTINGS["filterableAttributes"]}
    assert "documentation/UIKit/thing7.md" not in client.paths()


def test_settings_are_applied_to_the_live_index_only_where_they_differ(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    client.settings[LIVE]["sortableAttributes"] = ["file_size"]
    client.settings[LIVE]["filterableAttributes"].reverse()  # same set, another order
    client.reset_log()
    assert run(corpus, client) == 0
    assert client.enqueued == [("settingsUpdate", LIVE), ("documentAdditionOrUpdate", META)]
    assert client.payloads[0] == {"sortableAttributes": ["last_modified", "file_size"]}


def test_settings_comparison() -> None:
    current = json.loads(json.dumps(INDEX_SETTINGS))
    current["filterableAttributes"].reverse()
    current["sortableAttributes"].sort()
    current["faceting"]["sortFacetValuesBy"] = {"*": "alpha"}
    current["rankingRules"] = ["words"]
    assert settings_to_update(current, INDEX_SETTINGS) == {}
    current["searchableAttributes"].reverse()  # its order is the ranking priority
    assert settings_to_update(current, INDEX_SETTINGS) == {"searchableAttributes": INDEX_SETTINGS["searchableAttributes"]}
    del current["faceting"]
    current["filterableAttributes"].pop()
    assert set(settings_to_update(current, INDEX_SETTINGS)) == {"searchableAttributes", "faceting", "filterableAttributes"}


def test_a_new_file_is_added_and_swept_too(corpus: Path) -> None:
    # A new file may already have documents (e.g. a hash file restored from before):
    # its documents from older runs go too
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/fresh.md")
    client.indexes[LIVE]["swiftui_fresh_chunk_1"] = {
        "id": "swiftui_fresh_chunk_1", "file_path": "documentation/SwiftUI/fresh.md", "index_gen": "old"}
    assert run(corpus, client) == 0
    assert client.paths()["documentation/SwiftUI/fresh.md"] == 1 and id_of("SwiftUI/fresh.md") in client.docs()


# ---------------------------------------------------------------------------
# An update that stops after an add: the files it was sending stay pending
# ---------------------------------------------------------------------------

def stop_after_the_add(client: FakeClient, how: str) -> Any:
    """
    Make the next update stop after its add has reached the live index, as a failed
    delete or meta write, an add that times out and then succeeds, or a failed hash
    save do. Returns the context to run it in.
    """
    if how == "delete fails":
        client.fail = {"documentDeletion": (1, "failed")}
    elif how == "meta write fails":
        client.fail = {"documentAdditionOrUpdate": (2, "failed")}  # after the one add
    elif how == "add times out":
        client.timeout_types = {"documentAdditionOrUpdate"}
    elif how == "hash save fails":
        real_replace = os.replace
        saves: List[Any] = []

        def replace(src: Any, dst: Any) -> None:
            saves.append(dst)
            if len(saves) == 2:  # the save before the add succeeds, the last one doesn't
                raise OSError(28, "No space left on device")
            real_replace(src, dst)

        return mock.patch("os.replace", side_effect=replace)
    return contextlib.nullcontext()


def let_runs_succeed(client: FakeClient) -> None:
    client.fail = {}
    client.timeout_types = set()
    client.reset_log()


STOPS = ["delete fails", "meta write fails", "add times out", "hash save fails"]


@pytest.mark.parametrize("how", STOPS)
def test_a_new_file_from_a_stopped_update_is_deleted_once_removed(corpus: Path, how: str) -> None:
    # Its documents reached the live index but its hash wasn't saved: Apple then removes
    # it, and the next update deletes them (the hash file lists it as pending)
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/brandnew.md", "Fresh page.")
    client.reset_log()
    with stop_after_the_add(client, how):
        assert run(corpus, client) == 1
    assert id_of("SwiftUI/brandnew.md") in client.docs()
    assert (saved_hashes(corpus) or {})["SwiftUI/brandnew.md"] == PENDING_HASH

    (corpus / "SwiftUI" / "brandnew.md").unlink()
    let_runs_succeed(client)
    indexer = make_indexer(corpus, client)
    assert indexer.run() == 0
    assert "documentation/SwiftUI/brandnew.md" not in client.paths() and len(client.docs()) == 40
    assert indexer.stats["removed"] == 1
    assert "SwiftUI/brandnew.md" not in (saved_hashes(corpus) or {})


@pytest.mark.parametrize("how", STOPS)
def test_a_file_from_a_stopped_update_is_sent_again_though_reverted(corpus: Path, how: str) -> None:
    # The stopped run's content reached the live index, and the next scrape put the file
    # back as the hash file recorded it before: it is sent again, not left stale
    client = FakeClient()
    run(corpus, client)
    item0 = corpus / "SwiftUI" / "item0.md"
    original = item0.read_text()
    write_doc(corpus, "SwiftUI/item0.md", "Interim text.")
    client.reset_log()
    with stop_after_the_add(client, how):
        assert run(corpus, client) == 1
    assert "Interim text" in client.docs()[id_of("SwiftUI/item0.md")]["content"]

    item0.write_text(original)
    let_runs_succeed(client)
    assert run(corpus, client) == 0
    assert "Interim text" not in client.docs()[id_of("SwiftUI/item0.md")]["content"]
    assert (saved_hashes(corpus) or {})["SwiftUI/item0.md"] == index_to_meilisearch.compute_file_hash(item0)
    let_runs_succeed(client)
    assert run(corpus, client) == 0 and client.enqueued == [("documentAdditionOrUpdate", META)]


def test_a_new_file_from_a_stopped_update_is_deleted_while_rebuilds_fail(corpus: Path) -> None:
    # The update after each failed rebuild sees it as a removed file too
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/brandnew.md")
    client.reset_log()
    client.fail = {"documentDeletion": (1, "failed")}
    assert run(corpus, client) == 1
    (corpus / "SwiftUI" / "brandnew.md").unlink()
    let_runs_succeed(client)
    client.always_fail = {("documentAdditionOrUpdate", BUILD)}  # e.g. no disk for a second index
    assert run(corpus, client, now=client.clock + timedelta(days=7)) == 1
    assert "documentation/SwiftUI/brandnew.md" not in client.paths() and len(client.docs()) == 40
    assert "SwiftUI/brandnew.md" not in (saved_hashes(corpus) or {})
    assert (saved_state(corpus) or {})["rebuild_due"].startswith("weekly rebuild")


def test_the_files_are_recorded_as_pending_before_anything_changes(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    write_doc(corpus, "SwiftUI/item0.md", "Changed text.")
    write_doc(corpus, "SwiftUI/brandnew.md")
    client.settings[LIVE]["sortableAttributes"] = ["file_size"]  # a settings task comes first
    seen: List[Tuple[str, Dict[str, str]]] = []
    real_enqueue = client.enqueue

    def enqueue(kind: str, uid: str, payload: Any = None) -> SimpleNamespace:
        if uid == LIVE:
            seen.append((kind, saved_hashes(corpus) or {}))
        return real_enqueue(kind, uid, payload)

    client.reset_log()
    with mock.patch.object(client, "enqueue", side_effect=enqueue):
        assert run(corpus, client) == 0
    assert [kind for kind, _ in seen] == ["settingsUpdate", "documentAdditionOrUpdate", "documentDeletion"]
    assert all(hashes["SwiftUI/item0.md"] == hashes["SwiftUI/brandnew.md"] == PENDING_HASH for _, hashes in seen)
    final = saved_hashes(corpus) or {}
    assert PENDING_HASH not in final.values() and len(final) == 41


def test_a_left_out_file_is_not_left_pending(corpus: Path) -> None:
    # Nothing of it was sent: after a successful run its entry is as before (none, for a
    # new file), so it is tried again as a new file
    client = FakeClient()
    run(corpus, client)
    before = saved_hashes(corpus)
    (corpus / "Zz").mkdir()
    (corpus / "Zz" / "broken.md").write_bytes(b"# Broken\n\xff\xfe not utf-8\n")
    client.reset_log()
    assert run(corpus, client) == 0
    assert saved_hashes(corpus) == before
    assert client.enqueued == [("documentAdditionOrUpdate", META)]


# ---------------------------------------------------------------------------
# Paths a filter can't tell apart (case, Unicode forms)
# ---------------------------------------------------------------------------

def test_an_unchanged_file_whose_path_filters_the_same_is_kept(corpus: Path) -> None:
    # "page²" and "page2" are different file names but one filter value (NFKD), as
    # "a.md" and "A.md" are on Linux
    write_doc(corpus, "Zz/page².md")
    write_doc(corpus, "Zz/page2.md")
    client = FakeClient()
    run(corpus, client)
    assert client.paths()["documentation/Zz/page².md"] == 1
    write_doc(corpus, "Zz/page2.md", "Changed text.")
    client.reset_log()
    indexer = make_indexer(corpus, client)
    assert indexer.run() == 0
    # the twin was sent again with this run's index_gen, so the delete spares it
    assert indexer.stats["processed"] == 2
    assert client.paths()["documentation/Zz/page².md"] == 1 and client.paths()["documentation/Zz/page2.md"] == 1
    # removing one keeps the other
    (corpus / "Zz" / "page2.md").unlink()
    assert run(corpus, client) == 0
    assert client.paths().get("documentation/Zz/page².md") == 1
    assert "documentation/Zz/page2.md" not in client.paths()


def test_a_removed_file_waits_while_its_twin_cannot_be_indexed(corpus: Path) -> None:
    write_doc(corpus, "Zz/page².md")
    write_doc(corpus, "Zz/page2.md")
    client = FakeClient()
    run(corpus, client)
    (corpus / "Zz" / "page2.md").unlink()
    real_process: Callable[..., List[Dict[str, Any]]] = index_to_meilisearch.DocumentProcessor.process_document

    def process(self: Any, file_path: str) -> List[Dict[str, Any]]:
        if file_path.endswith("page².md"):
            raise ValueError("converter bug")
        return real_process(self, file_path)

    with mock.patch.object(index_to_meilisearch.DocumentProcessor, "process_document", process):
        assert run(corpus, client) == 0
    # deleting page2.md's documents would delete page².md's too: both wait
    assert client.paths()["documentation/Zz/page².md"] == 1
    assert "Zz/page2.md" in (saved_hashes(corpus) or {})
    assert run(corpus, client) == 0
    assert "documentation/Zz/page2.md" not in client.paths()
    assert client.paths()["documentation/Zz/page².md"] == 1
    assert "Zz/page2.md" not in (saved_hashes(corpus) or {})


# ---------------------------------------------------------------------------
# Hash file
# ---------------------------------------------------------------------------

def test_hash_file_loading(docs_root: Path) -> None:
    indexer = make_indexer(docs_root, FakeClient())
    hash_file = docs_root.parent / "meilisearch_hashes.json"
    hash_file.write_text(json.dumps({"A/a.md": "1", "B/b.md": "2"}))       # an older indexer's
    assert indexer.load_hashes() == ({"A/a.md": "1", "B/b.md": "2"}, {})
    hash_file.write_text(json.dumps({INDEX_STATE_KEY: {"processor_version": 1, "created_at": "x"}, "A/a.md": "1"}))
    assert indexer.load_hashes() == ({"A/a.md": "1"}, {"processor_version": 1, "created_at": "x"})
    hash_file.write_text("{not json")
    assert indexer.load_hashes() == ({}, {})
    hash_file.write_text("[]")
    assert indexer.load_hashes() == ({}, {})


# ---------------------------------------------------------------------------
# File-level errors: logged, counted, left out, exit 0
# ---------------------------------------------------------------------------

def test_bad_files_are_skipped_and_counted_but_the_run_succeeds(corpus: Path) -> None:
    client = FakeClient()
    run(corpus, client)
    long_path = "Zz/" + "a" * 200 + "/" + "b" * 200 + "/" + "c" * 60 + ".md"
    write_doc(corpus, long_path)                                      # file_path > 468 bytes
    (corpus / "Zz" / "broken.md").write_bytes(b"# Broken\n\xff\xfe not utf-8\n")  # processing error
    write_doc(corpus, "Zz/badid.md")                                  # a document id Meilisearch rejects
    write_doc(corpus, "Zz/unreadable.md")                             # can't be read
    write_doc(corpus, "Zz/good.md")

    real_process: Callable[..., List[Dict[str, Any]]] = index_to_meilisearch.DocumentProcessor.process_document
    real_hash: Callable[..., str] = MeilisearchIndexer.compute_file_hash

    def process(self: Any, file_path: str) -> List[Dict[str, Any]]:
        documents = real_process(self, file_path)
        if file_path.endswith("badid.md"):
            documents[0]["id"] = "x" * 512
        return documents

    def file_hash(self: Any, file_path: Path) -> str:
        if file_path.name == "unreadable.md":
            raise PermissionError(13, "Permission denied")
        return real_hash(self, file_path)

    client.reset_log()
    indexer = make_indexer(corpus, client)
    with mock.patch.object(index_to_meilisearch.DocumentProcessor, "process_document", process), \
            mock.patch.object(MeilisearchIndexer, "compute_file_hash", file_hash):
        assert indexer.run() == 0

    assert indexer.stats["errors"] == 2      # broken.md, unreadable.md
    assert indexer.stats["invalid"] == 2     # the long path, badid.md
    assert indexer.stats["processed"] == 1   # good.md
    paths = {path for path in client.paths() if path.startswith("documentation/Zz/")}
    assert paths == {"documentation/Zz/good.md"}
    # left-out files get no hash, so every run tries them again
    assert {key for key in saved_hashes(corpus) or {} if key.startswith("Zz/")} == {"Zz/good.md"}
    assert all(task.status == "succeeded" for task in client.tasks.values())


def test_a_few_bad_files_dont_stop_a_rebuild(corpus: Path) -> None:
    (corpus / "Zz").mkdir()
    (corpus / "Zz" / "broken.md").write_bytes(b"# Broken\n\xff\xfe not utf-8\n")
    client = FakeClient()
    indexer = make_indexer(corpus, client)
    assert indexer.run() == 0  # 40 of 41 files indexed: over 90%
    assert indexer.stats["errors"] == 1 and len(client.docs()) == 40
    assert "Zz/broken.md" not in (saved_hashes(corpus) or {})


@pytest.mark.parametrize("failing_step", ["read", "process", "validate"])
def test_a_file_name_that_is_not_utf8_is_left_out_on_a_strict_stdout(corpus: Path, failing_step: str) -> None:
    # Linux allows such a name (macOS doesn't, so the file is faked here). Whichever step
    # rejects the file, the run still exits 0, and the name prints as escapes even on a
    # stdout that can't write it (a strict UTF-8 one, as on a Linux host's en_US.UTF-8)
    bad = corpus.resolve() / "Zz" / "a\udcff.md"
    real_discover: Callable[..., List[Path]] = MeilisearchIndexer.discover_markdown_files
    real_process: Callable[..., List[Dict[str, Any]]] = index_to_meilisearch.DocumentProcessor.process_document
    real_hash: Callable[..., str] = MeilisearchIndexer.compute_file_hash

    def discover(self: Any) -> List[Path]:
        return real_discover(self) + [bad]

    def file_hash(self: Any, file_path: Path) -> str:
        if file_path == bad:
            if failing_step == "read":
                raise PermissionError(13, "Permission denied", str(file_path))
            return "0" * 64
        return real_hash(self, file_path)

    def process(self: Any, file_path: str) -> List[Dict[str, Any]]:
        if file_path == str(bad):
            if failing_step == "process":
                raise UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
            return [{"id": "zz_a_", "file_path": "documentation/Zz/a\udcff.md", "content": "x"}]
        return real_process(self, file_path)

    stdout = io.BytesIO()
    strict = io.TextIOWrapper(stdout, encoding="utf-8", errors="strict", write_through=True)
    client = FakeClient()
    indexer = make_indexer(corpus, client)
    with mock.patch.object(MeilisearchIndexer, "discover_markdown_files", discover), \
            mock.patch.object(MeilisearchIndexer, "compute_file_hash", file_hash), \
            mock.patch.object(index_to_meilisearch.DocumentProcessor, "process_document", process), \
            mock.patch.object(index_to_meilisearch, "console", Console(file=strict, width=200)):
        assert indexer.run() == 0

    out = stdout.getvalue().decode("utf-8")
    assert "Zz/a\\xff.md" in out
    assert indexer.stats["errors" if failing_step != "validate" else "invalid"] == 1
    assert indexer.stats["processed"] == 40
    assert len(saved_hashes(corpus) or {}) == 40 and "Zz/a\udcff.md" not in (saved_hashes(corpus) or {})
    assert all(task.status == "succeeded" for task in client.tasks.values())


@pytest.mark.parametrize("failing_step", ["read", "process", "validate"])
def test_markup_in_a_path_or_error_is_printed_verbatim(corpus: Path, failing_step: str) -> None:
    # A path can hold rich markup: a closing tag across a directory and a file name ("q[",
    # "x]"), or a "[word]". Unescaped, the closing tag raises MarkupError, which crashed every
    # run while the file existed, and a "[word]" vanished, so the line named the wrong file
    bad = write_doc(corpus, f"Zz/q[/x]/w[red]{failing_step}.md").resolve()
    real_process: Callable[..., List[Dict[str, Any]]] = index_to_meilisearch.DocumentProcessor.process_document
    real_hash: Callable[..., str] = MeilisearchIndexer.compute_file_hash

    def file_hash(self: Any, file_path: Path) -> str:
        if file_path == bad and failing_step == "read":
            raise PermissionError(13, "Permission denied", str(file_path))
        return real_hash(self, file_path)

    def process(self: Any, file_path: str) -> List[Dict[str, Any]]:
        documents = real_process(self, file_path)
        if file_path == str(bad):
            if failing_step == "process":
                raise ValueError("no [/y] [bold]title")
            documents[0]["id"] = "zz_[/x]"
        return documents

    out = io.StringIO()
    client = FakeClient()
    indexer = make_indexer(corpus, client)
    with mock.patch.object(MeilisearchIndexer, "compute_file_hash", file_hash), \
            mock.patch.object(index_to_meilisearch.DocumentProcessor, "process_document", process), \
            mock.patch.object(index_to_meilisearch, "console", Console(file=out, width=1000)):
        assert indexer.run() == 0

    assert {
        "read": f"Error reading {bad}: [Errno 13] Permission denied: '{bad}'",
        "process": f"Error processing {bad}: no [/y] [bold]title",
        "validate": "Skipping Zz/q[/x]/w[red]validate.md: invalid document id 'zz_[/x]'",
    }[failing_step] in out.getvalue()
    assert indexer.stats["errors" if failing_step != "validate" else "invalid"] == 1
    assert indexer.stats["processed"] == 40
    assert len(saved_hashes(corpus) or {}) == 40


def test_dry_run_validates_without_meilisearch(docs_root: Path) -> None:
    write_doc(docs_root, "Zz/" + "a" * 240 + "/" + "b" * 240 + ".md")
    client = FakeClient()
    indexer = make_indexer(docs_root, client, batch_size=1)
    assert indexer.run(dry_run=True) == 0
    assert client.enqueued == [] and indexer.stats["invalid"] == 1
    assert saved_hashes(docs_root) is None


def test_main_exits_with_the_run_exit_code(tmp_path: Path) -> None:
    argv = ["index_to_meilisearch.py", "--docs-path", str(tmp_path), "--hash-file", str(tmp_path / "h.json")]
    with mock.patch("sys.argv", argv), \
            mock.patch.object(index_to_meilisearch.meilisearch.Client, "health", return_value={"status": "available"}), \
            mock.patch.object(MeilisearchIndexer, "run", return_value=1), \
            pytest.raises(SystemExit) as exit_info:
        index_to_meilisearch.main()
    assert exit_info.value.code == 1
