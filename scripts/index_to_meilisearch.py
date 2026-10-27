#!/usr/bin/env python3
"""
Index Apple Developer Documentation to Meilisearch

This script reads all markdown files from the documentation directory,
processes them with metadata extraction and document chunking,
and indexes them into Meilisearch with incremental update support.

The live index keeps serving every search through every run: an incremental update adds
the new and changed files' documents first and deletes their old ones after (removed
files' documents too), and a rebuild builds a new index next to the live one and swaps it
in once it is complete. A rebuild starts only when the disk has room for the second index.
A due rebuild that fails, or is skipped for lack of disk, leaves the live index serving,
and the run updates it instead.
"""

import os
import re
import sys
import json
import shutil
import argparse
import unicodedata
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from datetime import datetime, timedelta, timezone
import time

import meilisearch
from meilisearch.errors import MeilisearchApiError, MeilisearchError, MeilisearchTimeoutError
from meilisearch.index import Index
from meilisearch.models.task import Task, TaskInfo
from rich.console import Console
from rich.markup import escape
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from rich.table import Table
from dotenv import load_dotenv
from collections import defaultdict

# Add parent directory to path to import local modules
sys.path.append(str(Path(__file__).parent.parent))

from scripts.metadata_extractor import MetadataExtractor
from scripts.document_processor import DocumentProcessor
from scripts.utilities.hash_utils import compute_file_hash, write_text_atomic

# Load environment variables
load_dotenv()

console = Console()

# Meilisearch fails a whole add task when one document id is longer than 511 bytes or
# has a character outside [A-Za-z0-9_-]: one bad id loses its entire batch.
MAX_DOCUMENT_ID_BYTES = 511
DOCUMENT_ID_PATTERN = re.compile(r'[A-Za-z0-9_-]+')

# A filterable value longer than 468 bytes (MAX_FACET_VALUE_LENGTH = 500 - 32) is stored cut
# to its first 468 bytes. A filter on the whole value never matches it: expand_result can't
# find the doc, and a filter delete of it "succeeds" while deleting nothing. A filter on
# those first 468 bytes does match it, so a filter delete of another file whose path is
# exactly those bytes would delete its docs too. Meilisearch measures the value after
# normalizing it (NFKD, lowercased), which for an ASCII path is just its byte length.
# Verified on v1.49.
MAX_FILTER_VALUE_BYTES = 468

# How long to wait for one Meilisearch task. A task that takes longer aborts the run like a
# failed one (nothing saved, so the next run indexes the same files again).
TASK_TIMEOUT_MS = 10 * 60 * 1000

# Version of the documents the indexer builds from a file (document_processor,
# metadata_extractor and the fields set here). Bump it whenever that output changes: an
# incremental run re-sends only the files whose content changed, so the next start that
# finds another version in the hash file rebuilds the whole index.
# 2: sha1(file_path) document ids, one id per chunk, oversized blocks split wherever they
#    come; kind, platforms, url, api_name and overview from the page's own lines
# 3: deprecated and deprecation (metadata_extractor)
# 4: a page without a "# " title takes its front matter's title, else its first heading,
#    else its file name, never an empty title (metadata_extractor extract_title); an
#    overview is never cut inside a link (cut_overview)
# 5: an overview after the title skips any leading quote, not only Apple's deprecation
#    summary: the HIG's "> **Updated …:**" banner was 108 pages' summary
PROCESSOR_VERSION = 5

# The hash file is a flat map of file path -> content hash plus this one key, which no
# .md path can be: the processor version and the createdAt of the live index the hashes
# belong to. A rebuild swaps in a new index with a new createdAt, so a hash file saved for
# another index (a rebuild that stopped after its swap, a replaced volume) never matches.
# It also records a rebuild that failed and is still due ("rebuild_due"). Older indexers
# read the file as a flat map and keep this key on their incremental saves, so their runs
# are detected from the live index's settings instead (INDEX_GEN_ATTRIBUTE).
INDEX_STATE_KEY = "__index__"

# The hash an update records for each file it is about to send, saved before its first
# add: a run that stops after an add (a failed delete or meta write, a timeout, a killed
# container) saves no hashes, and the hash file must still list every file whose documents
# may be in the live index. No content hash equals it, so the next run sends the file
# again, or deletes its documents if it was removed since (a new file would otherwise have
# no entry, and its documents would stay in search until the next rebuild).
PENDING_HASH = "pending"

# The run that indexed a document. Every run of this indexer leaves it filterable on the
# live index; every start of an older indexer (before add-then-sweep: a rollback) resets
# the filterable attributes without it, and its incremental runs only add, leaving
# documents behind that no update deletes (e.g. the old chunks of a file that shrank).
# So a live index where it isn't filterable is rebuilt.
INDEX_GEN_ATTRIBUTE = 'index_gen'

# A rebuild builds "<index>-build" next to the live index and swaps it in when complete
BUILD_INDEX_SUFFIX = "-build"

# Weekly safety-net rebuild, counted from the live index's createdAt (UTC). 6.5 days, so
# the deploy after the Tue/Fri scrape a week later is never a few hours short of it.
REBUILD_AFTER = timedelta(days=6.5)

# An update that changes more than this fraction of the files rebuilds instead
REBUILD_CHANGED_FRACTION = 0.25

# A new index must hold at least this fraction of the files to be swapped in (catches
# indexing failures). Without DOC_FILE_COUNT (local builds), the image's files must also
# be at least this fraction of the live index's documents.
MIN_INDEXED_FRACTION = 0.9

# file_path values per filter delete (5,000 values took 1.6 s on v1.49)
MAX_FILTER_VALUES = 2000

# Meilisearch's database directory, where a rebuild writes its second index. It runs with
# --db-path /data/meilisearch (mcp-server/docker/supervisord.conf), and the image sets
# MEILI_DB_PATH to the same; outside the image (no such directory) the disk isn't checked.
DEFAULT_MEILI_DB_PATH = "/data/meilisearch"

# A rebuild holds two indexes on disk until its swap: the build takes about what the live
# index takes (measured on v1.49: 0.99-1.02x; 4.8 GB on disk for the full corpus, which
# /stats' usedDatabaseSize reports as ~3.1 GB). Meilisearch writes through mmap, so a disk
# that fills kills it (SIGBUS), and it can't start again while the unfinished build index
# keeps the disk full: search would stay down until someone freed disk by hand. So a
# rebuild over a live index starts only with BUILD_DISK_FACTOR x the database's size on
# disk + BUILD_DISK_MARGIN free, and stops (deleting its build index) when free space
# falls under BUILD_DISK_FLOOR between two batches (e.g. something else filling the disk).
# The update applied in place of a failed rebuild stops at the same floor.
BUILD_DISK_FACTOR = 1.2
BUILD_DISK_MARGIN = 1024 ** 3
BUILD_DISK_FLOOR = 1024 ** 3

# After a request failed mid-rebuild, how long to wait for Meilisearch to answer again
# before deleting the build index and updating the live index: when it crashed or was
# OOM-killed, supervisord restarts it within a second, and it then reopens its database
MEILISEARCH_RECOVERY_SECONDS = 120

