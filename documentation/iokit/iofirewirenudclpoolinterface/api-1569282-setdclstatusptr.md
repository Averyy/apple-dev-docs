# SetDCLStatusPtr

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set the status pointer for a NuDCL

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn (*SetDCLStatusPtr)(NuDCLRef dcl, UInt32 *statusPtr);
```

#### Return Value

Returns an IOReturn error code.

#### Discussion

Setting a the status pointer for a NuDCL causes the packet transmit/receive hardware status to be recorded when the DCL executes. This DCL must be updated after it has executed for the status to be valid.

This change will apply immediately to a non-running DCL program. To apply the change to a running program use IOFireWireLocalIsochPortInterface::Notify()

Status values are as follows: (from the OHCI spec, section 3.1.1)

| **5'h1D** | ack_data_error (receive) | A data field CRC or data_length error. |
| --- | --- | --- |
| **5'h11** | ack_complete (receive/transmit) | No event occurred. (Success) |
| **5'h0E** | evt_unknown (receive/transmit) | An error condition has occurred that cannot be represented by any other event codes defined herein. |
| **5'h0B** | evt_tcode_err (transmit) | A bad tCode is associated with this packet. The packet was flushed. |
| **5'h0A** | evt_timeout (transmit) | Indicates that the asynchronous transmit response packet expired and was not  transmitted, or that an IT DMA context experienced a skip processing overflow (See  section9.3.4). |
| **5'h08** | evt_data_write (receive/transmit) | An error occurred while the Host Controller was attempting to write to host memory  either in the data stage of descriptor processing (AR, IR), or when processing a single  16-bit host memory write (IT). |
| **5'h07** | evt_data_read (transmit) | An error occurred while the Host Controller was attempting to read from host memory  in the data stage of descriptor processing. |
| **5'h06** | evt_descriptor_read (receive/transmit) | An unrecoverable error occurred while the Host Controller was reading a descriptor  block. |
| **5'h05** | evt_overrun (receive) | A receive FIFO overflowed during the reception of an isochronous packet. |
| **5'h02** | evt_long_packet (receive) | The received data length was greater than the buffer's data_length. |
| **5'h00** | No event status. |

Applies: Any NuDCLRef.

## Parameters

- `dcl`: The DCL for which status pointer will be set
- `statusPtr`: A pointer to a quadlet which will hold the status after 'dcl' is updated.

## See Also

### Miscellaneous
- [AllocateReceivePacket](./api-1569189-allocatereceivepacket.md)
  Allocate a ReceivePacket NuDCL and append it to the program
- [AllocateReceivePacket_v](./api-1569299-allocatereceivepacket_v.md)
  Allocate a ReceivePacket NuDCL and append it to the program
- [AllocateSendPacket](./api-1569297-allocatesendpacket.md)
  Allocate a SendPacket NuDCL and append it to the program.
- [AllocateSendPacket_v](./api-1569323-allocatesendpacket_v.md)
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
- [SetDCLSyncBits](./api-1569275-setdclsyncbits.md)
- [SetDCLTagBits](./api-1569229-setdcltagbits.md)
- [SetDCLTimeStampPtr](./api-1569346-setdcltimestampptr.md)
  Set the time stamp pointer for a NuDCL
- [SetDCLUpdateList](./api-1569340-setdclupdatelist.md)
- [SetDCLUserHeaderPtr](./api-1569249-setdcluserheaderptr.md)
  Set a user specified header for a send NuDCL
- [SetDCLWaitControl](./api-1569186-setdclwaitcontrol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirenudclpoolinterface/1569282-setdclstatusptr)*