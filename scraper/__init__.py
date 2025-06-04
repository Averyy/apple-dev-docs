"""Apple Documentation Scraper package."""

from scraper.json_scraper import AppleJSONDocumentationScraper

# Use the JSON scraper as the default
AppleDocumentationScraper = AppleJSONDocumentationScraper

__all__ = ['AppleDocumentationScraper', 'AppleJSONDocumentationScraper']