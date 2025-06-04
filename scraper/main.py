"""Main entry point for Apple documentation scraper."""

import asyncio
import sys
from pathlib import Path
from typing import List, Optional

import click

from scraper.apple_scraper import AppleDocumentationScraper
from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.config import Config
from scraper.framework_discovery import discover_frameworks
from scraper.utils.logger import setup_logging, get_logger

logger = get_logger(__name__)


@click.group()
@click.option('--log-level', default='INFO', help='Logging level')
@click.option('--log-file', type=click.Path(), help='Log file path')
@click.option('--debug', is_flag=True, help='Enable debug mode')
def cli(log_level: str, log_file: Optional[str], debug: bool) -> None:
    """Apple Developer Documentation Scraper."""
    # Update config
    Config.LOG_LEVEL = log_level
    if log_file:
        Config.LOG_FILE = Path(log_file)
    if debug:
        Config.DEBUG = True
        Config.LOG_LEVEL = 'DEBUG'
    
    # Setup logging
    setup_logging(
        log_level=Config.LOG_LEVEL,
        log_file=Config.LOG_FILE,
        log_format=Config.LOG_FORMAT
    )
    
    # Ensure directories exist
    Config.ensure_directories()


@cli.command('scrape-page')
@click.argument('framework_id')
@click.argument('url')
async def scrape_page(framework_id: str, url: str) -> None:
    """Scrape a single documentation page."""
    logger.info("scraping_single_page", framework=framework_id, url=url)
    
    async with AppleJSONDocumentationScraper(framework_id) as scraper:
        data = await scraper.extract_page_data(None, url)
        if data:
            await scraper.save_page_data(url, data)
            click.echo(f"Successfully scraped: {url}")
        else:
            click.echo(f"Failed to scrape: {url}")


@cli.command('scrape-framework')
@click.argument('framework_id')
@click.option('--limit', type=int, help='Limit number of pages to scrape')
async def scrape_framework(framework_id: str, limit: Optional[int]) -> None:
    """Scrape an entire framework."""
    logger.info("scraping_framework", framework=framework_id, limit=limit)
    
    async with AppleJSONDocumentationScraper(framework_id) as scraper:
        # First discover all URLs
        click.echo(f"Discovering pages for {framework_id}...")
        await scraper.discover_framework_pages(f"https://developer.apple.com/documentation/{framework_id}")
        
        urls = list(scraper.discovered_urls)
        if limit:
            urls = urls[:limit]
        
        click.echo(f"Found {len(scraper.discovered_urls)} pages, scraping {len(urls)}...")
        
        # Scrape all pages
        stats = {'pages_scraped': 0, 'pages_failed': 0}
        for i, url in enumerate(urls, 1):
            try:
                data = await scraper.extract_page_data(None, url)
                if data:
                    await scraper.save_page_data(url, data)
                    stats['pages_scraped'] += 1
                    if i % 10 == 0:
                        click.echo(f"Progress: {i}/{len(urls)} pages")
                else:
                    stats['pages_failed'] += 1
            except Exception as e:
                logger.error(f"Failed to scrape {url}: {e}")
                stats['pages_failed'] += 1
        
        click.echo(f"\nScraping complete:")
        click.echo(f"  Pages scraped: {stats['pages_scraped']}")
        click.echo(f"  Pages failed: {stats['pages_failed']}")


@cli.command()
@click.argument('framework_id')
async def discover(framework_id: str) -> None:
    """Discover all pages in a framework."""
    logger.info("discovering_framework_pages", framework=framework_id)
    
    async with AppleJSONDocumentationScraper(framework_id) as scraper:
        await scraper.discover_framework_pages(f"https://developer.apple.com/documentation/{framework_id}")
        
        urls = sorted(scraper.discovered_urls)
        click.echo(f"\nDiscovered {len(urls)} pages in {framework_id}:")
        
        # Group by type (classes, protocols, etc)
        by_type = {}
        for url in urls:
            parts = url.split('/')
            if len(parts) > 5:
                type_hint = parts[5]  # Usually the type indicator
                by_type.setdefault(type_hint, []).append(url)
        
        for type_name, type_urls in sorted(by_type.items())[:5]:
            click.echo(f"\n{type_name} ({len(type_urls)} items):")
            for url in type_urls[:3]:
                click.echo(f"  - {url}")
            if len(type_urls) > 3:
                click.echo(f"  ... and {len(type_urls) - 3} more")


@cli.command('discover-frameworks')
@click.option('--save-to', type=click.Path(), help='Save framework list to file')
async def discover_frameworks_cmd(save_to: Optional[str]) -> None:
    """Discover all available Apple frameworks."""
    logger.info("starting_framework_discovery")
    
    frameworks = await discover_frameworks()
    
    # Display summary
    click.echo(f"\nDiscovered {len(frameworks)} frameworks:")
    
    # Group by category
    by_category = {}
    for fw in frameworks:
        category = fw.get('category', 'other')
        by_category.setdefault(category, []).append(fw)
    
    for category, items in sorted(by_category.items()):
        click.echo(f"\n{category.upper()} ({len(items)} frameworks):")
        for fw in items[:5]:  # Show first 5
            click.echo(f"  - {fw['name']} ({fw['id']})")
        if len(items) > 5:
            click.echo(f"  ... and {len(items) - 5} more")
    
    if save_to:
        output_path = Path(save_to)
        output_path.write_text(
            '\n'.join(f"{fw['id']},{fw['name']},{fw['url']}" for fw in frameworks)
        )
        click.echo(f"\nSaved framework list to {save_to}")


