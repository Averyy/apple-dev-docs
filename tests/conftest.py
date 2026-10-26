"""Shared test setup."""

from typing import Iterator

import pytest

from scraper import site


@pytest.fixture(autouse=True)
def no_docc_sites(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """No scrape.py run of a test reaches a real DocC site (docs.swift.org): a
    test that runs one configures its own (site.DOCC_SITES)."""
    monkeypatch.setattr(site, "DOCC_SITES", ())
    yield
