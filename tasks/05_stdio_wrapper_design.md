# Stdio Wrapper Design for Meilisearch MCP

## Overview

The stdio wrapper enables Claude Code to communicate with a Meilisearch instance deployed on a separate networked computer (192.168.2.5) through the meilisearch-mcp server. It acts as a bridge between Claude's stdio-based MCP protocol and the HTTP-based Meilisearch API.

## Architecture

```
Claude Code <--> stdio <--> Wrapper <--> meilisearch-mcp <--> HTTP <--> Meilisearch@192.168.2.5
```

## Components

### 1. Stdio Wrapper (`meilisearch_stdio_wrapper.py`)

```python
import asyncio
import json
import sys
import os
import subprocess
from typing import Optional
import logging

class MeilisearchStdioWrapper:
    def __init__(self, meilisearch_url: str, api_key: Optional[str] = None):
        self.meilisearch_url = meilisearch_url
        self.api_key = api_key
        self.process = None
        
    async def start(self):
        """Launch meilisearch-mcp server as subprocess"""
        env = os.environ.copy()
        env['MEILISEARCH_URL'] = self.meilisearch_url
        if self.api_key:
            env['MEILISEARCH_API_KEY'] = self.api_key
            
        # Launch meilisearch-mcp server
        self.process = await asyncio.create_subprocess_exec(
            sys.executable, '-m', 'meilisearch_mcp',
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env
        )
        
    async def forward_stdio(self):
        """Forward messages between Claude and meilisearch-mcp"""
        tasks = [
            self._forward_input(),
            self._forward_output(),
            self._forward_errors()
        ]
        await asyncio.gather(*tasks)
        
    async def _forward_input(self):
        """Forward stdin to subprocess"""
        reader = asyncio.StreamReader()
        protocol = asyncio.StreamReaderProtocol(reader)
        await asyncio.get_running_loop().connect_read_pipe(
            lambda: protocol, sys.stdin
        )
        
        while True:
            line = await reader.readline()
            if not line:
                break
            self.process.stdin.write(line)
            await self.process.stdin.drain()
            
    async def _forward_output(self):
        """Forward subprocess stdout to stdout"""
        async for line in self.process.stdout:
            sys.stdout.buffer.write(line)
            sys.stdout.buffer.flush()
            
    async def _forward_errors(self):
        """Log subprocess stderr"""
        async for line in self.process.stderr:
            logging.error(f"meilisearch-mcp: {line.decode().strip()}")
```

### 2. Configuration

The wrapper reads configuration from environment variables:

```bash
# Required
MEILISEARCH_URL=http://192.168.2.5:7700

# Optional (for production)
MEILISEARCH_API_KEY=your-master-key

# Optional (for debugging)
MEILISEARCH_WRAPPER_LOG_LEVEL=INFO
```

### 3. Error Handling

The wrapper implements robust error handling:

1. **Connection Errors**: Retry with exponential backoff
2. **Authentication Errors**: Clear error messages
3. **Process Crashes**: Automatic restart with limits
4. **Network Timeouts**: Configurable timeouts
5. **Invalid Messages**: Graceful degradation

### 4. Health Checks

Built-in health monitoring:

```python
async def health_check(self):
    """Verify Meilisearch connectivity"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.meilisearch_url}/health",
                headers={'Authorization': f'Bearer {self.api_key}'}
            ) as response:
                return response.status == 200
    except Exception as e:
        logging.error(f"Health check failed: {e}")
        return False
```

## MCP Server Configuration

### Claude Desktop Config

```json
{
  "mcpServers": {
    "apple-docs-meilisearch": {
      "command": "python",
      "args": [
        "/path/to/meilisearch_stdio_wrapper.py"
      ],
      "env": {
        "MEILISEARCH_URL": "http://192.168.2.5:7700",
        "MEILISEARCH_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Wrapper Entry Point

```python
# meilisearch_stdio_wrapper.py
async def main():
    # Setup logging
    logging.basicConfig(
        level=os.getenv('MEILISEARCH_WRAPPER_LOG_LEVEL', 'WARNING'),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='/tmp/meilisearch_wrapper.log'
    )
    
    # Get configuration
    url = os.getenv('MEILISEARCH_URL')
    if not url:
        print(json.dumps({
            "error": "MEILISEARCH_URL environment variable required"
        }), file=sys.stderr)
        sys.exit(1)
    
    api_key = os.getenv('MEILISEARCH_API_KEY')
    
    # Create and start wrapper
    wrapper = MeilisearchStdioWrapper(url, api_key)
    
    # Health check
    if not await wrapper.health_check():
        print(json.dumps({
            "error": "Cannot connect to Meilisearch"
        }), file=sys.stderr)
        sys.exit(1)
    
    await wrapper.start()
    await wrapper.forward_stdio()

if __name__ == "__main__":
    asyncio.run(main())
```

## Security Considerations

1. **API Key Management**
   - Never log API keys
   - Use environment variables only
   - Implement key rotation support

2. **Network Security**
   - Support HTTPS connections
   - Validate SSL certificates
   - Implement request timeouts

3. **Process Isolation**
   - Run with minimal privileges
   - Sanitize all inputs
   - Limit resource usage

## Monitoring and Debugging

1. **Logging**
   - Structured JSON logs
   - Configurable log levels
   - Separate error streams

2. **Metrics**
   - Request latency
   - Error rates
   - Connection status

3. **Debug Mode**
   ```bash
   MEILISEARCH_WRAPPER_DEBUG=1 python meilisearch_stdio_wrapper.py
   ```

## Testing Strategy

1. **Unit Tests**
   - Mock stdio streams
   - Test error handling
   - Verify message forwarding

2. **Integration Tests**
   - Test with real Meilisearch
   - Verify MCP protocol compliance
   - Test network failures

3. **Performance Tests**
   - Measure latency overhead
   - Test concurrent requests
   - Stress test error paths

## Deployment Checklist

- [ ] Install Python dependencies
- [ ] Configure environment variables
- [ ] Test Meilisearch connectivity
- [ ] Verify MCP server installation
- [ ] Configure Claude Desktop
- [ ] Test search functionality
- [ ] Monitor logs for errors
- [ ] Document troubleshooting steps

## Troubleshooting Guide

### Common Issues

1. **"Cannot connect to Meilisearch"**
   - Check MEILISEARCH_URL is correct
   - Verify network connectivity
   - Check firewall rules

2. **"Authentication failed"**
   - Verify MEILISEARCH_API_KEY
   - Check Meilisearch master key
   - Ensure key has correct permissions

3. **"Subprocess crashed"**
   - Check meilisearch-mcp installation
   - Review stderr logs
   - Verify Python environment

4. **"Timeout errors"**
   - Check network latency
   - Increase timeout values
   - Verify Meilisearch performance

## Future Enhancements

1. **Connection Pooling**: Reuse HTTP connections
2. **Response Caching**: Cache frequent searches
3. **Batch Operations**: Group multiple requests
4. **Compression**: Compress large responses
5. **Metrics Export**: Prometheus/OpenTelemetry support