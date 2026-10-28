# MPDeleteCriticalRegion

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Removes the specified critical region object. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDeleteCriticalRegion(MPCriticalRegionID criticalRegion);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

Calling this function unblocks all tasks waiting to enter the critical region and their respective  [`MPEnterCriticalRegion`](./api-1585622-mpentercriticalregion.md)  calls will return with the result code `kMPDeletedErr`.

Also see the function  [`MPCreateCriticalRegion`](./api-1585663-mpcreatecriticalregion.md). 

## Parameters

- `criticalRegion`: The critical region object you want to remove. 

## See Also

### Handling Critical Regions
- [MPCreateCriticalRegion](./api-1585663-mpcreatecriticalregion.md)
  Creates a critical region object.
- [MPEnterCriticalRegion](./api-1585622-mpentercriticalregion.md)
  Attempts to enter a critical region. 
- [MPExitCriticalRegion](./api-1585758-mpexitcriticalregion.md)
  Exits a critical region. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585704-mpdeletecriticalregion)*