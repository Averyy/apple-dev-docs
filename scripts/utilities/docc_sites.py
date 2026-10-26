"""The DocC sites other than Apple's (site.DOCC_SITES), as the Apple process scrapes them.

Each site's roots (its allow-list) are jobs of the Apple run (scrape.py),
next to the Apple technologies, with its own namespace, hash files and
local links. Before its jobs, its index root is loaded (load_site, rule 7(f)
of todo-4's D6 design):
- a 200 whose body lists pages: its first segments are the site's index
  roots, persisted as metadata.index_roots in .hashes/<namespace>/_site.json
  (not a *_hashes.json name: no per-root step, dirmap or count sees it);
- a 404/410: index_root_gone; the persisted index roots stand in (with none
  persisted yet, it is a failure, as below);
- anything else (5xx, timeout, challenge, a body that isn't the index): our
  failure; the site's jobs are skipped this run, which exits 1.
The site's top-level set is its allow-list, its excludes and its index roots,
so a page of a top-level segment it doesn't crawl (e.g. docs.swift.org's 14
private stdlib modules) is never crawled, as a root or as a module.

Its removals are automatic (rule 7): a top-level hash file whose root left
the allow-list goes with its dir, at the end of the next run that covers the
site (config_removals), and a site that left the config goes whole, its
namespace's docs dir and hash dir (gone_sites). A root that answers 404/410
on 2 consecutive runs goes as an Apple root does (root_gone_runs); other
failures follow the 2.1 policy. Module sinks under a namespace (D6) are only
ever removed by the module rules.
"""

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Final, List, Optional, Sequence, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scraper.base import NOT_MODIFIED, BaseAppleScraper, FetchFailed
from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper, SiteRemoval
from scraper.sink import CHILD_MODULES_KEY, HASH_FILE_SUFFIX, MODULE_KEY, Sink, metadata_ids
from scraper.site import DocCSite
from scraper.utils.hash_manager import HashManager, read_hash_file
from scraper.utils.logger import get_logger
from scraper.utils.naming import dirmap
from scraper.utils.rate_limiter import AdaptiveRateLimiter

logger = get_logger(__name__)

# A site's own file in its hash dir: metadata.site (its name) and, for a site
# with an index root, metadata.index_roots
SITE_FILE: Final = "_site.json"
SITE_KEY: Final = "site"
INDEX_ROOTS_KEY: Final = "index_roots"
GONE_STATUSES: Final = (404, 410)


def site_file(site: DocCSite) -> Path:
    """A site's _site.json: .hashes/<namespace>/_site.json."""
    return Config.get_hash_dir(site.namespace) / SITE_FILE


def persisted_index_roots(site: DocCSite) -> List[str]:
    """The index roots the site's last successful index load persisted (cased; [] if none)."""
    try:
        _, metadata = read_hash_file(site_file(site))
    except (OSError, ValueError):
        return []
    roots = metadata.get(INDEX_ROOTS_KEY)
    return [root for root in roots if isinstance(root, str) and root] if isinstance(roots, list) else []


def index_roots(site: DocCSite, body: str) -> List[str]:
    """The first segments of the documentation pages an index root's references list.

    Each as its identifier cases it (doc://…/documentation/MigrationGuide ->
    MigrationGuide), else as its URL does. Raises ValueError for a body that
    isn't such a page (no JSON, or no reference to a documentation page).
    """
    data = json.loads(body)
    references = data.get("references") if isinstance(data, dict) else None
    if not isinstance(references, dict):
        raise ValueError("no references")
    roots: Dict[str, str] = {}
    for identifier, reference in references.items():
        url = reference.get("url") if isinstance(reference, dict) else None
        if not (isinstance(url, str) and reference.get("type") == "topic" and url.startswith(site.doc_path)):
            continue
        segment = url[len(site.doc_path):].split("/", 1)[0].split("#", 1)[0]
        if not segment:
            continue
        identifier_path = str(identifier).partition("/documentation/")[2]
        cased = identifier_path.split("/", 1)[0].split("#", 1)[0]
        roots.setdefault(segment.lower(), cased if cased.lower() == segment.lower() else segment)
    if not roots:
        raise ValueError("no documentation page in its references")
    return sorted(roots.values(), key=str.lower)


