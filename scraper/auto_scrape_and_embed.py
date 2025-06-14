#!/usr/bin/env python3
"""
Combined scraping and embedding script for automated weekly updates.
This script runs the scraper and then automatically triggers embedding generation.
"""

import os
import sys
import argparse
import subprocess
import logging
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("auto_scrape_and_embed")


def run_scraper(skip_confirmation=False):
    """Run the main scraping process"""
    logger.info("🚀 Starting Apple Documentation scraping...")
    
    try:
        # Change to project root directory
        project_root = Path(__file__).parent.parent
        os.chdir(project_root)
        
        # Build command for scraping
        cmd = [sys.executable, "scrape.py", "--all"]
        
        if skip_confirmation:
            cmd.append("--yes")
            logger.info("✅ Auto-confirmed scraping (--yes flag)")
        
        # Run the scraper
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            logger.error(f"❌ Scraping failed with return code {result.returncode}")
            logger.error(f"Error output: {result.stderr}")
            return False
        
        # Log output
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line.strip():
                    logger.info(f"Scraper: {line}")
        
        logger.info("✅ Scraping complete!")
        return True
        
    except Exception as e:
        logger.error(f"❌ Scraping failed: {e}", exc_info=True)
        return False


def run_embedding_generation():
    """Run the embedding generation process"""
    logger.info("🧠 Starting embedding generation...")
    
    try:
        # Path to the build_index.py script
        build_script = Path(__file__).parent.parent / "mcp-server" / "scripts" / "build_index.py"
        
        if not build_script.exists():
            logger.error(f"❌ Embedding script not found: {build_script}")
            return False
        
        # Run the embedding script
        cmd = [
            sys.executable,
            str(build_script),
            "--yes"  # Auto-confirm
        ]
        
        # Add environment variables
        env = os.environ.copy()
        
        result = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True,
            cwd=build_script.parent
        )
        
        if result.returncode != 0:
            logger.error(f"❌ Embedding generation failed with return code {result.returncode}")
            logger.error(f"Error output: {result.stderr}")
            return False
        
        # Log output
        if result.stdout:
            for line in result.stdout.split('\n'):
                if line.strip():
                    logger.info(f"Embeddings: {line}")
        
        logger.info("✅ Embedding generation complete!")
        return True
        
    except Exception as e:
        logger.error(f"❌ Embedding generation failed: {e}", exc_info=True)
        return False


def cleanup_markdown_files():
    """Clean up markdown files if KEEP_MARKDOWN_FILES is false"""
    keep_markdown = os.getenv("KEEP_MARKDOWN_FILES", "true").lower() == "true"
    
    if not keep_markdown:
        logger.info("🗑️  Cleaning up markdown files (KEEP_MARKDOWN_FILES=false)...")
        
        docs_path = Path(__file__).parent.parent / "documentation"
        if docs_path.exists():
            md_count = 0
            for md_file in docs_path.rglob("*.md"):
                try:
                    md_file.unlink()
                    md_count += 1
                except Exception as e:
                    logger.warning(f"Could not delete {md_file}: {e}")
            
            logger.info(f"✅ Deleted {md_count:,} markdown files")
            
            # Clean up empty directories
            for dirpath in sorted(docs_path.rglob("*"), reverse=True):
                if dirpath.is_dir() and not any(dirpath.iterdir()):
                    try:
                        dirpath.rmdir()
                    except:
                        pass
    else:
        logger.info("📁 Keeping markdown files (KEEP_MARKDOWN_FILES=true)")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Automated Apple documentation scraping and embedding"
    )
    parser.add_argument(
        "--embed",
        action="store_true",
        help="Also generate embeddings after scraping"
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip all confirmation prompts"
    )
    
    args = parser.parse_args()
    
    logger.info("="*60)
    logger.info("🍎 Apple Documentation Auto-Update")
    logger.info(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*60)
    
    # Run scraping
    scrape_success = run_scraper(skip_confirmation=args.yes)
    
    if not scrape_success:
        logger.error("❌ Scraping failed, skipping embedding generation")
        return 1
    
    # Run embedding if requested
    if args.embed:
        embed_success = run_embedding_generation()
        
        if not embed_success:
            logger.error("❌ Embedding generation failed")
            return 1
        
        # Clean up markdown files if configured
        cleanup_markdown_files()
    
    logger.info("="*60)
    logger.info("✅ Auto-update completed successfully!")
    logger.info(f"📅 Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*60)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())