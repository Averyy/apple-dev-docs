"""The DocC sites the scraper reads.

A DocCSite is one site's URLs: where its documentation pages and their JSON
are, what its references' root-relative URLs are under, and the doc://
prefix of its own bundles. The JSON scraper, the page naming
(naming.page_path, naming.dirmap) and the local links (links.doc_link) take
every URL from it, never from a literal. APPLE is developer.apple.com (its
asset CDN is json_scraper.DOCS_ASSETS_URL).
"""

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class DocCSite:
    """One DocC site's URLs.

    Attributes:
        name: The site's name, its key in the run's sinks (sink.SinkRegistry)
        site_url: The site's origin: a reference's root-relative URL
            ("/documentation/…") is under it
        doc_base: The base of its documentation pages' URLs:
            <doc_base>/<framework>/…
        json_base: The base of its pages' JSON: <json_base>/<framework>/….json
        bundle_prefix: How the doc:// identifiers of its own bundles start
    """

    name: str
    site_url: str
    doc_base: str
    json_base: str
    bundle_prefix: str

    @property
    def doc_prefix(self) -> str:
        """A documentation page's URL up to its path: "<doc_base>/"."""
        return f"{self.doc_base}/"

    @property
    def json_prefix(self) -> str:
        """A page's JSON URL up to its path: "<json_base>/"."""
        return f"{self.json_base}/"

    def doc_url(self, path: str) -> str:
        """The URL of the documentation page at path (what follows "<doc_base>/")."""
        return f"{self.doc_prefix}{path}"

    def url(self, url_path: str) -> str:
        """A root-relative URL ("/…") of the site, made absolute."""
        return f"{self.site_url}{url_path}"

    def is_own_identifier(self, identifier: str) -> bool:
        """Whether a doc:// identifier is of one of the site's own bundles."""
        return identifier.startswith(self.bundle_prefix)


APPLE: Final = DocCSite(
    name="apple",
    site_url="https://developer.apple.com",
    doc_base="https://developer.apple.com/documentation",
    json_base="https://developer.apple.com/tutorials/data/documentation",
    bundle_prefix="doc://com.apple.",
)
