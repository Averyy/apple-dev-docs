# Apple Docs MCP Server - Project Overview

## Project Goal
Build a simple, fast, and accurate local MCP (Model Context Protocol) server that enables LLMs to search and answer questions about Apple's developer documentation.

## Architecture Summary
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Claude/LLM     │────▶│   MCP Server    │────▶│   RAG Engine    │
│                 │◀────│                 │◀────│                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                          │
                                                          ▼
                                                 ┌─────────────────┐
                                                 │  Vector Store   │
                                                 │   (ChromaDB)    │
                                                 └─────────────────┘
```

## Key Technologies
- **MCP SDK**: For LLM integration
- **ChromaDB**: Local vector database
- **OpenAI**: Embeddings only (text-embedding-3-small)
- **Python 3.11+**: Async support
- **No LangChain**: Direct API calls for simplicity
- **No GPT-4**: Claude handles all reasoning

## Task Breakdown (Updated)
1. **Environment Setup** (15-20 min)
2. **Build Vector Index** (1-2 hours + 1 hour indexing)
3. **Implement RAG Engine** (2-3 hours)
4. **Create MCP Server** (3-4 hours)
5. **Essential Testing** (2-3 hours)

**Total Timeline**: ~1.5 days of development (much faster!)

## Cost Analysis (Actual Numbers)

### One-Time Costs
- **Initial Indexing**: ~$1-2 for embedding ~45K documents

### Ongoing Costs (Monthly)
- **Light Usage** (50 queries/day): ~$0.003/month
- **Moderate Usage** (100 queries/day): ~$0.006/month
- **Heavy Usage** (500 queries/day): ~$0.03/month

### Cost Breakdown per Query
- **All queries**: ~$0.00002 (embedding only)
- **No generation costs**: Claude handles reasoning
- **6,600x cheaper** than GPT-4 approach!

## Embedding Model Comparison

### OpenAI text-embedding-3-small
- **Dimensions**: 1536
- **Cost**: $0.02 per 1M tokens
- **Pros**: 
  - Excellent LangChain integration
  - High quality for technical content
  - Good multilingual support
- **Cons**: Higher dimensionality = more storage

### Voyage-3
- **Dimensions**: 1024
- **Cost**: $0.02 per 1M tokens
- **Pros**:
  - Smaller vectors (33% less storage)
  - Specialized for retrieval
  - Good performance
- **Cons**: Less ecosystem support

**Recommendation**: OpenAI text-embedding-3-small for better tooling support and marginal quality improvement.

## Why No GPT-4?

Since Claude is already an LLM that will be using this MCP server:

1. **Redundant Processing**: Claude can handle all reasoning and formatting
2. **Cost Efficiency**: 6,600x cheaper to just return search results
3. **Simpler Architecture**: No need for prompt engineering or chaining
4. **Faster Responses**: Direct retrieval without generation step
5. **Better Context**: Claude sees all retrieved chunks, not a summary

### The Simple Flow
1. Claude asks MCP server to search for something
2. MCP embeds query and searches vector DB
3. MCP returns raw chunks with metadata
4. Claude processes and presents the information

No additional LLM needed!

## Key Design Decisions

1. **No LangChain**: Direct API calls are simpler and clearer
2. **No GPT-4**: Claude handles all reasoning and formatting
3. **No Caching**: Fast enough without it (< 500ms)
4. **Simple Chunking**: Basic markdown-aware splitting
5. **Local Vector DB**: ChromaDB for simplicity and portability
6. **MCP Tools Only**: Just search functionality exposed

## Success Metrics
- **Speed**: <500ms response time
- **Accuracy**: >90% relevant results in top 5
- **Cost**: <$0.01/month for typical developer usage
- **Simplicity**: <500 lines of code total
- **Reliability**: 99.9% uptime for local server

## Next Steps
1. Review all task files (01-05)
2. Set up development environment
3. Start with Task 1: Environment Setup
4. Iterate and improve based on testing

## Notes
- All processing is local (vector DB, MCP server)
- Only external calls are to OpenAI for embeddings/generation
- No Apple documentation is sent to third parties (only your queries)
- System is designed to be extended with more RAG techniques as needed