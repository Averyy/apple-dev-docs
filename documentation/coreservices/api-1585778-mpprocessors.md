# MPProcessors

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the number of processors on the host computer. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
ItemCount MPProcessors(void);
```

## Return Value

The number of physical processors on the host computer. 

## Discussion

See also the function  [`MPProcessorsScheduled`](./api-1585777-mpprocessorsscheduled.md). 

## See Also

### Determining Multiprocessing Services And Processor Availability
- [_MPIsFullyInitialized](./carbon_core/multiprocessing_services/api-1809315-_mpisfullyinitialized.md)
  Indicates whether Multiprocessing Services is available for use.
- [MPGetNextCpuID](./api-1508189-mpgetnextcpuid.md)
  Obtains the next CPU ID in the list of physical processors of the specified memory coherence group. 
- [MPProcessorsScheduled](./api-1585777-mpprocessorsscheduled.md)
  Returns the number of active processors available on the host computer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585778-mpprocessors)*