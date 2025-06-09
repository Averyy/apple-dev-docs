#!/usr/bin/env python3
"""
Test embedding generation with cost estimation before running
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import openai
import tiktoken

# Load environment variables
env_paths = [
    Path(__file__).parent.parent / "mcp-server" / ".env",
    Path(__file__).parent.parent / ".env"
]

for env_path in env_paths:
    if env_path.exists():
        load_dotenv(env_path)
        break

# Test frameworks with file counts
TEST_FRAMEWORKS = {
    "tiny": [
        ("AdSupport", 5),
        ("AppTrackingTransparency", 10),
        ("AccountDataTransfer", 17)
    ],
    "small": [
        ("PushKit", 49),
        ("ExtensionFoundation", 62),
        ("PassKit", 93)
    ],
    "medium": [
        ("ContactProvider", 103),
        ("UniformTypeIdentifiers", 191),
        ("PencilKit", 275)
    ],
    "large": [
        ("Accessibility", 261),
        ("CloudKit", 915),
        ("Metal", 2965)
    ],
    "xlarge": [
        ("SwiftUI", 5907),
        ("Foundation", 8638),
        ("UIKit", 9263)
    ]
}

def count_tokens(text: str) -> int:
    """Count tokens for text using tiktoken"""
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def estimate_cost(framework: str, file_count: int) -> tuple:
    """Estimate tokens and cost for a framework"""
    docs_path = Path(__file__).parent.parent / "documentation" / framework
    
    if not docs_path.exists():
        return 0, 0.0
    
    # Sample first 10 files to estimate average size
    total_tokens = 0
    sample_count = 0
    
    for md_file in list(docs_path.rglob("*.md"))[:10]:
        try:
            content = md_file.read_text(encoding='utf-8')
            total_tokens += count_tokens(content)
            sample_count += 1
        except:
            pass
    
    if sample_count == 0:
        return 0, 0.0
    
    # Estimate total tokens
    avg_tokens_per_file = total_tokens / sample_count
    estimated_total_tokens = int(avg_tokens_per_file * file_count)
    
    # Calculate cost ($0.02 per 1M tokens)
    cost = (estimated_total_tokens / 1_000_000) * 0.02
    
    return estimated_total_tokens, cost

def test_single_file():
    """Test with a single file first"""
    print("🧪 Testing with single file...\n")
    
    # Configure OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OPENAI_API_KEY not found")
        return False
    
    # Find a test file
    test_file = None
    docs_path = Path(__file__).parent.parent / "documentation"
    
    for framework in ["AdSupport", "PushKit", "ContactProvider"]:
        framework_path = docs_path / framework
        if framework_path.exists():
            files = list(framework_path.rglob("*.md"))
            if files:
                test_file = files[0]
                break
    
    if not test_file:
        print("❌ No test file found")
        return False
    
    # Read content
    content = test_file.read_text(encoding='utf-8')[:1000]  # First 1000 chars
    tokens = count_tokens(content)
    
    print(f"📄 Test file: {test_file.name}")
    print(f"📊 Tokens: {tokens}")
    print(f"💰 Cost: ${(tokens / 1_000_000) * 0.02:.6f}")
    
    # Test embedding
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.embeddings.create(
            input=[content],
            model="text-embedding-3-small"
        )
        
        embedding_dim = len(response.data[0].embedding)
        print(f"✅ Success! Embedding dimension: {embedding_dim}")
        return True
        
    except openai.RateLimitError as e:
        print(f"❌ Rate limit/quota error: {e}")
        print("\n⚠️  Your OpenAI account has exceeded its quota.")
        print("   Please check your OpenAI billing at: https://platform.openai.com/usage")
        print("   You may need to add payment method or upgrade your plan.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def show_estimates():
    """Show cost estimates for different test sizes"""
    print("\n📊 COST ESTIMATES BY FRAMEWORK SIZE\n")
    
    total_cost = 0
    
    for size, frameworks in TEST_FRAMEWORKS.items():
        print(f"\n{size.upper()} Frameworks:")
        print("-" * 50)
        
        size_cost = 0
        for framework, file_count in frameworks:
            tokens, cost = estimate_cost(framework, file_count)
            size_cost += cost
            
            print(f"{framework:30} {file_count:6} files  ~{tokens:10,} tokens  ${cost:7.4f}")
        
        print(f"{'Subtotal':30} {sum(f[1] for f in frameworks):6} files  {'':10} ${size_cost:7.4f}")
        total_cost += size_cost
    
    print("\n" + "=" * 70)
    print(f"TOTAL ALL 259,026 files: ~187M tokens ≈ $3.74")
    print(f"Test samples above: ${total_cost:.4f}")

def interactive_test():
    """Interactive testing with user confirmation"""
    
    # First test single file
    print("=" * 70)
    print("STEP 1: Single File Test")
    print("=" * 70)
    
    if not test_single_file():
        print("\n❌ Single file test failed. Fix issues before proceeding.")
        return
    
    # Show estimates
    print("\n" + "=" * 70)
    print("STEP 2: Framework Size Estimates")
    print("=" * 70)
    show_estimates()
    
    # Recommendations
    print("\n" + "=" * 70)
    print("RECOMMENDED TEST PROGRESSION:")
    print("=" * 70)
    print("\n1. Start with tiny (AdSupport - 5 files) ≈ $0.0001")
    print("2. Then small (PushKit - 49 files) ≈ $0.001")
    print("3. Then medium (ContactProvider - 103 files) ≈ $0.002")
    print("4. Then large (CloudKit - 915 files) ≈ $0.02")
    print("5. Finally full run (259,026 files) ≈ $3.74")
    
    print("\n💡 You can modify scripts/build_index_openai.py to filter by framework")
    print("   Example: if 'AdSupport' not in str(md_file): continue")

if __name__ == "__main__":
    interactive_test()