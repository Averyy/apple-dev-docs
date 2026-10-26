# AllocateSendPacket_v

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Allocate a SendPacket NuDCL and append it to the program.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
NuDCLSendPacketRef (*AllocateSendPacket_v)(IOFireWireLibNuDCLPoolRef self, CFMutableSetRef saveBag, IOVirtualRange *firstRange);
```

#### Return Value

Returns an NuDCLSendPacketRef on success or 0 on failure.

#### Discussion

Same as AllocateSendPacket but ranges are passed as a NULL-terminated vector of IOVirtualRange's

## Parameters

- `self`: The NuDCL pool to use.
- `saveBag`: The allocated DCL can be added to a CFBag for easily setting DCL update lists. Pass a CFMutableSetRef to add the allocated DCL to a CFBag; pass NULL to ignore. SaveBag is unmodified on failure.
- `firstRange`: The first buffer to be transmitted. Follow with additional ranges; terminate with NULL.

## See Also

### Miscellaneous
- [AllocateReceivePacket](./api-1569189-allocatereceivepacket.md)
  Allocate a ReceivePacket NuDCL and append it to the program
- [AllocateReceivePacket_v](./api-1569299-allocatereceivepacket_v.md)
  Allocate a ReceivePacket NuDCL and append it to the program
- [AllocateSendPacket](./api-1569297-allocatesendpacket.md)
  Allocate a SendPacket NuDCL and append it to the program.
- [AllocateSkipCycle](./api-1569236-allocateskipcycle.md)
  Allocate a SkipCycle NuDCL and append it to the program.
- [AppendDCLRanges](./api-1569263-appenddclranges.md)
  Add a memory range to the scatter gather list of a NuDCL
- [AppendDCLUpdateList](./api-1569230-appenddclupdatelist.md)
- [CopyDCLUpdateList](./api-1569302-copydclupdatelist.md)
- [CountDCLRanges](./api-1569365-countdclranges.md)
  Returns number of buffers for a NuDCL
- [FindDCLNextDCL](./api-1569217-finddclnextdcl.md)
  Get the next pointer for a NuDCL
- [GetDCLBranch](./api-1569274-getdclbranch.md)
  Get the branch pointer for a NuDCL
- [GetDCLCallback](./api-1569314-getdclcallback.md)
  Get callback for a NuDCL
- [GetDCLFlags](./api-1569338-getdclflags.md)
- [GetDCLRanges](./api-1569226-getdclranges.md)
  Get the scatter-gather list for a NuDCL
- [GetDCLRefcon](./api-1569337-getdclrefcon.md)
- [GetDCLs](./api-1569203-getdcls.md)
  Returns the pool's DCL program as a CFArray of NuDCLRef's.
- [GetDCLSize](./api-1569253-getdclsize.md)
  Returns number of bytes to be transferred by a NuDCL
- [GetDCLSkipBranch](./api-1569220-getdclskipbranch.md)
- [GetDCLSkipCallback](./api-1569350-getdclskipcallback.md)
- [GetDCLSkipRefcon](./api-1569331-getdclskiprefcon.md)
- [GetDCLSpan](./api-1569262-getdclspan.md)
  Returns a virtual range spanning lowest referenced buffer address to highest
- [GetDCLStatusPtr](./api-1569185-getdclstatusptr.md)
  Get the status pointer for a NuDCL.
- [GetDCLSyncBits](./api-1569280-getdclsyncbits.md)
- [GetDCLTagBits](./api-1569209-getdcltagbits.md)
- [GetDCLTimeStampPtr](./api-1569218-getdcltimestampptr.md)
  Get the time stamp pointer for a NuDCL.
- [GetDCLUserHeaderPtr](./api-1569294-getdcluserheaderptr.md)
- [GetProgram](./api-1569183-getprogram.md)
  Finds the first DCL in the pool not preceeded by any other DCL.
- [GetUserHeaderMaskPtr](./api-1569211-getuserheadermaskptr.md)
- [PrintDCL](./api-1569336-printdcl.md)
- [PrintProgram](./api-1569279-printprogram.md)
- [RemoveDCLUpdateList](./api-1569281-removedclupdatelist.md)
- [SetCurrentTagAndSync](./api-1569304-setcurrenttagandsync.md)
  Set current tag and sync bits
- [SetDCLBranch](./api-1569290-setdclbranch.md)
  Set the branch pointer for a NuDCL
- [SetDCLCallback](./api-1569248-setdclcallback.md)
  Set the callback for a NuDCL
- [SetDCLFlags](./api-1569321-setdclflags.md)
- [SetDCLRanges](./api-1569310-setdclranges.md)
  Set the scatter gather list for a NuDCL
- [SetDCLRefcon](./api-1569363-setdclrefcon.md)
- [SetDCLSkipBranch](./api-1569198-setdclskipbranch.md)
- [SetDCLSkipCallback](./api-1569352-setdclskipcallback.md)
- [SetDCLSkipRefcon](./api-1569313-setdclskiprefcon.md)
- [SetDCLStatusPtr](./api-1569282-setdclstatusptr.md)
  Set the status pointer for a NuDCL
- [SetDCLSyncBits](./api-1569275-setdclsyncbits.md)
- [SetDCLTagBits](./api-1569229-setdcltagbits.md)
- [SetDCLTimeStampPtr](./api-1569346-setdcltimestampptr.md)
  Set the time stamp pointer for a NuDCL
- [SetDCLUpdateList](./api-1569340-setdclupdatelist.md)
- [SetDCLUserHeaderPtr](./api-1569249-setdcluserheaderptr.md)
  Set a user specified header for a send NuDCL
- [SetDCLWaitControl](./api-1569186-setdclwaitcontrol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirenudclpoolinterface/1569323-allocatesendpacket_v)*