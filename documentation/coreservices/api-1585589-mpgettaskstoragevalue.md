# MPGetTaskStorageValue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the storage value stored at a specified index number. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
TaskStorageValue MPGetTaskStorageValue(TaskStorageIndex taskIndex);
```

## Return Value

The value stored at the specified index number. See the description of the `TaskStorageValue` data type.

## Discussion

Calling this function from within a task effectively reads a value in a two-dimensional array cross-referenced by task storage index value and the task ID.

Note that since this function does not return any status information, it may not be immediately obvious whether the returned storage value is valid. 

Also see the function  [`MPSetTaskStorageValue`](./api-1585626-mpsettaskstoragevalue.md). 

## Parameters

- `index`: The index number of the storage value you want to obtain. 

## See Also

### Accessing Per-Task Storage Variables
- [MPAllocateTaskStorageIndex](./api-1585719-mpallocatetaskstorageindex.md)
  Returns an index number to access per-task storage. 
- [MPDeallocateTaskStorageIndex](./api-1585649-mpdeallocatetaskstorageindex.md)
  Frees an index number used to access per-task storage 
- [MPSetTaskStorageValue](./api-1585626-mpsettaskstoragevalue.md)
  Sets the storage value for a given index number. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585589-mpgettaskstoragevalue)*