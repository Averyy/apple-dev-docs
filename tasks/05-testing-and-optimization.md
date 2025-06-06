# Task 5: Essential Testing

## Objective
Verify the MCP server works correctly with Claude Desktop and provides accurate Apple documentation results.

## Essential Testing Only

### 1. Basic Functionality Tests

#### Core Test Scenarios (5 tests)
1. **Basic API Search**: "SwiftUI Button"
2. **Framework Filtering**: "NSPredicate in Foundation" 
3. **Complex Query**: "URLSession async await example"
4. **Full Content Mode**: Search with `include_full_content=true`
5. **Error Handling**: Invalid framework name

#### Success Criteria
- Each query returns relevant results
- Framework filtering works
- Full content mode returns complete docs
- Errors return helpful messages

### 2. MCP Integration Test

#### With Claude Desktop
1. Configure MCP server in Claude config
2. Restart Claude Desktop
3. Ask: "Search Apple docs for SwiftUI Button"
4. Verify: Claude automatically uses the tool
5. Check: Results are properly formatted

### 3. Basic Performance Check

#### Simple Metrics
- Response time < 500ms for searches
- Memory usage stable (no leaks)
- Server starts without errors

#### Quick Load Test
- Run 10 search queries in sequence
- Verify consistent response times
- Check for any errors or crashes

## Simple Deployment Test

### 4. Docker Test (Optional)
If using Docker deployment:
1. Build Docker image
2. Run with test volumes
3. Verify MCP server starts
4. Test search functionality
5. Check persistent data

## Cost Analysis (Updated)

### Actual Usage Costs
```
Initial setup: ~$1-2 (one-time embedding)
Monthly usage: ~$0.01 (100 queries/day)
Quarterly updates: ~$0.10 (ETag-based updates)
Annual total: < $1
```

### Why So Cheap?
1. **No generation costs**: Claude handles all reasoning
2. **One-file-per-embedding**: ~50K embeddings (not 200K)
3. **ETag optimization**: Only re-embed changed docs
4. **Direct retrieval**: No post-processing needed

## Important Links
- [MCP Testing Guide](https://modelcontextprotocol.io/docs/testing)
- [FastMCP Examples](https://github.com/jlowin/fastmcp/tree/main/examples)
- [ChromaDB Testing](https://docs.trychroma.com/deployment)

## Success Criteria
- [ ] Basic test scenarios pass (5 tests)
- [ ] MCP integration with Claude works
- [ ] Response time < 500ms for searches
- [ ] No crashes or memory leaks
- [ ] Docker deployment works (if used)

## Time Estimate
2-3 hours for essential testing (not days!)