"""The DocC sites the scraper reads.

A DocCSite is one site's URLs: where its documentation pages and their JSON
are, what its references' root-relative URLs are under, and the doc://
prefix of its own bundles. The JSON scraper, the page naming
(naming.page_path, naming.dirmap) and the local links (links.doc_link) take
every URL from it, never from a literal. APPLE is developer.apple.com (its
asset CDN is json_scraper.DOCS_ASSETS_URL).

A site other than Apple's (DOCC_SITES) also has a namespace: its docs dirs
are documentation/<namespace>/<Dir>/ and its hash files
.hashes/<namespace>/<Dir>_hashes.json, so none of them is a top-level dir
of another scraper or an Apple framework, and no glob of .hashes/*_hashes.json
sees them. Its roots (each a job, as an Apple technology is) are either an
explicit allow-list, its top-level set then being the allow-list, its
excludes and the first segments its index root lists (docs.swift.org), or
the first segments of the paths its navigator index lists (a Swift Package
Index package: SPI_PACKAGES), as docc_sites.load_site reads them.
"""

from dataclasses import dataclass
from typing import FrozenSet, Final, Optional, Tuple

# What a DocC site's index (DocCSite.index_url) is. A page index is a DocC
# page whose references list the site's top-level pages; its roots are the
# site's allow-list (docs.swift.org's documentation.json). A navigator index
# is DocC's index/index.json: the first segments of the documentation paths
# it lists are the site's roots, each a job (a Swift Package Index package)
INDEX_PAGE: Final = "page"
INDEX_NAVIGATOR: Final = "navigator"


