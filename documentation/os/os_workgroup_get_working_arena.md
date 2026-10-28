# os_workgroup_get_working_arena

**Framework**: os  
**Kind**: func  
**Role**: Function

Retrieves the workgroup’s shared data, and the thread-specific index into that data.

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
extern void *os_workgroup_get_working_arena(os_workgroup_t wg, os_workgroup_index *index_out);
```

## Return Value

A pointer to the workgroup’s shared data, or `NULL` if the workgroup has no shared data.

## Discussion

Use this function to retrieve the workgroup’s shared data. The first time you call this function on a thread and request an index, the workgroup assigns an index to the thread and returns it. On subsequent calls from the same thread, the workgroup returns the same index value.

When you call the [`os_workgroup_set_working_arena`](./os_workgroup_set_working_arena.md) function, you specify the maximum number of unique threads that may request an index from the workgroup. If you exceed that maximum, this function crashes your app.

## Parameters

- `wg`: The workgroup that contains the context data. If the current thread isn’t a member of this workgroup, this function crashes the app.
- `index_out`: A pointer to an index variable. On output, this parameter contains the index of the thread in the specified workgroup. Specify `NULL` if you don’t want the function to assign a unique index to this thread.

## See Also

### Workgroup Configuration
- [os_workgroup_max_parallel_threads](./os_workgroup_max_parallel_threads.md)
  Returns the maximum number of threads that the system recommends you add to the specified workgroup.
- [os_workgroup_mpt_attr_t](./os_workgroup_mpt_attr_t.md)
  An opaque structure containing attributes related to a request for the maximum number of parallel threads.
- [os_workgroup_set_working_arena](./os_workgroup_set_working_arena.md)
  Distributes a block of managed memory to the threads of a workgroup.
- [os_workgroup_index](./os_workgroup_index.md)
  A unique index that the workgroup assigns to its joined threads.
- [os_workgroup_working_arena_destructor_t](./os_workgroup_working_arena_destructor_t.md)
  A function that deallocates a workgroup’s currently assigned shared memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_get_working_arena)*