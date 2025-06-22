# Quick Wins - Immediate Tasks

## 30-Minute Tasks

### 1. Create Meilisearch Directory Structure
```bash
mkdir -p meilisearch/{data,dumps}
mkdir -p scripts/meilisearch
mkdir -p tests/meilisearch
touch meilisearch/.gitignore
echo "data/" >> meilisearch/.gitignore
echo "dumps/" >> meilisearch/.gitignore
echo "*.ms.snapshot" >> meilisearch/.gitignore
```

### 2. Generate Secure Master Key
```bash
# Generate a secure key (minimum 16 characters)
openssl rand -base64 32

# Add to .env
echo "MEILI_MASTER_KEY=your-generated-key" >> .env
echo "MEILISEARCH_URL=http://192.168.2.5:7700" >> .env
```

### 3. Create Basic Docker Compose
```yaml
# meilisearch/docker-compose.yml
version: '3.8'
services:
  meilisearch:
    image: getmeili/meilisearch:v1.6
    ports:
      - "7700:7700"
    environment:
      - MEILI_MASTER_KEY=${MEILI_MASTER_KEY}
      - MEILI_ENV=production
    volumes:
      - ./data:/meili_data
```

---

## 1-Hour Tasks

### 1. Test Metadata Extraction Locally
Create a simple test script to validate the metadata extraction approach:

```python
# scripts/test_metadata_extraction.py
import re
from pathlib import Path

def quick_extract(file_path):
    content = Path(file_path).read_text()
    
    # Extract title
    title = re.search(r'^# (.+)$', content, re.MULTILINE)
    
    # Extract framework
    framework = re.search(r'\*\*Framework\*\*:\s*(.+)', content)
    
    # Extract platforms
    platforms = re.findall(r'- (iOS|macOS|tvOS|watchOS|visionOS)', content)
    
    return {
        "title": title.group(1) if title else None,
        "framework": framework.group(1) if framework else None,
        "platforms": list(set(platforms))
    }

# Test with a few files
test_files = [
    "documentation/SwiftUI/View.md",
    "documentation/StoreKit/promoting-in-app-purchases.md"
]

for file in test_files:
    if Path(file).exists():
        print(f"\n{file}:")
        print(quick_extract(file))
```

### 2. Count Total Documents
```bash
# Quick document count
find documentation -name "*.md" -type f | wc -l

# Count by framework
find documentation -type d -maxdepth 1 | while read dir; do
    count=$(find "$dir" -name "*.md" -type f 2>/dev/null | wc -l)
    if [ $count -gt 0 ]; then
        echo "$dir: $count files"
    fi
done | sort -t: -k2 -nr | head -20
```

### 3. Install meilisearch-mcp Package
```bash
# Check if package exists and install
pip install meilisearch-mcp

# If not available, check GitHub
git clone https://github.com/meilisearch/meilisearch-mcp.git temp_mcp
cd temp_mcp && pip install -e .
```

---

## 2-Hour Tasks

### 1. Create Minimal Indexing Script
```python
# scripts/quick_index.py
import asyncio
from pathlib import Path
import meilisearch_python_async as meilisearch
import os
from dotenv import load_dotenv

load_dotenv()

async def quick_index():
    client = meilisearch.Client(
        os.getenv('MEILISEARCH_URL'),
        os.getenv('MEILI_MASTER_KEY')
    )
    
    # Create index
    index = client.index('apple-docs')
    
    # Index 10 sample documents
    docs = []
    for i, file in enumerate(Path('documentation').rglob('*.md')):
        if i >= 10:
            break
            
        content = file.read_text()
        doc = {
            'id': str(file).replace('/', '_'),
            'path': str(file),
            'content': content[:1000],  # First 1000 chars
            'framework': file.parts[1] if len(file.parts) > 1 else 'unknown'
        }
        docs.append(doc)
    
    # Add documents
    await index.add_documents(docs)
    print(f"Indexed {len(docs)} documents")
    
    # Test search
    results = await index.search('View')
    print(f"Search results: {results}")

if __name__ == "__main__":
    asyncio.run(quick_index())
```

### 2. Create Health Check Script
```python
# scripts/check_meilisearch.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def check_health():
    url = os.getenv('MEILISEARCH_URL')
    key = os.getenv('MEILI_MASTER_KEY')
    
    # Health check
    try:
        r = requests.get(f"{url}/health")
        print(f"Health: {r.status_code} - {r.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
    
    # Version check
    try:
        r = requests.get(f"{url}/version")
        print(f"Version: {r.json()}")
    except:
        pass
    
    # Stats check (requires auth)
    try:
        headers = {"Authorization": f"Bearer {key}"}
        r = requests.get(f"{url}/stats", headers=headers)
        print(f"Stats: {r.json()}")
    except:
        pass
    
    return True

if __name__ == "__main__":
    check_health()
```

---

## Validation Checklist

### After 30 minutes:
- [ ] Directory structure created
- [ ] Master key generated and saved
- [ ] Basic docker-compose.yml ready

### After 1 hour:
- [ ] Know total document count
- [ ] Metadata extraction tested on sample files
- [ ] meilisearch-mcp package status known

### After 2 hours:
- [ ] Meilisearch deployed (or attempted)
- [ ] Health check script working
- [ ] Sample documents indexed (if Meilisearch running)
- [ ] Basic search tested

---

## If Blocked

### Can't Deploy Meilisearch:
1. Run locally instead:
   ```bash
   docker run -p 7700:7700 -e MEILI_MASTER_KEY=test getmeili/meilisearch:v1.6
   ```

2. Use Meilisearch Cloud free tier:
   - Sign up at https://cloud.meilisearch.com
   - Get API key and URL
   - Update .env

### Can't Install meilisearch-mcp:
1. Proceed with HTTP API directly:
   ```python
   import requests
   # Use requests to call Meilisearch HTTP API
   ```

2. Build minimal MCP wrapper later

### Metadata Extraction Complex:
1. Start with just framework + title
2. Add platforms later
3. Use filename as fallback for API name

---

## Next Steps After Quick Wins

1. **If Meilisearch Running**: Focus on indexing all documents
2. **If Indexing Works**: Build the adapter layer
3. **If Blocked on Infrastructure**: Work on extraction/chunking logic
4. **If All Smooth**: Start performance testing early

Remember: The goal is to validate feasibility quickly, not build perfectly.