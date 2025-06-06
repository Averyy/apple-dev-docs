#!/usr/bin/env python3
"""
Apple Documentation Scraper - Main Entry Point

This is the primary script for scraping Apple's developer documentation.
It provides a clean interface to the comprehensive scraping system.

Usage:
    python3 scrape.py                    # Interactive mode with prompts
    python3 scrape.py --all --yes        # Scrape all frameworks without prompts
    python3 scrape.py --frameworks SwiftUI UIKit --yes  # Specific frameworks
    python3 scrape.py --dry-run          # Preview what would be scraped

Examples:
    # Scrape all 342+ frameworks (production run):
    python3 scrape.py --all --yes
    
    # Scrape specific frameworks:
    python3 scrape.py --frameworks SwiftUI UIKit Foundation --yes
    
    # Resume interrupted scraping:
    python3 scrape.py --resume --yes
"""

import sys
import os

# Add scripts directory to path so we can import utilities
scripts_dir = os.path.join(os.path.dirname(__file__), 'scripts', 'utilities')
sys.path.insert(0, scripts_dir)

try:
    from scrape_all_frameworks import scrape_everything
    import asyncio
    
    if __name__ == "__main__":
        # Simply delegate to the main scraper
        asyncio.run(scrape_everything())
        
except ImportError as e:
    print(f"❌ Error importing scraper module: {e}")
    print("💡 Make sure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error running scraper: {e}")
    sys.exit(1)