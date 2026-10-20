"""Image and video URLs of DocC pages, shared by the Apple and HIG scrapers.

Dependency-free: the HIG scraper (scripts/scrape_hig_docs.py) imports it with
the repo root on sys.path.
"""

from typing import Any, Dict, List, Optional


def hosting_root(json_base_url: str) -> str:
    """The DocC hosting root of a JSON API base URL: its prefix before "/data/".

    https://developer.apple.com/tutorials/data/documentation ->
    https://developer.apple.com/tutorials. Apple serves assets under it
    (/tutorials/images/…, /tutorials/videos/…); the same path at the site root
    is a 404.
    """
    return json_base_url.split('/data/', 1)[0]


def asset_url(url: str, root: str) -> str:
    """An asset URL as linked from a page: a root-relative URL ("/images/…")
    under the hosting root (plain concatenation: urljoin would drop the root's
    path), anything else unchanged."""
    if url.startswith('/'):
        return f"{root}{url}"
    return url


def pick_variant(variants: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """The variant an asset reference is shown with: 2x and light, else light,
    else the first. None when there is none."""
    if not variants:
        return None
    for variant in variants:
        traits = variant.get('traits') or []
        if '2x' in traits and 'light' in traits:
            return variant
    for variant in variants:
        if 'light' in (variant.get('traits') or []):
            return variant
    return variants[0]


def variant_url(reference: Dict[str, Any], root: str) -> str:
    """The URL of an asset reference's preferred variant, under the hosting
    root; "" when it has none."""
    variant = pick_variant(reference.get('variants') or [])
    url = (variant or {}).get('url') or ''
    return asset_url(url, root) if url else ''