class SiteIndexLoader(BaseAppleScraper):
    """Loads a DocC site's index root through the scraper's HTTP client (its retries and rate limit).

    Its hash manager is the site's _site.json, saved on exit.
    """

    def __init__(self, site: DocCSite, rate_limiter: Optional[AdaptiveRateLimiter] = None) -> None:
        self.site = site
        self._site_file = HashManager(site_file(site), Config.get_docs_dir(site.namespace))
        super().__init__(
            framework_id=site.name,
            framework_name=site.label,
            base_url=site.index_url,
            hash_dir=Config.get_hash_dir(site.namespace),
            rate_limiter=rate_limiter,
        )

    @property
    def hash_manager(self) -> HashManager:
        """The site's _site.json."""
        return self._site_file

    async def save_page_data(self, sink: Sink, url: str, data: Dict[str, Any]) -> bool:
        raise NotImplementedError("the index root is never saved as a page")

    async def load(self) -> Tuple[str, List[str], Optional[str]]:
        """Fetch the index root.

        Returns:
            ("ok", its index roots, None), persisted in _site.json;
            ("gone", [], why) for a 404/410; ("failed", [], why) otherwise
        """
        assert self.site.index_url is not None
        result = await self.fetch_page_with_etag(self.site.index_url, use_etag=False)
        if isinstance(result, FetchFailed):
            state = "gone" if result.status in GONE_STATUSES else "failed"
            return state, [], f"{self.site.index_url}: {result.error}"
        if result is NOT_MODIFIED:
            return "failed", [], f"{self.site.index_url}: HTTP 304 without a conditional request"
        try:
            roots = index_roots(self.site, result[0])
        except ValueError as e:
            return "failed", [], f"{self.site.index_url}: not the site's index ({e})"
        self._site_file.set_metadata(INDEX_ROOTS_KEY, roots)
        return "ok", roots, None


@dataclass
class SiteRun:
    """A DocC site's share of a run, from its config and its index root (load_site).

    Attributes:
        site: The site
        jobs: Its roots to crawl this run, (root id, docs dir as cased):
            none when error is set
        top_level: Its top-level set (lowercased): its allow-list, its
            excludes' first segments and its index roots
        known_dirs: Its docs dirs linked locally, {name.lower(): name}: those
            its hash dir shows (naming.dirmap) and its jobs'
        error: Why its jobs are skipped this run (7(f)): an error for the run
    """

    site: DocCSite
    jobs: List[Tuple[str, str]] = field(default_factory=list)
    top_level: Set[str] = field(default_factory=set)
    known_dirs: Dict[str, str] = field(default_factory=dict)
    error: Optional[str] = None


async def load_site(site: DocCSite, rate_limiter: Optional[AdaptiveRateLimiter] = None) -> SiteRun:
    """A site's share of the run: its index root loaded (7(f)), its jobs and its top-level set.

    Its _site.json records the site (metadata.site) on every load, so a
    site that later leaves the config is found (gone_sites).

    Args:
        site: The site
        rate_limiter: The limiter its jobs share
    """
    run = SiteRun(site=site)
    roots: List[str] = []
    async with SiteIndexLoader(site, rate_limiter) as index:
        assert isinstance(index, SiteIndexLoader)
        index.hash_manager.set_metadata(SITE_KEY, site.name)
        if site.index_url:
            state, roots, why = await index.load()
            if state == "gone":
                logger.warning("index_root_gone", site=site.name, url=site.index_url, error=why)
                roots = persisted_index_roots(site)
                if not roots:
                    run.error = f"{site.name}: index root gone (404/410) with no index_roots persisted: {why}"
            elif state == "failed":
                run.error = f"{site.name}: index root failed: {why}"
    if run.error is not None:
        logger.error("index_root_failed", site=site.name, url=site.index_url, error=run.error)
        return run

    hash_dir = Config.get_hash_dir(site.namespace)
    cased = {root.lower(): root for root in roots}
    run.top_level = (
        {root.lower() for root in site.roots}
        | {exclude.split("/", 1)[0].lower() for exclude in site.excludes}
        | set(cased)
    )
    run.known_dirs = dirmap(hash_dir, site.json_prefix) if hash_dir.exists() else {}
    for root in site.roots:
        dir_name = AppleJSONDocumentationScraper._canonical_framework_id(cased.get(root, root), hash_dir)
        run.jobs.append((root, dir_name))
        run.known_dirs[dir_name.lower()] = dir_name
    return run


