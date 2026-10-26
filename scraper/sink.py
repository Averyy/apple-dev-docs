"""The sinks of a scrape: where a page's file and hash entries go.

A Sink is one docs dir and its hash file, on one DocC site: the dir, its
HashManager, the converter that renders its pages (their links are relative
to their files in the dir), and this run's state for its pages (processed,
the failure policy's sets, the write-time tripwire's map). Every path of the
JSON scraper that acts for a page takes the page's sink. A framework job's
primary sink is its own docs dir and hash file.

The SinkRegistry holds a run's sinks, one per site and dir (in any casing),
each created, with its hash file loaded, on first use.
"""

from typing import TYPE_CHECKING, Dict, Mapping, Optional, Set, Tuple

from scraper.config import Config
from scraper.site import DocCSite
from scraper.utils.hash_manager import HashManager
from scraper.utils.markdown_converter import AppleDocMarkdownConverter

if TYPE_CHECKING:
    from scraper.json_scraper import PageFetchFailure


class Sink:
    """One docs dir with its hash file, and this run's state for its pages.

    Attributes:
        site: The DocC site of its pages
        dir_name: Its docs dir's name, the framework's id as its hash file
            cases it (BaseAppleScraper._canonical_framework_id)
        framework_name: What its pages' **Framework** line names
        output_dir: Its docs dir. Created lazily on the first file write, so
            a sink that writes no file (e.g. its root returns 404) leaves no
            empty dir behind
        hash_manager: Its hash file, loaded on create
        known_dirs: The docs dirs its pages link to locally, {name.lower(): name}:
            the run's (SinkRegistry.known_dirs) and its own
        markdown_converter: Renders its pages
        processed_urls: The JSON URLs of its pages this run fetched (or is fetching)
        fetch_failures: JSON URL -> the fetch failure that counts toward D8
        fetch_ok: a 200, or a 304 whose discovery refetch succeeded
        gone: answered 404/410: Apple removed the page
        local_errors: JSON URL -> convert/save error
        saved_ok: pages processed without a local error
        known_pages: Its previously good pages, the storm threshold's base
            when a run's failures cut discovery short
        path_owner_map: The write-time tripwire's map, seeded on first use
            (AppleJSONDocumentationScraper._path_owners)
    """

    def __init__(
        self,
        site: DocCSite,
        dir_name: str,
        framework_name: str,
        known_dirs: Mapping[str, str],
        render_version: Optional[int],
    ) -> None:
        """Set up the sink and load its hash file.

        Args:
            site: The DocC site of its pages
            dir_name: Its docs dir's name, already cased
            framework_name: What its pages' **Framework** line names
            known_dirs: The run's docs dirs linked locally, {name.lower(): name}
            render_version: The scraper's RENDER_VERSION (HashManager.stale)
        """
        self.site = site
        self.dir_name = dir_name
        self.framework_name = framework_name
        self.output_dir = Config.get_framework_output_dir(dir_name)
        self.hash_manager = HashManager(
            Config.get_hash_file(dir_name), self.output_dir, render_version=render_version
        )
        self.known_dirs: Dict[str, str] = {**known_dirs, dir_name.lower(): dir_name}
        self.markdown_converter = AppleDocMarkdownConverter(self.output_dir, self.known_dirs)

        # This run's state for its pages, which the failure policy counts once
        self.processed_urls: Set[str] = set()
        self.fetch_failures: Dict[str, "PageFetchFailure"] = {}
        self.fetch_ok: Set[str] = set()
        self.gone: Set[str] = set()
        self.local_errors: Dict[str, str] = {}
        self.saved_ok: Set[str] = set()
        self.known_pages = sum(
            1 for url, entry in self.hash_manager.hashes.items()
            if url.startswith(site.json_base) and entry.get('file_path')
        )
        self.path_owner_map: Optional[Dict[str, str]] = None


class SinkRegistry:
    """A run's sinks: one per site and dir name (any casing), created on first use.

    One registry serves every framework job of a run. A job's primary sink
    leaves it once the job is done (evict), so the run holds the hash
    managers (every entry of a framework) of the jobs in flight only.
    """

    def __init__(self, known_dirs: Optional[Mapping[str, str]] = None) -> None:
        """Start a run's registry, with no sink yet.

        Args:
            known_dirs: The docs dirs whose pages are linked locally,
                {name.lower(): name}: the Apple framework dirs with a hash
                file (naming.dirmap) and the run's frameworks. A sink's own
                dir is always known; any other framework's pages get their
                Apple URL
        """
        self.known_dirs: Dict[str, str] = dict(known_dirs or {})
        self._sinks: Dict[Tuple[str, str], Sink] = {}

    @staticmethod
    def _key(site: DocCSite, dir_name: str) -> Tuple[str, str]:
        """A sink's key: its site's name and its dir name, lowercased (a dir is one in any casing)."""
        return site.name, dir_name.lower()

    def get(self, site: DocCSite, dir_name: str, framework_name: str, render_version: Optional[int]) -> Sink:
        """The sink of a site's dir, created (its hash file loaded) if the run has none yet.

        Args:
            site: The DocC site
            dir_name: The dir's name, already cased; a sink that exists keeps its own casing
            framework_name: What a new sink's pages' **Framework** line names
            render_version: A new sink's RENDER_VERSION
        """
        key = self._key(site, dir_name)
        sink = self._sinks.get(key)
        if sink is None:
            sink = self._sinks[key] = Sink(site, dir_name, framework_name, self.known_dirs, render_version)
        return sink

    def evict(self, sink: Sink) -> None:
        """Drop a sink whose job is done: its hash file is saved and its outcome made.

        Nothing reads it again this run; a later get loads its hash file again.
        """
        key = self._key(sink.site, sink.dir_name)
        if self._sinks.get(key) is sink:
            del self._sinks[key]
