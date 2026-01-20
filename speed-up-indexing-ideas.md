# Speed Up Indexing - Safe Options

Current status: Meilisearch v1.33.0, batch_size=10000

---

## Local Test Results (v1.9 - Old Indexer)

These results are from Meilisearch v1.9 with the **old indexer**:

| Batch Size | Total Time | Peak Memory | Rate |
|------------|------------|-------------|------|
| 500 | 1h 38min | 1.77GB | ~3,400 docs/min |
| 10,000 | **37 min** | 1.68GB | ~9,000 docs/min |

**batch_size=10000 is 2.6x faster** and uses slightly less peak memory (fewer merge cycles).

---

## v1.32 Upgrade Findings (New Indexer)

**IMPORTANT:** Meilisearch v1.12+ uses a completely rewritten indexer ("Indexer 2024 Edition") with different memory characteristics.

### What Changed

| Aspect | Old Indexer (v1.9) | New Indexer (v1.12+) |
|--------|-------------------|---------------------|
| Memory model | Chunked processing, heavy disk I/O | Bumpalo arena allocators, holds data in RAM |
| Batch handling | Each batch independent | Extraction phase holds data until merger completes |
| `--max-indexing-memory` | Mostly respected | Only controls 5% of memory (arena); LMDB unrestricted |

### OOM Tests with 2GB Container

| Version | Batch Size | Experimental Flag | OOM at Docs | % of 335K | Rate |
|---------|------------|-------------------|-------------|-----------|------|
| v1.32.2 | 10,000 | No | 110,000 | 33% | ~9,500/min |
| v1.33.0 | 5,000 | No | 185,000 | 55% | ~9,500/min |
| v1.33.0 | 10,000 | **Yes** | 280,000 | 83% | ~9,500/min |
| v1.33.0 | 5,000 | **Yes** | Aborted | — | ~8K/min |
| v1.33.0 | 10,000 | **Yes** + 3GB | ✅ **335,304** | **100%** | ~6,500/min |

#### Test 1: v1.32.2 + batch_size=10000

- **Date:** 2026-01-20
- **Memory limit:** 2GB (docker-compose.local.yml)
- **Result:** OOM kill (SIGKILL) at ~110K docs (33% of 335K)
- **Memory behavior:** Peaked at ~1.9GB before crash
- **Observation:** Supervisor restarted Meilisearch, but indexing script failed

#### Test 2: v1.33.0 + batch_size=5000

- **Date:** 2026-01-20
- **Memory limit:** 2GB (docker-compose.local.yml)
- **Result:** OOM kill (SIGKILL) at ~185K docs (55% of 335K)
- **Memory behavior:** Fluctuated between 1.0-1.9GB, stable until crash
- **Rate:** Consistent ~9,500 docs/min throughout
- **Observation:** Reducing batch size helped (got 68% further) but still insufficient

