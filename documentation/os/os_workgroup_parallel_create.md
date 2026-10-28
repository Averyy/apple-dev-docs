# os_workgroup_parallel_create

**Framework**: os  
**Kind**: func  
**Role**: Function

Creates a new workgroup that manges threads working on a single task in parallel.

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
extern os_workgroup_parallel_tos_workgroup_parallel_create(const char *name, os_workgroup_attr_t attr);
```

## Return Value

An opaque workgroup object that tracks a parallel workload.

## Discussion

The returned workgroup doesn’t initially have any associated threads. Join individual threads to the workgroup by calling `os_workgroup_join_self` from the thread itself.

## Parameters

- `name`: An optional name for the workgroup. Use this name to identify the workgroups you create. You may specify `NULL` for this parameter.
- `attr`: The attributes you apply to the workgroup.

## See Also

### Parallel
- [os_workgroup_parallel_t](./os_workgroup_parallel_t.md)
  A workgroup object that supports the scheduling of threads that work in parallel to complete a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/os_workgroup_parallel_create)*