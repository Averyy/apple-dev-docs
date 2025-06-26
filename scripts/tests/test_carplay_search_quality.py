#!/usr/bin/env python3
"""
Test search quality for CarPlay-related queries
"""

import meilisearch
import json
from datetime import datetime

def test_carplay_searches():
    """Test various CarPlay implementation searches"""
    client = meilisearch.Client('http://localhost:7700', 'local_test_key')
    index = client.index('apple-docs')
    
    # Real-world CarPlay implementation queries
    test_queries = [
        # Basic template searches
        {
            "query": "how to implement CPListTemplate",
            "expected_results": ["CPListTemplate", "init", "delegate"],
            "context": "Developer wants to implement a list template"
        },
        {
            "query": "CarPlay navigation app setup",
            "expected_results": ["CPTemplateApplicationScene", "navigation", "map"],
            "context": "Setting up a navigation app for CarPlay"
        },
        {
            "query": "CPGridTemplate button actions", 
            "expected_results": ["CPGridTemplate", "CPGridButton", "handler"],
            "context": "Handling grid template button clicks"
        },
        # Specific implementation details
        {
            "query": "CPListItem async image loading",
            "expected_results": ["CPListItem", "setImage", "async"],
            "context": "Loading images asynchronously in list items"
        },
        {
            "query": "CarPlay audio app requirements",
            "expected_results": ["audio", "CPNowPlayingTemplate", "MPRemoteCommandCenter"],
            "context": "Building an audio app for CarPlay"
        },
        {
            "query": "CPMapTemplate pan button customization",
            "expected_results": ["CPMapTemplate", "PanDirection", "panButton"],
            "context": "Customizing map controls"
        },
        # Integration queries
        {
            "query": "CarPlay entitlements configuration",
            "expected_results": ["entitlement", "CarPlay", "Info.plist"],
            "context": "Setting up CarPlay entitlements"
        },
        {
            "query": "CPInterfaceController rootTemplate",
            "expected_results": ["CPInterfaceController", "setRootTemplate", "animated"],
            "context": "Managing the root template"
        },
        # Error handling
        {
            "query": "CarPlay connection delegate methods",
            "expected_results": ["CPTemplateApplicationSceneDelegate", "didConnect", "didDisconnect"],
            "context": "Handling CarPlay connection lifecycle"
        },
        {
            "query": "CPListTemplate maximum items limit",
            "expected_results": ["CPListTemplate", "maximum", "500", "items"],
            "context": "Understanding list template limitations"
        }
    ]
    
    results = {
        "test_date": datetime.now().isoformat(),
        "total_queries": len(test_queries),
        "queries": []
    }
    
    print("🚗 CarPlay Search Quality Test\n" + "="*50 + "\n")
    
    for test in test_queries:
        query = test["query"]
        expected = test["expected_results"]
        context = test["context"]
        
        # Search with limit of 10
        search_results = index.search(query, {
            'limit': 10,
            'attributesToRetrieve': ['title', 'api_name', 'framework', 'overview', 'content']
        })
        
        # Analyze results
        query_result = {
            "query": query,
            "context": context,
            "expected_keywords": expected,
            "total_hits": search_results['estimatedTotalHits'],
            "top_results": [],
            "keywords_found": [],
            "relevance_score": 0
        }
        
        print(f"📍 Query: '{query}'")
        print(f"   Context: {context}")
        print(f"   Found: {search_results['estimatedTotalHits']} results")
        
        # Check top 10 results
        for i, hit in enumerate(search_results['hits'], 1):
            title = hit.get('title', 'No title')
            framework = hit.get('framework', 'Unknown')
            content = hit.get('content', '')
            overview = hit.get('overview', '')
            
            # Check for expected keywords
            full_text = f"{title} {content} {overview}".lower()
            found_keywords = [kw for kw in expected if kw.lower() in full_text]
            
            result_info = {
                "position": i,
                "title": title,
                "framework": framework,
                "keywords_matched": found_keywords
            }
            
            query_result["top_results"].append(result_info)
            query_result["keywords_found"].extend(found_keywords)
            
            if i <= 3:  # Show top 3
                print(f"   {i}. {title} ({framework}) - Keywords: {found_keywords}")
        
        # Calculate relevance score
        unique_keywords_found = set(query_result["keywords_found"])
        query_result["keywords_found"] = list(unique_keywords_found)
        query_result["relevance_score"] = len(unique_keywords_found) / len(expected) * 100
        
        print(f"   ✓ Relevance: {query_result['relevance_score']:.0f}% ({len(unique_keywords_found)}/{len(expected)} keywords found)\n")
        
        results["queries"].append(query_result)
    
    # Summary statistics
    avg_relevance = sum(q["relevance_score"] for q in results["queries"]) / len(results["queries"])
    queries_with_results = sum(1 for q in results["queries"] if q["total_hits"] > 0)
    
    results["summary"] = {
        "average_relevance_score": avg_relevance,
        "queries_with_results": queries_with_results,
        "success_rate": queries_with_results / len(test_queries) * 100
    }
    
    print("\n" + "="*50)
    print("📊 Summary:")
    print(f"   Average Relevance: {avg_relevance:.1f}%")
    print(f"   Success Rate: {results['summary']['success_rate']:.1f}%")
    print(f"   Queries with Results: {queries_with_results}/{len(test_queries)}")
    
    # Save results
    with open('carplay_search_quality_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("\n✅ Results saved to carplay_search_quality_results.json")
    
    return results

if __name__ == "__main__":
    test_carplay_searches()