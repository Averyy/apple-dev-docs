"""JSON-based Apple documentation scraper that uses Apple's data endpoints."""

import asyncio
import copy
import json
import re
import time
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Deque, Dict, Final, List, Literal, Optional, Sequence, Set, Tuple, Union
from urllib.parse import urlparse

from scraper.base import NOT_MODIFIED, BaseAppleScraper, FetchFailed
from scraper.config import Config
from scraper.sink import HANDOFF_KEY, MODULE_KEY, Sink, SinkRegistry, metadata_ids, module_parents
from scraper.site import APPLE, DocCSite
from scraper.utils.assets import hosting_root, variant_url
from scraper.utils.hash_manager import COUNTER_FIELDS, HashManager, same_name_any_case, write_text_atomic
from scraper.utils.links import doc_link, link_base
from scraper.utils.logger import get_logger
from scraper.utils.markdown_converter import AppleDocMarkdownConverter, join_blocks, labeled, quote_blocks
from scraper.utils.naming import clash_suffix, page_path, seg_name

logger = get_logger(__name__)

# The JSON the converter renders: the block and inline types that
# _process_content_items and _resolve_inline_content render (exactly these,
# pinned by a test) and the section kinds read. Any other is rendered as its
# text (_fallback_blocks) and logged (unknown_content), once per type and
# framework with its count. In such an unknown item, these tables also tell
# a list of blocks from one of inline content
KNOWN_BLOCK_TYPES: Final = frozenset({
    'paragraph', 'heading', 'codeListing', 'unorderedList', 'orderedList',
    'table', 'aside', 'imageBlock', 'termList', 'thematicBreak',
    'tabNavigator', 'row', 'links', 'video',
})
KNOWN_INLINE_TYPES: Final = frozenset({
    'text', 'reference', 'codeVoice', 'emphasis', 'strong', 'image', 'strikethrough',
})
KNOWN_SECTION_KINDS: Final = frozenset({
    'declarations', 'content', 'discussion', 'returnValue', 'task', 'restBody',
    'restResponses', 'possibleValues', 'thrown_errors', 'details', 'attributes',
    'properties', 'restEndpoint', 'restParameters', 'parameters', 'mentions',
})
# Top-level and metadata keys: those read, and those ignored on purpose. Any
# other is only logged (unknown_content)
KNOWN_TOP_LEVEL_KEYS: Final = frozenset({
    'metadata', 'abstract', 'primaryContentSections', 'topicSections',
    'seeAlsoSections', 'relationshipsSections', 'defaultImplementationsSections',
    'references', 'variantOverrides', 'deprecationSummary', 'sampleCodeDownload',
    'diffAvailability', 'variants', 'hierarchy',
    # Ignored on purpose
    'identifier', 'kind', 'schemaVersion', 'legalNotices', 'sections',
    'documentVersion', 'legacy_identifier', 'topicSectionsStyle',
})
KNOWN_METADATA_KEYS: Final = frozenset({
    'title', 'externalID', 'symbolKind', 'navigatorTitle', 'roleHeading',
    'required', 'modules', 'fragments', 'platforms', 'conformance',
    # Ignored on purpose
    'role', 'availableLanguages', 'extendedModule', 'parent', 'images', 'color',
    'customMetadata', 'defaultSuggestedTags',
})

# A sample code download's relative URL (<hash>/<name>.zip) is served here
DOCS_ASSETS_URL: Final = "https://docs-assets.developer.apple.com/published/"

# A doc:// link written as text in Apple's prose: up to the first whitespace or
# ">" (parentheses occur inside them); a trailing ".", "," or ";" is the prose's
DOC_LITERAL: Final = re.compile(r'doc://[^/\s>]+/[^\s>]*')

# A page's Objective-C/C declarations (interfaceLanguage occ) are fenced as
# objc when one shows Objective-C syntax, else cpp when one shows C++, else c
OBJC_MARKERS: Final = re.compile(
    r'^\s*[-+]\s*\(|@(?:interface|protocol|property|class|optional|required|end)\b', re.MULTILINE)
CPP_MARKERS: Final = re.compile(
    r'::|\b(?:virtual|template|class|namespace|typename|operator|constexpr|override|explicit)\b')

# Declaration fences: Swift first, the Objective-C/C variant last
DECLARATION_ORDER: Final = {'swift': 0, 'occ': 2}

# Attribute kinds of a property, parameter or key, with their labels
ATTRIBUTE_LABELS: Final = {
    'default': 'Default',
    'minimum': 'Minimum',
    'minimumExclusive': 'Minimum (exclusive)',
    'maximum': 'Maximum',
    'maximumExclusive': 'Maximum (exclusive)',
    'minimumLength': 'Minimum Length',
    'maximumLength': 'Maximum Length',
}


def apply_json_patch(document: Any, patch: List[Dict[str, Any]]) -> Any:
    """An RFC 6902 patch's add, replace and remove operations applied to a copy of document.

    The containers along each operation's path are copied and every value is
    deep-copied, so document is never changed. Paths are JSON pointers ("~1"
    for "/", "~0" for "~"); "" is the whole document.

    Raises:
        KeyError, IndexError, ValueError, TypeError: A path doesn't exist in
            the document, or an operation isn't one of these three
    """
    copied: Set[int] = set()  # containers of the result that are already copies

    def copy_of(container: Any) -> Any:
        if id(container) in copied:
            return container
        fresh = list(container) if isinstance(container, list) else dict(container)
        copied.add(id(fresh))
        return fresh

    root = document
    for operation in patch:
        op = operation.get('op')
        if op not in ('add', 'replace', 'remove'):
            raise ValueError(f"unsupported patch operation {op!r}")
        path = operation.get('path', '')
        tokens = [t.replace('~1', '/').replace('~0', '~') for t in path.split('/')[1:]] if path else []
        if not tokens:
            if op == 'remove':
                raise ValueError("can't remove the whole document")
            root = copy.deepcopy(operation.get('value'))
            continue
        root = copy_of(root)
        parent = root
        for token in tokens[:-1]:
            index: Any = int(token) if isinstance(parent, list) else token
            child = copy_of(parent[index])
            parent[index] = child
            parent = child
        last = tokens[-1]
        if isinstance(parent, list):
            position = len(parent) if last == '-' else int(last)
            if op == 'add':
                parent.insert(position, copy.deepcopy(operation.get('value')))
            elif op == 'replace':
                parent[position] = copy.deepcopy(operation.get('value'))
            else:
                del parent[position]
        elif isinstance(parent, dict):
            if op == 'remove':
                del parent[last]
            else:
                parent[last] = copy.deepcopy(operation.get('value'))
        else:
            raise TypeError(f"patch path {path!r} runs through a {type(parent).__name__}")
    return root


# 404/410: Apple removed the page. A removal, never a block.
GONE_STATUSES: Final = (404, 410)

# A 200 whose body is not JSON is treated as a transient fetch failure.
INVALID_JSON: Final = "invalid json"

# A page's fetch failure (D8) or local error counts once per framework run; at
# this many consecutive runs it stops blocking cleanup and flags the run.
PERSISTENT_FAILURE_RUNS: Final = 3

# More fetch failures in one run than max(5, 1% of the framework's pages) is a
# failure storm: they block but aren't counted, unless the storm lasts
# FAILURE_STORM_RUNS consecutive runs.
FAILURE_STORM_MIN: Final = 5
FAILURE_STORM_SHARE: Final = 0.01
FAILURE_STORM_RUNS: Final = 3

# How a page's fetch failed this run (see _handle_fetch_failure):
# previously_good: a page with a live entry failed; it is kept and touched.
# after_304: a 304 proved the page live, then its discovery refetch failed.
# never_good: a transient failure on a URL with no live entry.
FailureKind = Literal["previously_good", "after_304", "never_good"]


@dataclass(frozen=True)
class PageFetchFailure:
    """A page fetch failure of this run that counts toward D8."""

    kind: FailureKind
    failure: FetchFailed


# The sections whose identifiers a page links its child pages through. A
# protocol requirement's defaultImplementationsSections list its default
# implementations, which no other section links (1.4); those in another
# top-level technology of the bundle are handed off to its sink (_route)
LINK_SECTIONS: Final = (
    'topicSections', 'relationshipsSections', 'seeAlsoSections', 'defaultImplementationsSections',
    'diffAvailability', 'variants',
)


@dataclass(frozen=True)
class PageLink:
    """A page's link to a documentation page, as the reference resolver makes it (1.1).

    Attributes:
        json_url: The target's JSON URL, from its reference's URL
            (references[id].url): fragment stripped, lowercased, dot
            segments escaped
        segment: Its first path segment, lowercased: the sink it goes to (D6)
        dir_name: That segment as the identifier cases it: a new sink's dir
        bundle: The identifier's bundle, lowercased (e.g. com.apple.sirikit)
        identifier: The doc:// identifier
    """

    json_url: str
    segment: str
    dir_name: str
    bundle: str
    identifier: str


@dataclass(frozen=True)
class PageLinks:
    """A page's outgoing links and its own bundle: what the scope rule reads (_in_scope)."""

    bundle: str
    links: Tuple[PageLink, ...]


@dataclass
class OrphanScan:
    """A framework's orphan candidates, computed right after its hash file was saved.

    The end-of-run cleanup works from these, so neither the scraper nor its
    hash manager (every entry of the framework) is kept until then.

    Attributes:
        framework_dir: The framework's docs dir (its output dir, or that dir
            in another casing)
        hash_file: The framework's hash file
        files: How many .md files the docs dir holds
        orphans: The orphan candidates: the .md files no entry this run
            touched records (HashManager.get_untouched_files)
        pending_orphans: metadata.pending_orphans as the run's save left it:
            the candidates an earlier clean run held for confirmation
        stale_errors: The error entries no page this run reached links to
            any more (stale_error_entries): the cleanup drops them
    """

    framework_dir: Path
    hash_file: Path
    files: int
    orphans: List[Path]
    pending_orphans: List[str]
    stale_errors: List[str] = field(default_factory=list)


@dataclass
class FrameworkOutcome:
    """What a framework run means for orphan cleanup and the run's exit code.

    Attributes:
        framework_id: The framework's id, as its output dir and hash file use it
        blocks: Why orphan cleanup must skip the framework this run (our own
            failed requests or errors), reason -> the URLs or messages
        persistent_fetch_failures: URLs whose fetch failed for the
            PERSISTENT_FAILURE_RUNS-th consecutive run (or more); they no
            longer block cleanup but flag the run
        persistent_local_errors: URLs whose convert/save failed for the
            PERSISTENT_FAILURE_RUNS-th consecutive run (or more); same
        filename_clashes: JSON URLs of pages whose file name another
            page's file already has (the naming isn't injective there):
            each was written under a hashed stem. They flag the run but
            never block cleanup, since a clash recurs every run
        root_fetch_failed: The root failed with something other than 404/410,
            or with a 404/410 after it answered 200/304 in this run (our
            failure: it blocks cleanup and never reaches D8)
        root_gone_runs: Consecutive runs the root returned 404/410, if it did
            this run and never answered 200/304 (else 0); cleanup skips the
            framework, which isn't our failure, until the end-of-run pass
            deletes it at 2
        failure_storm: Too many fetch failures this run (see FAILURE_STORM_*)
        raised: The error, if the framework's scrape raised
        stats: The scraper's stats
        orphan_scan: The framework's orphan candidates, for a framework the
            end-of-run cleanup may clean (see scan_orphans)
        handoff_writers: The other jobs its hash file records as writers
            (metadata.handoff_from, D6): its cleanup also needs each of them
            to have run clean this run (rule 1)
    """

    framework_id: str
    blocks: Dict[str, List[str]] = field(default_factory=dict)
    persistent_fetch_failures: List[str] = field(default_factory=list)
    persistent_local_errors: List[str] = field(default_factory=list)
    filename_clashes: List[str] = field(default_factory=list)
    root_fetch_failed: bool = False
    root_gone_runs: int = 0
    failure_storm: bool = False
    raised: Optional[str] = None
    stats: Dict[str, Any] = field(default_factory=dict)
    orphan_scan: Optional[OrphanScan] = None
    handoff_writers: List[str] = field(default_factory=list)

    def block(self, reason: str, detail: str) -> None:
        """Block this framework's orphan cleanup for this run."""
        details = self.blocks.setdefault(reason, [])
        if detail not in details:
            details.append(detail)

    @property
    def blocked(self) -> bool:
        """Cleanup is blocked by a failure of ours (an error for the run)."""
        return bool(self.blocks) or self.raised is not None

    @property
    def skip_cleanup(self) -> bool:
        """Orphan cleanup must leave this framework alone this run."""
        return self.blocked or self.root_gone_runs > 0


@dataclass
class ModuleScan:
    """A D6 module sink of this run, for the end-of-run cleanup (rules 1–4).

    Attributes:
        dir_name: Its docs dir's name
        output_dir: Its docs dir
        hash_file: Its hash file
        routed_by: The parents that routed it a page this run (rule 2: their
            counters reset)
        orphan_scan: Its orphan candidates from every writer's touched set
            (finish_run), with --cleanup-orphans
    """

    dir_name: str
    output_dir: Path
    hash_file: Path
    routed_by: Set[str]
    orphan_scan: Optional[OrphanScan] = None


@dataclass
class RunSinks:
    """What the end-of-run cleanup needs of the run's sinks (D6 rules 1–4).

    Attributes:
        listed: The ids this run's technologies.json lists (its full list,
            lowercased): a module whose id it lists is promoted
        modules: The run's module sinks
        module_files: The module hash files on disk at run start
        handoff_files: The top-level hash files that carried handoff_from
            at run start, or got it this run
        child_modules: Module id (lowercased) -> the hash files of the
            parents whose child_modules listed it at run start
    """

    listed: Set[str] = field(default_factory=set)
    modules: List[ModuleScan] = field(default_factory=list)
    module_files: List[Path] = field(default_factory=list)
    handoff_files: List[Path] = field(default_factory=list)
    child_modules: Dict[str, List[Path]] = field(default_factory=dict)


def doc_url_of(site: DocCSite, json_url: str) -> str:
    """A page's documentation URL, from its JSON URL on the site."""
    path = json_url.replace(site.json_prefix, '')
    if path.endswith('.json'):
        path = path[:-5]
    return site.doc_url(path)


