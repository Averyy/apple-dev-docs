#!/usr/bin/env python3
"""
Single health test for embedding system
"""

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timedelta

sys.path.append(str(Path(__file__).parent.parent))

def test_embedding_health():
    """Run all health checks for the embedding system"""
    print("EMBEDDING SYSTEM HEALTH CHECK")
    print("="*50)
    
    project_root = Path(__file__).parent.parent
    errors = []
    
    # 1. Check vectorstore
    vectorstore = project_root / "vectorstore"
    if not vectorstore.exists():
        errors.append("Vectorstore directory not found")
    else:
        db_files = list(vectorstore.rglob("*.bin")) + list(vectorstore.rglob("*.parquet"))
        if not db_files:
            errors.append("No database files in vectorstore")
        else:
            size_gb = sum(f.stat().st_size for f in db_files) / (1024**3)
            print(f"✅ Vectorstore: {size_gb:.1f}GB")
    
    # 2. Check ChromaDB collection
    try:
        import chromadb
        client = chromadb.PersistentClient(path=str(vectorstore))
        collection = client.get_collection("apple_docs")
        count = collection.count()
        
        if count < 300000:
            errors.append(f"Too few embeddings: {count}")
        else:
            # Test query performance
            start = time.time()
            results = collection.query(
                query_embeddings=[[0.1] * 1536],
                n_results=5
            )
            elapsed = time.time() - start
            
            if elapsed > 1.0:
                errors.append(f"Query too slow: {elapsed:.2f}s")
            
            print(f"✅ Collection: {count:,} embeddings, {elapsed:.3f}s query")
    except Exception as e:
        errors.append(f"ChromaDB error: {e}")
    
    # 3. Check hash file
    hash_file = project_root / ".hashes" / "embedding_hashes.json"
    if not hash_file.exists():
        errors.append("Hash file not found")
    else:
        try:
            with open(hash_file, 'r') as f:
                data = json.load(f)
            
            if "metadata" not in data or "hashes" not in data:
                errors.append("Invalid hash file structure")
            else:
                last_updated = datetime.fromisoformat(data["metadata"]["last_updated"])
                age = datetime.now() - last_updated
                if age > timedelta(days=30):
                    errors.append(f"Hash file too old: {age.days} days")
                
                print(f"✅ Hash file: {data['metadata']['total_pages']:,} entries")
        except Exception as e:
            errors.append(f"Hash file error: {e}")
    
    # 4. Check documentation
    docs_dir = project_root / "documentation"
    if not docs_dir.exists():
        errors.append("Documentation directory not found")
    else:
        md_files = list(docs_dir.rglob("*.md"))
        if len(md_files) < 300000:
            errors.append(f"Too few docs: {len(md_files)}")
        else:
            print(f"✅ Documentation: {len(md_files):,} files")
    
    # 5. Summary
    print("="*50)
    if errors:
        print(f"❌ FAILED: {len(errors)} issues found:")
        for error in errors:
            print(f"  - {error}")
        return 1
    else:
        print("✅ HEALTHY: All checks passed")
        return 0

if __name__ == "__main__":
    sys.exit(test_embedding_health())