# Documents per fetch when listing the documents an older indexer left (see update)
UNSTAMPED_FETCH_LIMIT = 10000

# Applied to the build index before its documents, and to the live index only where they
# differ from its current settings: a settings update queues a task (even one that
# changes nothing), and while it runs /health reports the live index as indexing
INDEX_SETTINGS: Dict[str, Any] = {
    'filterableAttributes': [
        'framework',
        'platforms',
        'kind',
        'is_framework_main',
        'file_path',
        'api_name',
        'is_chunk',
        INDEX_GEN_ATTRIBUTE,  # old documents are deleted by it
    ],
    'sortableAttributes': [
        'last_modified',
        'file_size'
    ],
    # Searchable attributes with priority
    # NOTE: content_cleaned was removed to reduce document size
    'searchableAttributes': [
        'title',
        'api_name',
        'overview',
        'content'
    ],
    # Show all frameworks in facets
    'faceting': {
        'maxValuesPerFacet': 5000  # Every framework value (462 on 2026-10-26): list_frameworks and the no-results message read the full list
    },
}

# Settings Meilisearch keeps as sets (it returns them in another order)
UNORDERED_SETTINGS = {'filterableAttributes', 'sortableAttributes'}


class TaskFailedError(Exception):
    """A Meilisearch task failed, was canceled or didn't finish in time"""


class CheckFailedError(Exception):
    """A safety check stopped the run before it swapped or deleted anything"""


class BuildFailedError(Exception):
    """A rebuild failed before its swap: the live index and the hash file are as they were"""


class RebuildFailedError(Exception):
    """A due rebuild failed before its swap, and the live index was updated in place instead"""


def filter_key(value: str) -> str:
    """
    A filterable string as Meilisearch compares it: trimmed, NFKD-normalized and
    lowercased (verified on v1.49). Two file paths with the same key are the same value
    to a filter, so a delete of one deletes the other's documents too.
    """
    return unicodedata.normalize('NFKD', value.strip()).lower()


def filter_value_bytes(value: str) -> int:
    """
    Length of a filterable string as Meilisearch's 468-byte limit counts it.

    Raises:
        UnicodeEncodeError: The value isn't valid UTF-8 text (e.g. a file name with
            invalid bytes, which Linux allows)
    """
    return len(filter_key(value).encode('utf-8'))


def quote_filter_value(value: str) -> str:
    """
    A string as a quoted filter value. Backslashes are escaped first: Meilisearch
    unescapes the value, and one bare backslash fails the whole filter (verified on v1.49).
    """
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def settings_to_update(current: Dict[str, Any], desired: Dict[str, Any]) -> Dict[str, Any]:
    """The desired settings that differ from the index's current ones"""
    changes: Dict[str, Any] = {}
    for name, value in desired.items():
        have = current.get(name)
        if isinstance(value, dict):
            # Meilisearch adds keys of its own (e.g. faceting.sortFacetValuesBy)
            same = isinstance(have, dict) and all(have.get(k) == v for k, v in value.items())
        elif name in UNORDERED_SETTINGS:
            same = (isinstance(have, list) and all(isinstance(item, str) for item in have)
                    and len(have) == len(value) and set(have) == set(value))
        else:
            same = have == value
        if not same:
            changes[name] = value
    return changes


def expected_file_count() -> Optional[int]:
    """
    The .md count of the checkout the image was built from (DOC_FILE_COUNT, set by
    docker-build), or None when it isn't set (local builds leave it empty).

    Raises:
        CheckFailedError: It isn't a number
    """
    raw = os.getenv("DOC_FILE_COUNT", "").strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        raise CheckFailedError(f"DOC_FILE_COUNT is {raw!r}, not a number") from None


def meilisearch_db_path() -> Optional[Path]:
    """
    Meilisearch's database directory when this indexer runs beside it (in the image), or
    None when there is no such directory here (a Meilisearch on another host or volume,
    whose disk this indexer can't measure).
    """
    path = Path(os.getenv("MEILI_DB_PATH") or DEFAULT_MEILI_DB_PATH)
    return path if path.is_dir() else None


def size_on_disk(path: Path) -> int:
    """
    Bytes the files under path take on disk: their allocated blocks, since each index's
    LMDB data.mdb is a sparse file as large as its map (2 TiB on v1.49).
    """
    total = 0
    for root, _dirs, names in os.walk(path):
        for name in names:
            try:
                total += os.lstat(os.path.join(root, name)).st_blocks * 512
            except OSError:
                pass  # removed while walking (a finished task's update file)
    return total


def free_disk_bytes(path: Path) -> int:
    """Free bytes on the filesystem that holds path"""
    return shutil.disk_usage(path).free


def gib(size: float) -> str:
    """A byte count in GiB, for the log"""
    return f"{size / 1024 ** 3:.1f} GiB"


def parse_meilisearch_time(value: str) -> datetime:
    """A Meilisearch timestamp (RFC 3339 in UTC, e.g. createdAt) as an aware datetime"""
    parsed = datetime.fromisoformat(value)
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def printable_path(path: Path) -> str:
    """
    A path as text any UTF-8 stdout can write: bytes of a file name that aren't valid
    UTF-8 (Linux allows them) show as escapes.
    """
    return os.fsencode(path).decode('utf-8', 'backslashreplace')


def find_invalid_document(documents: List[Dict[str, Any]]) -> Optional[str]:
    """
    Check a file's documents before they are sent.

    Returns why Meilisearch would reject one of them (failing its whole batch) or could
    never filter it by file_path, or None when all are valid.
    """
    for doc in documents:
        doc_id = doc.get('id')
        if not isinstance(doc_id, str) or not DOCUMENT_ID_PATTERN.fullmatch(doc_id):
            return f"invalid document id {str(doc_id)[:100]!r} (allowed: A-Z a-z 0-9 _ -)"
        if len(doc_id.encode('utf-8')) > MAX_DOCUMENT_ID_BYTES:
            return f"document id is {len(doc_id.encode('utf-8'))} bytes (max {MAX_DOCUMENT_ID_BYTES})"
        file_path = doc.get('file_path')
        if not isinstance(file_path, str) or not file_path:
            return "document has no file_path"
        try:
            path_bytes = filter_value_bytes(file_path)
        except UnicodeEncodeError:
            # Meilisearch can't parse it (a lone surrogate in the JSON) and fails the whole
            # batch. Verified on v1.49.
            return "file name is not valid UTF-8"
        if path_bytes > MAX_FILTER_VALUE_BYTES:
            return (f"file_path is {path_bytes} bytes as Meilisearch filters it "
                    f"(max {MAX_FILTER_VALUE_BYTES})")
    return None


