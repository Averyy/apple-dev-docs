"""Local links to documentation pages of a DocC site.

A link to a page of a known docs dir of the linking page's site is the path
of the page's file (naming.page_path, the scraper's own path rule) relative
to the linking file's folder: "./" before it unless it starts with "../"
(the MCP server's link resolver tells it from a legacy framework-relative
link by that), percent-encoded with urllib.parse.quote (safe "/,":
parentheses and spaces are encoded, and the server unquotes them), then the
URL's #fragment as it is. A page of any other dir keeps its absolute URL. Whether the target
file exists isn't checked, so a link to a page not yet in the docs heals by
itself once the page is scraped. A page of another site (e.g. Apple's,
linked from docs.swift.org), or one its site excludes (never fetched, e.g. a
package's design proposals and the pages only its proposals collection
lists: DocCSite.linked_by_url), keeps its absolute URL.
"""

import posixpath
from typing import Final, Mapping
from urllib.parse import quote

from scraper.site import APPLE, DocCSite
from scraper.utils.naming import page_path

# The characters an absolute URL in a link holds as they are (markdown_url): RFC 3986's
# reserved ones and "%", so its delimiters and escapes stay. The same as the MCP server's
# (mcp-server/apple_docs_mcp.py link_url) and scripts/utilities/source_policy.py's
URL_SAFE_CHARACTERS: Final = "!#$%&'()*+,/:;=?@[]~"


def markdown_url(url: str) -> str:
    """An absolute URL as a markdown link's destination holds it (a page's footer): every
    character a URL can't hold as it is percent-encoded, and its parentheses too when they
    don't pair up (Apple and the Swift Package Index cut a long symbol's URL inside its
    argument list, and an unclosed "(" leaves no link; the %28 form is the same page).
    Paired ones stay, as in Apple's URLs (init(_:)), so any other page's URL is as it is.
    The MCP server's link_url does the same for a result's link. A reader gets the page's
    URL back with urllib.parse.unquote: a DocC page's URL holds no "%" of its own."""
    url = quote(url, safe=URL_SAFE_CHARACTERS)
    depth = 0
    for char in url:
        depth += {"(": 1, ")": -1}.get(char, 0)
        if depth < 0:
            break
    if depth:
        url = url.replace("(", "%28").replace(")", "%29")
    return url


def link_base(dir_name: str, doc_url: str, site: DocCSite = APPLE) -> str:
    """The folder of a page's file, relative to the docs root: the base of the links on it.

    Args:
        dir_name: The page's framework docs dir
        doc_url: The page's URL (a URL of no page of the dir gives the dir)
        site: The page's DocC site
    """
    path = page_path(dir_name, doc_url, site)
    if path:
        return posixpath.dirname(path)
    return f"{site.namespace}/{dir_name}" if site.namespace else dir_name


def doc_link(url: str, base: str, dirs: Mapping[str, str], site: DocCSite = APPLE) -> str:
    """The link to a page, from a file in base.

    Args:
        url: The page's URL; a page of the site's documentation is
            <its doc prefix><framework>/… (Apple's:
            https://developer.apple.com/documentation/<framework>/…), with
            any ?query (dropped: a file has none) or #fragment
        base: The linking file's folder, relative to the docs root (link_base)
        dirs: The site's known docs dirs, {name.lower(): name}: the framework
            segment matches one in any casing
        site: The linking page's DocC site: a page of any other site keeps its URL

    Returns:
        url as it is, unless it is a page of a known dir the site doesn't
        exclude: then the page's file relative to base, "./" first unless it
        starts with "../", quoted, and the #fragment after ".md"
    """
    if not url.startswith(site.doc_prefix):
        return url
    location, hash_mark, fragment = url.partition('#')
    location = location.partition('?')[0].rstrip('/')
    if site.excludes and site.linked_by_url(location[len(site.doc_prefix):].lower()):
        return url
    dir_name = dirs.get(location[len(site.doc_prefix):].split('/', 1)[0].lower())
    path = page_path(dir_name, location, site) if dir_name else None
    if path is None:
        return url
    relative = posixpath.relpath(path, base)
    if not relative.startswith('../'):
        relative = f'./{relative}'
    return quote(relative, safe='/,') + hash_mark + fragment
