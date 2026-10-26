"""The sinks of a scrape: where a page's file and hash entries go.

A Sink is one docs dir and its hash file, on one DocC site: the dir, its
HashManager, the converter that renders its pages (their links are relative
to their files in the dir), and this run's state for its pages (processed,
the failure policy's sets, the write-time tripwire's map). Every path of the
JSON scraper that acts for a page takes the page's sink. A framework job's
primary sink is its own docs dir and hash file.

A page goes to the sink of its URL's first path segment (D6), whichever job
reached it:
- the job's own framework: its primary sink;
- a D6 module (a first segment of the job's bundle that is no top-level
  technology, e.g. Intents under SiriKit): the module's sink, with its own
  docs dir and hash file (metadata.module: its bundle and its parents, each
  with a counter of the parent's clean runs that routed it no page);
- another top-level technology of the job's bundle (a handoff): that
  technology's own sink (its metadata.handoff_from records the job).
A sink written by more than one job (every module sink, and a top-level sink
that receives handoff pages) is a multi-writer sink: its failure policy, its
render version and its orphan scan are worked out at the end of the run,
from every writer's pages (json_scraper.finish_run).

The SinkRegistry holds a run's sinks, one per site and dir (in any casing),
each created, with its hash file loaded, on first use. A top-level sink's
hash manager leaves memory once no job in flight uses it (release); the
sink keeps this run's state for its pages, and loads its hash file again if
a later job routes it a page.
"""

import asyncio
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Mapping, Optional, Set, Tuple

from scraper.config import Config
from scraper.site import APPLE, DocCSite
from scraper.utils.hash_manager import HashManager, read_hash_file
from scraper.utils.logger import get_logger
from scraper.utils.markdown_converter import AppleDocMarkdownConverter
from scraper.utils.naming import dirmap

if TYPE_CHECKING:
    from scraper.json_scraper import FrameworkOutcome, PageFetchFailure, PageLinks

logger = get_logger(__name__)

HASH_FILE_SUFFIX = "_hashes.json"

# A D6 module's hash file metadata: {"bundle": <its pages' bundle>, "parents":
# {<parent id>: {UNLINKED_KEY: <the parent's clean runs in a row that routed
# it no page>}}}. Top-level technologies never carry it
MODULE_KEY = "module"
UNLINKED_KEY = "unlinked_clean_runs"
# A top-level hash file's other writers: {<job id>: {}}, the jobs that routed
# it a page (a handoff)
HANDOFF_KEY = "handoff_from"
# A parent's modules: {<module id>: {}}, on the parent's own hash file
CHILD_MODULES_KEY = "child_modules"


def metadata_ids(value: Any) -> Dict[str, Any]:
    """A metadata id map ({id: value}) as loaded; anything else is empty."""
    return dict(value) if isinstance(value, dict) else {}


def module_parents(module: Any) -> Dict[str, int]:
    """A metadata.module's parents with their unlinked_clean_runs ({} for a malformed value)."""
    parents = metadata_ids(module.get("parents")) if isinstance(module, dict) else {}
    counts: Dict[str, int] = {}
    for parent, value in parents.items():
        runs = value.get(UNLINKED_KEY, 0) if isinstance(value, dict) else 0
        counts[str(parent).lower()] = runs if isinstance(runs, int) else 0
    return counts


def module_metadata(bundle: Any, parents: Mapping[str, int]) -> Dict[str, Any]:
    """A metadata.module value: its bundle (if known) and its parents' counters."""
    module: Dict[str, Any] = {"parents": {parent: {UNLINKED_KEY: runs} for parent, runs in sorted(parents.items())}}
    if isinstance(bundle, str) and bundle:
        module["bundle"] = bundle
    return module


