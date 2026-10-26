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
sees them. Its roots are an explicit allow-list (each a job, as an Apple
technology is), and its top-level set is the allow-list, its excludes and
the first segments its index root lists (scrape_all_frameworks.load_site).
"""

from dataclasses import dataclass
from typing import Final, Optional, Tuple


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
        index_url: Its index root, the JSON page whose references list the
            site's top-level pages (load_site), if it has one
        roots: The root ids (lowercased) it crawls, each a job; empty for
            Apple, whose roots are technologies.json's
        excludes: Documentation paths (lowercased, without "/documentation/")
            never fetched: a root id, or a page with every page under it
    """

    name: str
    site_url: str
    doc_base: str
    json_base: str
    bundle_prefix: str
    label: str = "Apple Developer"
    namespace: str = ""
    index_url: Optional[str] = None
    roots: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()

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

# The DocC sites other than Apple's, scraped in the Apple process (scrape.py)
DOCC_SITES: Final[Tuple[DocCSite, ...]] = (SWIFT_ORG,)