def config_removals(site: DocCSite) -> List[SiteRemoval]:
    """Rule 7(a): the site's top-level hash files whose root left its allow-list, each with its dir.

    A module's hash file (metadata.module) is never one: modules leave only
    through the module rules. One that can't be read counts as top-level,
    unless a readable file of the site lists it in child_modules (it may be
    a module's).
    """
    hash_dir = Config.get_hash_dir(site.namespace)
    if not hash_dir.is_dir():
        return []
    roots = {root.lower() for root in site.roots}
    candidates: List[Tuple[str, bool]] = []
    children: Set[str] = set()
    for path in sorted(hash_dir.glob(f"*{HASH_FILE_SUFFIX}")):
        name = path.name[: -len(HASH_FILE_SUFFIX)]
        try:
            _, metadata = read_hash_file(path)
        except (OSError, ValueError):
            candidates.append((name, False))
            continue
        children |= {str(child).lower() for child in metadata_ids(metadata.get(CHILD_MODULES_KEY))}
        candidates.append((name, bool(metadata.get(MODULE_KEY))))
    removals = []
    for name, module in candidates:
        if module or name.lower() in roots or name.lower() in children:
            continue
        logger.warning("root_not_configured", site=site.name, root=name)
        removals.append(SiteRemoval(
            site=site.name,
            namespace=site.namespace,
            framework_id=name,
            output_dir=Config.get_framework_output_dir(name, namespace=site.namespace),
            hash_file=Config.get_hash_file(name, namespace=site.namespace),
        ))
    return removals


def gone_sites(configured: Sequence[DocCSite]) -> List[SiteRemoval]:
    """Rule 7(a): the namespaces whose site left the config, each whole.

    A dir under .hashes holding a _site.json (at any depth: SPI's are
    .hashes/SPI/<repo>/) that is no configured site's hash dir.
    """
    if not Config.CACHE_DIR.is_dir():
        return []
    configured_dirs = {str(Config.get_hash_dir(site.namespace)).lower() for site in configured}
    removals = []
    for path in sorted(Config.CACHE_DIR.rglob(SITE_FILE)):
        hash_dir = path.parent
        if hash_dir == Config.CACHE_DIR or str(hash_dir).lower() in configured_dirs:
            continue
        namespace = hash_dir.relative_to(Config.CACHE_DIR).as_posix()
        try:
            _, metadata = read_hash_file(path)
        except (OSError, ValueError):
            metadata = {}
        name = metadata.get(SITE_KEY) if isinstance(metadata.get(SITE_KEY), str) else namespace
        logger.warning("site_not_configured", site=name, namespace=namespace)
        removals.append(SiteRemoval(
            site=str(name),
            namespace=namespace,
            framework_id="",
            output_dir=Config.get_docs_dir(namespace),
            hash_file=hash_dir,
        ))
    return removals


def check_namespaces(sites: Sequence[DocCSite], reserved: Dict[str, str], apple_ids: Set[str]) -> None:
    """The startup assertion: no DocC namespace's top-level dir is another's.

    Not, case-insensitively, a top-level dir of the MLX, Swift or HIG
    scrapers (their orphan scans cover their whole dirs, so they would
    delete the site's pages every run), nor an Apple hash file's id; and no
    two sites share a namespace.

    Raises:
        ValueError: A namespace collides (the run aborts before scraping)
    """
    seen: Dict[str, str] = {}
    for site in sites:
        if not site.namespace:
            raise ValueError(f"DocC site {site.name} has no namespace")
        top = site.namespace_top.lower()
        if top in reserved:
            raise ValueError(f"DocC site {site.name}'s namespace {site.namespace} is another scraper's dir "
                             f"({reserved[top]})")
        if top in apple_ids:
            raise ValueError(f"DocC site {site.name}'s namespace {site.namespace} is an Apple framework's dir")
        if site.namespace.lower() in seen:
            raise ValueError(f"DocC sites {seen[site.namespace.lower()]} and {site.name} share the namespace "
                             f"{site.namespace}")
        seen[site.namespace.lower()] = site.name
