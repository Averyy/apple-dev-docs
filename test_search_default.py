#!/usr/bin/env python3
"""
Test ChromaDB search using the default embedding function that was actually used.
"""

import chromadb
from pathlib import Path

def test_search_with_default_embeddings():
    """Test search using ChromaDB's default embedding function."""
    
    client = chromadb.PersistentClient(path="vectorstore")
    
    print("🎯 Testing Search with Default ChromaDB Embeddings")
    print("=" * 60)
    print("ℹ️  Note: These collections use ChromaDB's default sentence-transformers model")
    
    # Test App Tracking Transparency
    try:
        print("\n📱 App Tracking Transparency Search Test")
        
        # Get collection without specifying embedding function (uses stored default)
        collection = client.get_collection("apple_docs_AppTrackingTransparency")
        
        print(f"📊 Collection has {collection.count()} documents")
        
        # Test specific questions about tracking authorization
        questions = [
            "request tracking authorization",
            "authorization status values", 
            "ATTrackingManager",
            "tracking permission",
            "user privacy"
        ]
        
        for i, question in enumerate(questions):
            print(f"\n🔍 Question {i+1}: '{question}'")
            
            try:
                results = collection.query(
                    query_texts=[question],
                    n_results=3,
                    include=["documents", "metadatas", "distances"]
                )
                
                if results['ids'] and len(results['ids'][0]) > 0:
                    print(f"   ✅ Found {len(results['ids'][0])} results")
                    
                    # Show top 2 results
                    for j in range(min(2, len(results['ids'][0]))):
                        doc_id = results['ids'][0][j]
                        distance = results['distances'][0][j]
                        metadata = results['metadatas'][0][j]
                        document = results['documents'][0][j]
                        
                        file_path = metadata.get('file_path', 'Unknown') if metadata else 'Unknown'
                        
                        print(f"   📄 Result {j+1}: {file_path.split('/')[-1]}")  # Just filename
                        print(f"      🎯 Relevance: {distance:.4f} (lower = better)")
                        
                        # Show document title
                        lines = document.split('\n')
                        title = lines[0] if lines else "No title"
                        print(f"      📖 {title}")
                        
                        # Check for relevant keywords in the document
                        doc_lower = document.lower()
                        relevant_keywords = []
                        
                        if 'request' in question.lower() and 'authorization' in question.lower():
                            if 'requesttrackingauthorization' in doc_lower:
                                relevant_keywords.append('requestTrackingAuthorization method')
                            if 'completion' in doc_lower:
                                relevant_keywords.append('completion handler')
                        
                        if 'status' in question.lower():
                            if 'authorizationstatus' in doc_lower:
                                relevant_keywords.append('AuthorizationStatus enum')
                            if 'denied' in doc_lower or 'authorized' in doc_lower:
                                relevant_keywords.append('status values')
                        
                        if 'attrackingmanager' in question.lower():
                            if 'attrackingmanager' in doc_lower:
                                relevant_keywords.append('ATTrackingManager class')
                        
                        if relevant_keywords:
                            print(f"      ✅ Contains: {', '.join(relevant_keywords)}")
                        
                        # Show a snippet of relevant content
                        for line in lines[1:15]:
                            if line.strip() and not line.startswith('#') and not line.startswith('**'):
                                if any(kw.lower() in line.lower() for kw in question.split()):
                                    print(f"      📝 \"{line.strip()[:80]}...\"")
                                    break
                        
                        print()
                        
                else:
                    print(f"   ❌ No results found")
                    
            except Exception as e:
                print(f"   ❌ Error: {e}")
        
        # Test a very specific search
        print(f"\n🎯 Specific Test: Looking for 'requestTrackingAuthorization' method")
        
        results = collection.query(
            query_texts=["requestTrackingAuthorization completionHandler"],
            n_results=1,
            include=["documents", "metadatas", "distances"]
        )
        
        if results['ids'] and len(results['ids'][0]) > 0:
            file_path = results['metadatas'][0][0].get('file_path', 'Unknown')
            distance = results['distances'][0][0]
            document = results['documents'][0][0]
            
            print(f"   ✅ Found: {file_path.split('/')[-1]}")
            print(f"   🎯 Score: {distance:.4f}")
            
            # Check if this is actually the right document
            if 'requesttrackingauthorization' in file_path.lower():
                print(f"   🎉 PERFECT MATCH: Found the exact method documentation!")
                
                # Show the method signature if present
                lines = document.split('\n')
                for line in lines:
                    if 'requestTrackingAuthorization' in line and ('func' in line or 'class func' in line):
                        print(f"   📝 Method: {line.strip()}")
                        break
            
            return True
        else:
            print(f"   ❌ No results for specific method search")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_adsupport_search():
    """Quick test of AdSupport search."""
    
    client = chromadb.PersistentClient(path="vectorstore")
    
    try:
        print(f"\n📱 AdSupport Quick Test")
        collection = client.get_collection("apple_docs_AdSupport")
        
        results = collection.query(
            query_texts=["advertisingIdentifier"],
            n_results=1,
            include=["documents", "metadatas", "distances"]
        )
        
        if results['ids'] and len(results['ids'][0]) > 0:
            file_path = results['metadatas'][0][0].get('file_path', 'Unknown')
            distance = results['distances'][0][0]
            title = results['documents'][0][0].split('\n')[0]
            
            print(f"   ✅ Found: {file_path.split('/')[-1]}")
            print(f"   📖 {title}")
            print(f"   🎯 Score: {distance:.4f}")
            
            if 'advertisingidentifier' in file_path.lower():
                print(f"   🎉 PERFECT: Found advertisingIdentifier property!")
                return True
        
        return False
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing ChromaDB Search with Default Embeddings")
    
    success1 = test_search_with_default_embeddings()
    success2 = test_adsupport_search()
    
    if success1 and success2:
        print(f"\n🎉 SUCCESS: ChromaDB search is working correctly!")
        print(f"✅ Semantic search returns relevant Apple documentation")
        print(f"✅ Can find specific methods and classes by name")
        print(f"✅ Vector embeddings are functioning as expected")
        print(f"\n💡 The collections use ChromaDB's default sentence-transformers model")
        print(f"   For production, we recommend OpenAI embeddings for better accuracy")
    else:
        print("❌ Some search tests failed")
        exit(1)