@dataclass(frozen=True)
class DocCSite:
    """One DocC site's URLs.

    Attributes:
        name: The site's name, its key in the run's sinks (sink.SinkRegistry)
            and on the command line (scrape.py --sites)
        site_url: The site's DocC hosting base: a reference's root-relative
            URL ("/documentation/…") is under it
        doc_base: The base of its documentation pages' URLs:
            <doc_base>/<framework>/…
        json_base: The base of its pages' JSON: <json_base>/<framework>/….json
        bundle_prefix: How the doc:// identifiers of its own bundles start
        label: What a page's footer names it ("View on <label>")
        namespace: The dir its docs dirs and hash files are under
            (documentation/<namespace>/, .hashes/<namespace>/); "" for
            Apple's, which are top-level
        index_url: Its index, if it has one (load_site): the JSON page
            whose references list the site's top-level pages, or its
            navigator index (index_kind)
        index_kind: What its index is: INDEX_PAGE or INDEX_NAVIGATOR
        roots: The root ids (lowercased) it crawls, each a job; empty for
            Apple, whose roots are technologies.json's, and for a site whose
            navigator index lists them
        excludes: Documentation paths (lowercased, without "/documentation/")
            never fetched: a root id, or a page with every page under it
        excluded_pages: The pages its excluded collections list that no
            crawl of it has reached (their paths, as excludes), read at a
            run's start (docc_sites.load_site): a page the collection alone
            holds (a package's proposal template) is never fetched, so a
            link to one keeps its URL (linked_by_url), as one to the
            collection does. Never a crawl rule: a page in-scope curation
            reaches is crawled as ever
        collection_pages: Every page its excluded collections list, read
            with excluded_pages (whether a crawl reached it or not): an
            inline link to one is never followed (a proposal is no page of
            the docs, OD3), so only curation keeps one in the docs
        max_retries: Its requests' retries after a 5xx, 429 or network
            error (None: Config.MAX_RETRIES, Apple's)
        retry_backoff: The wait before the n-th retry after a 5xx or a
            network error is n times this many seconds (None:
            Config.RETRY_BACKOFF_FACTOR, Apple's)
        max_jobs: At most this many jobs of its host's sites run at once
            (0: no cap), the others waiting outside the run's job slots, so
            a host whose rate is low never holds the Apple jobs' slots
        page_gone_runs: A page we have (not a root) is removed once it
            answers 404/410 on this many consecutive runs; on the runs
            before, it is kept and its job's cleanup skipped, with no error
            (1: removed on its first 404/410, as Apple's are)
    """

    name: str
    site_url: str
    doc_base: str
    json_base: str
    bundle_prefix: str
    label: str = "Apple Developer"
    namespace: str = ""
    index_url: Optional[str] = None
    index_kind: str = INDEX_PAGE
    roots: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    excluded_pages: FrozenSet[str] = frozenset()
    collection_pages: FrozenSet[str] = frozenset()
    max_retries: Optional[int] = None
    retry_backoff: Optional[float] = None
    max_jobs: int = 0
    page_gone_runs: int = 1

    @property
    def doc_prefix(self) -> str:
        """A documentation page's URL up to its path: "<doc_base>/"."""
        return f"{self.doc_base}/"

    @property
    def json_prefix(self) -> str:
        """A page's JSON URL up to its path: "<json_base>/"."""
        return f"{self.json_base}/"

    @property
    def doc_path(self) -> str:
        """A reference's root-relative URL of a documentation page, up to its path ("/documentation/")."""
        return self.doc_prefix[len(self.site_url):]

    @property
    def roots_from_index(self) -> bool:
        """Whether its roots are those its navigator index lists (not an allow-list)."""
        return self.index_kind == INDEX_NAVIGATOR

    @property
    def namespace_top(self) -> str:
        """The top-level docs dir its namespace takes ("" for Apple's)."""
        return self.namespace.split("/", 1)[0]

    def doc_url(self, path: str) -> str:
        """The URL of the documentation page at path (what follows "<doc_base>/")."""
        return f"{self.doc_prefix}{path}"

    def url(self, url_path: str) -> str:
        """A root-relative URL ("/…") of the site, made absolute."""
        return f"{self.site_url}{url_path}"

    def is_own_identifier(self, identifier: str) -> bool:
        """Whether a doc:// identifier is of one of the site's own bundles."""
        return identifier.startswith(self.bundle_prefix)

    def framework_label(self, dir_name: str) -> str:
        """What a namespaced docs dir's pages name their framework: <namespace leaf>/<Dir>
        (e.g. Swift-Org/PackagePlugin), so it never equals another source's label.
        An Apple dir's is its name."""
        if not self.namespace:
            return dir_name
        return f"{self.namespace.rsplit('/', 1)[-1]}/{dir_name}"

    def excluded(self, path: str) -> bool:
        """Whether a documentation path (lowercased, without "/documentation/") is never fetched:
        an excluded path, or a page under one."""
        return any(path == exclude or path.startswith(f"{exclude}/") for exclude in self.excludes)

    def linked_by_url(self, path: str) -> bool:
        """Whether a link to a documentation path (as excluded's) keeps its URL: an excluded
        path or a page under one, or exactly one of excluded_pages."""
        return self.excluded(path) or path in self.excluded_pages


APPLE: Final = DocCSite(
    name="apple",
    site_url="https://developer.apple.com",
    doc_base="https://developer.apple.com/documentation",
    json_base="https://developer.apple.com/tutorials/data/documentation",
    bundle_prefix="doc://com.apple.",
)

# docs.swift.org (Phase 5 row 1). Its bundles have no common prefix
# (org.swift.migration.6, com.apple.Swift, APIGuidelines…), so every doc://
# identifier on its pages counts as its own
SWIFT_ORG: Final = DocCSite(
    name="swift-org",
    site_url="https://docs.swift.org/latest",
    doc_base="https://docs.swift.org/latest/documentation",
    json_base="https://docs.swift.org/latest/data/documentation",
    bundle_prefix="doc://",
    label="docs.swift.org",
    namespace="Swift-Org",
    index_url="https://docs.swift.org/latest/data/documentation.json",
    # The allow-list (exact root ids): the migration guide, SwiftPM and its
    # plugin API, the compiler diagnostics, Embedded Swift, Wasm, Android,
    # Linux, swiftly, the VS Code extension, swift-java, C++ interop, DocC
    # and the API Design Guidelines. Never index.json or the root's full
    # references: they hold the 14 private/test stdlib modules
    roots=(
        "migrationguide", "packagemanagerdocs", "packageplugin", "diagnostics", "embeddedswift",
        "wasmguide", "swiftandroid", "swiftlinux", "swiftlydocs", "userdocs",
        "swiftjavadocumentation", "cxx", "cxxstdlib", "docc", "apiguidelines",
    ),
    # Already in the corpus, from Apple or Swift-Book
    excludes=(
        "swift", "testing", "the-swift-programming-language", "regexbuilder", "synchronization",
        "distributed", "observation", "packagedescription",
    ),
)

