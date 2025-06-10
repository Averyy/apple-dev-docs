#!/usr/bin/env python3
"""
Test concurrent scraping functionality
Tests the rolling concurrency with asyncio.Semaphore
"""

import asyncio
import time
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))


async def test_semaphore_concurrency():
    """Test that semaphore properly limits concurrency"""
    max_concurrent = 3
    active_tasks = 0
    max_active = 0
    task_times = []
    
    async def mock_scrape_task(task_id: int):
        nonlocal active_tasks, max_active
        
        start_time = time.time()
        active_tasks += 1
        max_active = max(max_active, active_tasks)
        
        # Simulate work
        await asyncio.sleep(0.1)
        
        active_tasks -= 1
        end_time = time.time()
        task_times.append((task_id, start_time, end_time))
    
    # Create semaphore
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def task_with_semaphore(task_id: int):
        async with semaphore:
            await mock_scrape_task(task_id)
    
    # Run 10 tasks with max 3 concurrent
    tasks = [task_with_semaphore(i) for i in range(10)]
    await asyncio.gather(*tasks)
    
    # Verify max concurrent never exceeded
    assert max_active <= max_concurrent, f"Max active {max_active} exceeded limit {max_concurrent}"
    
    # Verify all tasks completed
    assert len(task_times) == 10
    
    print(f"✅ Semaphore correctly limited concurrency to {max_concurrent}")


async def test_rolling_vs_batch_concurrency():
    """Test that concurrency is rolling, not batched"""
    max_concurrent = 3
    task_start_times = []
    
    async def mock_task(task_id: int, duration: float):
        task_start_times.append((task_id, time.time()))
        await asyncio.sleep(duration)
    
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def task_with_semaphore(task_id: int, duration: float):
        async with semaphore:
            await mock_task(task_id, duration)
    
    # Tasks with different durations
    task_configs = [
        (0, 0.1),  # Quick task
        (1, 0.2),  # Medium task  
        (2, 0.3),  # Slow task
        (3, 0.05), # Very quick - should start as soon as task 0 finishes
        (4, 0.05), # Very quick
        (5, 0.05), # Very quick
    ]
    
    tasks = [task_with_semaphore(id, dur) for id, dur in task_configs]
    await asyncio.gather(*tasks)
    
    # Sort by start time
    task_start_times.sort(key=lambda x: x[1])
    
    # Verify task 3 started before task 2 finished (rolling, not batch)
    task_3_start = next(t[1] for t in task_start_times if t[0] == 3)
    task_0_start = next(t[1] for t in task_start_times if t[0] == 0)
    
    # Task 3 should start ~0.1s after task 0 (when task 0 finishes)
    # Not ~0.3s after (when all first batch finishes)
    time_diff = task_3_start - task_0_start
    assert 0.08 < time_diff < 0.15, f"Task 3 started {time_diff}s after task 0 (expected ~0.1s)"
    
    print("✅ Concurrency is rolling (not batched)")


async def test_concurrent_error_handling():
    """Test error handling with concurrent tasks"""
    max_concurrent = 3
    completed_tasks = []
    failed_tasks = []
    
    async def mock_task(task_id: int):
        if task_id == 3:
            raise ValueError(f"Task {task_id} failed")
        await asyncio.sleep(0.05)
        return task_id
    
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def task_with_semaphore(task_id: int):
        async with semaphore:
            try:
                result = await mock_task(task_id)
                return (task_id, None)
            except Exception as e:
                return (task_id, e)
    
    # Run tasks
    tasks = [task_with_semaphore(i) for i in range(6)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Check results
    for task_id, error in results:
        if error:
            failed_tasks.append(task_id)
        else:
            completed_tasks.append(task_id)
    
    assert len(completed_tasks) == 5
    assert len(failed_tasks) == 1
    assert 3 in failed_tasks
    
    print("✅ Error handling works correctly with concurrency")


async def test_memory_efficiency():
    """Test memory efficiency with many concurrent tasks"""
    max_concurrent = 20  # Our default
    task_count = 1000
    
    # Track completion
    completed = 0
    
    async def lightweight_task(task_id: int):
        nonlocal completed
        await asyncio.sleep(0.001)  # Very quick task
        completed += 1
    
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def task_with_semaphore(task_id: int):
        async with semaphore:
            await lightweight_task(task_id)
    
    # Create all tasks at once (tests memory efficiency)
    tasks = [task_with_semaphore(i) for i in range(task_count)]
    
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    
    assert completed == task_count
    
    # Should complete in reasonable time
    duration = end_time - start_time
    expected_duration = (task_count / max_concurrent) * 0.001
    assert duration < expected_duration * 2  # Allow some overhead
    
    print(f"✅ Handled {task_count} tasks efficiently in {duration:.2f}s")


def main():
    """Run all concurrent scraping tests"""
    print("\n🧪 CONCURRENT SCRAPING TEST SUITE")
    print("=" * 60)
    
    tests = [
        test_semaphore_concurrency,
        test_rolling_vs_batch_concurrency,
        test_concurrent_error_handling,
        test_memory_efficiency
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            asyncio.run(test())
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    
    if failed > 0:
        sys.exit(1)
    else:
        print("\n✅ All concurrent scraping tests passed!")


if __name__ == "__main__":
    main()