#!/usr/bin/env python3
"""
Build the navigator-path fixture of the naming injectivity test (tests/test_naming.py).

Apple's navigator index of a framework (https://developer.apple.com/tutorials/
data/index/<dir>) lists its pages, including many the crawl doesn't reach
yet (e.g. Objective-C-only symbols). The injectivity test also checks that
these would never share a file with each other or with our pages. This script
fetches the index of every Apple docs dir (the dirmap of .hashes: ~400
requests, at most --rate per second) and writes every path under
/documentation/ it lists, in every interface language, one per line: lowercased,
with dot segments '-escaped as the crawler does (the identity the scraper's
JSON URLs give), sorted.

Run it in the scratch copy at window-gate time (Apple's indexes change), then
the test with the fixture:
    python scripts/utilities/build_navigator_fixture.py --out /tmp/navigator_paths.txt
    NAVIGATOR_FIXTURE=/tmp/navigator_paths.txt python -m pytest tests/test_naming.py

--only fetches just the named dirs (any casing), for a quick sample.

Exit code: 0, or 1 if an index fetch failed with something other than 404
(after retries; the fixture is written without it, so re-run).
"""

import argparse
import asyncio
import sys
import time
from pathlib import Path
from typing import Any, Final, List, Optional, Set, Tuple

import httpx

# The repo root, for the scraper package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scraper.config import Config
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.naming import dirmap

INDEX_URL: Final = "https://developer.apple.com/tutorials/data/index/{}"
DOC_PATH_PREFIX: Final = "/documentation/"
RETRIES: Final = 3


def doc_paths(node: Any, found: Set[str]) -> None:
    """Every "path" under /documentation/ in a navigator index, as the crawler's identity."""
    if isinstance(node, dict):
        path = node.get("path")
        if isinstance(path, str) and path.startswith(DOC_PATH_PREFIX):
            found.add(AppleJSONDocumentationScraper._escape_dot_path_segments(path.lower()))
        for value in node.values():
            doc_paths(value, found)
    elif isinstance(node, list):
        for value in node:
            doc_paths(value, found)


async def fetch_index(client: httpx.AsyncClient, name: str) -> Optional[Any]:
    """A dir's navigator index; None on a 404. Raises on any other failure, after retries."""
    url = INDEX_URL.format(name.lower())
    for attempt in range(RETRIES + 1):
        try:
            response = await client.get(url)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except (httpx.HTTPError, ValueError):
            if attempt == RETRIES:
                raise
            await asyncio.sleep(2 ** attempt)
    return None


async def build(names: List[str], rate: float) -> Tuple[Set[str], List[str], List[str]]:
    """The paths of every named dir's index; (paths, dirs without an index, failed dirs)."""
    found: Set[str] = set()
    missing: List[str] = []
    failed: List[str] = []
    async with httpx.AsyncClient(
        timeout=Config.REQUEST_TIMEOUT, headers={"User-Agent": Config.USER_AGENT}, follow_redirects=True
    ) as client:
        for i, name in enumerate(names, 1):
            started = time.monotonic()
            try:
                index = await fetch_index(client, name)
            except (httpx.HTTPError, ValueError) as e:
                failed.append(f"{name}: {e}")
            else:
                if index is None:
                    missing.append(name)
                else:
                    before = len(found)
                    doc_paths(index, found)
                    print(f"[{i}/{len(names)}] {name}: {len(found) - before:,} new paths ({len(found):,} in all)")
            await asyncio.sleep(max(0.0, 1 / rate - (time.monotonic() - started)))
    return found, missing, failed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, required=True, help="The fixture file to write")
    parser.add_argument("--only", help="Comma-separated dirs to fetch (default: every Apple docs dir)")
    parser.add_argument("--rate", type=float, default=5.0, help="Requests per second at most (default 5)")
    args = parser.parse_args()

    dirs = dirmap(Config.CACHE_DIR)
    if args.only:
        wanted = [name.strip().lower() for name in args.only.split(",") if name.strip()]
        unknown = [name for name in wanted if name not in dirs]
        if unknown:
            print(f"❌ Not an Apple docs dir in {Config.CACHE_DIR}: {', '.join(unknown)}")
            return 1
        names = [dirs[name] for name in wanted]
    else:
        names = sorted(dirs.values())
    if not names:
        print(f"❌ No Apple hash file in {Config.CACHE_DIR}")
        return 1

    found, missing, failed = asyncio.run(build(names, args.rate))
    args.out.write_text("".join(f"{path}\n" for path in sorted(found)), encoding="utf-8")
    print(f"Wrote {len(found):,} paths from {len(names) - len(missing) - len(failed)} indexes to {args.out}")
    if missing:
        print(f"  no index (404): {len(missing)}: {', '.join(missing)}")
    for failure in failed:
        print(f"❌ {failure}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