SPI_URL: Final = "https://swiftpackageindex.com"


def spi_package(owner: str, repo: str, excludes: Tuple[str, ...] = ()) -> DocCSite:
    """A Swift Package Index package's documentation (Phase 5 rows 2-3), from its main branch.

    The packages share one host, so each is its own namespace under SPI
    (documentation/SPI/<repo>/<Module>/, .hashes/SPI/<repo>/), and its pages
    name their framework <repo>/<Module>. Its roots are the first segments
    of the paths its navigator index (index/index.json) lists: SPI builds
    each documentation target as its own bundle, so each is a top-level root.
    """
    base = f"{SPI_URL}/{owner}/{repo}/main"
    return DocCSite(
        name=f"spi-{repo.lower()}",
        site_url=base,
        doc_base=f"{base}/documentation",
        json_base=f"{base}/data/documentation",
        bundle_prefix="doc://",
        label="Swift Package Index",
        namespace=f"SPI/{repo}",
        index_url=f"{base}/index/index.json",
        index_kind=INDEX_NAVIGATOR,
        excludes=excludes,
        # Measured 2026-10-26: ~2% of its requests answer 503, at ~3.7 or
        # ~1.2 requests/s alike, and a URL that did answers the same 503 for
        # ~10 s (its CDN keeps it): of 406 such URLs in an 18.7K-request
        # run, every retry at +2 and +6 s failed, 392 succeeded at +12 s,
        # and the 14 that failed again failed at +20 s too (each answered
        # 200 when fetched later). So its retries wait 6, 12, 18 and 24 s
        # (at +6, +18, +36 and +60 s), each but the first past that window:
        # in a 6.9K-request run, of 160 such URLs 157 succeeded at +18 s,
        # 2 at +36 s and 1 at +60 s, none failed
        max_retries=4,
        retry_backoff=6.0,
        # Its jobs share one limiter, but each fetches one page at a time and
        # its pages take ~0.7 s on average (median 0.3 s, measured
        # 2026-10-26), so 4 jobs reached only ~4.5 requests/s and made it
        # the run's longest step; 8 reach ~9-11/s, under the limiter's
        # 20/s (its 503 rate was the same at ~1.2 and ~3.7 requests/s)
        max_jobs=8,
        # It answers 404 for pages we have while it rebuilds a package's
        # docs: on 2026-10-26 two mlx-swift-lm pages did for one run, one a
        # parent whose 5 children went with it, and all 7 were back the run
        # after. So a page goes on its 2nd 404/410 in a row, and its first
        # keeps it and the pages only it links for that run
        page_gone_runs=2,
    )


# The Swift Package Index packages: CareKit (OD2), the 6 Apple and MLX
# packages that host no DocC of their own, and mlx-swift-lm (OD4). Their
# design proposals aren't documentation (OD3): each proposals collection is
# excluded, and with it the proposals only it lists, which are not under its
# path (logging/slg-0001, not logging/proposals/…): never reached, they are
# linked by URL (excluded_pages)
SPI_PACKAGES: Final[Tuple[DocCSite, ...]] = (
    spi_package("carekit-apple", "CareKit"),
    spi_package("ml-explore", "mlx-swift"),
    spi_package("apple", "swift-argument-parser"),
    spi_package("apple", "swift-log", excludes=("logging/proposals",)),
    spi_package("apple", "swift-async-algorithms"),
    spi_package("apple", "swift-openapi-generator", excludes=("swift-openapi-generator/proposals",)),
    spi_package("apple", "swift-configuration", excludes=("configuration/proposals",)),
    spi_package("ml-explore", "mlx-swift-lm"),
)

# The DocC sites other than Apple's, scraped in the Apple process (scrape.py)
DOCC_SITES: Final[Tuple[DocCSite, ...]] = (SWIFT_ORG, *SPI_PACKAGES)