class MeilisearchIndexer:
    """Handles indexing of Apple documentation to Meilisearch"""
    
    def __init__(self,
                 meilisearch_url: str,
                 api_key: str,
                 docs_path: str = "../documentation",
                 index_name: str = "apple-docs",
                 batch_size: int = 10000,  # 10K is fastest; needs 3GB+ memory with exp flag
                 hash_file: str = "../.hashes/meilisearch_hashes.json"):
        """
        Initialize the indexer
        
        Args:
            meilisearch_url: URL of Meilisearch instance
            api_key: Master key or API key for Meilisearch
            docs_path: Path to documentation directory
            index_name: Name of the Meilisearch index
            batch_size: Number of documents to upload in each batch
            hash_file: Path to store file hashes for incremental updates
        """
        self.client = meilisearch.Client(meilisearch_url, api_key)
        self.docs_path = Path(docs_path).resolve()
        self.index_name = index_name
        self.build_index_name = f"{index_name}{BUILD_INDEX_SUFFIX}"
        self.batch_size = batch_size
        self.hash_file = Path(hash_file)
        
        self.metadata_extractor = MetadataExtractor()
        self.document_processor = DocumentProcessor()
        
        # Stamped on every document this run sends (index_gen), so the documents a file
        # had before this run can be deleted by filter after its new ones are added
        self.index_gen = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")

        # Meilisearch's database directory while a rebuild over a live index is building
        # (its free space is checked between batches), else None
        self.build_db_path: Optional[Path] = None

        # Statistics ("errors" and "invalid" count files left out of the index)
        self.stats = {
            "total_files": 0,
            "processed": 0,
            "skipped": 0,
            "removed": 0,
            "errors": 0,
            "invalid": 0,
            "chunks_created": 0,
            "documents_deleted": 0,
            "start_time": time.time()
        }
        
    def now(self) -> datetime:
        """The current time, timezone-aware in UTC"""
        return datetime.now(timezone.utc)

    def load_hashes(self) -> Tuple[Dict[str, str], Dict[str, Any]]:
        """
        Load the stored file hashes and the state of the index they belong to
        (INDEX_STATE_KEY). A hash file an older indexer saved has no state.
        """
        if self.hash_file.exists():
            try:
                data = json.loads(self.hash_file.read_text(encoding='utf-8'))
                if not isinstance(data, dict):
                    raise ValueError("not a JSON object")
            except (OSError, ValueError) as e:
                console.print(f"[yellow]Warning: Could not load hash file: {escape(str(e))}[/yellow]")
                return {}, {}
            state = data.pop(INDEX_STATE_KEY, None)
            hashes = {path: value for path, value in data.items() if isinstance(value, str)}
            return hashes, state if isinstance(state, dict) else {}
        return {}, {}
    
    def save_hashes(self, hashes: Dict[str, str], created_at: str,
                    still_due: Optional[Dict[str, Any]] = None, log: bool = True) -> None:
        """
        Save file hashes for next run, bound to the live index's createdAt.

        Args:
            still_due: After a rebuild that failed, the state that keeps it due:
                "rebuild_due" (why), and the "processor_version" of the documents the
                update left as they were (the recorded one, not PROCESSOR_VERSION)
            log: Print the save (not for the one an update makes before it changes anything)

        Written whole or not at all, so a failed write leaves the previous hashes as they
        were. Raises OSError, which fails the run.
        """
        state: Dict[str, Any] = {"processor_version": PROCESSOR_VERSION, "created_at": created_at,
                                 **(still_due or {})}
        self.hash_file.parent.mkdir(parents=True, exist_ok=True)
        write_text_atomic(self.hash_file, json.dumps({INDEX_STATE_KEY: state, **hashes}, indent=2))
        if log:
            console.print(f"\n💾 Saved {len(hashes)} file hashes")
    
    def compute_file_hash(self, file_path: Path) -> str:
        """Compute SHA-256 hash of a file"""
        return compute_file_hash(file_path)
    
    def discover_markdown_files(self) -> List[Path]:
        """
        Find all markdown files in documentation directory.

        Uses sorted() to ensure deterministic ordering across runs,
        which helps with incremental indexing and debugging.
        """
        # Note: We convert to list because we need len() for progress tracking
        # and iterate twice (once for framework counts, once for processing).
        # For 334K files, this uses ~35MB of memory which is acceptable.
        # The actual file contents are streamed one at a time during processing.
        return sorted(self.docs_path.rglob("*.md"))
    
    def wait_for_task(self, task_info: TaskInfo, action: str) -> Task:
        """
        Wait for a Meilisearch task and check its outcome.

        The client's wait_for_task returns failed and canceled tasks without raising, so
        every task the indexer enqueues goes through here.

        Raises:
            TaskFailedError: The task didn't succeed within TASK_TIMEOUT_MS
        """
        try:
            task = self.client.wait_for_task(task_info.task_uid, timeout_in_ms=TASK_TIMEOUT_MS)
        except MeilisearchTimeoutError as e:
            raise TaskFailedError(
                f"{action}: task {task_info.task_uid} didn't finish within {TASK_TIMEOUT_MS // 1000} s"
            ) from e
        if task.status != "succeeded":
            error = task.error or {}
            # The message can quote a whole document (e.g. missing_document_id)
            message = str(error.get('message', ''))[:300]
            raise TaskFailedError(
                f"{action}: task {task.uid} {task.status}"
                + (f" ({error.get('code')}: {message})" if error else "")
            )
        return task

    def get_index(self, uid: str) -> Optional[Dict[str, Any]]:
        """The index (uid, createdAt, …), or None when it doesn't exist (other errors are raised)"""
        try:
            index: Dict[str, Any] = self.client.get_raw_index(uid)
            return index
        except MeilisearchApiError as e:
            if e.code == "index_not_found":
                return None
            raise

    def index_exists(self, uid: str) -> bool:
        """Whether the index exists (other errors are raised)"""
        return self.get_index(uid) is not None

    def document_count(self, uid: str) -> int:
        """Number of documents in the index"""
        return int(self.client.index(uid).get_stats().number_of_documents)

    def relative_key(self, file_path: Path) -> str:
        """A file's key in the hash file: its path relative to the docs dir"""
        return str(file_path.relative_to(self.docs_path))

    def file_path_value(self, key: str) -> str:
        """
        The file_path its documents carry, built the same way they are
        (normalize_file_path): hash keys lack the documentation/ prefix, so a filter on
        a hash key deletes nothing
        """
        value: str = self.metadata_extractor.normalize_file_path(str(self.docs_path / key))
        return value

    def check_image(self, file_count: int, live_docs: int) -> None:
        """
        Check that the image holds every doc of the checkout it was built from, before
        anything is written: a truncated image must neither be swapped in nor have its
        missing files' documents deleted.

        Raises:
            CheckFailedError: The image is incomplete
        """
        expected = expected_file_count()
        if expected is not None:
            if file_count != expected:
                raise CheckFailedError(
                    f"the image holds {file_count:,} .md files, but its build counted {expected:,} "
                    f"(DOC_FILE_COUNT): the image is incomplete. Nothing was swapped, added or "
                    f"deleted; the live index keeps serving"
                )
            console.print(f"✓ Image complete: {file_count:,} .md files, as its build counted")
        elif live_docs and file_count < MIN_INDEXED_FRACTION * live_docs:
            # Local builds carry no DOC_FILE_COUNT: fall back to the live index's size
            raise CheckFailedError(
                f"{file_count:,} .md files for {live_docs:,} documents in the live index (under "
                f"{MIN_INDEXED_FRACTION:.0%}), and no DOC_FILE_COUNT to tell a removal from a "
                f"truncated image. Nothing was swapped, added or deleted; set DOC_FILE_COUNT to "
                f"the expected .md count to confirm"
            )

    def rebuild_reason(self, live: Optional[Dict[str, Any]], state: Dict[str, Any],
                       live_settings: Dict[str, Any]) -> Optional[str]:
        """
        Why the index must be rebuilt instead of updated, or None. The live index is never
        partial (every build is swapped in complete), so its state in the hash file says
        whether the stored hashes describe it, and its settings whether an older indexer
        has run on it since.
        """
        if live is None:
            return f"no '{self.index_name}' index yet"
        recorded = state.get("processor_version")
        if recorded != PROCESSOR_VERSION:
            if recorded is None:
                return "the hash file records no processor version"
            return f"processor version {recorded} -> {PROCESSOR_VERSION}"
        created_at = live.get("createdAt")
        if state.get("created_at") != created_at:
            return (f"the hash file belongs to another index (createdAt {state.get('created_at')}, "
                    f"live index {created_at})")
        if state.get("rebuild_due"):
            return f"still due after a failed rebuild: {state['rebuild_due']}"
        if INDEX_GEN_ATTRIBUTE not in (live_settings.get('filterableAttributes') or []):
            return (f"an older indexer has run on the live index ({INDEX_GEN_ATTRIBUTE} isn't filterable), "
                    f"leaving documents no update deletes")
        try:
            age = self.now() - parse_meilisearch_time(str(created_at))
        except ValueError:
            return f"the live index's createdAt {created_at!r} can't be read"
        if age >= REBUILD_AFTER:
            return f"weekly rebuild: the live index was built {age.total_seconds() / 86400:.1f} days ago"
        return None

    def check_disk_for_build(self) -> None:
        """
        Before a rebuild over a live index: the disk must have room for the second index
        (see BUILD_DISK_FACTOR). Not checked when Meilisearch's database isn't on this
        host (meilisearch_db_path).

        Raises:
            CheckFailedError: Too little free space; nothing has been built
        """
        db_path = meilisearch_db_path()
        if db_path is None:
            return
        used = size_on_disk(db_path)
        free = free_disk_bytes(db_path)
        need = int(used * BUILD_DISK_FACTOR) + BUILD_DISK_MARGIN
        if free < need:
            raise CheckFailedError(
                f"not enough disk for a second index: {gib(free)} free on {db_path}, and a rebuild "
                f"needs {gib(need)} ({BUILD_DISK_FACTOR}x the {gib(used)} the database takes, plus "
                f"{gib(BUILD_DISK_MARGIN)}). Nothing was built; the live index keeps serving"
            )
        console.print(f"✓ Disk: {gib(free)} free on {escape(str(db_path))}, a rebuild needs {gib(need)}")
        self.build_db_path = db_path

    def check_disk_during_build(self) -> None:
        """
        Between two batches of a rebuild over a live index: stop it before the disk fills.

        Raises:
            CheckFailedError: Free space fell under BUILD_DISK_FLOOR
        """
        self.check_disk_floor(self.build_db_path, "during the build",
                              "The build was stopped and its index deleted")

    def check_disk_floor(self, db_path: Optional[Path], during: str, stopped: str) -> None:
        """
        Stop a rebuild, or the update that replaces a failed one, before the disk that
        holds Meilisearch's database (db_path; None: not on this host) fills up.

        Raises:
            CheckFailedError: Free space is under BUILD_DISK_FLOOR
        """
        if db_path is None:
            return
        free = free_disk_bytes(db_path)
        if free < BUILD_DISK_FLOOR:
            raise CheckFailedError(
                f"the disk is filling up {during}: {gib(free)} free on {db_path} "
                f"(under {gib(BUILD_DISK_FLOOR)}). {stopped}; the live index keeps serving"
            )

    def wait_until_available(self) -> bool:
        """
        Wait (up to MEILISEARCH_RECOVERY_SECONDS) until Meilisearch answers its health
        check: after a request failed mid-rebuild, it may be restarting.

        Returns:
            Whether it answered
        """
        deadline = time.monotonic() + MEILISEARCH_RECOVERY_SECONDS
        waited = False
        while True:
            try:
                if self.client.health().get('status') == 'available':
                    if waited:
                        console.print("[green]✓ Meilisearch is answering again[/green]")
                    return True
            except MeilisearchError:
                pass
            if time.monotonic() >= deadline:
                console.print(f"[red]Meilisearch didn't answer within {MEILISEARCH_RECOVERY_SECONDS} s[/red]")
                return False
            if not waited:
                console.print("[yellow]Waiting for Meilisearch to answer again...[/yellow]")
                waited = True
            time.sleep(2)

    def apply_settings_if_changed(self, index: Index, current: Dict[str, Any]) -> None:
        """Update the live index's settings (current) only where they differ from INDEX_SETTINGS"""
        changes = settings_to_update(current, INDEX_SETTINGS)
        if not changes:
            console.print("✅ Index settings unchanged")
            return
        console.print(f"🔧 Updating index settings: {', '.join(sorted(changes))}")
        self.wait_for_task(index.update_settings(changes), "update index settings")
        console.print("✅ Index settings configured")
    
    def process_file(self, file_path: Path) -> List[Dict]:
        """Process a single markdown file into documents"""
        try:
            # Process with document processor (it reads the file internally)
            documents = self.document_processor.process_document(str(file_path))
            return documents
                
        except Exception as e:
            console.print(f"[red]Error processing {escape(printable_path(file_path))}: {escape(str(e))}[/red]")
            self.stats['errors'] += 1
            return []
    
    def add_documents_batch(self, index: Index, documents: List[Dict[str, Any]]) -> None:
        """
        Send one batch and wait for it, in full and incremental mode alike: its files'
        hashes are saved only once every batch has been indexed.

        Raises:
            TaskFailedError: Meilisearch didn't index the batch
        """
        self.wait_for_task(index.add_documents(documents), f"add {len(documents)} documents")
    
    def run(self, limit: Optional[int] = None, dry_run: bool = False, force: bool = False) -> int:
        """
        Run the indexing process
        
        Args:
            limit: Maximum number of files to process (for testing)
            dry_run: If True, don't actually index documents
            force: If True, rebuild the whole index (by swap) whatever the hashes say

        Returns:
            The exit code. 0 when every Meilisearch task succeeded: files that can't be
            indexed are logged, counted and left out, so one bad file can't fail every
            future run. 1 when a task failed, Meilisearch couldn't be reached, a safety
            check failed (an incomplete image, too few documents in a new index) or the
            hash file couldn't be saved: the run stops there and saves no hashes, so the
            next run indexes the same files again (an update records the files it sends
            as pending first, so one removed since has its documents deleted), and the
            live index keeps serving.
            Also 1 when a due rebuild failed before its swap: the live index is then
            updated in place instead (new, changed and removed files), and the next run
            retries the rebuild.
        """
        try:
            self._run(limit=limit, dry_run=dry_run, force=force)
        except RebuildFailedError as e:
            self.print_summary()
            console.print(f"\n[red]✗ Rebuild failed: {escape(str(e))}[/red]")
            console.print("[red]  The live index was updated in place instead; the next run retries the rebuild[/red]")
            return 1
        except (TaskFailedError, CheckFailedError, BuildFailedError, MeilisearchError, OSError) as e:
            # The cause comes last, after the summary, where a reader looks first
            self.print_summary()
            console.print(f"\n[red]✗ Indexing aborted: {escape(str(e))}[/red]")
            console.print("[red]  No hashes saved: the next run indexes these files again[/red]")
            return 1
        return 0

    def _run(self, limit: Optional[int], dry_run: bool, force: bool) -> None:
        """The indexing run (see run). Raises on a failed task or check."""
        if force:
            console.print("\n[bold]Apple Documentation Meilisearch Indexer - Full Rebuild Mode[/bold]\n")
            console.print(f"[yellow]⚠️  This rebuilds the entire index in '{escape(self.build_index_name)}' "
                          f"and swaps it in; the live index keeps serving until then[/yellow]")
        else:
            console.print("\n[bold]Apple Documentation Meilisearch Indexer[/bold]\n")
            console.print("🔍 Checking for documentation updates...")
        
        # Discover files
        console.print("🔍 Discovering markdown files...")
        all_files = self.discover_markdown_files()
        file_count = len(all_files)
        self.stats['total_files'] = file_count
        
        # Count files by framework
        framework_counts: Dict[str, int] = defaultdict(int)
        for file_path in all_files:
            parts = file_path.relative_to(self.docs_path).parts
            if parts:
                framework = parts[0]
                framework_counts[framework] += 1
        
        console.print(f"📁 Found {file_count} markdown files across {len(framework_counts)} frameworks")
        console.print(f"   Top frameworks: {', '.join(f'{escape(k)}:{v}' for k, v in sorted(framework_counts.items(), key=lambda x: x[1], reverse=True)[:5])}")
        
        files = all_files
        if limit:
            files = all_files[:limit]
            console.print(f"[yellow]Limited to {limit} files[/yellow]")

        stored_hashes, state = self.load_hashes()
        console.print(f"\n📋 Existing hashes: {len(stored_hashes)} files")

        if dry_run:
            # No Meilisearch: process and validate what an update would send
            hashes = self.hash_files(files)
            to_index = self.changed_files(files, hashes, {} if force else stored_hashes)
            self.stats['skipped'] = len(hashes) - len(to_index)
            self.index_files(None, to_index, hashes)
            console.print(f"\n[yellow]Dry run: Would index {self.stats['chunks_created']} documents[/yellow]")
        else:
            self.index_or_rebuild(all_files, files, stored_hashes, state, force)

        self.print_summary()
        left_out = self.stats['errors'] + self.stats['invalid']
        if left_out:
            console.print(f"[yellow]⚠️  {left_out} file(s) left out of the index (errors above); "
                          f"they are retried on the next run[/yellow]")

    def changed_files(self, files: List[Path], hashes: Dict[str, str],
                      stored_hashes: Dict[str, str]) -> List[Path]:
        """The read files whose content isn't the stored one (new or changed)"""
        changed = []
        for file_path in files:
            key = self.relative_key(file_path)
            if key in hashes and stored_hashes.get(key) != hashes[key]:
                changed.append(file_path)
        return changed

    def index_or_rebuild(self, all_files: List[Path], files: List[Path], stored_hashes: Dict[str, str],
                         state: Dict[str, Any], force: bool) -> None:
        """
        Update the live index, or rebuild it when a rebuild is due (or forced). A due
        rebuild that fails before its swap, or is not started for lack of disk for a
        second index, is followed by the update, so a rebuild that keeps failing never
        stops new docs and Apple's removals from reaching search.

        Raises:
            RebuildFailedError: The rebuild failed and the update was applied instead
        """
        file_count = len(all_files)
        live = self.get_index(self.index_name)
        live_docs = self.document_count(self.index_name) if live else 0
        if live:
            console.print(f"📚 Live index '{escape(self.index_name)}': {live_docs:,} documents, "
                          f"created {escape(str(live.get('createdAt')))}")

        # Nothing is written before the image is known to be complete
        self.check_image(file_count, live_docs)

        live_settings: Dict[str, Any] = self.client.index(self.index_name).get_settings() if live else {}
        reason = "--force" if force else self.rebuild_reason(live, state, live_settings)
        hashes = self.hash_files(files)
        to_index = self.changed_files(files, hashes, stored_hashes)
        present = {self.relative_key(f) for f in all_files}
        removed = sorted(key for key in stored_hashes if key not in present)
        if reason is None:
            changed = len(to_index) + len(removed)
            if changed > REBUILD_CHANGED_FRACTION * file_count:
                reason = (f"{changed:,} of {file_count:,} files changed "
                          f"(more than {REBUILD_CHANGED_FRACTION:.0%})")

        # Every document of an index this indexer built carries index_gen (the hash file
        # records a processor version); one without it was added by an older indexer since
        older_documents = state.get("processor_version") is not None

        if live is not None and reason is None:
            console.print(f"Mode: Incremental update ({len(to_index):,} new or changed files, "
                          f"{len(removed):,} removed)")
            self.update(all_files, to_index, removed, hashes, stored_hashes, str(live.get('createdAt')),
                        live_settings, reindex_older=older_documents)
            return

        console.print(f"Mode: Rebuild by swap ({escape(str(reason))})")
        if live is not None and len(files) < file_count:
            raise CheckFailedError(
                f"--limit would swap in an index of {len(files):,} of the {file_count:,} files in place "
                f"of the whole live index: a rebuild with --limit is only done on a fresh index. "
                f"Nothing was swapped, added or deleted"
            )
        stats_before = dict(self.stats)
        try:
            self.rebuild(files, hashes, live is not None, live_docs)
        except BuildFailedError as e:
            if live is None or force:
                raise
            # The live index and its hash file are as they were, and an update never
            # deletes a current file's documents (the image is complete): apply it, and
            # record the rebuild as still due (the update saves that before it changes
            # anything), so every start retries it until it succeeds
            console.print(f"[red]✗ Rebuild failed before its swap: {escape(str(e))}[/red]")
            # A crashed or OOM-killed Meilisearch is back within seconds (supervisord): wait
            # for it, or the update would fail too and no change would reach search
            self.wait_until_available()
            console.print(f"Mode: Incremental update instead ({len(to_index):,} new or changed files, "
                          f"{len(removed):,} removed); the live index keeps serving")
            self.stats.update(stats_before)  # count the update, not the abandoned build
            still_due = {"processor_version": state.get("processor_version"),
                         "rebuild_due": str(state.get("rebuild_due") or reason)}
            # It can re-index more than REBUILD_CHANGED_FRACTION of the files in place, after
            # a rebuild skipped or stopped for lack of disk: it stops at the build's floor too
            self.update(all_files, to_index, removed, hashes, stored_hashes, str(live.get('createdAt')),
                        live_settings, still_due, reindex_older=older_documents,
                        disk_floor_path=meilisearch_db_path())
            raise RebuildFailedError(str(e)) from e

    def hash_files(self, files: List[Path]) -> Dict[str, str]:
        """
        Content hash of each file, by hash-file key. A file that can't be read is logged,
        counted and left out.
        """
        hashes: Dict[str, str] = {}
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("{task.completed}/{task.total}"),
            console=console
        ) as progress:
            task = progress.add_task("Checking files...", total=len(files))
            for file_path in files:
                try:
                    hashes[self.relative_key(file_path)] = self.compute_file_hash(file_path)
                except OSError as e:
                    console.print(f"[red]Error reading {escape(printable_path(file_path))}: {escape(str(e))}[/red]")
                    self.stats['errors'] += 1
                progress.update(task, advance=1)
        return hashes

    def index_files(self, index: Optional[Index], files: List[Path],
                    hashes: Dict[str, str], after_batch: Optional[Callable[[], None]] = None) -> Dict[str, str]:
        """
        Process the files and send their documents in batches (none when index is None,
        a dry run), stamped with this run's index_gen.

        Args:
            after_batch: Called after each batch has been indexed (it may raise to stop)

        Returns:
            The hashes of the files whose documents were all sent
        """
        new_hashes: Dict[str, str] = {}
        pending_batch: List[Dict[str, Any]] = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("{task.completed}/{task.total}"),
            TimeRemainingColumn(),
            console=console
        ) as progress:

            task = progress.add_task("Processing files...", total=len(files))

            for file_path in files:
                relative_path = file_path.relative_to(self.docs_path)

                documents = self.process_file(file_path)
                # A document Meilisearch would reject fails its whole batch: leave the
                # file out (no hash recorded, so it's tried again on the next run)
                problem = find_invalid_document(documents) if documents else None
                if problem:
                    console.print(f"[red]Skipping {escape(printable_path(relative_path))}: {escape(problem)}[/red]")
                    self.stats['invalid'] += 1
                elif documents:
                    for document in documents:
                        document[INDEX_GEN_ATTRIBUTE] = self.index_gen
                    pending_batch.extend(documents)
                    new_hashes[str(relative_path)] = hashes[str(relative_path)]
                    self.stats['processed'] += 1
                    self.stats['chunks_created'] += len(documents)

                    # Send batch to Meilisearch when it's full (memory-efficient)
                    if len(pending_batch) >= self.batch_size:
                        if index is not None:
                            self.add_documents_batch(index, pending_batch)
                            if after_batch is not None:
                                after_batch()
                        pending_batch = []

                    # Log progress for debugging
                    if self.stats['processed'] % 1000 == 0:
                        console.print(f"[dim]Processed {self.stats['processed']} files, created {self.stats['chunks_created']} documents[/dim]")

                progress.update(task, advance=1)

        # Index remaining documents
        if pending_batch and index is not None:
            self.add_documents_batch(index, pending_batch)
            if after_batch is not None:
                after_batch()
        return new_hashes

    def delete_old_documents(self, index: Index, file_paths: List[str]) -> None:
        """
        Delete the documents of these file_path values that this run didn't send:
        documents of removed files, and documents a re-indexed file no longer has (fewer
        chunks, a chunked file that became one document or the reverse). Only called once
        every add of the run has succeeded, so a file is never missing from search.
        """
        for start in range(0, len(file_paths), MAX_FILTER_VALUES):
            chunk = file_paths[start:start + MAX_FILTER_VALUES]
            task = self.wait_for_task(
                index.delete_documents(filter=(
                    f"file_path IN [{', '.join(quote_filter_value(value) for value in chunk)}] "
                    f"AND {INDEX_GEN_ATTRIBUTE} != {quote_filter_value(self.index_gen)}"
                )),
                f"delete old documents of {len(chunk)} files"
            )
            self.stats['documents_deleted'] += int((task.details or {}).get('deletedDocuments') or 0)

    def rebuild(self, files: List[Path], hashes: Dict[str, str], live_exists: bool, live_docs: int) -> None:
        """
        Build the whole index into the build index and swap it in (rename it on a fresh
        volume). The live index serves every search until the swap, and is untouched by
        any failure before it. Over a live index, the build starts only when the disk has
        room for it, and stops when the disk fills up (check_disk_for_build).

        Raises:
            BuildFailedError: A task, check or request failed before the swap
        """
        build = self.build_index_name
        file_count = len(files)  # the files this run indexes (fewer with --limit)
        swapped = False
        try:
            if self.index_exists(build):
                console.print(f"[yellow]Deleting '{escape(build)}' left by an unfinished rebuild[/yellow]")
                self.wait_for_task(self.client.delete_index(build), f"delete index '{build}'")
            if live_exists:
                # After the leftover's deletion, which frees its disk at once (v1.49)
                self.check_disk_for_build()
            self.wait_for_task(self.client.create_index(build, {'primaryKey': 'id'}), f"create index '{build}'")
            console.print(f"[green]Created index '{escape(build)}'[/green]" + (
                " (the live index keeps serving until the swap)" if live_exists else
                f" (renamed to '{escape(self.index_name)}' when complete)"))
            build_index = self.client.index(build)
            console.print("🔧 Configuring index settings...")
            self.wait_for_task(build_index.update_settings(INDEX_SETTINGS), "configure index settings")
            console.print("✅ Index settings configured")

            console.print(f"\n🔄 Full rebuild - processing all {len(hashes)} files")
            new_hashes = self.index_files(build_index, [f for f in files if self.relative_key(f) in hashes], hashes,
                                          after_batch=self.check_disk_during_build)
            console.print(f"\n[green]✓ Indexed {self.stats['chunks_created']} documents[/green]")

            built = self.document_count(build)
            if built < MIN_INDEXED_FRACTION * file_count:
                raise CheckFailedError(
                    f"the new index has {built:,} documents for {file_count:,} files (under "
                    f"{MIN_INDEXED_FRACTION:.0%}): not swapped in, the live index keeps serving"
                )
            if expected_file_count() is None and built < MIN_INDEXED_FRACTION * live_docs:
                raise CheckFailedError(
                    f"the new index has {built:,} documents, the live index {live_docs:,} (under "
                    f"{MIN_INDEXED_FRACTION:.0%}), and no DOC_FILE_COUNT to tell a removal from a "
                    f"truncated image: not swapped in, the live index keeps serving"
                )

            if live_exists:
                self.wait_for_task(self.client.swap_indexes([{"indexes": [self.index_name, build]}]),
                                   f"swap '{build}' with '{self.index_name}'")
                swapped = True
                console.print(f"[green]✓ Swapped the new index in as '{escape(self.index_name)}' "
                              f"({built:,} documents)[/green]")
                # The old index now has the build's name
                self.wait_for_task(self.client.delete_index(build), f"delete the old index (now '{build}')")
            else:
                # A swap needs both indexes; rename needs the target to be missing
                self.wait_for_task(
                    self.client.swap_indexes([{"indexes": [build, self.index_name], "rename": True}]),
                    f"rename '{build}' to '{self.index_name}'"
                )
                swapped = True
                console.print(f"[green]✓ Renamed the new index to '{escape(self.index_name)}' "
                              f"({built:,} documents)[/green]")
        except (TaskFailedError, CheckFailedError, MeilisearchError) as e:
            self.discard_build_index()
            if swapped:
                raise
            raise BuildFailedError(str(e)) from e
        except Exception:
            self.discard_build_index()
            raise
        finally:
            self.build_db_path = None

        live = self.get_index(self.index_name)
        if live is None:
            raise CheckFailedError(f"'{self.index_name}' is missing after the swap")

        # Every task so far succeeded: record the run, then save the hashes last (bound to
        # the new index), so a failure before this point rebuilds again on the next run
        self.update_metadata(content_changed=True, force_rebuild=True)
        self.save_hashes(new_hashes, str(live.get('createdAt')))

    def files_by_filter_key(self, all_files: List[Path], keys: Set[str]) -> Dict[str, List[Path]]:
        """The current files whose file_path a filter compares as one of keys (filter_key)"""
        files_by_key: Dict[str, List[Path]] = defaultdict(list)
        if keys:
            for file_path in all_files:
                key = filter_key(self.file_path_value(self.relative_key(file_path)))
                if key in keys:
                    files_by_key[key].append(file_path)
        return files_by_key

    def older_document_paths(self, index: Index) -> List[str]:
        """
        The file_path of every document in the index without index_gen: documents an
        older indexer (a rollback) added. index_gen must be filterable.
        """
        paths: Set[str] = set()
        offset = 0
        while True:
            results = index.get_documents({
                "filter": f"{INDEX_GEN_ATTRIBUTE} NOT EXISTS",
                "fields": ["file_path"],
                "limit": UNSTAMPED_FETCH_LIMIT,
                "offset": offset,
            })
            documents = [dict(document) for document in results.results]
            paths.update(str(document["file_path"]) for document in documents if document.get("file_path"))
            offset += len(documents)
            if not documents or offset >= int(results.total):
                return sorted(paths)

    def update(self, all_files: List[Path], to_index: List[Path], removed: List[str],
               hashes: Dict[str, str], stored_hashes: Dict[str, str], created_at: str,
               live_settings: Dict[str, Any], still_due: Optional[Dict[str, Any]] = None,
               reindex_older: bool = False, disk_floor_path: Optional[Path] = None) -> None:
        """
        Update the live index in place: add the new and changed files' documents, then
        delete the documents they no longer have and those of removed files.

        Args:
            live_settings: The live index's current settings
            still_due: Saved with the hashes after a failed rebuild (see save_hashes)
            reindex_older: The index was built by this indexer (the hash file records a
                processor version), so a document without index_gen was added by an older
                indexer since (a rollback): its file is indexed again and those documents
                are deleted
            disk_floor_path: Meilisearch's database directory, after a failed rebuild: the
                update stops before its first batch, or between two, when the free space
                on its disk is under BUILD_DISK_FLOOR (a CheckFailedError; no hash is saved
                for the files not indexed, and the live index keeps serving)
        """
        def check_disk() -> None:
            self.check_disk_floor(disk_floor_path, "during the update",
                                  "The update was stopped before its next batch")

        # Before anything changes the live index
        check_disk()
        index = self.client.index(self.index_name)

        # Filters compare file_path normalized (case, Unicode forms), so a delete for one
        # path also deletes the documents of a file whose path compares the same. Every
        # current file with a path touched here is indexed again, so the deletes, which
        # keep this run's documents, spare it.
        touched = ({filter_key(self.file_path_value(self.relative_key(f))) for f in to_index}
                   | {filter_key(self.file_path_value(key)) for key in removed})
        files_by_key = self.files_by_filter_key(all_files, touched)
        reindex = sorted({f for group in files_by_key.values() for f in group
                          if self.relative_key(f) in hashes} | set(to_index))
        if len(reindex) > len(to_index):
            console.print(f"Also re-indexing {len(reindex) - len(to_index)} unchanged file(s) whose "
                          f"file_path a filter can't tell from a changed or removed one")

        # Saved before anything changes the live index: the files about to be sent as
        # pending (see PENDING_HASH), and after a failed rebuild the rebuild as still due
        # (the settings below make index_gen filterable again, which would hide an older
        # indexer's run if the update then stopped)
        pending = {self.relative_key(f): PENDING_HASH for f in reindex}
        if pending or still_due:
            self.save_hashes({**stored_hashes, **pending}, created_at, still_due, log=False)

        # Before any delete: they filter on index_gen
        self.apply_settings_if_changed(index, live_settings)

        # An older indexer (a rollback) adds a changed file's documents without index_gen
        # and deletes nothing, so its old documents stay beside them, and the hash file it
        # saved calls the file indexed. The rebuild a return to this indexer starts clears
        # them; until one succeeds, those files are indexed again here, and the sweep below
        # deletes both their older indexer's documents and the stale ones. A document whose
        # file is gone is deleted with it (the image is complete).
        stray_values: List[str] = []
        if reindex_older:
            older = {filter_key(value): value for value in self.older_document_paths(index)}
            new_keys = set(older) - touched
            if new_keys:
                touched |= new_keys
                files_by_key.update(self.files_by_filter_key(all_files, new_keys))
                # (touched holds the removed files' keys already)
                stray_values = sorted(older[key] for key in new_keys if not files_by_key[key])
                more = sorted({f for key in new_keys for f in files_by_key[key]
                               if self.relative_key(f) in hashes} - set(reindex))
                console.print(f"Also re-indexing {len(more)} file(s), and deleting the documents of "
                              f"{len(stray_values)} file(s) no longer here, that an older indexer added "
                              f"documents for (a rollback)")
                if more:
                    reindex = sorted(set(reindex) | set(more))
                    pending.update({self.relative_key(f): PENDING_HASH for f in more})
                    self.save_hashes({**stored_hashes, **pending}, created_at, still_due, log=False)

        self.stats['skipped'] = len(hashes) - len(reindex)
        new_hashes = self.index_files(index, reindex, hashes, after_batch=check_disk)
        if new_hashes:
            console.print(f"\n[green]✓ Indexed {self.stats['chunks_created']} documents[/green]")
        else:
            console.print("\n[green]No new or changed documents to index[/green]")

        # A path whose files weren't all indexed this run keeps its documents (deleting
        # them would take that file out of search): retried on the next run
        complete = {key for key in touched
                    if all(self.relative_key(f) in new_hashes for f in files_by_key[key])}
        deleted_removed = [key for key in removed if filter_key(self.file_path_value(key)) in complete]
        values = sorted({self.file_path_value(self.relative_key(f)) for key in complete for f in files_by_key[key]}
                        | {self.file_path_value(key) for key in deleted_removed}
                        | set(stray_values))
        if values:
            self.delete_old_documents(index, values)
            console.print(f"🧹 Deleted {self.stats['documents_deleted']} old documents "
                          f"({len(deleted_removed)} removed files)")
        held = len(removed) - len(deleted_removed)
        if held:
            console.print(f"[yellow]Kept the documents of {held} removed file(s) whose file_path compares "
                          f"the same as a file left out this run; retried on the next run[/yellow]")
        self.stats['removed'] = len(deleted_removed)

        # Every task so far succeeded: record the run, then save the hashes last, so
        # a failure before this point leaves the files to be indexed again
        self.update_metadata(content_changed=bool(new_hashes or deleted_removed or stray_values), force_rebuild=False)
        if pending or deleted_removed:
            # Removed files' keys are dropped, so their deletes aren't sent again. A file
            # left out this run had none of its documents sent: it keeps its stored entry
            gone = set(deleted_removed)
            kept = {key: value for key, value in stored_hashes.items() if key not in gone}
            self.save_hashes({**kept, **new_hashes}, created_at, still_due)

    def discard_build_index(self) -> None:
        """
        Best effort, after a failed rebuild: free the build index's disk space now (once
        Meilisearch answers again, if the failure was that it went down)
        """
        try:
            self.wait_until_available()
            if self.index_exists(self.build_index_name):
                self.wait_for_task(self.client.delete_index(self.build_index_name),
                                   f"delete index '{self.build_index_name}'")
                console.print(f"[yellow]Deleted the unfinished '{escape(self.build_index_name)}'[/yellow]")
        except (TaskFailedError, MeilisearchError) as e:
            console.print(f"[yellow]Could not delete '{escape(self.build_index_name)}' "
                          f"(the next rebuild deletes it first): {escape(str(e))}[/yellow]")
    
    def update_metadata(self, content_changed: bool = True, force_rebuild: bool = False) -> None:
        """
        Store metadata about the indexing run in Meilisearch.

        Raises:
            TaskFailedError: The meta index couldn't be created or written
            MeilisearchError: The stored metadata couldn't be read (other than not found)
        """
        meta_index_name = f"{self.index_name}-meta"

        # Create the metadata index on first use
        if not self.index_exists(meta_index_name):
            self.wait_for_task(
                self.client.create_index(meta_index_name, {'primaryKey': 'id'}),
                f"create index '{meta_index_name}'"
            )

        meta_index = self.client.index(meta_index_name)

        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")

        # Get existing metadata to preserve values if appropriate
        existing: Dict[str, Any] = {}
        try:
            doc = meta_index.get_document("index_metadata")
            # get_document returns Document object, not dict - must convert
            existing = dict(doc) if doc else {}
        except MeilisearchApiError as e:
            if e.code != "document_not_found":
                raise

        # Store metadata
        metadata = {
            "id": "index_metadata",
            "last_indexed": now,  # When indexing completed
            "last_updated": now if content_changed else existing.get("last_updated"),
            # last_index_full: Only set by a rebuild (when its index was swapped in)
            "last_index_full": now if force_rebuild else existing.get("last_index_full"),
            "documents_indexed": self.stats['chunks_created'],
            "files_processed": self.stats['processed'],
            "total_files": self.stats['total_files']
        }

        self.wait_for_task(meta_index.add_documents([metadata]), f"write '{meta_index_name}'")
        console.print(f"[green]✓ Updated index metadata[/green]")

    def print_summary(self) -> None:
        """Print indexing summary"""
        duration = time.time() - self.stats['start_time']

        table = Table(title="Indexing Summary", show_header=False)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Total Files", str(self.stats['total_files']))
        table.add_row("Files Processed", str(self.stats['processed']))
        table.add_row("Files Skipped", str(self.stats['skipped']))
        table.add_row("Files Removed", str(self.stats['removed']))
        table.add_row("Documents Created", str(self.stats['chunks_created']))
        table.add_row("Documents Deleted", str(self.stats['documents_deleted']))
        table.add_row("Errors", str(self.stats['errors']) if self.stats['errors'] == 0 else f"[red]{self.stats['errors']}[/red]")
        table.add_row("Invalid (left out)", str(self.stats['invalid']) if self.stats['invalid'] == 0 else f"[red]{self.stats['invalid']}[/red]")
        table.add_row("Duration", f"{duration:.2f} seconds")
        
        if self.stats['processed'] > 0:
            rate = self.stats['processed'] / duration
            table.add_row("Processing Rate", f"{rate:.1f} files/second")
        
        console.print("\n")
        console.print(table)