**Root cause:** LMDB memory consumption is NOT restricted by `--max-indexing-memory` ([GitHub Issue #4764](https://github.com/meilisearch/meilisearch/issues/4764) - still open). The new indexer does larger bulk writes which cause bigger LMDB memory spikes.

From the Meilisearch team's own testing with 2GB limit set:
- 8GB wiki full indexing: spike at **5.37GB**
- 1GB songs full indexing: spike at **5.00GB**

#### Test 3: v1.33.0 + batch_size=10000 + experimental flag

- **Date:** 2026-01-20
- **Memory limit:** 2GB (docker-compose.local.yml)
- **Result:** OOM kill (SIGKILL) at ~280K docs (83% of 335K)
- **Memory behavior:** Fluctuated between 1.6-1.95GB, stable until crash
- **Rate:** Started ~11K/min, slowed to ~9.2K/min as index grew
- **Duration:** ~31 minutes before crash
- **Observation:** Experimental flag helped significantly (2.5x further than Test 1, 1.5x further than Test 2), but still insufficient for 335K docs in 2GB

#### Test 4: v1.33.0 + batch_size=5000 + experimental flag (Aborted)

- **Date:** 2026-01-20
- **Memory limit:** 2GB (docker-compose.local.yml)
- **Result:** Aborted at ~80K docs to try larger batches
- **Memory behavior:** **Higher than Test 3 at same doc counts!**
  - At 70K: Test 3 used 1.14-1.69 GiB, Test 4 used 1.93 GiB
- **Rate:** ~8K/min (slower than 10K batches)
- **Observation:** Smaller batches = more merge cycles = higher cumulative memory. Counterintuitive but confirmed.

#### Test 5: v1.33.0 + batch_size=30000 + experimental flag (Abandoned)

- **Date:** 2026-01-20
- **Memory limit:** 2GB (docker-compose.local.yml)
- **Result:** Abandoned - 30K batches too slow (~5.5K/min) and timeouts needed adjustment
- **Observation:** Larger batches don't improve speed; 10K is the sweet spot

#### Test 6: v1.33.0 + batch_size=10000 + experimental flag + 3GB ✅ SUCCESS

- **Date:** 2026-01-20
- **Memory limit:** 3GB (docker-compose.local.yml)
- **Result:** ✅ **COMPLETE** - 335,304 docs indexed successfully
- **Total time:** 51 min 46 sec
- **Memory behavior:** Cycled between 1.5-2.8GiB, never OOM'd
- **Rate:** Started ~10K/min, stabilized at ~6.5K/min
- **Observation:** The extra 1GB of headroom was the key. Experimental flag enables memory release cycles that prevent accumulation.

**This is the winning configuration for local testing that mirrors production constraints.**

### Solutions

1. **Experimental flag** - `MEILI_EXPERIMENTAL_REDUCE_INDEXING_MEMORY_USAGE=true` (enables MDB_WRITEMAP, may slow writes)
2. **Larger batch sizes** - Fewer merges may reduce cumulative memory (testing 30K)
3. **Increase container memory to 4GB** - Match production

**Current test:** experimental flag + batch_size=30000

### TODO: Review Items

- **Health check "indexing" detection window (90s)** - Currently checks if last indexing task finished within 90 seconds. Based on observed batch gaps of 33-71s. May need tuning if batch sizes or hardware change.

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

### 2. Upgrade Meilisearch from v1.9 to v1.32 (DONE - Medium Effort, High Impact)

**Status:** ✅ Upgraded to v1.33.0

The new indexer in v1.12+ is fundamentally faster:
- **2x faster** for new documents
- **4x faster** for incremental updates
- **30% smaller** database size
- Better parallelism with pipelined writes

**Caveats discovered:**
- ⚠️ Higher memory usage due to new indexer architecture
- ⚠️ `--max-indexing-memory` doesn't restrict LMDB ([Issue #4764](https://github.com/meilisearch/meilisearch/issues/4764))
- ⚠️ May need to reduce batch size or increase container memory

**Implementation:**
```dockerfile
# Dockerfile - updated to v1.33.0
wget -qO /usr/bin/meilisearch https://github.com/meilisearch/meilisearch/releases/download/v1.33.0/meilisearch-linux-amd64
```

**Expected improvement:** 2-4x faster indexing (once memory tuned)

---

## Comparison Summary

| Option | Effort | Risk | Impact | Dependencies |
|--------|--------|------|--------|--------------|
| Batch 10K+ | 1 line change | Low | High | None |
| Meilisearch v1.12+ | Update Dockerfile | Low-Med | Very High | Test first |
| Experimental flag | Add env var | Low | High | v1.12+ |

## Current Configuration (VERIFIED WORKING)

Based on testing (2026-01-20):

1. ✅ Meilisearch v1.33.0
2. ✅ `MEILI_EXPERIMENTAL_REDUCE_INDEXING_MEMORY_USAGE=true`
3. ✅ batch_size=10000 (optimal speed)
4. ✅ Memory: 3GB minimum (production has 4GB)
5. ✅ **Full index: 335,304 docs in 52 minutes**

## Not Recommended (Higher Risk)

- **Fire-and-forget batches** (remove wait_for_task) - can OOM
- **Parallel batch submission** - adds complexity, marginal gain with large batches
- **Disable features** (facet search, etc.) - might need them later

## References

- [Meilisearch Indexing Best Practices](https://www.meilisearch.com/docs/learn/indexing/indexing_best_practices)
- [New Indexer in v1.12](https://www.meilisearch.com/blog/introducing-indexer-2024)
- [RAM and Multi-threading Impact](https://www.meilisearch.com/docs/learn/indexing/ram_multithreading_performance)
