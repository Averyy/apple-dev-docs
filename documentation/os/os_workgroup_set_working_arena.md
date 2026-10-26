# os_workgroup_set_working_arena

**Framework**: os  
**Kind**: func  
**Role**: Function

Distributes a block of managed memory to the threads of a workgroup.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern int os_workgroup_set_working_arena(os_workgroup_t wg, void *arena, uint32_t max_workers, os_workgroup_working_arena_destructor_t destructor);
```

#### Return Value

`0` on success or an error code if the function encountered a problem. For example, the function returns `ENOMEM` if it is unable to allocate the memory it needs to manage the arena data.

#### Discussion

Use this function to distribute a block of memory that you created to the threads of the workgroup. Configure the block of memory with the work that you want to those threads to perform. Call this function before you start an interval or parallel workgroup, and before you join any threads to the workgroup.

After assigning the arena data to the workgroup, join your threads and start your task. In each thread, call the [`os_workgroup_get_working_arena`](./os_workgroup_get_working_arena.md) function to retrieve the shared `arena` data, and optionally the thread’s unique index into that data. Unique indexes allow you to divide the `arena` data evenly among your threads. Each thread uses its index to access the appropriate portion of the data.

If you call this function more than once, each subsequent call uses the `destructor` function to clean up the previous arena data.

## Parameters

- `wg`: The workgroup in which to store the shared data. The workgroup must not have any joined threads, and the workgroup must be idle.
- `arena`: A pointer to the data you want to distribute among the workgroup’s threads. Specify `NULL` to remove any shared data from a workgroup.
- `max_workers`: The maximum number of threads that may request a unique index from the workgroup. If your threads share all of the data, rather than operate on only part of that data, specify `0` for this parameter.
- `destructor`: A function to deallocate the memory in the `arena` parameter.

## See Also

### Workgroup Configuration
- [os_workgroup_max_parallel_threads](./os_workgroup_max_parallel_threads.md)
  Returns the maximum number of threads that the system recommends you add to the specified workgroup.
- [os_workgroup_mpt_attr_t](./os_workgroup_mpt_attr_t.md)
  An opaque structure containing attributes related to a request for the maximum number of parallel threads.
- [os_workgroup_get_working_arena](./os_workgroup_get_working_arena.md)
  Retrieves the workgroup’s shared data, and the thread-specific index into that data.
- [os_workgroup_index](./os_workgroup_index.md)
  A unique index that the workgroup assigns to its joined threads.
- [os_workgroup_working_arena_destructor_t](./os_workgroup_working_arena_destructor_t.md)
  A function that deallocates a workgroup’s currently assigned shared memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_set_working_arena)*