def main() -> None:
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Index Apple Developer Documentation to Meilisearch"
    )
    parser.add_argument(
        "--url",
        default=os.getenv("MEILI_HTTP_ADDR", "http://localhost:7700"),
        help="Meilisearch URL (default: http://localhost:7700 or MEILI_HTTP_ADDR env)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv("MEILI_MASTER_KEY", ""),
        help="Meilisearch API key (default: MEILI_MASTER_KEY env)"
    )
    parser.add_argument(
        "--docs-path",
        default="../documentation",
        help="Path to documentation directory (default: ../documentation)"
    )
    parser.add_argument(
        "--index",
        default="apple-docs",
        help="Meilisearch index name (default: apple-docs)"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=10000,
        help="Batch size for indexing (default: 10000)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of files to process (for testing; a rebuild with it is only done on a fresh index)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Process files but don't index to Meilisearch"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild the whole index now (built beside the live index and swapped in), ignoring hash cache"
    )
    parser.add_argument(
        "--hash-file",
        help="Path to store file hashes for incremental updates (default: auto-detect)"
    )

    args = parser.parse_args()

    # Determine hash file location
    # In Docker, use /data/logs/ for persistence across container restarts
    # Locally, use ../.hashes/ relative to scripts directory
    if args.hash_file:
        hash_file = args.hash_file
    elif Path("/data/logs").exists():
        # Running in Docker
        hash_file = "/data/logs/meilisearch_hashes.json"
    else:
        # Running locally
        hash_file = str(Path(__file__).parent.parent / ".hashes" / "meilisearch_hashes.json")
    
    # Validate Meilisearch connection
    if not args.dry_run:
        try:
            client = meilisearch.Client(args.url, args.api_key)
            health = client.health()
            console.print(f"[green]✓ Connected to Meilisearch at {escape(args.url)}[/green]")
        except Exception as e:
            console.print(f"[red]✗ Could not connect to Meilisearch at {escape(args.url)}: {escape(str(e))}[/red]")
            console.print("[yellow]Make sure Meilisearch is running and accessible[/yellow]")
            sys.exit(1)
    
    # Run indexer
    indexer = MeilisearchIndexer(
        meilisearch_url=args.url,
        api_key=args.api_key,
        docs_path=args.docs_path,
        index_name=args.index,
        batch_size=args.batch_size,
        hash_file=hash_file
    )

    console.print(f"[dim]Hash file: {escape(hash_file)}[/dim]")
    
    sys.exit(indexer.run(limit=args.limit, dry_run=args.dry_run, force=args.force))


if __name__ == "__main__":
    main()