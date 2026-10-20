"""Local links to Apple documentation pages.

A link to a page of a known docs dir is the path of the page's file
(naming.page_path, the scraper's own path rule) relative to the linking
file's folder: "./" before it unless it starts with "../" (the MCP server's
link resolver tells it from a legacy framework-relative link by that),
percent-encoded with urllib.parse.quote (safe "/,": parentheses and spaces
are encoded, and the server unquotes them), then the URL's #fragment as it
is. A page of any other dir keeps its absolute Apple URL. Whether the target
file exists isn't checked, so a link to a page not yet in the docs heals by
itself once the page is scraped.
"""

import posixpath
from typing import Mapping
from urllib.parse import quote

from scraper.utils.naming import DOC_URL_PREFIX, page_path


def link_base(dir_name: str, doc_url: str) -> str:
    """The folder of a page's file, relative to the docs root: the base of the links on it.

    Args:
        dir_name: The page's framework docs dir
        doc_url: The page's URL (a URL of no page of the dir gives the dir)
    """
    path = page_path(dir_name, doc_url)
    return posixpath.dirname(path) if path else dir_name


def doc_link(url: str, base: str, dirs: Mapping[str, str]) -> str:
    """The link to a page, from a file in base.

    Args:
        url: The page's URL; a page of Apple's documentation is
            https://developer.apple.com/documentation/<framework>/…, with any
            ?query (dropped: a file has none) or #fragment
        base: The linking file's folder, relative to the docs root (link_base)
        dirs: The known docs dirs, {name.lower(): name}: the framework
            segment matches one in any casing

    Returns:
        url as it is, unless it is a page of a known dir: then the page's
        file relative to base, "./" first unless it starts with "../",
        quoted, and the #fragment after ".md"
    """
    if not url.startswith(DOC_URL_PREFIX):
        return url
    location, hash_mark, fragment = url.partition('#')
    location = location.partition('?')[0].rstrip('/')
    dir_name = dirs.get(location[len(DOC_URL_PREFIX):].split('/', 1)[0].lower())
    path = page_path(dir_name, location) if dir_name else None
    if path is None:
        return url
    relative = posixpath.relpath(path, base)
    if not relative.startswith('../'):
        relative = f'./{relative}'
    return quote(relative, safe='/,') + hash_mark + fragment
