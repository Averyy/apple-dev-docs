# MPDeallocateTaskStorageIndex

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Frees an index number used to access per-task storage 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDeallocateTaskStorageIndex(TaskStorageIndex taskIndex);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

Also see the function  [`MPAllocateTaskStorageIndex`](./api-1585719-mpallocatetaskstorageindex.md). 

## Parameters

- `index`: The index number you want to deallocate. 

## See Also

### Accessing Per-Task Storage Variables
- [MPAllocateTaskStorageIndex](./api-1585719-mpallocatetaskstorageindex.md)
  Returns an index number to access per-task storage. 
- [MPGetTaskStorageValue](./api-1585589-mpgettaskstoragevalue.md)
  Gets the storage value stored at a specified index number. 
- [MPSetTaskStorageValue](./api-1585626-mpsettaskstoragevalue.md)
  Sets the storage value for a given index number. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585649-mpdeallocatetaskstorageindex)*