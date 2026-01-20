# Speed Up Indexing - Safe Options

Current status: batch_size=10000, ~37 min for 335K docs locally (with Rosetta overhead)

---

## Local Test Results

See CLAUDE.md for how to run local tests.

| Batch Size | Total Time | Peak Memory | Rate |
|------------|------------|-------------|------|
| 500 | 1h 38min | 1.77GB | ~3,400 docs/min |
| 10,000 | **37 min** | 1.68GB | ~9,000 docs/min |

**batch_size=10000 is 2.6x faster** and uses slightly less peak memory (fewer merge cycles).

### Why Indexing Slows Down as it Progresses

Observed: Production with batch_size=25 slowed significantly after 80%+

**Root causes:**

1. **Index segment merging** - As the index grows, Meilisearch merges smaller segments into larger ones. These merge operations get more expensive with more data.

2. **Memory pressure** - When RAM usage hits 90%+, Meilisearch does more disk I/O instead of keeping things in memory.

3. **Massive Block I/O** - Production showed ~2TB of disk I/O for 335K docs. As the index grows, each batch triggers more compaction/rewriting.

4. **Small batch size compounds it** - With 13,400 batches (batch_size=25), each triggering its own merge cycle, you get way more I/O churn than larger batches that can merge more efficiently.

**Why larger batches help:**
- Fewer merge cycles (670 batches at 500 vs 13,400 at 25)
- More efficient bulk operations
- Less I/O overhead per document

---

## Top 3 Safe Options

### 1. Increase Batch Size to 10,000+ (Easiest, Highest Impact)

**Current:** 500 docs/batch → 670 batches
**Proposed:** 10,000 docs/batch → 34 batches

Official Meilisearch docs recommend 10K-50K per batch:
> A single large HTTP payload is processed more quickly than multiple smaller payloads.

**Why it's safe:**
- We already wait for each batch to complete (`wait_for_task`)
- Memory spike is transient and released after batch completes
- Can always reduce if OOM occurs

**Implementation:**
```python
# index_to_meilisearch.py line 46
batch_size: int = 10000,  # was 500
```

**Expected improvement:** ~50 min → ~20-30 min

---

### 2. Upgrade Meilisearch from v1.9 to v1.12+ (Medium Effort, Very High Impact)

The new indexer in v1.12 is fundamentally faster:
- **2x faster** for new documents
- **4x faster** for incremental updates
- **30% smaller** database size
- Better parallelism with pipelined writes

**Why it's safe:**
- Official stable release
- Same API, drop-in replacement
- Can test locally first

**Implementation:**
```dockerfile
# Dockerfile - change download URL
wget -qO /usr/bin/meilisearch https://github.com/meilisearch/meilisearch/releases/download/v1.12.0/meilisearch-linux-amd64
```

**Expected improvement:** 2-4x faster indexing

---

### 3. Configure Meilisearch Threading/Memory (Low Effort, Medium Impact)

Allow Meilisearch to use more resources during indexing:

```yaml
# docker-compose.yml or startup environment
environment:
  - MEILI_MAX_INDEXING_THREADS=3      # Use 3 of 4 cores for indexing
  - MEILI_MAX_INDEXING_MEMORY=3Gb     # Allow 3GB for indexing operations
```

**Why it's safe:**
- Official configuration options
- Only affects indexing, not search
- Can tune based on VPS capacity

**Current defaults:**
- Threads: half of available cores (2 on 4-core VPS)
- Memory: 2/3 of available RAM

**Expected improvement:** 20-40% faster

---

## Comparison Summary

| Option | Effort | Risk | Impact | Dependencies |
|--------|--------|------|--------|--------------|
| Batch 10K+ | 1 line change | Low | High | None |
| Meilisearch v1.12 | Update Dockerfile | Low-Med | Very High | Test first |
| Threading/Memory | Add env vars | Low | Medium | None |

## Recommended Order

1. **Now:** Already at 500, let it finish and verify stability
2. **Next deploy:** Bump to 10K batch size
3. **After that:** Upgrade to Meilisearch v1.12
4. **Fine-tuning:** Add threading/memory config

## Not Recommended (Higher Risk)

- **Fire-and-forget batches** (remove wait_for_task) - can OOM
- **Parallel batch submission** - adds complexity, marginal gain with large batches
- **Disable features** (facet search, etc.) - might need them later

## References

- [Meilisearch Indexing Best Practices](https://www.meilisearch.com/docs/learn/indexing/indexing_best_practices)
- [New Indexer in v1.12](https://www.meilisearch.com/blog/introducing-indexer-2024)
- [RAM and Multi-threading Impact](https://www.meilisearch.com/docs/learn/indexing/ram_multithreading_performance)
