# MPEnterCriticalRegion

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Attempts to enter a critical region. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPEnterCriticalRegion(MPCriticalRegionID criticalRegion, Duration timeout);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

If another task currently occupies the critical region, the current task is blocked until the critical region is released or until the designated timeout expires. Otherwise the task enters the critical region and `MPEnterCriticalRegion` increments the region’s use count. 

Once a task enters a critical region it can make further calls to `MPEnterCriticalRegion` without blocking (its use count increments for each call). However, each call to `MPEnterCriticalRegion` must be balanced by a call to  [`MPExitCriticalRegion`](./api-1585758-mpexitcriticalregion.md) ; otherwise the region is not released for use by other tasks.

Note that you can enter a critical region from a cooperative task. Each cooperative task is treated as unique and different from any preemptive task. If you call this function from a cooperative task, you should specify only `kDurationImmediate` for the timeout length; other waits will cause the task to block.  

## Parameters

- `criticalRegion`: The ID of the critical region you want to enter. 
- `timeout`: The maximum time to wait for entry before timing out. See [Timer Duration Constants](./api-1585641-timer_duration_constants.md) for a list of constants you can use to specify the wait interval. 

## See Also

### Handling Critical Regions
- [MPCreateCriticalRegion](./api-1585663-mpcreatecriticalregion.md)
  Creates a critical region object.
- [MPDeleteCriticalRegion](./api-1585704-mpdeletecriticalregion.md)
  Removes the specified critical region object. 
- [MPExitCriticalRegion](./api-1585758-mpexitcriticalregion.md)
  Exits a critical region. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585622-mpentercriticalregion)*