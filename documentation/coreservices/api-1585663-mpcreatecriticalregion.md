# MPCreateCriticalRegion

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a critical region object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCreateCriticalRegion(MPCriticalRegionID *criticalRegion);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

Also see the function  [`MPDeleteCriticalRegion`](./api-1585704-mpdeletecriticalregion.md). 

## Parameters

- `criticalRegion`: On return, the `criticalRegion` contains the ID of the newly created critical region object. 

## See Also

### Handling Critical Regions
- [MPDeleteCriticalRegion](./api-1585704-mpdeletecriticalregion.md)
  Removes the specified critical region object. 
- [MPEnterCriticalRegion](./api-1585622-mpentercriticalregion.md)
  Attempts to enter a critical region. 
- [MPExitCriticalRegion](./api-1585758-mpexitcriticalregion.md)
  Exits a critical region. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585663-mpcreatecriticalregion)*