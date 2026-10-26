# MPProcessorsScheduled

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the number of active processors available on the host computer. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
ItemCount MPProcessorsScheduled(void);
```

#### Return Value

The number of active processors available on the host computer. 

#### Discussion

The number of active processors is defined as the number of processors scheduled to run tasks. This number varies while the system is running. Advanced power management facilities may stop or start scheduling processors in the system to control power consumption or to maintain a proper operating temperature.

See also the function  [`MPProcessors`](./api-1585778-mpprocessors.md). 

## See Also

### Determining Multiprocessing Services And Processor Availability
- [_MPIsFullyInitialized](./carbon_core/multiprocessing_services/api-1809315-_mpisfullyinitialized.md)
  Indicates whether Multiprocessing Services is available for use.
- [MPGetNextCpuID](./api-1508189-mpgetnextcpuid.md)
  Obtains the next CPU ID in the list of physical processors of the specified memory coherence group. 
- [MPProcessors](./api-1585778-mpprocessors.md)
  Returns the number of processors on the host computer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585777-mpprocessorsscheduled)*