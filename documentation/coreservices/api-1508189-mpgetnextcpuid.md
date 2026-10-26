# MPGetNextCpuID

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Obtains the next CPU ID in the list of physical processors of the specified memory coherence group. 

**Availability**:
- macOS 10.4+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPGetNextCpuID(MPCoherenceID owningCoherenceID, MPCpuID *cpuID);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

By iterating on this function (after calling  [`MPProcessors`](./api-1585778-mpprocessors.md) , for example), you can obtain the IDs of all the processors available on the host computer. Generally, you would only use this function in diagnostic programs.

## Parameters

- `owningCoherenceID`: The ID of the memory coherence group whose physical processor IDs you want to obtain. Pass `kMPInvalidIDErr`, as only one coherence group, internal RAM, is currently defined. 
- `cpuID`: On return, `cpuID` points to the ID of the next physical processor. 

## See Also

### Determining Multiprocessing Services And Processor Availability
- [_MPIsFullyInitialized](./carbon_core/multiprocessing_services/api-1809315-_mpisfullyinitialized.md)
  Indicates whether Multiprocessing Services is available for use.
- [MPProcessors](./api-1585778-mpprocessors.md)
  Returns the number of processors on the host computer. 
- [MPProcessorsScheduled](./api-1585777-mpprocessorsscheduled.md)
  Returns the number of active processors available on the host computer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1508189-mpgetnextcpuid)*