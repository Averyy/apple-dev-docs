# MPSetTaskStorageValue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets the storage value for a given index number. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPSetTaskStorageValue(TaskStorageIndex taskIndex, TaskStorageValue value);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

Typically you use `MPSetTaskStorageValue` to store pointers to task-specific structures or data.

Calling this function from within a task effectively assigns a value in a two-dimensional array cross-referenced by task storage index value and the task ID. 

Also see the function  [`MPGetTaskStorageValue`](./api-1585589-mpgettaskstoragevalue.md). 

## Parameters

- `index`: The index number whose storage value you want to set. 
- `value`: The value you want to set. 

## See Also

### Accessing Per-Task Storage Variables
- [MPAllocateTaskStorageIndex](./api-1585719-mpallocatetaskstorageindex.md)
  Returns an index number to access per-task storage. 
- [MPDeallocateTaskStorageIndex](./api-1585649-mpdeallocatetaskstorageindex.md)
  Frees an index number used to access per-task storage 
- [MPGetTaskStorageValue](./api-1585589-mpgettaskstoragevalue.md)
  Gets the storage value stored at a specified index number. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585626-mpsettaskstoragevalue)*