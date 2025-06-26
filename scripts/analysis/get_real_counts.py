#!/usr/bin/env python3
"""Get real document counts from Meilisearch."""

import os
import meilisearch
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

console = Console()

def get_real_counts():
    """Get actual document counts from Meilisearch."""
    client = meilisearch.Client(
        os.getenv('MEILI_HTTP_ADDR', 'http://localhost:7700'),
        os.getenv('MEILI_MASTER_KEY', '')
    )
    
    index = client.index('apple-docs')
    
    # Get total documents from stats
    stats = index.get_stats()
    total_docs = stats.number_of_documents if hasattr(stats, 'number_of_documents') else 0
    
    console.print(f"📊 Total documents in index: {total_docs:,}")
    
    # Test with higher limits
    console.print("\n🔍 Testing framework counts with higher limits...")
    
    test_frameworks = ['UIKit', 'Foundation', 'Swift', 'kernel']
    
    for framework in test_frameworks:
        # Try with a much higher limit
        result = index.search('', {
            'filter': f'framework = "{framework}"',
            'limit': 0,
            'showRankingScore': False
        })
        
        # Get different count methods
        estimated = result.get('estimatedTotalHits', 0)
        total_hits = result.get('totalHits', 0) 
        hits_count = len(result.get('hits', []))
        
        console.print(f"\n{framework}:")
        console.print(f"  estimatedTotalHits: {estimated:,}")
        console.print(f"  totalHits: {total_hits:,}")
        console.print(f"  hits returned: {hits_count}")
        
        # Try with facets to get accurate count
        facet_result = index.search('', {
            'facets': ['framework'],
            'limit': 0
        })
        
        if 'facetDistribution' in facet_result and 'framework' in facet_result['facetDistribution']:
            framework_facets = facet_result['facetDistribution']['framework']
            if framework in framework_facets:
                console.print(f"  facet count: {framework_facets[framework]:,}")
    
    # Get all framework counts via facets
    console.print("\n📊 All framework counts via facets:")
    facet_result = index.search('', {
        'facets': ['framework'],
        'limit': 0
    })
    
    if 'facetDistribution' in facet_result and 'framework' in facet_result['facetDistribution']:
        frameworks = facet_result['facetDistribution']['framework']
        total_via_facets = 0
        
        # Sort by count
        sorted_frameworks = sorted(frameworks.items(), key=lambda x: x[1], reverse=True)
        
        for framework, count in sorted_frameworks[:20]:
            console.print(f"  {framework:25s}: {count:6,}")
            total_via_facets += count
        
        console.print(f"\nTotal documents (via facets): {total_via_facets:,}")
        console.print(f"Total documents (from stats): {total_docs:,}")
        console.print(f"Difference: {total_docs - total_via_facets:,}")

if __name__ == "__main__":
    get_real_counts()