# FSAllocateFork

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSAllocateFork(FSIORefNum forkRefNum, FSAllocationFlags flags, UInt16 positionMode, SInt64 positionOffset, UInt64 requestCount, UInt64 *actualCount);
```

## See Also

### Allocating Storage for Forks
- [PBAllocateForkSync](./api-1565523-pballocateforksync.md)
- [PBAllocateForkAsync](./api-1566083-pballocateforkasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1566175-fsallocatefork)*