@cli.command('scrape-legacy')
@click.argument('framework_id')
@click.option('--dry-run', is_flag=True, help='Discover URLs without scraping')
@click.option('--limit', type=int, help='Limit number of pages to scrape')
async def scrape_legacy(framework_id: str, dry_run: bool, limit: Optional[int]) -> None:
    """[Legacy] Scrape documentation for a specific framework using the old scraper."""
    if dry_run:
        Config.DRY_RUN = True
    
    logger.info(
        "starting_scrape",
        framework=framework_id,
        dry_run=dry_run,
        limit=limit
    )
    
    # Use generic scraper for all frameworks
    async with AppleDocumentationScraper(framework_id) as scraper:
        if dry_run:
            urls = await scraper.discover_urls()
            click.echo(f"\nDiscovered {len(urls)} URLs for {framework_id}:")
            for url in urls[:10]:
                click.echo(f"  - {url}")
            if len(urls) > 10:
                click.echo(f"  ... and {len(urls) - 10} more")
        else:
            stats = await scraper.scrape_framework()
            click.echo(f"\nScraping complete:")
            click.echo(f"  Pages scraped: {stats['pages_scraped']}")
            click.echo(f"  Pages skipped: {stats['pages_skipped']}")
            click.echo(f"  Pages failed: {stats['pages_failed']}")
            click.echo(f"  Duration: {stats.get('duration', 0):.1f}s")


@cli.command()
@click.option('--frameworks', '-f', multiple=True, help='Specific frameworks to scrape')
@click.option('--category', '-c', help='Scrape all frameworks in a category')
@click.option('--all', 'scrape_all', is_flag=True, help='Scrape all frameworks')
@click.option('--parallel', type=int, default=1, help='Number of parallel scrapers')
async def scrape_batch(
    frameworks: List[str],
    category: Optional[str],
    scrape_all: bool,
    parallel: int
) -> None:
    """Scrape multiple frameworks in batch."""
    # Discover available frameworks
    all_frameworks = await discover_frameworks()
    
    # Determine which frameworks to scrape
    to_scrape = []
    
    if scrape_all:
        to_scrape = all_frameworks
    elif category:
        to_scrape = [fw for fw in all_frameworks if fw.get('category') == category]
    elif frameworks:
        # Find matching frameworks
        for fw_id in frameworks:
            matching = [fw for fw in all_frameworks if fw['id'].lower() == fw_id.lower()]
            if matching:
                to_scrape.extend(matching)
            else:
                logger.warning(f"Framework not found: {fw_id}")
    
    if not to_scrape:
        click.echo("No frameworks to scrape")
        return
    
    click.echo(f"\nPreparing to scrape {len(to_scrape)} frameworks:")
    for fw in to_scrape[:5]:
        click.echo(f"  - {fw['name']} ({fw['id']})")
    if len(to_scrape) > 5:
        click.echo(f"  ... and {len(to_scrape) - 5} more")
    
    # Scrape in batches
    for i in range(0, len(to_scrape), parallel):
        batch = to_scrape[i:i + parallel]
        tasks = []
        
        for fw in batch:
            async def scrape_framework(framework_id: str, framework_name: str):
                async with AppleDocumentationScraper(framework_id, framework_name) as scraper:
                    return await scraper.scrape_framework()
            
            tasks.append(scrape_framework(fw['id'], fw['name']))
        
        # Run batch
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Report results
        for fw, result in zip(batch, results):
            if isinstance(result, Exception):
                logger.error(f"Failed to scrape {fw['name']}: {result}")
            else:
                logger.info(f"Completed {fw['name']}: {result}")


@cli.command()
@click.argument('framework_id')
async def validate(framework_id: str) -> None:
    """Validate scraped documentation for a framework."""
    output_dir = Config.get_framework_output_dir(framework_id)
    
    if not output_dir.exists():
        click.echo(f"No documentation found for {framework_id}")
        return
    
    # Count files
    md_files = list(output_dir.rglob("*.md"))
    click.echo(f"\nValidation for {framework_id}:")
    click.echo(f"  Total files: {len(md_files)}")
    
    # Check file sizes
    total_size = sum(f.stat().st_size for f in md_files)
    click.echo(f"  Total size: {total_size / 1024 / 1024:.1f} MB")
    
    # Sample content check
    issues = []
    for file in md_files[:10]:  # Check first 10 files
        content = file.read_text()
        
        # Check for common issues
        if len(content) < 100:
            issues.append(f"Very short content: {file.name}")
        if "# " not in content:
            issues.append(f"No title found: {file.name}")
        if "```" not in content and "code" in file.name.lower():
            issues.append(f"No code blocks: {file.name}")
    
    if issues:
        click.echo(f"\nPotential issues found:")
        for issue in issues[:5]:
            click.echo(f"  - {issue}")
        if len(issues) > 5:
            click.echo(f"  ... and {len(issues) - 5} more")
    else:
        click.echo("\nNo obvious issues found!")


def main() -> None:
    """Main entry point."""
    # Let click handle everything
    cli()


if __name__ == '__main__':
    main()