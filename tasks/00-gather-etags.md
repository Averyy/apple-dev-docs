# Task 0: Gather ETags for Existing Documentation

## Objective
Collect ETags for all previously scraped documentation to enable efficient change detection in future updates.

## Background
We discovered that Apple's JSON API supports ETags - unique identifiers that change when content is updated. This enables efficient change detection without downloading full content.

## Implementation Steps

### 1. Create ETag Collection Script
`scripts/collect_etags.py`:
```python
#!/usr/bin/env python3
"""
One-time script to collect ETags for all existing documentation.
Only needs to run once to enable efficient future updates.
"""

import asyncio
import httpx
import json
from pathlib import Path
from tqdm import tqdm
import time

class ETagCollector:
    def __init__(self, docs_path="/data/scraped", metadata_path="/data/metadata"):
        self.docs_path = Path(docs_path)
        self.metadata_path = Path(metadata_path)
        self.client = httpx.AsyncClient(timeout=30.0)
        self.etag_cache = {}
        
    async def collect_etags(self):
        """Collect ETags for all scraped documents using HEAD requests"""
        
        # Find all scraped markdown files
        md_files = list(self.docs_path.rglob("*.md"))
        print(f"Found {len(md_files)} documents to process")
        
        # Process in batches to avoid overwhelming the server
        batch_size = 50
        for i in tqdm(range(0, len(md_files), batch_size)):
            batch = md_files[i:i+batch_size]
            tasks = [self.get_etag_for_file(f) for f in batch]
            await asyncio.gather(*tasks)
            
            # Small delay between batches
            await asyncio.sleep(0.5)
        
        # Save all ETags
        self.save_etags()
        
    async def get_etag_for_file(self, file_path):
        """Get ETag for a single file using HEAD request"""
        
        # Convert file path to API URL
        relative_path = file_path.relative_to(self.docs_path)
        url = self.path_to_url(relative_path)
        
        try:
            response = await self.client.head(url)
            if response.status_code == 200:
                etag = response.headers.get('ETag')
                if etag:
                    self.etag_cache[str(relative_path)] = {
                        'etag': etag,
                        'url': url,
                        'collected_at': time.time()
                    }
        except Exception as e:
            print(f"Error getting ETag for {url}: {e}")
    
    def path_to_url(self, relative_path):
        """Convert file path to Apple API URL"""
        # Remove .md extension and convert path
        path_str = str(relative_path).replace('.md', '')
        return f"https://developer.apple.com/tutorials/data/documentation/{path_str}.json"
    
    def save_etags(self):
        """Save collected ETags to metadata"""
        etag_file = self.metadata_path / "etags.json"
        etag_file.parent.mkdir(exist_ok=True)
        
        with open(etag_file, 'w') as f:
            json.dump(self.etag_cache, f, indent=2)
        
        print(f"Saved {len(self.etag_cache)} ETags to {etag_file}")

if __name__ == "__main__":
    collector = ETagCollector()
    asyncio.run(collector.collect_etags())
```

### 2. Update Metadata Structure

Add ETag storage to existing metadata:
```json
{
  "path": "swiftui/text.md",
  "url": "https://developer.apple.com/tutorials/data/documentation/swiftui/text.json",
  "content_hash": "sha256:abc123...",
  "etag": "W/\"399a0f24205d58c9443159732da8989a\"",
  "last_scraped": "2024-01-15T10:30:00Z",
  "last_modified": "2024-01-15T10:30:00Z"
}
```

### 3. Environment Variable for Markdown Storage

Add configuration for markdown file handling:
```
KEEP_MARKDOWN_FILES=true   # Development: Keep markdown files for debugging
KEEP_MARKDOWN_FILES=false  # Production: Delete after embedding to save space
```

This allows the same codebase to work differently in development vs production.

### 4. Integration with Incremental Updates

Update the incremental updater to use ETags:
```python
async def check_for_changes(self, url, stored_etag):
    """Check if content changed using ETag"""
    
    response = await self.client.head(
        url,
        headers={"If-None-Match": stored_etag}
    )
    
    if response.status_code == 304:
        # Not modified
        return False, stored_etag
    elif response.status_code == 200:
        # Modified - return new ETag
        return True, response.headers.get('ETag')
```

## Execution Plan

### One-Time Setup
1. Run `collect_etags.py` on existing scraped content
2. This will make ~237K HEAD requests (lightweight, no body)
3. Estimated time: 1-2 hours with rate limiting
4. Creates `etags.json` mapping file paths to ETags

### Future Benefits
- Change detection becomes ~40x faster
- Only download files that actually changed
- Reduce bandwidth from ~5GB to ~120MB for checks
- More frequent update checks become feasible

## Important Notes
- This is a ONE-TIME operation
- HEAD requests are lightweight and less likely to trigger rate limits
- Once ETags are collected, all future updates use them automatically
- No need to re-embed existing content - just collecting metadata

## Success Criteria
- [ ] All scraped documents have associated ETags
- [ ] ETags are properly stored in metadata
- [ ] Future scraper uses ETags for change detection
- [ ] Update checks complete in <1 hour instead of 3-4 hours

## Time Estimate
1-2 hours to run the collection script (one time only)