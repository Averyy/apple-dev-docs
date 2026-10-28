# os_workgroup_working_arena_destructor_t

**Framework**: os  
**Kind**: typealias  
**Role**: Type Alias

A function that deallocates a workgroup’s currently assigned shared memory.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef void (*)(void *) os_workgroup_working_arena_destructor_t;
```

## Discussion

Define a custom function of this type to clean up or deallocate the shared memory you assign to a workgroup. If you call the [`os_workgroup_set_working_arena`](./os_workgroup_set_working_arena.md) function on a workgroup that already has a shared memory block, the workgroup calls this function with the current block before saving the new block to the workgroup.

## See Also

### Workgroup Configuration
- [os_workgroup_max_parallel_threads](./os_workgroup_max_parallel_threads.md)
  Returns the maximum number of threads that the system recommends you add to the specified workgroup.
- [os_workgroup_mpt_attr_t](./os_workgroup_mpt_attr_t.md)
  An opaque structure containing attributes related to a request for the maximum number of parallel threads.
- [os_workgroup_set_working_arena](./os_workgroup_set_working_arena.md)
  Distributes a block of managed memory to the threads of a workgroup.
- [os_workgroup_get_working_arena](./os_workgroup_get_working_arena.md)
  Retrieves the workgroup’s shared data, and the thread-specific index into that data.
- [os_workgroup_index](./os_workgroup_index.md)
  A unique index that the workgroup assigns to its joined threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_working_arena_destructor_t)*