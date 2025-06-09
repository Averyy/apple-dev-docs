#!/usr/bin/env python3
"""
ChromaDB utility functions with edge case handling
Based on best practices from Context7 documentation
"""

import re
import json
import logging
from typing import Dict, List, Any, Optional
import hashlib

logger = logging.getLogger(__name__)

# ChromaDB Constants and Limits
COLLECTION_NAME_MIN_LENGTH = 3
COLLECTION_NAME_MAX_LENGTH = 63
MAX_DOCUMENT_SIZE = 5000  # bytes
MAX_METADATA_SIZE = 40000  # bytes  
MAX_BATCH_SIZE = 1000  # Conservative limit for ChromaDB
MAX_ID_LENGTH = 64  # ChromaDB ID length limit

def validate_collection_name(name: str) -> bool:
    """
    Validate ChromaDB collection name according to requirements:
    - 3-63 characters long
    - Start and end with alphanumeric
    - Only contain alphanumeric, underscore, or hyphen
    """
    if len(name) < COLLECTION_NAME_MIN_LENGTH or len(name) > COLLECTION_NAME_MAX_LENGTH:
        return False
    
    # Must match pattern: start with alnum, middle can have alnum/-/_, end with alnum
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9_-]{1,61}[a-zA-Z0-9]$'
    return bool(re.match(pattern, name))

def sanitize_collection_name(name: str) -> str:
    """
    Sanitize a string to be a valid ChromaDB collection name
    """
    # Replace invalid characters with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    
    # Ensure it starts and ends with alphanumeric
    sanitized = re.sub(r'^[^a-zA-Z0-9]+', '', sanitized)
    sanitized = re.sub(r'[^a-zA-Z0-9]+$', '', sanitized)
    
    # Handle length constraints
    if len(sanitized) < COLLECTION_NAME_MIN_LENGTH:
        sanitized = f"col_{sanitized}"
    elif len(sanitized) > COLLECTION_NAME_MAX_LENGTH:
        # Truncate but keep it valid
        sanitized = sanitized[:COLLECTION_NAME_MAX_LENGTH-1]
        sanitized = re.sub(r'[^a-zA-Z0-9]+$', '', sanitized)
        if not sanitized[-1].isalnum():
            sanitized = sanitized[:-1] + '0'
    
    # Final validation
    if not validate_collection_name(sanitized):
        # Fallback to a generic valid name
        sanitized = f"collection_{hashlib.md5(name.encode()).hexdigest()[:8]}"
    
    return sanitized

def validate_document_size(document: str) -> bool:
    """Check if document size is within ChromaDB limits"""
    return len(document.encode('utf-8')) <= MAX_DOCUMENT_SIZE

def truncate_document(document: str, max_size: int = MAX_DOCUMENT_SIZE) -> str:
    """
    Truncate document to fit within size limits while preserving UTF-8 validity
    """
    encoded = document.encode('utf-8')
    if len(encoded) <= max_size:
        return document
    
    # Truncate and ensure valid UTF-8
    truncated = encoded[:max_size].decode('utf-8', errors='ignore')
    
    # Try to truncate at a word boundary
    last_space = truncated.rfind(' ')
    if last_space > max_size * 0.8:  # Only if we're not losing too much
        truncated = truncated[:last_space]
    
    return truncated + "..."

def validate_metadata(metadata: Dict[str, Any]) -> bool:
    """Check if metadata size is within ChromaDB limits"""
    try:
        metadata_str = json.dumps(metadata)
        return len(metadata_str) <= MAX_METADATA_SIZE
    except (TypeError, ValueError):
        return False

