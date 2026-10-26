# MPExitCriticalRegion

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Exits a critical region. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPExitCriticalRegion(MPCriticalRegionID criticalRegion);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If the task does not own the critical region specified by `criticalRegion`, `MPExitCriticalRegion` returns `kMPInsufficientResourcesErr`.

#### Discussion

This function decrements the use count of the critical region object. When the use count reaches zero, ownership of the critical region object is released (which allows another task to use the critical region).

Also see the function  [`MPEnterCriticalRegion`](./api-1585622-mpentercriticalregion.md). 

## Parameters

- `criticalRegion`: The ID of the critical region you want to exit. 

## See Also

### Handling Critical Regions
- [MPCreateCriticalRegion](./api-1585663-mpcreatecriticalregion.md)
  Creates a critical region object.
- [MPDeleteCriticalRegion](./api-1585704-mpdeletecriticalregion.md)
  Removes the specified critical region object. 
- [MPEnterCriticalRegion](./api-1585622-mpentercriticalregion.md)
  Attempts to enter a critical region. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585758-mpexitcriticalregion)*