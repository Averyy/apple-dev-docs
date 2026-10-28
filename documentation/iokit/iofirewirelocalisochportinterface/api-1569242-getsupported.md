# GetSupported

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

The method is called to determine which FireWire isochronous channels and speed this port supports.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetSupported)(IOFireWireLibIsochPortRef self, IOFWSpeed *maxSpeed, UInt64 *chanSupported);
```

## Return Value

Return kIOReturnSuccess on success, other return any other IOReturn error code.

## Discussion

This method is called by the channel object to which a port has been added. Subclasses of IOFireWireIsochPortInterface override this method to support specific hardware. Do not call this method directly.

## Parameters

- `self`: The isoch port interface to use.
- `maxSpeed`: A pointer to an IOFWSpeed which should be filled with the maximum speed this port can talk or listen.
- `chanSupported`: A pointer to a UInt64 which should be filled with a bitmask representing the FireWire bus isochonous channels on which the port can talk or listen. Set '1' for supported, '' for unsupported.

## See Also

### Miscellaneous
- [AllocatePort](./api-1569283-allocateport.md)
  The method is called when the port should configure its associated hardware to prepare to send or receive isochronous data on the channel number and at the speed specified.
- [GetRefCon](./api-1569219-getrefcon.md)
  Get reference value associated with this port.
- [ModifyJumpDCL](./api-1569296-modifyjumpdcl.md)
  Change the jump target label of a jump DCL.
- [ModifyTransferPacketDCL](./api-1569359-modifytransferpacketdcl.md)
  Modify the transfer size of a transfer packet DCL (send or receive)
- [ModifyTransferPacketDCLBuffer](./api-1569193-modifytransferpacketdclbuffer.md)
  NOT IMPLEMENTED. Modify the transfer size of a transfer packet DCL (send or receive)
- [ModifyTransferPacketDCLSize](./api-1569237-modifytransferpacketdclsize.md)
  Modify the transfer size of a transfer packet DCL (send or receive)
- [PrintDCLProgram](./api-1569238-printdclprogram.md)
  Display the contents of a DCL program.
- [ReleasePort](./api-1569332-releaseport.md)
  The method is called to release the hardware after the channel has been stopped.
- [SetFinalizeCallback](./api-1569239-setfinalizecallback.md)
  Set the finalize callback for a local isoch port
- [SetRefCon](./api-1569318-setrefcon.md)
  Set reference value associated with this port.
- [Start](./api-1569339-start.md)
  The method is called when the port is to begin talking or listening.
- [Stop](./api-1569247-stop.md)
  The method is called when the port is to stop talking or listening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelocalisochportinterface/1569242-getsupported)*