def sanitize_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitize metadata to ensure it fits within ChromaDB limits
    """
    # First, ensure all values are JSON serializable
    clean_metadata = {}
    for key, value in metadata.items():
        if isinstance(value, (str, int, float, bool, type(None))):
            clean_metadata[key] = value
        else:
            clean_metadata[key] = str(value)
    
    # Check size
    if validate_metadata(clean_metadata):
        return clean_metadata
    
    # If too large, progressively remove/truncate fields
    # Priority: keep framework, api_name, url; truncate/remove others
    priority_fields = ['framework', 'api_name', 'url']
    
    # First, truncate string values
    for key, value in list(clean_metadata.items()):
        if isinstance(value, str) and len(value) > 200:
            if key in priority_fields:
                clean_metadata[key] = value[:500]
            else:
                clean_metadata[key] = value[:200]
    
    # If still too large, remove non-priority fields
    if not validate_metadata(clean_metadata):
        for key in list(clean_metadata.keys()):
            if key not in priority_fields:
                del clean_metadata[key]
                if validate_metadata(clean_metadata):
                    break
    
    return clean_metadata

def generate_document_id(source: str, chunk_index: int = 0) -> str:
    """
    Generate a unique, consistent document ID
    - Based on content for deduplication
    - Within ChromaDB's ID length limits
    - Consistent across runs
    """
    # Create a unique identifier
    id_source = f"{source}:chunk_{chunk_index}"
    
    # Use SHA-256 for consistency, truncate to fit ID limits
    doc_id = hashlib.sha256(id_source.encode()).hexdigest()
    
    # ChromaDB IDs should be reasonable length
    return doc_id[:min(MAX_ID_LENGTH, 32)]

def chunk_for_chromadb(items: List[Any], max_batch_size: int = MAX_BATCH_SIZE) -> List[List[Any]]:
    """
    Split items into batches that respect ChromaDB's limits
    """
    batches = []
    for i in range(0, len(items), max_batch_size):
        batches.append(items[i:i + max_batch_size])
    return batches

def validate_embeddings(embeddings: List[List[float]], expected_dim: int = 1536) -> bool:
    """
    Validate embeddings before storing in ChromaDB
    - Check dimensions consistency
    - Check for valid floats
    """
    if not embeddings:
        return False
    
    for embedding in embeddings:
        if len(embedding) != expected_dim:
            return False
        if not all(isinstance(x, (int, float)) for x in embedding):
            return False
    
    return True

def handle_chromadb_error(error: Exception, context: str = "") -> Optional[str]:
    """
    Analyze ChromaDB errors and provide actionable advice
    """
    error_str = str(error).lower()
    
    if "database is locked" in error_str:
        return "Database is locked. Another process may be accessing it. Wait and retry."
    
    elif "unique constraint failed" in error_str:
        return "Duplicate ID detected. Use unique IDs or upsert instead of add."
    
    elif "dimension" in error_str or "embedding" in error_str:
        return "Embedding dimension mismatch. Ensure all embeddings have the same dimensions."
    
    elif "collection" in error_str and "not found" in error_str:
        return "Collection not found. Create it first or check the collection name."
    
    elif "metadata" in error_str:
        return "Metadata error. Ensure metadata is JSON-serializable and within size limits."
    
    elif "batch" in error_str or "too large" in error_str:
        return f"Batch too large. Reduce batch size (current limit: {MAX_BATCH_SIZE})."
    
    else:
        return f"ChromaDB error in {context}: {error}"

def create_collection_safely(client, name: str, **kwargs):
    """
    Safely create a ChromaDB collection with validation
    """
    # Validate and sanitize name
    safe_name = sanitize_collection_name(name)
    if safe_name != name:
        logger.warning(f"Collection name sanitized: '{name}' -> '{safe_name}'")
    
    try:
        # Try to get existing collection first
        return client.get_collection(safe_name)
    except:
        # Create new collection
        return client.create_collection(safe_name, **kwargs)

def upsert_documents_safely(collection, documents: List[str], 
                          embeddings: List[List[float]], 
                          metadatas: List[Dict[str, Any]], 
                          ids: List[str]) -> Dict[str, Any]:
    """
    Safely upsert documents with comprehensive validation
    """
    results = {
        'success': 0,
        'failed': 0,
        'errors': []
    }
    
    # Validate inputs
    if not (len(documents) == len(embeddings) == len(metadatas) == len(ids)):
        results['errors'].append("Input lists must have the same length")
        return results
    
    # Process in batches
    batches = chunk_for_chromadb(list(range(len(documents))))
    
    for batch_indices in batches:
        batch_docs = [documents[i] for i in batch_indices]
        batch_embeddings = [embeddings[i] for i in batch_indices]
        batch_metadatas = [metadatas[i] for i in batch_indices]
        batch_ids = [ids[i] for i in batch_indices]
        
        # Validate and sanitize batch
        clean_docs = []
        clean_embeddings = []
        clean_metadatas = []
        clean_ids = []
        
        for i in range(len(batch_docs)):
            # Validate document size
            doc = truncate_document(batch_docs[i])
            
            # Validate metadata
            metadata = sanitize_metadata(batch_metadatas[i])
            
            # Validate ID length
            doc_id = batch_ids[i][:MAX_ID_LENGTH]
            
            clean_docs.append(doc)
            clean_embeddings.append(batch_embeddings[i])
            clean_metadatas.append(metadata)
            clean_ids.append(doc_id)
        
        # Attempt to upsert
        try:
            collection.upsert(
                documents=clean_docs,
                embeddings=clean_embeddings,
                metadatas=clean_metadatas,
                ids=clean_ids
            )
            results['success'] += len(clean_docs)
        except Exception as e:
            results['failed'] += len(clean_docs)
            error_msg = handle_chromadb_error(e, f"batch of {len(clean_docs)} documents")
            results['errors'].append(error_msg)
            logger.error(error_msg)
    
    return results

# Configuration validation for HNSW parameters
def validate_hnsw_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate and sanitize HNSW configuration parameters
    """
    valid_spaces = ['l2', 'ip', 'cosine']
    
    clean_config = {}
    
    # Validate space
    if 'space' in config:
        if config['space'] in valid_spaces:
            clean_config['space'] = config['space']
        else:
            logger.warning(f"Invalid HNSW space '{config['space']}', using 'l2'")
            clean_config['space'] = 'l2'
    
    # Validate numeric parameters
    numeric_params = {
        'ef_construction': (10, 1000, 200),  # min, max, default
        'ef_search': (10, 1000, 100),
        'M': (4, 64, 16),
        'num_threads': (1, 32, 4)
    }
    
    for param, (min_val, max_val, default) in numeric_params.items():
        if param in config:
            val = config[param]
            if isinstance(val, (int, float)) and min_val <= val <= max_val:
                clean_config[param] = int(val)
            else:
                logger.warning(f"Invalid HNSW {param}={val}, using default={default}")
                clean_config[param] = default
    
    return clean_config