class AppleJSONDocumentationScraper(BaseAppleScraper):
    """Scraper that uses Apple's JSON data endpoints instead of HTML pages."""
    
    # Base URL for JSON data: Apple's (site.APPLE), as the scripts that read
    # Apple hash files use it
    JSON_BASE_URL = APPLE.json_base
    # Root-relative image and video URLs ("/images/…") are served under it
    ASSET_ROOT = hosting_root(JSON_BASE_URL)
    # The converter's output version (BaseAppleScraper.RENDER_VERSION): bump
    # it when a change to the conversion, the file names or the links changes
    # the files of pages whose JSON didn't change, so every framework is
    # rendered again on its next clean run
    RENDER_VERSION = 1
    
    def __init__(self, framework_id: str, framework_name: Optional[str] = None, 
                 include_cross_refs: bool = False, sinks: Optional[SinkRegistry] = None) -> None:
        """Initialize JSON-based scraper.
        
        Args:
            framework_id: Framework identifier (e.g., 'swiftui', 'uikit')
            framework_name: Human-readable name (defaults to framework_id)
            include_cross_refs: Whether to include cross-framework references
            sinks: The run's sinks, shared by its framework jobs; they
                hold the docs dirs linked locally (SinkRegistry.known_dirs).
                A scraper on its own has its own, which knows no other dir
        """
        super().__init__(
            framework_id=framework_id,
            framework_name=framework_name or framework_id.replace('-', ' ').title()
        )
        # The framework's DocC site: every URL the scraper builds comes from it
        self.site = APPLE
        self.sinks = sinks if sinks is not None else SinkRegistry()
        # The job's id: its framework's, lowercased (a module's parent, a handoff writer)
        self.job_id = self.framework_id.lower()
        # The primary sink: the framework's own docs dir and hash file
        self.sink = self.sinks.get(self.site, self.framework_id, self.framework_name, self.RENDER_VERSION)
        self.sink.primary_ran = True
        self.sink.users.add(self.job_id)
        # Discovery: the URLs this job has queued (each once), and how the
        # links it followed case each other sink's dir and name its bundle
        self._queued: Set[str] = set()
        self._routes: Dict[str, Tuple[str, str]] = {}
        self._collisions: Set[str] = set()
        # Links with no reference, followed by their identifier's path
        self.reference_fallbacks = 0
        # The page being converted (_extract_from_json) and its sink: its
        # links are relative to its file
        self._current_scraping_url = ''
        self._current_sink = self.sink
        self.include_cross_refs = include_cross_refs
        self.cross_framework_refs: Dict[str, Set[str]] = {}  # Track cross-framework references
        # JSON the converter doesn't know, (what, name) -> count, logged at the end
        self._unknown_content: Counter[Tuple[str, str]] = Counter()
        self._unknown_examples: Dict[Tuple[str, str], str] = {}  # (what, name) -> a page's URL

        # Failure policy state for this run, applied once by scrape_framework
        # (the pages' own state is their sink's)
        self.root_json_url = f"{self.site.json_prefix}{self.framework_id}.json"
        self.outcome = FrameworkOutcome(framework_id=self.framework_id)
        self.sinks.outcomes[self.job_id] = self.outcome
        self._root_ok = False  # the root answered 200 or 304
        self._root_gone = False  # the root answered 404/410
        if self.sink.load_error is not None:
            # The hash file exists but loaded nothing, so this run can't tell
            # the pages we have from new ones. This run's save replaces the
            # file, so the block lasts one run.
            self.outcome.block("hash_load_failed", str(self.hash_manager.cache_file))
    
    @property
    def hash_manager(self) -> HashManager:
        """The framework's own hash file (its primary sink's)."""
        return self.sink.hash_manager

    @property
    def output_dir(self) -> Path:
        """The framework's own docs dir (its primary sink's)."""
        return self.sink.output_dir

    @property
    def markdown_converter(self) -> AppleDocMarkdownConverter:
        """The converter of the framework's own pages (its primary sink's)."""
        return self.sink.markdown_converter

    def _convert_doc_url_to_json_url(self, doc_url: str) -> str:
        """Convert a documentation URL to its JSON data URL.
        
        Args:
            doc_url: Documentation URL like https://developer.apple.com/documentation/swiftui/text
            
        Returns:
            JSON URL like https://developer.apple.com/tutorials/data/documentation/swiftui/text.json
        """
        parsed = urlparse(doc_url)
        path = parsed.path
        
        # Remove /documentation/ prefix
        if path.startswith('/documentation/'):
            path = path[len('/documentation/'):]
        
        # Add .json extension if not present
        if not path.endswith('.json'):
            path += '.json'
        
        return f"{self.site.json_prefix}{path}"
    
    def _convert_json_url_to_doc_url(self, json_url: str) -> str:
        """Convert a JSON data URL back to documentation URL (doc_url_of).
        
        Args:
            json_url: JSON URL
            
        Returns:
            Documentation URL
        """
        return doc_url_of(self.site, json_url)
    
    async def scrape_framework(self) -> Dict[str, Any]:
        """Override base scrape_framework to use streaming approach."""
        self.stats["start_time"] = time.time()
        # Being scraped means technologies.json lists the framework: its count
        # of unlisted runs (cleanup_removed_frameworks.py) starts over, also
        # when that script's own fetch failed this run. Saved by __aexit__.
        self.hash_manager.set_metadata("unlisted_runs", 0)
        # The same goes for a D6 module that technologies.json now lists
        # (promoted): from now on it is judged as a framework, in the same
        # dir and hash file
        if self.hash_manager.get_metadata(MODULE_KEY):
            logger.info("module_promoted", framework=self.framework_name)
            self.hash_manager.set_metadata(MODULE_KEY, None)
        if self.hash_manager.stale:
            logger.info(
                "render_version_stale",
                framework=self.framework_name,
                stored=self.hash_manager.stored_render_version,
                version=self.RENDER_VERSION,
            )

        await self.discover_and_scrape_streaming()
        self._apply_failure_policy(self.sink)
        self._store_render_version(self.sink)
        
        self.stats["end_time"] = time.time()
        self.stats["duration"] = self.stats["end_time"] - self.stats["start_time"]
        self.outcome.stats = self.stats
        
        # Save cross-framework references if tracking was enabled
        if self.include_cross_refs:
            self.save_cross_framework_summary()
        self._log_unknown_content()
        if self.reference_fallbacks:
            logger.info("reference_fallbacks", framework=self.framework_name, count=self.reference_fallbacks)
        
        logger.info(
            "framework_scrape_complete",
            framework=self.framework_name,
            stats=self.stats
        )
        
        return self.stats
    
    async def discover_and_scrape_streaming(self) -> None:
        """Discover URLs and scrape them immediately for real-time feedback."""
        logger.info("starting_streaming_discovery_and_scrape", framework=self.framework_name)
        
        # Start with the framework's main JSON file
        framework_json_url = self.root_json_url
        
        # Scrape the main framework page first
        main_doc_url = self.site.doc_url(self.framework_id)
        await self._scrape_and_save_url(self.sink, main_doc_url)
        
        # Use iterative approach instead of recursion to avoid stack overflow
        try:
            await self._discover_and_scrape_iterative([framework_json_url])
        finally:
            # Logged even if discovery raised
            logger.info(
                "framework_scraping_finalized",
                framework=self.framework_name,
                pages_scraped=self.stats['pages_scraped'],
                pages_skipped=self.stats['pages_skipped'],
                pages_failed=self.stats['pages_failed']
            )
        
    async def _scrape_and_save_url(self, sink: Sink, url: str) -> bool:
        """Scrape a single URL and save it immediately (via scrape_page)."""
        try:
            return await self.scrape_page(sink, url) is not None
        except Exception as e:
            # Raised outside the page's own convert/save step: block, don't count
            logger.error("failed_to_scrape_url", url=url, error=str(e))
            self.outcome.block("exception", url)
            return False
    
    async def _discover_and_scrape_iterative(self, initial_json_urls) -> None:
        """Iterative version of discovery to avoid recursion depth issues with optimized ETag usage.

        Each URL goes to its sink (_route), and a sink's page is processed
        once per run, by the first job that reaches it (dedup per sink). A
        later job reaching it still gets the links it follows from it
        (_dedup_hit): from the page's kept links, or, while another job is
        processing it, once that ends; the loop doesn't finish while such a
        wait is pending.
        """
        from collections import deque

        # Queue of URLs to process
        if isinstance(initial_json_urls, str):
            initial_json_urls = [initial_json_urls]
        url_queue = deque(initial_json_urls)
        self._queued.update(initial_json_urls)

        logger.info(f"starting_iterative_discovery", initial_urls=len(initial_json_urls))
        
        # Track queue size for monitoring
        max_queue_size = 0
        processed_count = 0
        
        # Worker pool: process up to INTRA_FRAMEWORK_CONCURRENCY pages of this
        # framework at once (see todo-concurrency.md). asyncio is single-threaded,
        # so shared state (queue, the sinks' processed_urls and hash managers,
        # stats) is safe; URLs are marked processed before any await,
        # preventing duplicates.
        in_flight: Set["asyncio.Future[None]"] = set()
        # Dedup hits on pages another job is processing: page -> (its sink, its URL)
        waiting: Dict["asyncio.Future[None]", Tuple[Sink, str]] = {}

        while url_queue or in_flight or waiting:
            # Launch tasks up to the concurrency limit
            while url_queue and len(in_flight) < Config.INTRA_FRAMEWORK_CONCURRENCY:
                max_queue_size = max(max_queue_size, len(url_queue))
                json_url = url_queue.popleft()
                sink = self._route(json_url)
                if sink is None:
                    continue
                if sink.module:
                    # A module's root is part of its parents' crawl, also
                    # when they link only pages under it (e.g. Accelerate's
                    # simd-library links simd's symbols, never simd itself)
                    self._enqueue([f"{self.site.json_prefix}{sink.dir_name.lower()}.json"], url_queue)
                if json_url in sink.processed_urls:
                    self._dedup_hit(sink, json_url, url_queue, waiting)
                    continue
                sink.processed_urls.add(json_url)
                if self.job_id != sink.primary_id:
                    sink.writer[json_url] = self.job_id
                processed_count += 1
                if processed_count % 100 == 0:
                    logger.info(
                        "iterative_discovery_progress",
                        processed=processed_count,
                        queue_size=len(url_queue),
                        max_queue_size=max_queue_size,
                    )
                # Counted, and its waiters registered, before the task starts
                sink.pages_in_flight += 1
                page_done: Optional["asyncio.Future[None]"] = None
                if sink.stores_links(self.job_id):
                    page_done = asyncio.get_running_loop().create_future()
                    sink.pending[json_url] = page_done
                in_flight.add(asyncio.create_task(
                    self._process_page(sink, json_url, url_queue, page_done)
                ))

            if not in_flight and not waiting:
                continue  # queue contained only already-processed URLs

            done, _ = await asyncio.wait(in_flight | set(waiting), return_when=asyncio.FIRST_COMPLETED)
            for task in done:
                if task in waiting:
                    page_sink, page_url = waiting.pop(task)
                    self._take_links(page_sink, page_url, url_queue)
                    continue
                in_flight.discard(task)
                exc = task.exception()
                if exc:
                    logger.error("worker_task_error", error=str(exc))
                    self.outcome.block("worker_exception", str(exc))

        logger.info(
            "iterative_discovery_complete",
            total_processed=processed_count,
            max_queue_size=max_queue_size,
            framework=self.framework_name,
        )

    async def _process_page(
        self, sink: Sink, json_url: str, url_queue: Deque[str], page_done: Optional["asyncio.Future[None]"]
    ) -> None:
        """Process a page of a sink (_process_queued_url), then end its run accounting.

        In the finally: the page's waiters are woken (a dedup hit of another
        job waits on page_done), its count of pages in flight drops, and the
        sink is released if nothing in flight uses it any more
        (SinkRegistry.release_if_idle).
        """
        try:
            await self._process_queued_url(sink, json_url, url_queue)
        finally:
            if page_done is not None:
                sink.pending.pop(json_url, None)
                page_done.set_result(None)
            sink.pages_in_flight -= 1
            self.sinks.release_if_idle(sink)

    def _segment(self, json_url: str) -> Optional[str]:
        """A JSON URL's first path segment, lowercased (None for a URL not of the site)."""
        if not json_url.startswith(self.site.json_prefix):
            return None
        rest = json_url[len(self.site.json_prefix):]
        if rest.endswith('.json'):
            rest = rest[:-len('.json')]
        return rest.split('/', 1)[0].lower()

    def _route(self, json_url: str) -> Optional[Sink]:
        """The sink of a page: its URL's first path segment's (D6).

        The job's own framework's segment is its primary sink. Any other
        segment the scope rule follows (_in_scope) is a D6 module's (a
        segment of the job's bundle that is no top-level technology), or,
        for a top-level technology of the job's bundle, that technology's own
        sink (a handoff). A new sink's dir is cased as the link's identifier
        cases it, reconciled with an existing hash file
        (_canonical_framework_id), never from metadata.modules. The
        routing is recorded before the per-sink dedup (_note_route).

        Returns:
            The page's sink, or None when the Apple sinks may not have its
            dir: another scraper's top-level dir (namespace_collision, which
            blocks this job's cleanup); the page isn't fetched
        """
        segment = self._segment(json_url)
        if segment is None or segment == self.job_id:
            return self.sink
        sink = self.sinks.find(self.site, segment)
        if sink is None:
            dir_name, _ = self._routes.get(segment, (segment, ''))
            if self.sinks.refuses(dir_name):
                if segment not in self._collisions:
                    self._collisions.add(segment)
                    logger.error("namespace_collision", framework=self.framework_name, dir=dir_name, url=json_url)
                self.outcome.block("namespace_collision", dir_name)
                return None
            dir_name = self._canonical_framework_id(dir_name)
            if segment in self.sinks.top_level(self.site):
                sink = self.sinks.get(self.site, dir_name, self.sinks.title(dir_name), self.RENDER_VERSION)
            else:
                sink = self.sinks.get(self.site, dir_name, dir_name, self.RENDER_VERSION, module=True)
                logger.info("module_sink", module=sink.dir_name, parent=self.framework_name)
        self._note_route(sink, segment)
        return sink

    def _note_route(self, sink: Sink, segment: str) -> None:
        """Record the job's first routing to another sink this run, in both hash files.

        A module records the job among its parents (metadata.module, with
        its bundle) and the job's own hash file the module
        (metadata.child_modules); a top-level sink records the job as a
        handoff writer (metadata.handoff_from). The job is among the sink's
        parents_this_run (rule 2: routed, whatever the page's fetch then
        gives) and its users until it ends. A sink whose hash file failed
        to load blocks the job's cleanup, as its own would.
        """
        if self.job_id in sink.parents_this_run:
            return
        sink.parents_this_run.add(self.job_id)
        sink.users.add(self.job_id)
        if sink.module:
            sink.add_parent(self.job_id, self._routes.get(segment, ('', ''))[1])
            self.sink.add_child_module(sink.dir_name.lower())
        else:
            sink.add_handoff_writer(self.job_id)
            logger.info("handoff_sink", sink=sink.dir_name, writer=self.framework_name)
        if sink.load_error is not None:
            self.outcome.block("hash_load_failed", str(sink.hash_file))

    def _follows(self, sink: Sink) -> bool:
        """Whether the job follows the links of a sink's pages: its own, and a module's.

        A handoff page (another top-level technology's) is one hop: its
        links are that technology's job's to follow.
        """
        return sink is self.sink or sink.module

    def _dedup_hit(
        self,
        sink: Sink,
        json_url: str,
        url_queue: Deque[str],
        waiting: Dict["asyncio.Future[None]", Tuple[Sink, str]],
    ) -> None:
        """A page of a sink this run already processed (or is processing): the job's share of it.

        Nothing for a page the job processed itself, or one whose links it
        doesn't follow (_follows). Else the job gets the page's links in its
        own scope (_take_links): at once when the page is done, or, while
        another job is processing it, once that ends (the page's waiter).
        """
        if not self._follows(sink) or sink.writer_of(json_url) == self.job_id:
            return
        page_done = sink.pending.get(json_url)
        if page_done is not None:
            waiting[page_done] = (sink, json_url)
            return
        self._take_links(sink, json_url, url_queue)

    def _take_links(self, sink: Sink, json_url: str, url_queue: Deque[str]) -> None:
        """A page another job processed: its links in this job's scope, or the page's outcome.

        Its kept links are queued (_in_scope). Without links: a page whose
        processing raised blocks the job at once (exception), and one whose
        fetch failed (ours, counted toward D8) records the job on it
        (dedup_jobs): the end-of-run failure policy gives it the page's
        block or persistent flag. The pages in its scope reachable only
        through that page go untouched this run, and that block keeps its
        cleanup from orphaning them. A page Apple removed (404/410) gives
        nothing: what only it linked to is removed too.
        """
        links = sink.links.get(json_url)
        if links is not None:
            self._enqueue(self._in_scope(links), url_queue)
        elif json_url in sink.raised:
            self.outcome.block("exception", json_url)
        elif json_url in sink.fetch_failures:
            sink.dedup_jobs.setdefault(json_url, set()).add(self.job_id)

    async def _process_queued_url(self, sink: Sink, json_url: str, url_queue: Deque[str]) -> None:
        """Process a single discovered URL: fetch, enqueue children, save if changed.

        Args:
            sink: The page's sink
            json_url: The page's JSON URL
            url_queue: The discovery queue its links go to
        """
        hm = sink.hash_manager
        try:
            # OPTIMIZED: Fetch JSON with ETag support for discovery
            result = await self.fetch_page_with_etag(json_url, use_etag=True, hash_manager=hm)
            if isinstance(result, FetchFailed):
                # Never treated as a 304, and never refetched for discovery
                self._handle_fetch_failure(sink, json_url, result)
                return

            if result is NOT_MODIFIED:
                # Got 304 Not Modified - content unchanged
                if self._is_root(json_url):
                    self._root_ok = True
                doc_url = self._convert_json_url_to_doc_url(json_url)
                logger.debug("content_unchanged_skip_scrape", json_url=json_url, doc_url=doc_url)
                self.stats['pages_skipped'] += 1

                # Touch the entry for orphan detection even though content
                # unchanged. KEEP the recorded file path: a page the tripwire
                # gave a hashed stem keeps that file (recomputing the path
                # from its URL would record the other page's file of its
                # clash). Only an entry without one gets the tripwire's path.
                if json_url in hm.hashes:
                    if not hm.hashes[json_url].get('file_path'):
                        hm.set_file_path(
                            json_url, self._claim_path(sink, json_url, self._get_organized_file_path(sink, doc_url, {}))
                        )
                    hm.touch(json_url)

                # IMPORTANT: Still need to discover child pages!
                # The main page might be unchanged but children could be new/updated.
                if json_url in hm.hashes:
                    # We've seen this page before - need to rediscover its children
                    # Fetch without ETag to get content for discovery
                    discovery_result = await self.fetch_page_with_etag(json_url, use_etag=False)
                    if discovery_result is NOT_MODIFIED:
                        # No body to read the links from: a failed refetch
                        discovery_result = FetchFailed(
                            status=304, error="HTTP 304 on discovery refetch", transient=True
                        )
                    elif not isinstance(discovery_result, FetchFailed):
                        try:
                            data = json.loads(discovery_result[0])
                        except json.JSONDecodeError:
                            logger.warning("failed_to_parse_json_for_rediscovery", url=json_url)
                            discovery_result = self._invalid_json_failure()
                        else:
                            # Extract URLs for discovery
                            count = self._discover_links(sink, json_url, data, url_queue)
                            logger.debug("rediscovered_child_urls", parent=json_url, count=count)
                            sink.fetch_ok.add(json_url)
                    if isinstance(discovery_result, FetchFailed):
                        # The 304 proved the page live; only its links are missing
                        self._handle_fetch_failure(sink, json_url, discovery_result, after_304=True)
                return

            # Got 200 OK - content is new or changed
            response_text, etag = result

            # Parse JSON for discovery
            try:
                data = json.loads(response_text)
            except json.JSONDecodeError:
                logger.warning("failed_to_parse_json", url=json_url)
                self._handle_fetch_failure(sink, json_url, self._invalid_json_failure())
                return
            sink.fetch_ok.add(json_url)
            if self._is_root(json_url):
                self._root_ok = True

            # Links first: enqueue the children before, and independently of,
            # the save, so a convert or save error can never orphan them
            self._discover_links(sink, json_url, data, url_queue)

            # Process and save this page
            doc_url = self._convert_json_url_to_doc_url(json_url)
            saved = False
            file_path: Optional[Path] = None

            # Only this inner try counts as a local error (the links are queued)
            try:
                # Check if we need to process based on content hash
                if hm.has_changed(json_url, response_text, etag):
                    # Extract and save page data
                    page_data = self._extract_from_json(sink, data, doc_url)
                    if page_data:
                        # Calculate file path for hash updates
                        file_path = self._get_organized_file_path(sink, doc_url, page_data)

                        # Write the file first, then both hash keys
                        saved = await self._save_and_record(
                            sink, json_url, doc_url, page_data, file_path, response_text, etag
                        )
                else:
                    # Content hasn't changed according to hash
                    logger.debug("content_unchanged_via_hash", url=doc_url)
                    self.stats['pages_skipped'] += 1

                    # Still need to update hash with file path for orphan detection.
                    # Reuse the stored file path, as the 304 branch does; compute
                    # one only when none is stored, and then write the file first.
                    stored_path = hm.hashes[json_url].get('file_path')
                    if stored_path:
                        file_path = Path(stored_path)
                        # Touch both keys and record the new etag
                        hm.update_hash(json_url, response_text, etag, file_path)
                        hm.update_hash(doc_url, response_text, etag, file_path)
                    else:
                        page_data = self._extract_from_json(sink, data, doc_url)
                        file_path = self._get_organized_file_path(sink, doc_url, page_data)
                        await self._save_and_record(
                            sink, json_url, doc_url, page_data, file_path, response_text, etag
                        )
            except Exception as e:
                self._handle_local_error(sink, json_url, e, file_path)
                return
            sink.saved_ok.add(json_url)

            if saved:
                self.stats['pages_scraped'] += 1

                # Log progress every 10 files
                if self.stats['pages_scraped'] % 10 == 0:
                    logger.info(
                        "scraping_progress",
                        scraped=self.stats['pages_scraped'],
                        skipped=self.stats['pages_skipped'],
                        failed=self.stats['pages_failed'],
                        queue_size=len(url_queue)
                    )

        except Exception as e:
            # Raised before the page's links were enqueued: block, don't count
            logger.error("error_processing_url", url=json_url, error=str(e))
            self.outcome.block("exception", json_url)
            sink.raised.add(json_url)

    def _discover_links(self, sink: Sink, json_url: str, data: Dict[str, Any], url_queue: Deque[str]) -> int:
        """Read a fetched page's links: kept for the run if another job may need
        them (Sink.stores_links), queued if the job follows them (_follows).

        Returns:
            How many links were queued
        """
        page_links = self._page_links(data)
        if sink.stores_links(self.job_id):
            sink.links[json_url] = page_links
        if not self._follows(sink):
            return 0
        urls = self._in_scope(page_links)
        self._enqueue(urls, url_queue)
        return len(urls)

    def _enqueue(self, urls: List[str], url_queue: Deque[str]) -> None:
        """Queue the URLs this job hasn't queued yet; each sink deduplicates at pop time.

        A link to the framework's own root (lowercased, as every resolved
        link is) is its root URL, which keeps its id's casing.
        """
        for new_url in urls:
            if new_url != self.root_json_url and self._is_root(new_url):
                new_url = self.root_json_url
            if new_url not in self._queued:
                self._queued.add(new_url)
                url_queue.append(new_url)

    def _is_root(self, json_url: str) -> bool:
        """True for the framework root page's JSON URL."""
        return json_url.lower() == self.root_json_url.lower()

    @staticmethod
    def _is_previously_good(entry: Optional[Dict[str, Any]]) -> bool:
        """A live entry: it records a file and isn't an error entry."""
        return bool(entry and entry.get('file_path') and entry.get('status') != 'error')

    async def _save_and_record(
        self,
        sink: Sink,
        json_url: str,
        doc_url: str,
        page_data: Dict[str, Any],
        file_path: Path,
        content: str,
        etag: Optional[str],
    ) -> bool:
        """Write the page's file, then record it on both hash keys.

        Through the write-time tripwire (_tripwire_path): a page whose file
        name another page's file already has is a filename_clash (an ERROR
        that flags the run, never a block) and is written under a hashed
        stem instead. A page that had a hashed stem and is now written
        elsewhere loses its old file (_remove_moved_clash_file).

        Args:
            sink: The page's sink
            file_path: The page's path (_get_organized_file_path)

        Returns:
            True if the file was written. A file that is never written (an
            unsafe path) gets an error entry instead, so no key records it.
        """
        target = self._tripwire_path(sink, json_url, file_path)
        if target != file_path:
            logger.error(
                "filename_clash",
                url=json_url,
                path=str(file_path),
                other_url=self._path_owners(sink).get(self._path_key(file_path)),
                written_to=str(target),
            )
            if json_url not in self.outcome.filename_clashes:
                self.outcome.filename_clashes.append(json_url)
        if not await self.save_page_data(sink, doc_url, page_data, target):
            sink.hash_manager.mark_error(json_url, "unsafe file path")
            return False
        self._remove_moved_clash_file(sink, json_url, target)
        sink.hash_manager.update_hash(json_url, content, etag, target)
        sink.hash_manager.update_hash(doc_url, content, etag, target)
        self._path_owners(sink)[self._path_key(target)] = json_url.lower()
        return True

    def _path_owners(self, sink: Sink) -> Dict[str, str]:
        """A sink's write-time tripwire map (_tripwire_path): the page each file is.

        Lowercased path -> lowercased JSON URL (URL space is
        case-insensitive). Seeded on first use from the live JSON-URL keys'
        recorded files (a page answering 304 keeps its file), then every file
        this run records.
        """
        if sink.path_owner_map is None:
            sink.path_owner_map = {
                self._path_key(entry['file_path']): url.lower()
                for url, entry in sink.hash_manager.hashes.items()
                if url.startswith(sink.site.json_prefix) and self._is_previously_good(entry)
            }
        return sink.path_owner_map

    @staticmethod
    def _path_key(file_path: Union[str, Path]) -> str:
        """A file's key in the tripwire's map: its path, lowercased."""
        return str(Path(file_path)).lower()

    def _tripwire_path(self, sink: Sink, json_url: str, file_path: Path) -> Path:
        """Where the page's file goes: file_path, unless it is another page's file.

        Two pages whose URLs give the same file name (the naming isn't
        injective there, e.g. for a new Apple page) would overwrite each
        other's file. The page whose file it isn't gets the hashed stem
        <stem><clash_suffix> in the same folder, stable run to run (its
        children keep their folder). Its old name comes back once the other
        page is gone (its error entry seeds no file).
        """
        owner = self._path_owners(sink).get(self._path_key(file_path))
        if owner is None or owner == json_url.lower():
            return file_path
        return file_path.with_name(f"{file_path.stem}{clash_suffix(json_url)}.md")

    def _claim_path(self, sink: Sink, json_url: str, file_path: Path) -> Path:
        """The tripwire's path for a page whose file is recorded without a write; now the page's."""
        target = self._tripwire_path(sink, json_url, file_path)
        self._path_owners(sink)[self._path_key(target)] = json_url.lower()
        return target

    def _remove_moved_clash_file(self, sink: Sink, json_url: str, file_path: Path) -> None:
        """Delete the page's hashed-stem file once its file was written at file_path instead.

        Its keys are about to record file_path, so no entry would record the
        old file, and no cleanup would ever remove it. Only a recorded file
        named with this page's clash_suffix, inside the sink's dir.
        """
        suffix = clash_suffix(json_url)
        output_root = sink.output_dir.resolve()
        recorded = {
            (sink.hash_manager.hashes.get(key) or {}).get('file_path')
            for key in (json_url, self._convert_json_url_to_doc_url(json_url))
        }
        for old_path in sorted(path for path in recorded if path):
            old = Path(old_path)
            if self._path_key(old) == self._path_key(file_path):
                continue
            if old.stem.endswith(suffix) and output_root in old.resolve().parents:
                old.unlink(missing_ok=True)
                logger.info("clash_file_removed", url=json_url, file=old_path, now=str(file_path))

    def _handle_fetch_failure(
        self, sink: Sink, json_url: str, failure: FetchFailed, after_304: bool = False
    ) -> None:
        """Apply the failure policy to a fetch that gave no usable page.

        - 404/410: Apple removed the page. Its JSON-URL key becomes an error
          entry, so its file (and any subtree no longer reachable) is orphaned
          and cleaned. Never blocks.
        - Any other failure of a live page, or of a discovery refetch after a
          304: keep the entry and touch it, so its file isn't orphaned; it
          blocks cleanup and counts toward D8.
        - A URL with no live entry: an error entry. A transient failure blocks
          and counts (it may be the new parent of a moved page); a 4xx doesn't.
          A URL that no entry records but whose file is on disk, though, is a
          page we have whose entry was lost (e.g. its hash file failed to
          load): it is handled as a live page.
        - The root never reaches D8: any failure other than 404/410 keeps it
          and blocks cleanup, every run until it recovers. So does a 404/410
          after the root answered 200/304 in this run: the root is live, and
          this fetch, which reads its links, failed.

        Counting is done once per run by _apply_failure_policy.

        Args:
            sink: The page's sink
            json_url: The page's JSON URL
            failure: The failed fetch
            after_304: The failure is the discovery refetch after a 304
        """
        hm = sink.hash_manager
        if failure.status in GONE_STATUSES:
            if not (self._is_root(json_url) and self._root_ok):
                hm.mark_error(json_url, failure.error)
                logger.info("page_gone", url=json_url, status=failure.status)
                sink.gone.add(json_url)
                if self._is_root(json_url):
                    self._root_gone = True
                return
            logger.warning("root_fetch_conflict", url=json_url, status=failure.status)

        kind: FailureKind
        if after_304:
            # The 304 already touched the entry
            kind = "after_304"
        elif self._is_previously_good(hm.hashes.get(json_url)):
            hm.touch(json_url)
            kind = "previously_good"
        elif self._kept_unrecorded_file(sink, json_url):
            kind = "previously_good"
        else:
            hm.mark_error(json_url, failure.error)
            kind = "never_good"

        if self._is_root(json_url):
            logger.error("root_fetch_failed", url=json_url, status=failure.status, error=failure.error)
            self.outcome.root_fetch_failed = True
            self.outcome.block("root_fetch_failed", json_url)
            return
        if kind == "never_good" and not failure.transient:
            # A never-good 4xx: nothing to keep, so it doesn't block (many
            # frameworks link the same 4xx URLs every run); pages reachable
            # only through it are cleaned
            return
        logger.warning(
            "page_fetch_failed", url=json_url, kind=kind, status=failure.status, error=failure.error
        )
        sink.fetch_failures[json_url] = PageFetchFailure(kind, failure)

    def _handle_local_error(
        self,
        sink: Sink,
        json_url: str,
        error: Exception,
        file_path: Optional[Path] = None,
    ) -> None:
        """A convert or save error of ours: keep the page, block cleanup, count it.

        Never deletes: the page answered 200, so its file is kept. A live
        entry keeps its hash, etag and file_path (the old etag makes the next
        run refetch) and is touched, so its file is never orphaned. Without
        one, the page's file can still be on disk with no live JSON-URL key
        recording it: its JSON-URL key answered 404/410 (e.g. the root's first
        fetch this run), or D8 marked both keys, in a run whose cleanup didn't
        delete the file, or the hash file was lost. Then the JSON-URL key
        records that file again (HashManager.keep_file), so it is kept.
        Otherwise the URL gets an error entry, so its count persists. Never
        counts toward D8; counted once per run by _apply_failure_policy.

        Args:
            sink: The page's sink
            json_url: The page's JSON URL
            error: The convert or save error
            file_path: The path this run computed for the page's file, if it got that far
        """
        logger.error("page_save_failed", url=json_url, error=str(error))
        hm = sink.hash_manager
        if self._is_previously_good(hm.hashes.get(json_url)):
            hm.touch(json_url)
        elif not self._keep_file(sink, json_url, self._page_file_path(sink, json_url, file_path)):
            hm.mark_error(json_url, f"local error: {error}")
        sink.local_errors[json_url] = str(error)

    def _page_file_path(self, sink: Sink, json_url: str, file_path: Optional[Path]) -> Optional[Path]:
        """Where the file of a page without a live JSON-URL entry would be.

        Its doc-URL key's recorded path if that key is live; else the path
        this run computed, or for an error raised before that, the one its
        URL gives (the path depends on the URL alone), under the tripwire
        (never another page's file, see _tripwire_path). None if that fails.
        """
        doc_url = self._convert_json_url_to_doc_url(json_url)
        doc_entry = sink.hash_manager.hashes.get(doc_url)
        if doc_entry is not None and self._is_previously_good(doc_entry):
            return Path(doc_entry['file_path'])
        try:
            if file_path is None:
                file_path = self._get_organized_file_path(sink, doc_url, {})
            return self._tripwire_path(sink, json_url, file_path)
        except Exception as e:
            logger.warning("page_file_path_failed", url=json_url, error=str(e))
            return None

    def _keep_file(self, sink: Sink, json_url: str, file_path: Optional[Path]) -> bool:
        """HashManager.keep_file for a page's file found on disk; the file is then the page's.

        Returns:
            True if the file was found and is now recorded
        """
        if file_path is None or not sink.hash_manager.keep_file(json_url, file_path):
            return False
        self._path_owners(sink)[self._path_key(file_path)] = json_url.lower()
        return True

    def _kept_unrecorded_file(self, sink: Sink, json_url: str) -> bool:
        """Keep a failed page that no entry records but whose file is on disk.

        The file shows we have the page; only its entry was lost, by a
        failure of ours or an outside cause: the hash file failed to load
        (this run, where nothing loaded, so every page looks new), an earlier
        run couldn't record the page (a run whose hash file failed to load
        saves only the pages it reached; a failed save keeps the previous
        file, which lacks the pages saved in that run), or the hash file was
        deleted. Its JSON-URL key records that file again
        (HashManager.keep_file), so this run's save records a live page, and
        the failure counts toward D8 as for any page we have. A URL that has
        an entry is judged by it: an error entry (from a 404/410, a D8, an
        earlier never-good failure or a local error) stays never-good. The
        path comes from the URL alone, as every page's does.

        Returns:
            True if the file was found and is now recorded
        """
        if json_url in sink.hash_manager.hashes:
            return False
        return self._keep_file(sink, json_url, self._page_file_path(sink, json_url, None))

    def _apply_failure_policy(self, sink: Sink) -> None:
        """Count this run's failures once, and decide whether cleanup is blocked.

        Runs once per framework run, after discovery, for its primary sink.
        Updates the root_gone_runs metadata of the sink's hash file and the
        per-entry counters of the pages this job processed
        (apply_sink_failure_policy), and fills self.outcome. A sink whose
        hash file carried handoff_from when it was loaded (Sink.deferred)
        keeps only the root here: its storm check and per-entry counting are
        done at the end of the run, over every writer's pages (finish_run).
        """
        hm = sink.hash_manager
        outcome = self.outcome

        # Root: a 404/410 counts toward root_gone_runs once per run, any 200/304 resets it
        if self._root_ok:
            if self._root_gone:
                # A 404/410, then a 200/304 on the fetch that reads the root's
                # links: the root is live (had that fetch failed, it blocked
                # as root_fetch_failed)
                logger.warning("root_fetch_conflict", framework=self.framework_name, url=self.root_json_url)
            hm.set_metadata("root_gone_runs", 0)
        elif self._root_gone:
            runs = int(hm.get_metadata("root_gone_runs", 0)) + 1
            hm.set_metadata("root_gone_runs", runs)
            outcome.root_gone_runs = runs
            if runs == 1:
                logger.warning("root_gone_pending", framework=self.framework_name, root_gone_runs=runs)
            else:
                logger.warning("root_gone", framework=self.framework_name, root_gone_runs=runs)

        if not sink.deferred:
            apply_sink_failure_policy(
                sink, lambda job: outcome if job == self.job_id else self.sinks.outcomes.get(job),
                self.framework_name, writers={self.job_id},
            )

        if outcome.blocks:
            logger.warning(
                "cleanup_blocked",
                framework=self.framework_name,
                reasons={reason: len(details) for reason, details in outcome.blocks.items()},
            )

    def _store_render_version(self, sink: Sink) -> None:
        """Store RENDER_VERSION in a sink's hash file (metadata.render) after a clean run.

        Clean: cleanup isn't skipped (no failure of ours blocked it, nothing
        raised, the root isn't gone) and no page's local error is persistent,
        so every page this run reached was rendered by this version, with or
        without --cleanup-orphans. Otherwise the stored version stays and
        the next run renders the framework again: a framework whose root
        404'd, or a page whose rendering keeps failing (its file kept, its
        etag still matching), would else never be rendered again. A filename
        clash doesn't count: its page was written, under a hashed stem.
        When it stores a new version, the entries this run didn't touch lose
        their hash and etag (forget_untouched_renderings): their files keep
        the old rendering (a file the valve holds, or a page no longer
        reached), and such a page that comes back unchanged would else
        answer 304 and never be rendered again.
        Saved by __aexit__.

        A multi-writer sink stores it at the end of the run instead
        (finish_run): one whose hash file carried handoff_from when loaded,
        and one another job has processed a page of by now (that job's
        failures are counted only then).
        """
        outcome = self.outcome
        if sink.deferred or sink.other_writers():
            return
        if outcome.skip_cleanup or outcome.persistent_local_errors:
            return
        store_render_version(sink, self.framework_name)

    def scan_orphans(self, sink: Sink) -> None:
        """Find the orphan candidates of the framework's own sink, right after its hash file was saved.

        Fills self.outcome for the end-of-run cleanup, so neither the scraper
        nor its hash manager has to be kept until then:
        - A root that answered 404/410 this run: no cleanup (the end-of-run
          pass deletes the framework at 2 runs).
        - Zero-touched guard: a framework where this run touched no entry is
          never cleaned. It logs framework_zero_touched and blocks, as a
          failure of ours (every file it has would look orphaned).
        - The candidates are the .md files no entry this run touched records
          (the in-memory touched set). A blocked or raised framework keeps
          none.
        A sink whose hash file carried handoff_from when it was loaded is
        scanned at the end of the run instead, from every writer's touched
        set (finish_run); so is, again, one that another job routed a page
        to this run.
        """
        outcome = self.outcome
        if outcome.root_gone_runs or sink.deferred:
            return
        if not outcome.blocked and not sink.hash_manager.touched:
            logger.error("framework_zero_touched", framework=self.framework_name, framework_id=self.framework_id)
            outcome.block("zero_touched", self.framework_id)
        if outcome.blocked:
            return
        outcome.orphan_scan = orphan_scan_of(sink)

    def _extract_urls_from_json_data(self, data: Dict[str, Any]) -> List[str]:
        """The JSON URLs of a page's links that the job follows (_page_links, then _in_scope)."""
        return self._in_scope(self._page_links(data))

    @staticmethod
    def _bundle_of(identifier: str) -> str:
        """A doc:// identifier's bundle, lowercased ("" for anything else)."""
        if not identifier.startswith('doc://'):
            return ''
        return identifier[len('doc://'):].split('/', 1)[0].lower()

    def _page_links(self, data: Dict[str, Any]) -> PageLinks:
        """A page's links to documentation pages, resolved (_resolve), and its own bundle."""
        identifier = data.get('identifier')
        page_identifier = identifier.get('url', '') if isinstance(identifier, dict) else ''
        references = data.get('references')
        if not isinstance(references, dict):
            references = {}
        links: List[PageLink] = []

        # Extract related documentation from various sections
        for section_name in LINK_SECTIONS:
            if section_name in data and isinstance(data[section_name], list):
                logger.debug(f"Extracting URLs from {section_name} with {len(data[section_name])} items")
                
                for section in data[section_name]:
                    if isinstance(section, dict) and 'identifiers' in section:
                        identifiers = section.get('identifiers', [])
                        section_title = section.get('title', 'Unknown')
                        logger.info(f"Found section '{section_title}' with {len(identifiers)} identifiers")
                        
                        for link_identifier in identifiers:
                            if isinstance(link_identifier, str) and link_identifier.startswith('doc://'):
                                link = self._resolve(link_identifier, references)
                                if link is not None:
                                    links.append(link)
        return PageLinks(bundle=self._bundle_of(page_identifier if isinstance(page_identifier, str) else ''),
                         links=tuple(links))

    def _resolve(self, identifier: str, references: Dict[str, Any]) -> Optional[PageLink]:
        """The page a doc:// identifier links to, through its reference (1.1).

        A reference of type topic whose url is a documentation page's
        ("/documentation/…" on the site) gives the target: Apple's own URL,
        with the module's real first segment (sirikit's Intents is
        /documentation/intents, never sirikit/intents) and DocC's shortened
        long paths. Its #fragment (a section of the page) is stripped, it is
        lowercased and its dot segments escaped (_escape_dot_path_segments).
        Any other reference links no documentation page. Only an identifier
        with no reference falls back to its own path, as it is (never the
        framework's id prepended): counted and logged.

        Returns:
            The link, or None if it isn't to a documentation page
        """
        doc_path = urlparse(self.site.doc_prefix).path
        reference = references.get(identifier)
        if reference is not None:
            url = reference.get('url') if isinstance(reference, dict) else None
            if not (isinstance(reference, dict) and reference.get('type') == 'topic'
                    and isinstance(url, str) and url.startswith(doc_path)):
                return None
            json_url = self._page_json_url(url[len(doc_path):])
        else:
            json_url = self._convert_identifier_to_json_url(identifier)
            if json_url is not None:
                self.reference_fallbacks += 1
                logger.info("reference_missing", identifier=identifier)
        segment = self._segment(json_url) if json_url is not None else None
        if json_url is None or segment is None:
            return None
        identifier_path = identifier.split('/documentation/', 1)[1] if '/documentation/' in identifier else ''
        cased = identifier_path.split('#', 1)[0].split('/', 1)[0]
        return PageLink(
            json_url=json_url,
            segment=segment,
            dir_name=cased if cased.lower() == segment else segment,
            bundle=self._bundle_of(identifier),
            identifier=identifier,
        )

    def _page_json_url(self, path: str) -> Optional[str]:
        """The JSON URL of the page at a documentation path (what follows
        /documentation/): without its #fragment (a section of the page, never
        part of the page's URL), lowercased, dot segments escaped. None for
        an empty path."""
        path = path.split('#', 1)[0].lower().strip('/')
        if not path:
            return None
        return f"{self.site.json_prefix}{self._escape_dot_path_segments(path)}.json"

    def _in_scope(self, page_links: PageLinks) -> List[str]:
        """The scope rule: the JSON URLs of a page's links that this job follows.

        A link is followed if its first path segment is the job's framework,
        or if it is in the same bundle as the page (its identifier's bundle).
        A same-bundle segment that is no top-level technology is a D6
        module's; one that is another top-level technology goes to that
        technology's own sink (a handoff, _route). The top-level set is the
        full technologies.json (also under --frameworks) and our Apple hash
        files that aren't modules' (SinkRegistry.top_level). Scope is never
        decided by substring. Another top-level technology's root is never
        followed: its own job always fetches it (a handoff is for the pages
        it doesn't reach). Each followed link's dir casing and bundle are
        kept for its sink (_route).
        """
        urls: List[str] = []
        top_level: Optional[Set[str]] = None
        for link in page_links.links:
            if link.segment != self.job_id:
                if not link.bundle or link.bundle != page_links.bundle:
                    if self.include_cross_refs:
                        self._track_cross_framework_ref(link.identifier)
                    continue
                if link.json_url == f"{self.site.json_prefix}{link.segment}.json":
                    if top_level is None:
                        top_level = self.sinks.top_level(self.site)
                    if link.segment in top_level:
                        # Another technology's root is its own job's, which
                        # always fetches it (under its id's casing)
                        continue
                self._routes.setdefault(link.segment, (link.dir_name, link.bundle))
            self._check_resolution(link)
            urls.append(link.json_url)
        return urls

    def _check_resolution(self, link: PageLink) -> None:
        """Transition check (log only, temporary): url_resolution_changed when the
        reference's URL isn't the one the identifier gave before 1.1
        (_legacy_identifier_json_url) and that one is a live page of ours: its
        file is superseded (normal orphan cleanup removes it). Expected never
        to fire; remove the check after 2 clean runs with 1.1."""
        legacy = self._legacy_identifier_json_url(link.identifier)
        if legacy is None or legacy == link.json_url:
            return
        if self._is_previously_good(self.hash_manager.hashes.get(legacy)):
            logger.warning("url_resolution_changed", framework=self.framework_name, old=legacy, new=link.json_url)

    def _legacy_identifier_json_url(self, identifier: str) -> Optional[str]:
        """The JSON URL an identifier gave before the resolver (1.1): its path
        lowercased, with the framework's id prepended unless it starts with it."""
        if '/documentation/' not in identifier:
            return None
        path = identifier.split('/documentation/', 1)[1].lower()
        if not path.startswith(f"{self.job_id}/"):
            path = f"{self.job_id}/{path}"
        return f"{self.site.json_prefix}{self._escape_dot_path_segments(path)}.json"
    
    @staticmethod
    def _escape_dot_path_segments(path: str) -> str:
        """Escape path segments starting with '.' by adding apostrophe prefix.

        Apple's server requires path segments starting with dots (like the Swift
        range operators '...' and '..<') to be prefixed with an apostrophe in URLs.
        E.g. identifier path 'comparable/...(_:_:)' -> URL path 'comparable/\'...(_:_:)'
        """
        segments = path.split('/')
        escaped = []
        for seg in segments:
            if seg.startswith('.'):
                escaped.append(f"'{seg}")
            else:
                escaped.append(seg)
        return '/'.join(escaped)

    def _convert_identifier_to_json_url(self, identifier: str) -> Optional[str]:
        """A doc:// identifier's own path as a JSON URL (_page_json_url of what
        follows /documentation/), never with the framework's id prepended.
        None if it has no /documentation/ path."""
        if '/documentation/' not in identifier:
            return None
        return self._page_json_url(identifier.split('/documentation/', 1)[1])
    
    async def scrape_page(self, sink: Sink, url: str) -> Optional[Dict[str, Any]]:
        """Fetch the framework root page and save it if it changed.
        
        Writes the file first, then both hash keys. A failed fetch is never
        treated as a 304: it goes through the failure policy.
        
        Args:
            sink: The page's sink
            url: Documentation URL to scrape
            
        Returns:
            Extracted data if the page was saved, None if failed/unchanged
        """
        # Convert to JSON URL
        json_url = self._convert_doc_url_to_json_url(url)
        
        # Check if we have an ETag for this JSON URL
        hm = sink.hash_manager
        stored_etag = hm.get_etag(json_url)
        
        # Fetch JSON data with ETag support
        result = await self.fetch_page_with_etag(json_url, hash_manager=hm)
        if isinstance(result, FetchFailed):
            self._handle_fetch_failure(sink, json_url, result)
            return None
        if result is NOT_MODIFIED:
            # 304 Not Modified (content unchanged)
            if self._is_root(json_url):
                self._root_ok = True
            if stored_etag:
                # 304 response - content unchanged - touch the entries
                logger.debug("content_unchanged_via_etag", url=url, json_url=json_url)
                
                # Reuse the stored file_path (skip expensive recalculation)
                existing = hm.hashes.get(json_url) or hm.hashes.get(url) or {}
                file_path = Path(existing['file_path']) if existing.get('file_path') else self._get_organized_file_path(sink, url, {})
                
                # Touch both URLs' entries, so orphan detection keeps the file,
                # and record the file on both. Only a missing file_path or a
                # missing key (created with the stored etag) changes an entry,
                # so a 304 alone leaves the hash file as it is.
                for key in (json_url, url):
                    if key not in hm.hashes:
                        hm.hashes[key] = {'etag': stored_etag}
                    hm.touch(key)
                    hm.set_file_path(key, file_path)
                
                self.stats["pages_skipped"] += 1
            return None
        
        response_text, etag = result
        
        try:
            json_data = json.loads(response_text)
        except json.JSONDecodeError as e:
            logger.error("json_parse_error", url=json_url, error=str(e))
            self._handle_fetch_failure(sink, json_url, self._invalid_json_failure())
            return None
        sink.fetch_ok.add(json_url)
        if self._is_root(json_url):
            self._root_ok = True
        
        # Check hash to avoid re-processing unchanged content
        if not hm.has_changed(json_url, response_text, etag) and not hm.has_changed(url, response_text, etag):
            logger.debug("content_unchanged", url=url)
            
            # Content unchanged, but both keys are still touched for orphan detection
            try:
                page_data = self._extract_from_json(sink, json_data, url)
                if page_data:
                    file_path = self._get_organized_file_path(sink, url, page_data)
                    # Touch both keys and record the new etag
                    hm.update_hash(json_url, response_text, etag, file_path)
                    hm.update_hash(url, response_text, etag, file_path)
            except Exception as e:
                logger.warning("failed_to_touch_unchanged_root", url=url, error=str(e))
            
            self.stats["pages_skipped"] += 1
            return None
        
        # Basic validation
        if not self._validate_json_structure(json_data):
            logger.warning("invalid_json_structure", url=json_url)
            self.stats["pages_failed"] += 1
            return None
        
        # Extract, convert and save, then record both hash keys. Only this
        # try counts as a local error: the root's links are enqueued when it
        # is processed again as the first queued URL.
        try:
            data = self._extract_from_json(sink, json_data, url)
            
            if not data:
                logger.warning("no_data_extracted", url=url)
                self.stats["pages_failed"] += 1
                return None
                
            # Calculate file path for hash updates
            file_path = self._get_organized_file_path(sink, url, data)
            
            # Write the file first, then both hash keys
            saved = await self._save_and_record(sink, json_url, url, data, file_path, response_text, etag)
        except Exception as e:
            self._handle_local_error(sink, json_url, e)
            return None
        sink.saved_ok.add(json_url)
        if not saved:
            return None
        self.stats["pages_scraped"] += 1
        return data
    
    def _invalid_json_failure(self) -> FetchFailed:
        """A 200 whose body isn't JSON, as the transient failure it is treated as."""
        self.stats["pages_failed"] += 1
        return FetchFailed(status=200, error=INVALID_JSON, transient=True)
    
    def _extract_from_json(self, sink: Sink, json_data: Dict[str, Any], doc_url: str) -> Dict[str, Any]:
        """Extract structured data from Apple's JSON format.
        
        Args:
            sink: The page's sink (its framework, and the dir its links are relative to)
            json_data: Parsed JSON data
            doc_url: Original documentation URL
            
        Returns:
            Extracted data in our format
        """
        # Store current URL and sink for relative path calculation
        self._current_scraping_url = doc_url
        self._current_sink = sink
        
        data: Dict[str, Any] = {
            'source_url': doc_url,
            'framework': sink.framework_name,
            'framework_id': sink.dir_name
        }
        
        for key in json_data:
            if key not in KNOWN_TOP_LEVEL_KEYS:
                self._note_unknown('top-level key', key)

        # Extract comprehensive metadata
        metadata = json_data.get('metadata', {})
        for key in metadata:
            if key not in KNOWN_METADATA_KEYS:
                self._note_unknown('metadata key', key)
        data['title'] = metadata.get('title', 'Untitled')
        
        # Extract additional metadata fields
        data['external_id'] = metadata.get('externalID', '')
        data['symbol_kind'] = metadata.get('symbolKind') or ''  # JSON null -> ''
        data['navigator_title'] = metadata.get('navigatorTitle', '')
        data['role_heading'] = metadata.get('roleHeading') or ''
        data['required'] = metadata.get('required', False)
        data['modules'] = metadata.get('modules', [])
        
        # Extract symbol fragments for detailed signature information
        if 'fragments' in metadata:
            fragments = metadata['fragments']
            data['fragments'] = [
                {
                    'kind': frag.get('kind', ''),
                    'text': frag.get('text', ''),
                    'preciseIdentifier': frag.get('preciseIdentifier', '')
                }
                for frag in fragments
            ]
        
        # Extract references for later resolution
        references = json_data.get('references', {})
        
        # Extract abstract/brief description
        abstract = json_data.get('abstract', [])
        if abstract:
            data['brief_description'] = self._resolve_inline_content(abstract, references)
        
        # Sample code: its project's download (a header line)
        download = self._sample_download(json_data, references)
        if download:
            data['sample_download'] = download

        # Extract comprehensive availability information. A platform is
        # deprecated when it has deprecatedAt or deprecated: true (Apple often
        # sets only the version); a missing introduced version leaves the
        # bare platform name
        platforms = metadata.get('platforms', [])
        data['availability'] = []
        messages: List[str] = []
        for p in platforms:
            availability_info = {
                'platform': p.get('name', 'Unknown'),
                'introduced': p.get('introducedAt') or '',
                'deprecated': bool(p.get('deprecated', False) or p.get('deprecatedAt')),
                'beta': p.get('beta', False)
            }
            
            # Add deprecation details if available
            if p.get('deprecatedAt'):
                availability_info['deprecated_at'] = p['deprecatedAt']
            if p.get('renamed'):
                availability_info['renamed'] = p['renamed']
            if p.get('message') and p['message'] not in messages:
                messages.append(p['message'])
            
            # Add beta information
            if p.get('isBeta', False):
                availability_info['beta'] = True
            
            # Add unconditionally deprecated flag
            if p.get('unconditionallyDeprecated', False):
                availability_info['unconditionally_deprecated'] = True
            
            data['availability'].append(availability_info)
        
        # The deprecation summary, once: Apple's, or else the platforms' message
        deprecation = self._deprecation_summary(json_data.get('deprecationSummary') or [], messages, references)
        if deprecation:
            data['deprecation_summary'] = deprecation

        # Extract diff availability for version changes
        if 'diffAvailability' in json_data:
            diff_availability = json_data['diffAvailability']
            data['diff_availability'] = {
                'major': diff_availability.get('major', []),
                'minor': diff_availability.get('minor', [])
            }
        
        # Extract declarations: one fence each, Swift first, then the
        # Objective-C/C variant; a symbol's other overloads after them
        primary_content = json_data.get('primaryContentSections', [])
        data['declaration'], data['other_declarations'] = self._extract_declarations(json_data, primary_content)

        # The constraints a symbol is available under ("Available when …")
        conformance = metadata.get('conformance')
        if isinstance(conformance, dict) and conformance.get('constraints'):
            prefix = self._resolve_inline_content(conformance.get('availabilityPrefix') or [], references)
            constraints = self._resolve_inline_content(conformance['constraints'], references)
            data['conformance'] = f"{prefix} {constraints}".strip()
        
        # Extract all content sections comprehensively
        content_sections = self._extract_all_content_sections(primary_content, references, data['title'])
        data.update(content_sections)
        
        # Extract parameters
        parameters = []
        for section in primary_content:
            if section.get('kind') == 'parameters':
                for param in section.get('parameters', []):
                    param_data = {
                        'name': param.get('name', ''),
                        'description': ''
                    }
                    # Extract description from content (may have multiple paragraphs, termLists, etc.)
                    content = param.get('content', [])
                    desc_parts = self._process_content_items(content, references)
                    param_data['description'] = join_blocks(desc_parts, 2)
                    
                    parameters.append(param_data)
        
        data['parameters'] = parameters
        
        # Extract topics with complete signatures and descriptions from references
        data['topics'] = self._topic_groups(json_data.get('topicSections', []), references)

        # The default implementations of a protocol requirement
        data['default_implementations'] = self._topic_groups(
            json_data.get('defaultImplementationsSections') or [], references)

        # Extract see also, by group, with complete signatures
        data['see_also'] = self._topic_groups(json_data.get('seeAlsoSections', []), references)

        # Extract relationships (Inherited By, Conforming Types, etc.)
        relationships = []
        for section in json_data.get('relationshipsSections', []):
            relationship = {
                'title': section.get('title', ''),
                'type': section.get('type', ''),
                'items': []
            }
            for identifier in section.get('identifiers', []):
                if identifier in references:
                    ref_data = references[identifier]
                    name = ref_data.get('title', identifier.split('/')[-1])
                    relationship['items'].append({
                        'name': name,
                        'url': self._reference_url(ref_data.get('url', ''))
                    })
            if relationship['items']:
                relationships.append(relationship)

        data['relationships'] = relationships

        # Extract mentions (related documentation links)
        mentions = []
        for section in primary_content:
            if section.get('kind') == 'mentions':
                mention_items = section.get('mentions', [])
                for mention in mention_items:
                    if mention in references:
                        ref_data = references[mention]
                        mentions.append({
                            'title': ref_data.get('title', mention.split('/')[-1]),
                            'url': self._reference_url(ref_data.get('url', ''))
                        })

        data['mentions'] = mentions

        # Extract variants (different language implementations)
        if 'variants' in json_data:
            variants = json_data['variants']
            data['variants'] = [
                {
                    'traits': variant.get('traits', []),
                    'paths': variant.get('paths', [])
                }
                for variant in variants
            ]

        # Extract hierarchy information for navigation
        if 'hierarchy' in json_data:
            hierarchy = json_data['hierarchy']
            data['hierarchy'] = {
                'paths': hierarchy.get('paths', []),
                'modules': hierarchy.get('modules', [])
            }

        return data

    def _note_unknown(self, what: str, name: Any) -> None:
        """Count JSON the converter doesn't know (a block or inline type, a
        section kind, a top-level or metadata key); logged at the end of the
        framework's run (_log_unknown_content)."""
        key = (what, str(name))
        if key not in self._unknown_content:
            self._unknown_examples[key] = getattr(self, '_current_scraping_url', '')
        self._unknown_content[key] += 1

    def _log_unknown_content(self) -> None:
        """One WARN per unknown block or inline type, section kind or key seen this run, with its count."""
        for (what, name), count in sorted(self._unknown_content.items()):
            logger.warning(
                "unknown_content",
                framework=self.framework_name,
                what=what,
                name=name,
                count=count,
                example=self._unknown_examples.get((what, name), '')
            )

    def _reference_url(self, url_path: str) -> str:
        """A reference's URL as linked: the site's root-relative path made
        absolute (self.site.url), an absolute URL (an external link's) as it
        is, "" for a reference without one."""
        if not url_path:
            return ''
        if urlparse(url_path).scheme:
            return url_path
        return self.site.url(url_path)

    @staticmethod
    def _is_symbol_reference(ref_data: Dict[str, Any]) -> bool:
        """Whether a reference's title is shown as code, as DocC-Render does
        (Reference.vue isSymbolReference/isDisplaySymbol): a symbol (not a
        framework, role collection), shown by its symbol name."""
        return (ref_data.get('kind') == 'symbol'
                and ref_data.get('role') in ('symbol', 'dictionarySymbol')
                and (not ref_data.get('ideTitle') or ref_data.get('titleStyle') == 'symbol'))

    def _topic_groups(self, sections: List[Dict[str, Any]], references: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Topic-like sections (topics, default implementations, see also): per
        group its title and items, each with its complete signature, URL and abstract."""
        groups = []
        for section in sections:
            group: Dict[str, Any] = {
                'title': section.get('title', ''),
                'items': []
            }
            for identifier in section.get('identifiers', []):
                # Look up the identifier in references to get complete information
                if identifier in references:
                    ref_data = references[identifier]
                    
                    # Get the full title (which includes complete signature for methods)
                    full_title = ref_data.get('title', identifier.split('/')[-1])
                    
                    # Try to get an even more complete signature from fragments if available
                    if 'fragments' in ref_data:
                        fragments = ref_data['fragments']
                        # Reconstruct full signature from fragments
                        signature_parts = []
                        for frag in fragments:
                            text = frag.get('text', '')
                            if text:
                                signature_parts.append(text)
                        if signature_parts:
                            reconstructed_signature = ''.join(signature_parts)
                            # Use the reconstructed signature if it's more complete than title
                            if len(reconstructed_signature) > len(full_title):
                                full_title = reconstructed_signature
                    
                    # A reference without a URL (Apple's unresolvable ones) is plain text
                    url = self._reference_url(ref_data.get('url', ''))
                    
                    # Extract description/abstract from reference
                    description = ""
                    if 'abstract' in ref_data:
                        abstract_content = ref_data['abstract']
                        description = self._resolve_inline_content(abstract_content, references)
                    
                    group['items'].append({
                        'name': full_title,
                        'url': url,
                        'description': description
                    })
                else:
                    # Fallback for identifiers not in references
                    name = identifier.split('/')[-1] if '/' in identifier else identifier
                    if self.site.is_own_identifier(identifier):
                        parts = identifier.split('/documentation/')
                        if len(parts) == 2:
                            path = parts[1]
                            url = self.site.doc_url(path)
                        else:
                            url = identifier
                    else:
                        url = identifier
                    group['items'].append({
                        'name': name,
                        'url': url,
                        'description': ''
                    })
            
            if group['items']:
                groups.append(group)
        return groups

    def _extract_declarations(
        self, json_data: Dict[str, Any], primary_content: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """The page's declarations, one fence each, and its other overloads.

        Each declaration's language is in its languages: swift, occ (the
        Objective-C/C variant, fenced page-wide as objc, cpp or c), data (no
        tag). Swift comes first, then the page's own declarations in other
        languages, then the occ variant's: its declarations from the occ
        variantOverrides patch that the page doesn't show already. When one
        language has several declarations on different platforms, each is
        labeled with them (*DriverKit*).

        Returns:
            ([{language, code, label}], [{language, code}] of other overloads)
        """
        found: List[Dict[str, Any]] = []
        declarations = [
            self._declaration_item(dec)
            for section in primary_content if section.get('kind') == 'declarations'
            for dec in section.get('declarations', [])
        ]
        for declaration in declarations + self._occ_declarations(json_data):
            if declaration and not any(item['code'] == declaration['code'] for item in found):
                found.append(declaration)
        found.sort(key=lambda item: DECLARATION_ORDER.get(item['language'], 1))

        occ_tag = 'c'
        occ_code = '\n'.join(item['code'] for item in found if item['language'] == 'occ')
        if OBJC_MARKERS.search(occ_code):
            occ_tag = 'objc'
        elif CPP_MARKERS.search(occ_code):
            occ_tag = 'cpp'
        tags = {'swift': 'swift', 'occ': occ_tag, 'data': ''}

        result: List[Dict[str, Any]] = []
        other_declarations: List[Dict[str, Any]] = []
        for item in found:
            same_language = [other for other in found if other['language'] == item['language']]
            platform_labels = len(same_language) > 1 and len({tuple(other['platforms']) for other in same_language}) > 1
            tag = tags.get(item['language'], item['language'])
            result.append({
                'language': tag,
                'code': item['code'],
                'label': ', '.join(item['platforms']) if platform_labels and item['platforms'] else '',
            })
            other_declarations.extend({'language': tag, 'code': other} for other in item['others'])
        return result, other_declarations

    def _declaration_item(self, dec: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """A declaration's language (occ when its languages hold occ, else the
        first, swift without any), platforms, code and its other overloads'
        code; None for a declaration without code."""
        code = self._format_declaration_from_tokens(dec.get('tokens', []))
        if not code:
            return None
        languages = dec.get('languages') or ['swift']
        others = [
            self._format_declaration_from_tokens(other.get('tokens', []))
            for other in (dec.get('otherDeclarations') or {}).get('declarations', [])
        ]
        return {
            'language': 'occ' if 'occ' in languages else languages[0],
            'platforms': [platform for platform in dec.get('platforms') or [] if isinstance(platform, str)],
            'code': code,
            'others': [other for other in others if other],
        }

    def _occ_declarations(self, json_data: Dict[str, Any]) -> List[Optional[Dict[str, Any]]]:
        """The Objective-C/C declarations of the page's occ variant
        (_declaration_item): its variantOverrides patches for
        interfaceLanguage occ applied to a copy of the page (only their
        operations on primaryContentSections, the only part read), and of its
        declarations sections only the declarations whose languages contain
        occ. The variant is optional: when its data can't be read, patched or
        formatted, an occ_variant_patch_failed WARN and none (the page shows
        its own declarations)."""
        try:
            operations = [
                operation
                for override in json_data.get('variantOverrides') or []
                if any(isinstance(trait, dict) and trait.get('interfaceLanguage') == 'occ'
                       for trait in override.get('traits') or [])
                for operation in override.get('patch') or []
                if operation.get('path', '') in ('', '/primaryContentSections')
                or operation.get('path', '').startswith('/primaryContentSections/')
            ]
            if not operations:
                return []
            patched = apply_json_patch(
                {'primaryContentSections': json_data.get('primaryContentSections', [])}, operations)
            sections = patched.get('primaryContentSections') if isinstance(patched, dict) else None
            return [
                self._declaration_item(dec)
                for section in sections or [] if isinstance(section, dict) and section.get('kind') == 'declarations'
                for dec in section.get('declarations', [])
                if 'occ' in (dec.get('languages') or [])
            ]
        except Exception as e:  # malformed variant data: any error, as the variant is optional
            logger.warning("occ_variant_patch_failed", url=getattr(self, '_current_scraping_url', ''),
                           error=f"{type(e).__name__}: {e}")
            return []

    def _deprecation_summary(
        self, summary: List[Dict[str, Any]], messages: List[str], references: Dict[str, Any]
    ) -> str:
        """The page's deprecation summary as a "> **Deprecated**: …" quote
        (quote_blocks): Apple's deprecationSummary (its paragraphs on that
        line, joined with spaces; any other block on the quote's lines after
        it), or else the platforms' messages, each once. "" when there is neither."""
        blocks: List[str] = []
        if summary:
            paragraphs = self._process_content_items(
                [block for block in summary if block.get('type') == 'paragraph'], references)
            if paragraphs:
                blocks.append(' '.join(paragraphs))
            blocks.extend(self._process_content_items(
                [block for block in summary if block.get('type') != 'paragraph'], references))
        elif messages:
            blocks.append(' '.join(messages))
        return quote_blocks("**Deprecated**:", blocks) if blocks else ''

    def _sample_download(self, json_data: Dict[str, Any], references: Dict[str, Any]) -> Optional[Dict[str, str]]:
        """A sample code page's project download, {name, url}: its relative URL
        (<hash>/<name>.zip) under docs-assets; None when the page has none."""
        download = json_data.get('sampleCodeDownload')
        if not isinstance(download, dict):
            return None
        identifier = (download.get('action') or {}).get('identifier', '')
        url = (references.get(identifier) or {}).get('url') or identifier
        if not url:
            return None
        if not urlparse(url).scheme:
            url = f"{DOCS_ASSETS_URL}{url.lstrip('/')}"
        return {'name': url.rstrip('/').rsplit('/', 1)[-1], 'url': url}
    async def save_page_data(
        self, sink: Sink, url: str, data: Dict[str, Any], file_path: Optional[Path] = None
    ) -> bool:
        """Save extracted data as markdown with organized folder structure.
        
        Args:
            sink: The page's sink
            url: Source URL
            data: Extracted data
            file_path: Optional pre-calculated file path
            
        Returns:
            True if the file was written, False if its path was unsafe
        """
        # Convert to markdown
        markdown_content = sink.markdown_converter.convert_page(data)
        
        # Determine organized file path if not provided
        if file_path is None:
            file_path = self._get_organized_file_path(sink, url, data)

        # Containment guard: never write outside the sink's output dir
        # (mirrors the MLX scraper's is_safe_path; traversal is neutralized
        # upstream, this is defense in depth at the write sink).
        resolved = file_path.resolve()
        output_root = sink.output_dir.resolve()
        if resolved != output_root and output_root not in resolved.parents:
            logger.error("unsafe_file_path_skipped", url=url, path=str(file_path))
            return False

        # Creates the framework's output dir too, on its first file
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save markdown file (whole or not at all: a failed write keeps the old doc)
        write_text_atomic(file_path, markdown_content)
        
        # Log the save for real-time feedback in Finder
        try:
            relative_path = file_path.relative_to(Path.cwd())
        except ValueError:
            relative_path = file_path
        
        logger.info(
            "file_saved",
            file=str(relative_path),
            size=len(markdown_content),
            url=url
        )
        return True
    
    def _get_organized_file_path(self, sink: Sink, url: str, data: Dict[str, Any]) -> Path:
        """The page's file: the docs root (Config.OUTPUT_DIR) / naming.page_path.

        The path is a function of the URL alone (data isn't read), so the
        filename migration, links and the tripwire compute the same path.
        The framework segment matches case-insensitively: Apple emits URL
        casing inconsistently over time ('XCTest' vs 'xctest'), but the URL
        space itself is case-insensitive.

        Args:
            sink: The page's sink (its dir names the framework segment)
            url: The page's documentation URL
            data: The page's extracted data (unused)

        Returns:
            The file's path, documentation/<dir_name>/….md by default
        """
        relative = page_path(sink.dir_name, url)
        if relative is None:
            # Not a page of this framework (never crawled): a file named
            # after the whole URL in the sink's dir
            logger.warning("failed_to_parse_url_path", url=url, framework_id=sink.dir_name)
            safe_url = url.replace('https://', '').replace('http://', '').replace('/', '-')
            return sink.output_dir / f"{seg_name(safe_url)}.md"
        return Config.OUTPUT_DIR / relative

    def _convert_apple_url_to_local_path(self, apple_url: str) -> str:
        """The link to a referenced page from the page being converted (self._current_scraping_url).

        links.doc_link: the referenced page's file relative to this page's
        file in its sink's dir (self._current_sink), when its framework is a
        known dir (the sink's known_dirs); else its URL as it is.

        Args:
            apple_url: The referenced page's URL (_reference_url)
        """
        base = link_base(self._current_sink.dir_name, self._current_scraping_url)
        return doc_link(apple_url, base, self._current_sink.known_dirs)
    
    def _format_declaration_from_tokens(self, tokens: List[Dict[str, Any]]) -> str:
        """Format declaration tokens with proper Swift formatting.
        
        Args:
            tokens: List of token dictionaries from Apple's JSON
            
        Returns:
            Formatted declaration string
        """
        if not tokens:
            return ""
        
        parts = []
        
        # Check if declaration starts with attributes
        has_leading_attributes = False
        attribute_text = []
        i = 0
        
        # Collect all leading attributes
        while i < len(tokens) and tokens[i].get('kind') == 'attribute':
            attribute_text.append(tokens[i].get('text', ''))
            i += 1
            has_leading_attributes = True
        
        # If we have attributes, add them on their own line
        if has_leading_attributes:
            parts.append(''.join(attribute_text))
            # Skip whitespace after attributes
            while i < len(tokens) and tokens[i].get('text', '').strip() == '':
                i += 1
        
        # Add the rest of the declaration
        remaining = []
        for j in range(i, len(tokens)):
            remaining.append(tokens[j].get('text', ''))
        
        if remaining:
            parts.append(''.join(remaining))
        
        # Join lines
        result = '\n'.join(parts)
        
        # Additional formatting for long function signatures
        # If it's a function with multiple parameters and > 100 chars, format it
        if 'func ' in result and result.count(',') >= 2 and len(result) > 100:
            # This is a heuristic - in practice Apple's formatting is more complex
            # For now, keep single line to match most common cases
            pass
        
        return result
    
    def _validate_json_structure(self, json_data: Dict[str, Any]) -> bool:
        """Validate basic JSON structure from Apple API.
        
        Args:
            json_data: Parsed JSON to validate
            
        Returns:
            True if structure is valid
        """
        # Basic validation - check for required top-level fields
        required_fields = ['metadata', 'identifier']
        if not all(field in json_data for field in required_fields):
            return False
        
        # Check metadata structure
        metadata = json_data.get('metadata', {})
        if not isinstance(metadata, dict):
            return False
        
        return True
    
    def _resolve_inline_content(self, inline_content: List[Dict[str, Any]], references: Dict[str, Any]) -> str:
        """Resolve inline content with proper reference resolution.
        
        Args:
            inline_content: List of inline content items from Apple's JSON
            references: References dictionary for resolving identifiers
            
        Returns:
            Resolved text content
        """
        resolved_parts = []
        
        for item in inline_content:
            item_type = item.get('type', '')
            
            if item_type == 'text':
                resolved_parts.append(self._rewrite_doc_literals(item.get('text', '')))
            elif item_type == 'reference':
                # Resolve the reference to its actual name and create a proper link
                identifier = item.get('identifier', '')
                if identifier in references:
                    ref_data = references[identifier]
                    if item.get('overridingTitleInlineContent'):
                        # The prose's own wording, formatted as Apple wrote it
                        text = self._resolve_inline_content(item['overridingTitleInlineContent'], references)
                    elif item.get('overridingTitle'):
                        text = item['overridingTitle']
                    else:
                        # Code voice only for a symbol, as DocC-Render shows it
                        title = ref_data.get('title', identifier.split('/')[-1])
                        text = f"`{title}`" if self._is_symbol_reference(ref_data) else title
                    
                    # Get the URL for the reference
                    url = self._reference_url(ref_data.get('url', ''))
                    if url:
                        # Convert Apple URL to local markdown path
                        local_path = self._convert_apple_url_to_local_path(url)
                        # Create a markdown link to local file
                        resolved_parts.append(f"[{text}]({local_path})")
                    else:
                        # A reference without a URL (unresolvable) is plain text
                        resolved_parts.append(text)
                else:
                    # Fallback to the last part of the identifier
                    fallback = identifier.split('/')[-1] if '/' in identifier else identifier
                    resolved_parts.append(f"`{fallback}`")
            elif item_type == 'codeVoice':
                resolved_parts.append(f"`{item.get('code', '')}`")
            elif item_type == 'emphasis':
                # Italic text - recursively resolve nested content
                inner = self._resolve_inline_content(item.get('inlineContent', []), references)
                resolved_parts.append(f"*{inner}*")
            elif item_type == 'strong':
                # Bold text - recursively resolve nested content
                inner = self._resolve_inline_content(item.get('inlineContent', []), references)
                resolved_parts.append(f"**{inner}**")
            elif item_type == 'strikethrough':
                inner = self._resolve_inline_content(item.get('inlineContent', []), references)
                resolved_parts.append(f"~~{inner}~~")
            elif item_type == 'image':
                # Handle inline images
                image_content = self._process_image(item, references)
                resolved_parts.append(image_content)
            else:
                # Not rendered above: its text, never silently dropped, and a
                # WARN for a type that isn't known. On one line (each line break
                # a space, its other spaces kept): a block under it (a code
                # listing's fence, a list) can't break the paragraph
                if str(item_type) not in KNOWN_INLINE_TYPES:
                    self._note_unknown('inline type', item_type)
                resolved_parts.append(re.sub(
                    r'\s*\n\s*', ' ', ' '.join(self._fallback_parts(item, references, inline=True))))
        
        return ''.join(resolved_parts)
    
    def _rewrite_doc_literals(self, text: str) -> str:
        """A doc://<bundle>/<rest> link written as text, as its web URL: the
        site's page (self.site.doc_url) at <rest without a leading
        "documentation" and its slash>. A trailing ".", "," or ";" stays outside."""
        if 'doc://' not in text:
            return text

        def web_url(match: re.Match[str]) -> str:
            literal = match.group(0)
            stripped = literal.rstrip('.,;')
            rest = stripped.split('/', 3)[3] if stripped.count('/') >= 3 else ''
            if rest.startswith('documentation'):
                rest = rest[len('documentation'):]
            if rest.startswith('/'):
                rest = rest[1:]
            return f"{self.site.doc_url(rest)}{literal[len(stripped):]}"

        return DOC_LITERAL.sub(web_url, text)

    def _fallback_blocks(self, item: Dict[str, Any], references: Dict[str, Any]) -> List[str]:
        """The text of a block or section the converter doesn't render, as
        blocks (_fallback_parts), so that its content is never silently lost."""
        return [part for part in self._fallback_parts(item, references) if part.strip()]

    def _fallback_parts(
        self, item: Dict[str, Any], references: Dict[str, Any], inline: bool = False
    ) -> List[str]:
        """The text of a block, inline item or section the converter doesn't
        render: every value under it but its type name, in order, recursively
        (_fallback_value). inline: the item is inline content (code lines
        stay inline code)."""
        return [part for key, value in item.items() if not (key == 'type' and isinstance(value, str))
                for part in self._fallback_value(key, value, references, inline)]

    def _fallback_value(self, key: str, value: Any, references: Dict[str, Any], inline: bool) -> List[str]:
        """The text a value under key holds, recursively. A list holding known
        blocks (KNOWN_BLOCK_TYPES) is rendered as blocks, one holding known
        inline items (KNOWN_INLINE_TYPES) as one paragraph, and a dict of a
        known type as such; a list of untyped text fragments (tokens) is one
        text; in any other dict or list, each value the same way. A "text"
        string is text and a "code" string inline code; a "code" list of lines
        is an untagged code listing (inline code when inline). Other strings
        (identifiers, anchors, styles, syntax names) aren't text."""
        if isinstance(value, dict):
            if str(value.get('type')) in KNOWN_BLOCK_TYPES:
                return self._process_content_items([value], references)
            if str(value.get('type')) in KNOWN_INLINE_TYPES:
                return [self._resolve_inline_content([value], references)]
            return self._fallback_parts(value, references, inline)
        if isinstance(value, list):
            items = [v for v in value if isinstance(v, dict)]
            types = {v['type'] for v in items if isinstance(v.get('type'), str)}
            if types & KNOWN_BLOCK_TYPES:
                return self._process_content_items(items, references)
            if types & KNOWN_INLINE_TYPES:
                return [self._resolve_inline_content(items, references)]
            if key == 'code' and value and all(isinstance(line, str) for line in value):
                return [f"`{' '.join(value)}`" if inline else '```\n' + '\n'.join(value) + '\n```']
            if items and len(items) == len(value) and not types and all(
                    isinstance(v.get('text'), str) for v in items):
                return [''.join(v['text'] for v in items)]
            return [part for v in value for part in self._fallback_value(key, v, references, inline)]
        if isinstance(value, str) and key == 'text':
            return [self._rewrite_doc_literals(value)]
        if isinstance(value, str) and key == 'code' and value:
            return [f"`{value}`"]
        return []

    def _format_attributes(self, attributes: List[Dict[str, Any]]) -> List[str]:
        """A property's, parameter's or key's attributes, one "**Label**: value" each."""
        parts = []
        for attr in attributes or []:
            attr_kind = attr.get('kind', '')
            attr_value = attr.get('value', '')
            if attr_kind == 'allowedValues':
                values = attr.get('values', [])
                if values:
                    parts.append(f"**Allowed Values**: {', '.join(f'`{v}`' for v in values)}")
            elif attr_kind == 'allowedTypes':
                types = [''.join(t.get('text', '') for t in tokens) for tokens in attr.get('values', [])]
                if any(types):
                    parts.append(f"**Allowed Types**: {', '.join(f'`{t}`' for t in types if t)}")
            elif attr_kind in ATTRIBUTE_LABELS and attr_value:
                parts.append(f"**{ATTRIBUTE_LABELS[attr_kind]}**: `{attr_value}`")
        return parts

    def _format_rest_item(self, item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """A REST parameter's or an object property's list item: name, type,
        required and deprecated flags, then its description and attributes."""
        name = item.get('name', '')
        type_text = ''.join(t.get('text', '') for t in item.get('type', []))
        markers = (" *(required)*" if item.get('required', False) else "") + (
            " *(deprecated)*" if item.get('deprecated', False) else "")
        blocks = self._process_content_items(item.get('content', []), references)
        attributes = self._format_attributes(item.get('attributes', []))
        if attributes:
            blocks = blocks + ['; '.join(attributes)]
        desc = join_blocks(blocks, 2).strip()
        head = f"- `{name}` ({type_text}){markers}" if type_text else f"- `{name}`{markers}"
        return labeled(f"{head}:", desc, 2) if desc else head

    def _extract_all_content_sections(
        self, primary_content: List[Dict[str, Any]], references: Dict[str, Any], title: str = ''
    ) -> Dict[str, Any]:
        """Extract all content from primaryContentSections comprehensively.
        
        Args:
            primary_content: List of primary content sections
            references: References for resolving inline content
            title: The page's title (a key's Details show its Xcode title when it differs)
            
        Returns:
            Dictionary of extracted content
        """
        extracted: Dict[str, Any] = {}
        
        for section in primary_content:
            kind = section.get('kind', '')
            
            if kind == 'content':
                # General content - preserve the full structure
                content_items = section.get('content', [])
                content_parts = self._process_content_items(content_items, references)
                if content_parts:
                    # Instead of separating into overview/discussion, keep as one structured content
                    full_content = '\n\n'.join(content_parts)
                    if 'content' not in extracted:
                        extracted['content'] = full_content
                    else:
                        extracted['content'] += '\n\n' + full_content
            
            elif kind == 'discussion':
                # Explicit discussion section
                content_items = section.get('content', [])
                discussion_parts = self._process_content_items(content_items, references)
                if discussion_parts:
                    extracted['discussion'] = '\n\n'.join(discussion_parts)
            
            elif kind == 'returnValue':
                # Return value documentation
                content_items = section.get('content', [])
                return_parts = self._process_content_items(content_items, references)
                if return_parts:
                    extracted['return_value'] = '\n\n'.join(return_parts)
            
            elif kind == 'task':
                # Task/tutorial sections
                content_items = section.get('content', [])
                task_parts = self._process_content_items(content_items, references)
                if task_parts:
                    if 'tasks' not in extracted:
                        extracted['tasks'] = []
                    extracted['tasks'].append({
                        'title': section.get('title', 'Task'),
                        'content': '\n\n'.join(task_parts)
                    })
            
            elif kind == 'restBody':
                # REST API body: its content type and type, description and parameters
                body_head = []
                if section.get('mimeType'):
                    body_head.append(f"**Content-Type**: `{section['mimeType']}`")
                body_type = ''.join(t.get('text', '') for t in section.get('bodyContentType', []))
                if body_type:
                    body_head.append(f"**Type**: `{body_type}`")
                rest_parts = ['  \n'.join(body_head)] if body_head else []
                rest_parts.extend(self._process_content_items(section.get('content', []), references))
                body_parameters = [self._format_rest_item(p, references) for p in section.get('parameters', [])]
                if body_parameters:
                    rest_parts.append('\n'.join(body_parameters))
                if rest_parts:
                    extracted['rest_body'] = '\n\n'.join(rest_parts)
            
            elif kind == 'restResponses':
                # REST API responses: per status, its reason, type and MIME type, and description
                response_parts = self._process_content_items(section.get('content', []), references)
                response_lines = []
                for item in section.get('items', []):
                    head = f"- `{item.get('status', '')}`"
                    if item.get('reason'):
                        head += f" {item['reason']}"
                    extras = []
                    type_text = ''.join(t.get('text', '') for t in item.get('type', []))
                    if type_text:
                        extras.append(f"`{type_text}`")
                    if item.get('mimeType'):
                        extras.append(f"`{item['mimeType']}`")
                    if extras:
                        head += f" ({', '.join(extras)})"
                    desc = join_blocks(self._process_content_items(item.get('content', []), references), 2).strip()
                    response_lines.append(labeled(f"{head}:", desc, 2) if desc else head)
                if response_lines:
                    response_parts.append('\n'.join(response_lines))
                if response_parts:
                    extracted['rest_responses'] = '\n\n'.join(response_parts)
            
            elif kind == 'possibleValues':
                # Possible values of a key, property or REST type (shown after the Declaration)
                value_lines = []
                for value in section.get('values', []):
                    desc = join_blocks(self._process_content_items(value.get('content', []), references), 2).strip()
                    name = f"`{value.get('name', '')}`"
                    value_lines.append(labeled(f"- {name}:", desc, 2) if desc else f"- {name}")
                if value_lines:
                    extracted.setdefault('detail_sections', []).append({
                        'title': section.get('title') or 'Possible Values',
                        'content': '\n'.join(value_lines)
                    })
            
            elif kind == 'thrown_errors':
                # Error documentation
                content_items = section.get('content', [])
                error_parts = self._process_content_items(content_items, references)
                if error_parts:
                    extracted['thrown_errors'] = '\n\n'.join(error_parts)

            elif kind == 'details':
                # A key's details (shown after the Declaration): its raw name,
                # its Xcode title when that isn't the page's title, its type
                details = section.get('details', {})
                detail_lines = []
                if details.get('name'):
                    name_line = f"- **Name**: `{details['name']}`"
                    if details.get('ideTitle') and details['ideTitle'] != title:
                        name_line += f" ({details['ideTitle']})"
                    detail_lines.append(name_line)
                types = [
                    f"array of {v['baseType']}" if v.get('arrayMode') else v['baseType']
                    for v in details.get('value', []) if v.get('baseType')
                ]
                if types:
                    detail_lines.append(f"- **Type**: {', '.join(types)}")
                if detail_lines:
                    extracted.setdefault('detail_sections', []).append({
                        'title': section.get('title') or 'Details',
                        'content': '\n'.join(detail_lines)
                    })

            elif kind == 'attributes':
                # Default value and other attributes
                attr_parts = self._format_attributes(section.get('attributes', []))
                if attr_parts:
                    if 'content' not in extracted:
                        extracted['content'] = ''
                    extracted['content'] += '\n\n' + '\n\n'.join(attr_parts)

            elif kind == 'properties':
                # Object properties (common in App Store Connect API)
                prop_parts = [self._format_rest_item(prop, references) for prop in section.get('items', [])]
                if prop_parts:
                    extracted['properties'] = '\n'.join(prop_parts)

            elif kind == 'restEndpoint':
                # REST API endpoint URL
                tokens = section.get('tokens', [])
                endpoint = ''.join(t.get('text', '') for t in tokens)
                if endpoint:
                    extracted['rest_endpoint'] = endpoint

            elif kind == 'restParameters':
                # REST API parameters, one group per section (path, query, header)
                param_parts = [self._format_rest_item(param, references) for param in section.get('items', [])]
                if param_parts:
                    extracted.setdefault('rest_parameters', []).append({
                        'title': section.get('title', ''),
                        'items': '\n'.join(param_parts)
                    })

            elif kind not in KNOWN_SECTION_KINDS:
                # Unknown: its text, never silently dropped
                self._note_unknown('section kind', kind)
                fallback_parts = self._fallback_blocks(section, references)
                if fallback_parts:
                    fallback_content = '\n\n'.join(fallback_parts)
                    if 'content' not in extracted:
                        extracted['content'] = fallback_content
                    else:
                        extracted['content'] += '\n\n' + fallback_content

        return extracted
    
    def _process_content_items(self, content_items: List[Dict[str, Any]], references: Dict[str, Any]) -> List[str]:
        """Process a list of content items recursively.
        
        Args:
            content_items: List of content items to process
            references: References for resolving inline content
            
        Returns:
            List of processed content strings
        """
        processed_parts = []
        
        for item in content_items:
            item_type = item.get('type', '')
            
            if item_type == 'paragraph':
                # Standard paragraph
                resolved_content = self._resolve_inline_content(item.get('inlineContent', []), references)
                if resolved_content.strip():
                    processed_parts.append(resolved_content)
            
            elif item_type == 'heading':
                # Headings: DocC writes the text in text
                level = item.get('level', 1)
                heading_text = item.get('text') or ''
                if not heading_text.strip():
                    heading_text = self._resolve_inline_content(item.get('inlineContent', []), references)
                
                # If heading is empty but has an anchor, convert anchor to heading text
                if not heading_text.strip() and 'anchor' in item:
                    anchor = item['anchor']
                    # Convert anchor format to readable heading
                    # e.g., "Enable-the-Audio-Background-Mode" -> "Enable the Audio Background Mode"
                    heading_text = anchor.replace('-', ' ')
                    # Capitalize appropriately (title case)
                    heading_text = ' '.join(word.capitalize() for word in heading_text.split())
                    # Special case for common words that shouldn't be capitalized
                    lowercase_words = {'the', 'and', 'or', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'a', 'an'}
                    words = heading_text.split()
                    heading_text = ' '.join(
                        word if i == 0 or word.lower() not in lowercase_words else word.lower()
                        for i, word in enumerate(words)
                    )
                
                if heading_text.strip():
                    heading_prefix = '#' * min(level + 2, 6)  # Adjust level for markdown
                    processed_parts.append(f"{heading_prefix} {heading_text}")
            
            elif item_type == 'codeListing':
                # Code blocks (already handled elsewhere but ensuring completeness);
                # a null syntax gets no language tag, a missing one swift
                code_lines = item.get('code', [])
                if code_lines:
                    code = '\n'.join(code_lines)
                    language = item.get('syntax', 'swift')
                    processed_parts.append(f"```{language if language is not None else ''}\n{code}\n```")
            
            elif item_type == 'unorderedList':
                # Unordered lists: an item's later blocks on their own lines, under it
                list_items = item.get('items', [])
                list_parts = []
                for list_item in list_items:
                    list_content = self._process_content_items(list_item.get('content', []), references)
                    if list_content:
                        list_parts.append(f"- {join_blocks(list_content, 2)}")
                if list_parts:
                    processed_parts.append('\n'.join(list_parts))
            
            elif item_type == 'orderedList':
                # Ordered lists
                list_items = item.get('items', [])
                list_parts = []
                for i, list_item in enumerate(list_items, 1):
                    list_content = self._process_content_items(list_item.get('content', []), references)
                    if list_content:
                        marker = f"{i}. "
                        list_parts.append(f"{marker}{join_blocks(list_content, len(marker))}")
                if list_parts:
                    processed_parts.append('\n'.join(list_parts))
            
            elif item_type == 'table':
                # Tables (basic implementation)
                table_content = self._process_table(item, references)
                if table_content:
                    processed_parts.append(table_content)
            
            elif item_type == 'aside':
                # Callouts/notes/warnings
                aside_content = self._process_aside(item, references)
                if aside_content:
                    processed_parts.append(aside_content)
            
            elif item_type == 'imageBlock':
                # Images
                image_content = self._process_image(item, references)
                if image_content:
                    processed_parts.append(self._with_caption(image_content, item, references))

            elif item_type == 'termList':
                # Definition lists (term + definition pairs)
                term_parts = []
                for term_item in item.get('items', []):
                    term = term_item.get('term', {})
                    term_text = self._resolve_inline_content(term.get('inlineContent', []), references)
                    definition = term_item.get('definition', {})
                    def_content = self._process_content_items(definition.get('content', []), references)
                    if term_text:
                        term_parts.append(labeled(f"- **{term_text}**:", join_blocks(def_content, 2), 2))
                if term_parts:
                    processed_parts.append('\n'.join(term_parts))

            elif item_type == 'thematicBreak':
                # Horizontal rule
                processed_parts.append('---')

            elif item_type == 'tabNavigator':
                # Tabbed content (e.g., Swift/Objective-C code examples)
                tabs = item.get('tabs', [])
                for tab in tabs:
                    title = tab.get('title', '')
                    tab_content = tab.get('content', [])
                    tab_parts = self._process_content_items(tab_content, references)
                    if tab_parts:
                        if len(tabs) > 1 and title:
                            processed_parts.append(f"**{title}**:")
                        processed_parts.extend(tab_parts)

            elif item_type == 'row':
                # Grid layout: each column's content, in order
                for column in item.get('columns', []):
                    processed_parts.extend(self._process_content_items(column.get('content', []), references))

            elif item_type == 'links':
                # A list of links to other pages, each with its abstract
                link_lines = []
                for identifier in item.get('items', []):
                    link = self._resolve_inline_content(
                        [{'type': 'reference', 'identifier': identifier, 'isActive': True}], references)
                    if not link:
                        continue
                    link_lines.append(f"- {link}")
                    abstract = (references.get(identifier) or {}).get('abstract') or []
                    abstract_text = self._resolve_inline_content(abstract, references)
                    if abstract_text.strip():
                        link_lines.append(f"  {abstract_text}")
                if link_lines:
                    processed_parts.append('\n'.join(link_lines))

            elif item_type == 'video':
                video_content = self._process_video(item, references)
                if video_content:
                    processed_parts.append(self._with_caption(video_content, item, references))

            else:
                # Not rendered above: its text, never silently dropped, and a
                # WARN for a type that isn't known
                if str(item_type) not in KNOWN_BLOCK_TYPES:
                    self._note_unknown('block type', item_type)
                processed_parts.extend(self._fallback_blocks(item, references))
                continue

            # Handle any nested content recursively for item types that don't process content themselves
            # Skip recursive processing for items that handle their own content (aside, table, termList, tabNavigator, etc.)
            if ('content' in item and isinstance(item['content'], list) and
                item_type not in ['aside', 'table', 'imageBlock', 'termList', 'tabNavigator']):
                nested_content = self._process_content_items(item['content'], references)
                processed_parts.extend(nested_content)
        
        return processed_parts
    
    def _process_table(self, table_item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """Process table content into markdown format."""
        rows = table_item.get('rows', [])
        
        if not rows:
            return ""
        
        markdown_lines = []
        
        # In Apple's format, the header is often just "row" and actual headers are in first row
        # Process all rows, treating first row as potential header
        for row_idx, row in enumerate(rows):
            row_cells = []
            
            for cell in row:
                # Cell can be a list of content items
                if isinstance(cell, list):
                    # Extract text from all content items in the cell
                    cell_parts = []
                    for content_item in cell:
                        if isinstance(content_item, dict):
                            # Process the content item
                            processed = self._process_content_items([content_item], references)
                            if processed:
                                cell_parts.extend(processed)
                    
                    # Join all parts with space and clean up
                    cell_text = ' '.join(cell_parts).strip()
                    # Replace newlines with spaces in table cells
                    cell_text = cell_text.replace('\n', ' ')
                    row_cells.append(cell_text)
                elif isinstance(cell, dict):
                    # Single content item
                    processed = self._process_content_items([cell], references)
                    cell_text = ' '.join(processed).strip().replace('\n', ' ')
                    row_cells.append(cell_text)
                else:
                    # Plain text or other format
                    row_cells.append(str(cell))
            
            # Add row to table
            markdown_lines.append('| ' + ' | '.join(row_cells) + ' |')
            
            # Add separator after first row (header)
            if row_idx == 0:
                markdown_lines.append('| ' + ' | '.join(['---'] * len(row_cells)) + ' |')
        
        return '\n'.join(markdown_lines)
    
    def _process_aside(self, aside_item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """Process aside/callout content: its name (Precondition, Complexity…)
        or else its style's, then its blocks on the quote's lines (quote_blocks:
        the first on the name's line unless it can't share it)."""
        aside_type = aside_item.get('style', 'note')
        content_items = aside_item.get('content', [])
        aside_content = self._process_content_items(content_items, references)
        
        if not aside_content:
            return ""
        
        name = aside_item.get('name')
        if aside_type == 'warning':
            label = f"⚠️ **{name or 'Warning'}**:"
        elif aside_type == 'important':
            label = f"❗ **{name or 'Important'}**:"
        elif aside_type == 'tip':
            label = f"💡 **{name or 'Tip'}**:"
        else:
            label = f"**{name or 'Note'}**:"
        return quote_blocks(label, aside_content)
    
    def _process_image(self, image_item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """Process image content."""
        # For inline images in paragraphs
        if image_item.get('type') == 'image':
            image_identifier = image_item.get('identifier', '')
            
            # Look up image in references
            if image_identifier in references:
                ref_data = references[image_identifier]
                alt_text = ref_data.get('alt') or ''

                # The preferred variant (2x light), under the hosting root
                image_url = variant_url(ref_data, self.ASSET_ROOT)
                if image_url:
                    return f"![{alt_text}]({image_url})"
                
                return f"![{alt_text}](image:{image_identifier})"
            
            return f"![](image:{image_identifier})"
        
        # For imageBlock items (different structure)
        image_identifier = image_item.get('identifier', '')
        alt_text = image_item.get('alt') or ''
        
        # Look up image in references
        if image_identifier in references:
            ref_data = references[image_identifier]
            # Use alt from references if not provided
            if not alt_text:
                alt_text = ref_data.get('alt') or ''

            # The preferred variant (2x light), under the hosting root
            image_url = variant_url(ref_data, self.ASSET_ROOT)
            if image_url:
                return f"![{alt_text}]({image_url})"
        
        return f"![{alt_text}](image:{image_identifier})" if alt_text else ""
    
    def _with_caption(self, media: str, item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """An image or video block's markdown and, on the line under it, its
        caption: Apple's text under the figure (the block's metadata abstract),
        on one line."""
        metadata = item.get('metadata') or {}
        abstract = metadata.get('abstract') if isinstance(metadata, dict) else None
        if not isinstance(abstract, list) or not abstract:
            return media
        caption = ' '.join(self._resolve_inline_content(abstract, references).split())
        return f"{media}\n{caption}" if caption else media

    def _process_video(self, video_item: Dict[str, Any], references: Dict[str, Any]) -> str:
        """A video block as a link to the video (its preferred variant, under
        the hosting root), named by its alt text; "" when it has no URL."""
        identifier = video_item.get('identifier', '')
        ref_data = references.get(identifier) or {}
        video_url = variant_url(ref_data, self.ASSET_ROOT)
        if not video_url:
            return ""
        name = video_item.get('alt') or ref_data.get('alt') or identifier
        return f"[Video: {name}]({video_url})"
    def _track_cross_framework_ref(self, identifier: str) -> None:
        """Track a cross-framework reference."""
        # Extract target framework from identifier
        if '/documentation/' in identifier:
            parts = identifier.split('/documentation/', 1)[1].split('/')
            if parts:
                target_framework = parts[0]
                if target_framework not in self.cross_framework_refs:
                    self.cross_framework_refs[target_framework] = set()
                self.cross_framework_refs[target_framework].add(identifier)
    
    def save_cross_framework_summary(self) -> None:
        """Save summary of cross-framework references if any were found."""
        if not self.cross_framework_refs:
            return
        
        summary_path = self.output_dir / "_cross_framework_refs.json"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        summary_data = {
            "source_framework": self.framework_id,
            "total_external_refs": sum(len(refs) for refs in self.cross_framework_refs.values()),
            "referenced_frameworks": list(self.cross_framework_refs.keys()),
            "references": {
                fw: list(refs) for fw, refs in self.cross_framework_refs.items()
            }
        }
        
        write_text_atomic(summary_path, json.dumps(summary_data, indent=2))
        
        logger.info(
            "saved_cross_framework_summary",
            framework=self.framework_name,
            external_refs=summary_data["total_external_refs"],
            referenced_frameworks=len(summary_data["referenced_frameworks"])
        )


def apply_sink_failure_policy(
    sink: Sink,
    outcome_of: Callable[[str], Optional[FrameworkOutcome]],
    label: str,
    writers: Optional[Set[str]] = None,
    storm: bool = True,
) -> None:
    """Count a sink's page failures of this run once, and send each its block or flag.

    The per-entry counters of the pages the given writers processed (all of
    them by default): consecutive_failures (D8) and consecutive_local_errors.
    Each failure's block ("fetch_failed", "local_error") or persistent flag
    goes to the outcome of the job that processed the page, and of each job a
    dedup hit recorded on it (Sink.dedup_jobs). Runs once for a framework
    job's own pages, after its discovery (_apply_failure_policy), and once
    for a multi-writer sink's, after its last writer (finish_run).

    - Failure storm (storm): more failures than max(5, 1% of the sink's
      pages) block but aren't counted, unless the storm lasts
      FAILURE_STORM_RUNS runs (the sink's metadata.failure_storm_runs).
    - Resets. The D8 count is of failed runs in a row: a 200, a 304 whose
      refetch succeeded, a 404/410 (a removal, not a failure) or a run that
      never fetched the URL (no writer processed it this run) ends the
      streak, so a stale count can't lift the never-good block on our first
      new failure. A page processed without a local error resets that count.
    - At PERSISTENT_FAILURE_RUNS a failure stops blocking and flags the run;
      a previously good page is then treated as removed (D8: both keys
      become error entries, so its file is orphaned and cleaned).

    Args:
        sink: The sink
        outcome_of: A job's outcome, by job id
        label: The sink's name for the log
        writers: Count only the pages these jobs processed (Sink.writer_of)
        storm: Check for a failure storm (a first handoff run's end-of-run
            pass counts its handoff writers' pages without it)
    """
    hm = sink.hash_manager

    def counted(url: str) -> bool:
        return writers is None or sink.writer_of(url) in writers

    def outcomes(url: str) -> List[FrameworkOutcome]:
        jobs = [sink.writer_of(url), *sorted(sink.dedup_jobs.get(url, ()))]
        found = [outcome_of(job) for job in dict.fromkeys(job for job in jobs if job)]
        return [outcome for outcome in found if outcome is not None]

    failures = {url: failure for url, failure in sink.fetch_failures.items() if counted(url)}
    counting = True
    if storm:
        pages = max(sink.known_pages, len(sink.processed_urls))
        limit = max(FAILURE_STORM_MIN, FAILURE_STORM_SHARE * pages)
        if len(failures) > limit:
            storm_runs = int(hm.get_metadata("failure_storm_runs", 0)) + 1
            hm.set_metadata("failure_storm_runs", storm_runs)
            counting = storm_runs >= FAILURE_STORM_RUNS
            for url in failures:
                for outcome in outcomes(url):
                    outcome.failure_storm = True
            logger.warning(
                "failure_storm",
                framework=label,
                failures=len(failures),
                limit=limit,
                failure_storm_runs=storm_runs,
                counting=counting,
            )
        else:
            hm.set_metadata("failure_storm_runs", 0)

    unfetched = {
        url for url, entry in hm.hashes.items()
        if "consecutive_failures" in entry and url not in sink.processed_urls
    }
    fetched = {url for url in sink.fetch_ok | sink.gone if counted(url)}
    for url in (fetched | unfetched) - sink.fetch_failures.keys():
        hm.set_counter(url, "consecutive_failures", 0)
    for url in {url for url in sink.saved_ok if counted(url)} - sink.local_errors.keys():
        hm.set_counter(url, "consecutive_local_errors", 0)

    for url, page_failure in failures.items():
        runs = hm.get_counter(url, "consecutive_failures")
        if counting:
            runs += 1
            hm.set_counter(url, "consecutive_failures", runs)
        if runs < PERSISTENT_FAILURE_RUNS:
            sink.decisions[url] = "block"
            for outcome in outcomes(url):
                outcome.block("fetch_failed", url)
            continue
        # No longer protected: it stops blocking, and flags the run
        sink.decisions[url] = "persistent"
        logger.error(
            "persistent_fetch_failure",
            url=url,
            kind=page_failure.kind,
            runs=runs,
            error=page_failure.failure.error,
        )
        for outcome in outcomes(url):
            outcome.persistent_fetch_failures.append(url)
        if page_failure.kind == "previously_good":
            # D8: treat the page as removed. Both keys become error
            # entries (keeping the count), so its file and any subtree no
            # longer reachable are orphaned and cleaned in this run. After
            # a 304 the page is live and stays touched, so its file is kept.
            hm.mark_error(url, page_failure.failure.error)
            hm.mark_error(doc_url_of(sink.site, url), page_failure.failure.error)

    for url, error in sink.local_errors.items():
        if not counted(url):
            continue
        runs = hm.get_counter(url, "consecutive_local_errors") + 1
        hm.set_counter(url, "consecutive_local_errors", runs)
        if runs < PERSISTENT_FAILURE_RUNS:
            for outcome in outcomes(url):
                outcome.block("local_error", url)
        else:
            # Stop blocking; the entry stays touched, so its file is kept
            logger.error("persistent_local_error", url=url, runs=runs, error=error)
            sink.persistent_local_errors = True
            for outcome in outcomes(url):
                outcome.persistent_local_errors.append(url)


def store_render_version(sink: Sink, label: str) -> None:
    """Store a sink's RENDER_VERSION (metadata.render): every page it reached was rendered by it.

    When it stores a new version, the entries this run didn't touch lose
    their hash and etag (forget_untouched_renderings): their files keep the
    old rendering, and such a page that comes back unchanged would else
    answer 304 and never be rendered again.
    """
    hm = sink.hash_manager
    if hm.stale:
        not_rendered = hm.forget_untouched_renderings()
        logger.info(
            "render_version_stored",
            framework=label,
            version=hm.render_version,
            not_rendered=not_rendered,
        )
    hm.mark_rendered()
    sink.render_stored = True


def stale_error_entries(sink: Sink) -> List[str]:
    """A sink's error entries no page this run reached links to any more.

    An error entry (a page that answered 404/410, an earlier never-good
    failure, a D8) whose page no writer processed this run, with no run
    counter left: a link nothing makes any more (e.g. a section anchor's
    URL, or a module's page under its umbrella's id before 1.1). Its next
    link would fetch the page again anyway. A doc-URL key is judged by its
    JSON URL. The end-of-run cleanup drops them from a sink it cleans.
    """
    processed = {url.lower() for url in sink.processed_urls}
    site = sink.site
    stale = []
    for url, entry in sink.hash_manager.hashes.items():
        if (not isinstance(entry, dict) or entry.get('status') != 'error' or entry.get('file_path')
                or any(counter in entry for counter in COUNTER_FIELDS)):
            continue
        if url.startswith(site.json_prefix):
            json_url = url
        elif url.startswith(site.doc_prefix):
            json_url = f"{site.json_prefix}{url[len(site.doc_prefix):]}.json"
        else:
            continue
        if json_url.lower() not in processed:
            stale.append(url)
    return sorted(stale)


def orphan_scan_of(sink: Sink) -> OrphanScan:
    """A sink's orphan candidates: the .md files no entry this run touched records.

    From its hash manager's touched set, which for a multi-writer sink holds
    every writer's touches (Sink.release keeps them). Its docs dir is its
    output dir, or that dir in another casing.
    """
    hm = sink.hash_manager
    framework_dir = next(
        (path for path in same_name_any_case(sink.output_dir) if path.is_dir()), sink.output_dir
    )
    existing = hm.framework_files(framework_dir)
    pending = hm.get_metadata("pending_orphans")
    return OrphanScan(
        framework_dir=framework_dir,
        hash_file=hm.cache_file,
        files=len(existing),
        orphans=hm.get_untouched_files(framework_dir, existing),
        pending_orphans=[path for path in pending if isinstance(path, str)] if isinstance(pending, list) else [],
        stale_errors=stale_error_entries(sink),
    )


def sink_runs_clean(sink: Sink, outcome_of: Callable[[str], Optional[FrameworkOutcome]]) -> bool:
    """Rule 1's clean condition for a multi-writer sink this run.

    A module: every parent its hash file lists ran this run and ran clean
    (its cleanup isn't skipped). A top-level sink: its primary job ran
    clean, and every handoff writer its hash file records ran this run and
    ran clean (a writer that failed before its first handoff would else
    leave the pages only it reaches looking orphaned).
    """
    def clean(job: Optional[str]) -> bool:
        outcome = outcome_of(job) if job else None
        return outcome is not None and not outcome.skip_cleanup

    hm = sink.hash_manager
    if sink.module:
        parents = module_parents(hm.get_metadata(MODULE_KEY))
        return bool(parents) and all(clean(parent) for parent in parents)
    if not sink.primary_ran or not clean(sink.primary_id):
        return False
    return all(clean(writer) for writer in metadata_ids(hm.get_metadata(HANDOFF_KEY)))


def finish_run(
    sinks: SinkRegistry, outcomes: Sequence[FrameworkOutcome], cleanup_orphans: bool
) -> List[ModuleScan]:
    """The end of a run for its multi-writer sinks (D6), once every job has finished.

    The multi-writer sinks are every module sink, every top-level sink whose
    hash file carried handoff_from when loaded (Sink.deferred), and every
    top-level sink that another job routed a page to this run. In this order:
    1. Their failure policy (apply_sink_failure_policy), from the union of
       their writers' sets, each writer's blocks to its own outcome. A
       first handoff run (a top-level sink not deferred) counts only its
       handoff writers' pages, without the storm check: its primary job
       counted its own.
    2. Their render versions, under rule 1's clean condition
       (sink_runs_clean) and with no persistent local error among their pages.
    3. With cleanup_orphans, their orphan scans from every writer's touched
       set: a module's for the end-of-run cleanup (ModuleScan), a top-level
       sink's on its primary's outcome (handoff_writers too, for rule 1).
       Batch 2's zero-touched guard applies to a deferred top-level sink; a
       handoff-only sink (its primary didn't run) is never cleaned.
    4. Every sink saved (SinkRegistry.save_all), with or without
       cleanup_orphans: the cleanup then works on saved files.
    framework_errors and the cleanup read the outcomes after this.

    Returns:
        The run's module sinks, for the end-of-run cleanup
    """
    by_job: Dict[str, FrameworkOutcome] = dict(sinks.outcomes)
    for outcome in outcomes:
        by_job.setdefault(outcome.framework_id.lower(), outcome)
    multi = [sink for sink in sinks.all() if sink.deferred or sink.writer]

    for sink in multi:
        if sink.deferred:
            apply_sink_failure_policy(sink, by_job.get, sink.dir_name)
        else:
            apply_sink_failure_policy(sink, by_job.get, sink.dir_name, writers=sink.other_writers(), storm=False)
        sinks.release_if_idle(sink)

    modules: List[ModuleScan] = []
    for sink in multi:
        if not sink.render_stored and not sink.persistent_local_errors and sink_runs_clean(sink, by_job.get):
            store_render_version(sink, sink.dir_name)
        if sink.module:
            modules.append(ModuleScan(
                dir_name=sink.dir_name,
                output_dir=sink.output_dir,
                hash_file=sink.hash_file,
                routed_by=set(sink.parents_this_run),
                orphan_scan=orphan_scan_of(sink) if cleanup_orphans else None,
            ))
        elif sink.primary_ran and sink.primary_id is not None:
            primary = by_job.get(sink.primary_id)
            if primary is not None:
                primary.handoff_writers = sorted(metadata_ids(sink.hash_manager.get_metadata(HANDOFF_KEY)))
                if cleanup_orphans:
                    _rescan(sink, primary)
        sinks.release_if_idle(sink)

    sinks.save_all()
    return modules


def _rescan(sink: Sink, primary: FrameworkOutcome) -> None:
    """A top-level multi-writer sink's orphan scan at the end of the run, on its primary's outcome.

    From every writer's touched set: a scan right after its primary job's
    save would take the pages a handoff writer routed in later for orphans.
    A deferred sink gets Batch 2's zero-touched guard here; a sink whose
    primary's cleanup is skipped gets no scan.
    """
    if primary.root_gone_runs:
        return
    if sink.deferred and not primary.blocked and not sink.hash_manager.touched:
        logger.error("framework_zero_touched", framework=sink.framework_name, framework_id=sink.dir_name)
        primary.block("zero_touched", sink.dir_name)
    if primary.blocked:
        primary.orphan_scan = None
        return
    if sink.deferred or primary.orphan_scan is not None:
        primary.orphan_scan = orphan_scan_of(sink)
