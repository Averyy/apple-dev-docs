"""
Improved search logic for better multi-term query handling

Key improvements:
1. Better handling of multi-term queries
2. Boost results that contain ALL query terms
3. Consider term proximity and importance
"""

def calculate_multi_term_relevance(query: str, title: str, api_name: str, content: str, file_path: str) -> float:
    """
    Calculate relevance boost for multi-term queries.
    
    This function improves search quality by:
    - Boosting documents that contain ALL query terms
    - Giving higher weight to term proximity
    - Considering term importance (not just presence)
    """
    query_lower = query.lower()
    query_terms = query_lower.split()
    
    if len(query_terms) <= 1:
        return 0.0  # No multi-term boost needed
    
    # Combine all searchable text
    searchable_text = f"{title} {api_name} {file_path} {content}".lower()
    
    # Count how many query terms are present
    terms_found = 0
    term_positions = []
    
    for term in query_terms:
        if term in searchable_text:
            terms_found += 1
            # Find position of first occurrence
            pos = searchable_text.find(term)
            if pos >= 0:
                term_positions.append(pos)
    
    # Calculate boost based on terms found
    if terms_found == 0:
        return 0.0
    
    # Base boost for term coverage
    coverage_ratio = terms_found / len(query_terms)
    boost = 0.0
    
    # Strong boost if ALL terms are found
    if coverage_ratio == 1.0:
        boost = 0.4
        
        # Additional boost for term proximity (terms close together)
        if len(term_positions) > 1:
            term_positions.sort()
            # Calculate average distance between consecutive terms
            distances = [term_positions[i+1] - term_positions[i] for i in range(len(term_positions)-1)]
            avg_distance = sum(distances) / len(distances)
            
            # Boost if terms are close together (within ~50 characters)
            if avg_distance < 50:
                boost += 0.2
            elif avg_distance < 100:
                boost += 0.1
    
    # Partial boost for partial matches
    elif coverage_ratio >= 0.5:
        boost = 0.2 * coverage_ratio
    
    # Extra boost if all terms appear in title or API name
    title_api = f"{title} {api_name}".lower()
    if all(term in title_api for term in query_terms):
        boost += 0.3
    
    return min(boost, 0.8)  # Cap at 0.8 to not overshadow vector similarity


def improve_query_embedding_strategy(query: str) -> list[str]:
    """
    Generate multiple embedding strategies for better multi-term search.
    
    Instead of just embedding the full query, we can:
    1. Embed the full query
    2. Embed important term combinations
    3. Use weighted embeddings
    """
    query_terms = query.split()
    
    strategies = [query]  # Always include full query
    
    # For multi-term queries, add strategic combinations
    if len(query_terms) >= 2:
        # For queries like "NavigationView navigationBarTitle"
        # Also search for most specific term (usually the last one)
        if len(query_terms) == 2:
            strategies.append(query_terms[1])  # navigationBarTitle
        
        # For longer queries, focus on noun phrases
        # This is a simple heuristic - could be improved with NLP
        if len(query_terms) >= 3:
            # Try last two terms as they're often the most specific
            strategies.append(" ".join(query_terms[-2:]))
    
    return strategies


# Example integration into existing search method:
"""
# In the search method, after getting base results:

# Calculate multi-term relevance boost
multi_term_boost = calculate_multi_term_relevance(
    query=original_query,
    title=metadatas[i].get("title", ""),
    api_name=metadatas[i].get("api_name", ""),
    content=documents[i][:500],  # First 500 chars
    file_path=metadatas[i].get("file_path", "")
)

# Add to existing relevance calculation
base_relevance = 1 - (distances[i] if distances[i] else 0)
total_relevance = base_relevance + boost + multi_term_boost

# This ensures documents with ALL query terms rank higher
"""