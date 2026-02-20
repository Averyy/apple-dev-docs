# Intra-Framework Concurrency

## Problem

Kernel has ~78K pages and processes them sequentially (one URL at a time).
At ~0.05s rate limit + ~0.1s network latency per request, that's ~3.2 hours for Kernel alone.

## Proposed Fix

Add concurrent URL processing within `_discover_and_scrape_iterative` using a semaphore pattern,
similar to how cross-framework concurrency already works in `scrape_all_frameworks.py`.

## Why It's Safe

- asyncio is single-threaded (cooperative multitasking) — no race conditions
- `hash_manager` is an in-memory dict, saved once at exit
- `processed_urls` set is shared and checked before processing
- Rate limiter already has an asyncio Lock
- Duplicate URLs in the queue are already filtered via `processed_urls`

## Implementation Sketch

```python
# In _discover_and_scrape_iterative:
# Replace sequential loop with worker pool

semaphore = asyncio.Semaphore(10)  # 10 concurrent fetches within a framework
pending_tasks = set()

async def process_url(json_url):
    async with semaphore:
        # existing fetch + process logic
        # discovered child URLs get added back to url_queue
        pass

# Main loop: spawn tasks as URLs are discovered, up to semaphore limit
while url_queue or pending_tasks:
    while url_queue:
        json_url = url_queue.popleft()
        if json_url in self.processed_urls:
            continue
        self.processed_urls.add(json_url)
        task = asyncio.create_task(process_url(json_url))
        pending_tasks.add(task)
        task.add_done_callback(pending_tasks.discard)

    if pending_tasks:
        # Wait for at least one task to complete (may add new URLs to queue)
        done, _ = await asyncio.wait(pending_tasks, return_when=asyncio.FIRST_COMPLETED)
        for t in done:
            pending_tasks.discard(t)
```

## Key Considerations

- Semaphore value should be configurable (default 10, maybe CLI flag `--intra-concurrent`)
- Rate limiter already throttles globally, semaphore just controls how many requests are in-flight
- Progress file writes need to remain atomic
- Test with a small framework first before running on Kernel
- The sorted-by-size optimization means Kernel starts first, so concurrent fetching within it directly reduces total wall time

## Affected Files

- `scraper/json_scraper.py` — `_discover_and_scrape_iterative` method