class Sink:
    """One docs dir with its hash file, and this run's state for its pages.

    Attributes:
        site: The DocC site of its pages
        dir_name: Its docs dir's name, the framework's id as its hash file
            cases it (BaseAppleScraper._canonical_framework_id)
        framework_name: What its pages' **Framework** line names (a
            module's is its dir name)
        module: A D6 module: no job of its own, written by its parents
        output_dir: Its docs dir. Created lazily on the first file write, so
            a sink that writes no file (e.g. its root returns 404) leaves no
            empty dir behind
        hash_file: Its hash file
        hash_manager: Its hash file, loaded on create, and again on first
            use after a release
        load_error: Why its hash file failed to load when the sink was created
        handoff_loaded: Its hash file carried metadata.handoff_from when the
            sink was created (a multi-writer sink from the start of the run;
            never a handoff_from a writer adds during the run)
        known_dirs: The docs dirs its pages link to locally, {name.lower(): name}:
            its site's in the run (SinkRegistry.dirs_of) and its own
        markdown_converter: Renders its pages
        processed_urls: The JSON URLs of its pages this run fetched (or is fetching)
        writer: JSON URL -> the job that processed it, for the pages a job
            other than the sink's primary processed (writer_of)
        fetch_failures: JSON URL -> the fetch failure that counts toward D8
        fetch_ok: answered 200 with a JSON body
        gone: answered 404/410: Apple removed the page
        local_errors: JSON URL -> convert/save error
        saved_ok: pages processed without a local error
        known_pages: Its previously good pages, the storm threshold's base
            when a run's failures cut discovery short
        path_owner_map: The write-time tripwire's map, seeded on first use
            (AppleJSONDocumentationScraper._path_owners)
        primary_ran: Its own framework's job ran this run
        parents_this_run: The jobs other than its primary that routed it a
            page this run (recorded at the routing decision, before the
            dedup check): a module's parents, a top-level sink's handoff writers
        links: JSON URL -> the page's outgoing links, for a page another job
            may need the links of (stores_links): a dedup hit gives them to it
        pending: JSON URL -> resolved when the page's processing ends, for a
            page whose links are kept: a dedup hit on it waits for it
        raised: Pages whose processing raised
        dedup_jobs: JSON URL -> the jobs a dedup hit recorded on the page
            because its fetch failed (they take its block or persistent flag)
        decisions: JSON URL -> what the failure policy made of the page's
            fetch failure this run: "block" or "persistent"
        persistent_local_errors: A page's local error reached
            PERSISTENT_FAILURE_RUNS this run (its render version isn't stored)
        render_stored: Its RENDER_VERSION was stored this run
        users: The jobs in flight that use it (its primary, its writers)
        pages_in_flight: Pages of it being processed now, by any job
    """

    def __init__(
        self,
        site: DocCSite,
        dir_name: str,
        framework_name: str,
        known_dirs: Mapping[str, str],
        render_version: Optional[int],
        module: bool = False,
    ) -> None:
        """Set up the sink and load its hash file.

        Args:
            site: The DocC site of its pages
            dir_name: Its docs dir's name, already cased
            framework_name: What its pages' **Framework** line names
            known_dirs: The site's docs dirs linked locally in the run, {name.lower(): name}
            render_version: The scraper's RENDER_VERSION (HashManager.stale)
            module: A D6 module's sink
        """
        self.site = site
        self.dir_name = dir_name
        self.framework_name = framework_name
        self.module = module
        self.render_version = render_version
        self.output_dir = Config.get_framework_output_dir(dir_name, namespace=site.namespace)
        self.hash_file = Config.get_hash_file(dir_name, namespace=site.namespace)
        self._hash_manager: Optional[HashManager] = None
        # The touched set of a released manager, carried over when it is loaded again
        self._kept_touched: Set[str] = set()
        self.known_dirs: Dict[str, str] = {**known_dirs, dir_name.lower(): dir_name}
        self.markdown_converter = AppleDocMarkdownConverter(self.output_dir, self.known_dirs, site)
        hash_manager = self.hash_manager
        self.load_error = hash_manager.load_error
        self.handoff_loaded = bool(metadata_ids(hash_manager.get_metadata(HANDOFF_KEY)))

        # This run's state for its pages, which the failure policy counts once
        self.processed_urls: Set[str] = set()
        self.writer: Dict[str, str] = {}
        self.fetch_failures: Dict[str, "PageFetchFailure"] = {}
        self.fetch_ok: Set[str] = set()
        self.gone: Set[str] = set()
        self.local_errors: Dict[str, str] = {}
        self.saved_ok: Set[str] = set()
        self.known_pages = sum(
            1 for url, entry in hash_manager.hashes.items()
            if url.startswith(site.json_base) and isinstance(entry, dict) and entry.get('file_path')
        )
        self.path_owner_map: Optional[Dict[str, str]] = None

        # D6: its writers and what they need of each other's pages
        self.primary_ran = False
        self.parents_this_run: Set[str] = set()
        self.links: Dict[str, "PageLinks"] = {}
        self.pending: Dict[str, "asyncio.Future[None]"] = {}
        self.raised: Set[str] = set()
        self.dedup_jobs: Dict[str, Set[str]] = {}
        self.decisions: Dict[str, str] = {}
        self.persistent_local_errors = False
        self.render_stored = False
        self.users: Set[str] = set()
        self.pages_in_flight = 0

    @property
    def hash_manager(self) -> HashManager:
        """Its hash file's manager, loaded (again) on first use; the run's touched set carries over."""
        if self._hash_manager is None:
            hash_manager = HashManager(self.hash_file, self.output_dir, render_version=self.render_version)
            hash_manager.touched |= self._kept_touched
            self._hash_manager = hash_manager
        return self._hash_manager

    @property
    def loaded(self) -> bool:
        """Its hash manager is in memory."""
        return self._hash_manager is not None

    @property
    def primary_id(self) -> Optional[str]:
        """The job id of its own framework (None for a module, which has none)."""
        return None if self.module else self.dir_name.lower()

    @property
    def deferred(self) -> bool:
        """A multi-writer sink from the start of the run: a module, or a
        top-level sink whose hash file carried handoff_from. Its per-entry
        failure policy, render version and orphan scan wait for the end of
        the run (json_scraper.finish_run)."""
        return self.module or self.handoff_loaded

    def writer_of(self, url: str) -> Optional[str]:
        """The job that processed a page of it this run (its primary unless recorded)."""
        return self.writer.get(url, self.primary_id)

    def stores_links(self, job: str) -> bool:
        """Whether a page this job processes keeps its links for the run: another
        job may need them (a module's other parent, or the primary of a sink
        the job hands pages off to)."""
        return self.module or job != self.primary_id

    def other_writers(self) -> Set[str]:
        """The jobs other than its primary that processed a page of it this run."""
        return set(self.writer.values())

    def release(self) -> bool:
        """Save its hash file and drop the manager from memory, keeping this run's state.

        Its touched set is kept: a later load (hash_manager) starts from it,
        so the run's orphan scan still sees every page this run touched. So
        are processed_urls (a later job doesn't fetch a page again), the
        fetch failures, the kept links and the writers. Of a sink that isn't
        deferred, the failure policy's other sets keep only the other
        writers' pages: its primary job counted its own at its end.

        Returns:
            False if the save failed (logged); the manager then stays loaded
        """
        hash_manager = self._hash_manager
        if hash_manager is None:
            return True
        if not hash_manager.save():
            return False
        self._kept_touched = hash_manager.touched
        self._hash_manager = None
        self.path_owner_map = None
        if not self.deferred:
            # Its primary job's entries were counted at its end; only the
            # other writers' are counted again, at the end of the run
            self.fetch_ok = {url for url in self.fetch_ok if url in self.writer}
            self.gone = {url for url in self.gone if url in self.writer}
            self.saved_ok = {url for url in self.saved_ok if url in self.writer}
            self.local_errors = {url: error for url, error in self.local_errors.items() if url in self.writer}
        return True

    def add_parent(self, parent: str, bundle: str) -> None:
        """Record a parent that routed the module a page (metadata.module), and its bundle.

        A new parent's counter starts at 0. The save always writes the
        module's metadata.module, and drops a stray unlisted_runs.
        """
        hash_manager = self.hash_manager
        module = hash_manager.get_metadata(MODULE_KEY)
        parents = module_parents(module)
        parents.setdefault(parent, 0)
        stored_bundle = module.get("bundle") if isinstance(module, dict) else None
        hash_manager.set_metadata(MODULE_KEY, module_metadata(bundle or stored_bundle, parents))
        hash_manager.set_metadata("unlisted_runs", None)

    def add_handoff_writer(self, writer: str) -> None:
        """Record a job that routed this top-level sink a page (metadata.handoff_from)."""
        self._add_id(HANDOFF_KEY, writer)

    def add_child_module(self, module: str) -> None:
        """Record a module this framework's job routed a page to (metadata.child_modules)."""
        self._add_id(CHILD_MODULES_KEY, module)

    def _add_id(self, key: str, member: str) -> None:
        hash_manager = self.hash_manager
        ids = metadata_ids(hash_manager.get_metadata(key))
        if member not in ids:
            ids[member] = {}
            hash_manager.set_metadata(key, dict(sorted(ids.items())))


