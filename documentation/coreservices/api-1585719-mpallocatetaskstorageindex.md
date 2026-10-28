# MPAllocateTaskStorageIndex

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns an index number to access per-task storage. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPAllocateTaskStorageIndex(TaskStorageIndex *taskIndex);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

A call to the function `MPAllocateTaskStorageIndex` returns an index number that is common across all tasks in the current process. You can use this index number in calls to  [`MPSetTaskStorageValue`](./api-1585626-mpsettaskstoragevalue.md)  and  [`MPGetTaskStorageValue`](./api-1585589-mpgettaskstoragevalue.md)  to set a different value for each task using the same index. 

You can think of the task storage area as a two dimensional array cross-referenced by the task storage index number and the task ID. Note that since the amount of per-task storage is determined when the task is created, the number of possible index values associated with a task is limited.

Also see the function  [`MPDeallocateTaskStorageIndex`](./api-1585649-mpdeallocatetaskstorageindex.md). 

## Parameters

- `index`: On return, `index` contains an index number you can use to store task data. 

## See Also

### Accessing Per-Task Storage Variables
- [MPDeallocateTaskStorageIndex](./api-1585649-mpdeallocatetaskstorageindex.md)
  Frees an index number used to access per-task storage 
- [MPGetTaskStorageValue](./api-1585589-mpgettaskstoragevalue.md)
  Gets the storage value stored at a specified index number. 
- [MPSetTaskStorageValue](./api-1585626-mpsettaskstoragevalue.md)
  Sets the storage value for a given index number. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585719-mpallocatetaskstorageindex)*