def apple_top_level(hash_dir: Path, site: DocCSite) -> Set[str]:
    """The top-level technologies a hash dir's files show: their ids, lowercased.

    A file with a key under the site's JSON prefix and no metadata.module,
    and a file that can't be read (it may be a framework's: it is never
    taken for a module). The other scrapers' files have no such key. A
    namespaced site's are its hash dir's (.hashes/<namespace>/), with its
    roots and the first segments of its excludes.
    """
    found: Set[str] = {root.lower() for root in site.roots}
    found |= {exclude.split("/", 1)[0].lower() for exclude in site.excludes}
    for path in sorted(hash_dir.glob(f"*{HASH_FILE_SUFFIX}")):
        stem = path.name[: -len(HASH_FILE_SUFFIX)].lower()
        try:
            hashes, metadata = read_hash_file(path)
        except (OSError, ValueError):
            found.add(stem)
            continue
        if not metadata.get(MODULE_KEY) and any(url.startswith(site.json_prefix) for url in hashes):
            found.add(stem)
    return found


class SinkRegistry:
    """A run's sinks: one per site and dir name (any casing), created on first use.

    One registry serves every framework job of a run. A top-level sink's
    hash manager leaves memory once no job in flight uses it and none of its
    pages is being processed (release); module sinks stay loaded until the
    end of the run (save_all).
    """

    def __init__(
        self,
        known_dirs: Optional[Mapping[str, str]] = None,
        top_level: Optional[Mapping[str, Iterable[str]]] = None,
        titles: Optional[Mapping[str, str]] = None,
        reserved: Optional[Mapping[str, str]] = None,
    ) -> None:
        """Start a run's registry, with no sink yet.

        Args:
            known_dirs: The Apple docs dirs whose pages are linked locally,
                {name.lower(): name}: the Apple framework dirs with a hash
                file (naming.dirmap) and the run's frameworks. A sink's own
                dir is always known; any other framework's pages get their
                Apple URL. Another site's are added with add_site
            top_level: Each site's top-level technologies, {site name: ids}
                (any casing): a first segment among them is never a module.
                A site without one gets the technologies its hash files show
                (apple_top_level), on first use
            titles: The top-level technologies' titles, {id.lower(): title},
                what a sink created by a handoff names its pages' framework
            reserved: The top-level dirs of the other scrapers (MLX, Swift,
                HIG) and the DocC sites' namespaces, {name.lower(): name}: no
                Apple sink may have one (namespace_collision)
        """
        self.known_dirs: Dict[str, str] = dict(known_dirs or {})
        self._site_dirs: Dict[str, Dict[str, str]] = {APPLE.name: self.known_dirs}
        self._sinks: Dict[Tuple[str, str], Sink] = {}
        self._top_level: Dict[str, Set[str]] = {
            site: {name.lower() for name in names} for site, names in (top_level or {}).items()
        }
        self._roots: Dict[str, Set[str]] = {}
        self.titles: Dict[str, str] = {name.lower(): title for name, title in (titles or {}).items()}
        self.reserved: Dict[str, str] = {name.lower(): name for name in (reserved or {}).values()}
        # The run's jobs' outcomes, by (site name, job id): the multi-writer
        # sinks' failure policy sends each writer's blocks to its own
        self.outcomes: Dict[Tuple[str, str], "FrameworkOutcome"] = {}

    def add_site(
        self, site: DocCSite, known_dirs: Mapping[str, str], top_level: Iterable[str], roots: Iterable[str]
    ) -> None:
        """Set a DocC site's share of the run: its docs dirs linked locally, its
        top-level set and the roots it crawls (every other top-level page of it
        is never fetched: SinkRegistry.crawls)."""
        self._site_dirs[site.name] = dict(known_dirs)
        self._top_level[site.name] = {name.lower() for name in top_level}
        self._roots[site.name] = {root.lower() for root in roots}

    def dirs_of(self, site: DocCSite) -> Dict[str, str]:
        """A site's docs dirs linked locally in the run, {name.lower(): name}.

        A site add_site didn't set gets those its hash dir shows (naming.dirmap).
        """
        if site.name not in self._site_dirs:
            self._site_dirs[site.name] = dirmap(Config.get_hash_dir(site.namespace), site.json_prefix)
        return self._site_dirs[site.name]

    @staticmethod
    def _key(site: DocCSite, dir_name: str) -> Tuple[str, str]:
        """A sink's key: its site's name and its dir name, lowercased (a dir is one in any casing)."""
        return site.name, dir_name.lower()

    def top_level(self, site: DocCSite) -> Set[str]:
        """The site's top-level technologies, lowercased."""
        if site.name not in self._top_level:
            self._top_level[site.name] = apple_top_level(Config.get_hash_dir(site.namespace), site)
        return self._top_level[site.name]

    def crawls(self, site: DocCSite, segment: str) -> bool:
        """Whether a top-level segment of the site may be crawled: one of the
        roots it crawls (add_site, else its config's), or any for a site
        with neither (Apple's: every technology may be)."""
        roots = self._roots.get(site.name)
        if roots is None and site.roots:
            roots = self._roots[site.name] = {root.lower() for root in site.roots}
        return roots is None or segment.lower() in roots

    def refuses(self, dir_name: str, site: DocCSite = APPLE) -> bool:
        """A dir no sink of a top-level site (Apple's) may have: another
        scraper's top-level dir, or a DocC site's namespace
        (namespace_collision). A namespaced site's dirs are under its
        namespace, so it refuses none."""
        return not site.namespace and dir_name.lower() in self.reserved

    def find(self, site: DocCSite, dir_name: str) -> Optional[Sink]:
        """The run's sink of a site's dir, if it has one."""
        return self._sinks.get(self._key(site, dir_name))

    def get(
        self,
        site: DocCSite,
        dir_name: str,
        framework_name: str,
        render_version: Optional[int],
        module: bool = False,
    ) -> Sink:
        """The sink of a site's dir, created (its hash file loaded) if the run has none yet.

        Args:
            site: The DocC site
            dir_name: The dir's name, already cased; a sink that exists keeps its own casing
            framework_name: What a new sink's pages' **Framework** line names
            render_version: A new sink's RENDER_VERSION
            module: A new sink is a D6 module's
        """
        key = self._key(site, dir_name)
        sink = self._sinks.get(key)
        if sink is None:
            sink = self._sinks[key] = Sink(site, dir_name, framework_name, self.dirs_of(site), render_version, module)
        return sink

    def title(self, dir_name: str) -> str:
        """A top-level technology's title (its id, titled, if technologies.json has none)."""
        return self.titles.get(dir_name.lower()) or dir_name.replace('-', ' ').title()

    def all(self) -> List[Sink]:
        """Every sink of the run."""
        return list(self._sinks.values())

    def job_done(self, job: str) -> None:
        """A job has finished: release the top-level sinks nothing in flight uses any more."""
        for sink in self.all():
            if job in sink.users:
                sink.users.discard(job)
                self.release_if_idle(sink)

    def release_if_idle(self, sink: Sink) -> None:
        """Release a top-level sink once no job in flight uses it and none of its pages is in flight.

        A page a job processes records into the manager after its fetch, so
        the release waits for the last such page to end (counted down in the
        page's finally), then saves the manager again: that page recorded
        after the primary job's own save. A failed save marks the outcomes
        of the sink's primary and writers raised, as a failed save on a
        job's exit does.
        """
        if sink.module or sink.users or sink.pages_in_flight or not sink.loaded:
            return
        if not sink.release():
            self._save_failed(sink)

    def _save_failed(self, sink: Sink) -> None:
        """Mark the outcomes of every job that wrote to a sink raised: its save failed."""
        error = f"failed to save hash file {sink.hash_file}"
        jobs = set(sink.parents_this_run) | sink.other_writers()
        if sink.primary_ran and sink.primary_id:
            jobs.add(sink.primary_id)
        for job in jobs:
            outcome = self.outcomes.get((sink.site.name, job))
            if outcome is not None and outcome.raised is None:
                outcome.raised = error

    def save_all(self) -> None:
        """Save every sink still in memory and drop it: the run's sinks are done.

        Runs once every job has finished, before the end-of-run cleanup,
        which then works on the saved files; nothing saves a sink's manager
        after it. A failed save marks its writers' outcomes raised.
        """
        for sink in self.all():
            if not sink.release():
                self._save_failed(sink)
        self._sinks.clear()
