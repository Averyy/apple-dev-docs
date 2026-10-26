# ModifyTransferPacketDCLSize

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Modify the transfer size of a transfer packet DCL (send or receive)

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
IOReturn (*ModifyTransferPacketDCLSize)(IOFireWireLibLocalIsochPortRef self, DCLTransferPacket *inDCL, IOByteCount size);
```

#### Return Value

Returns kIOReturnSuccess on success. Will return an error if 'size' is too large for this program.

#### Discussion

Allows you to modify transfer packet DCLs after they have been compiled and while the DCL program is still running. The transfer size can be set to any size less than or equal to the size set when the DCL program was compiled (including 0).

Availability: IOFireWireLocalIsochPortInterface_v2 and newer.

## Parameters

- `self`: The local isoch port interface to use.
- `inDCL`: A pointer to the DCL to modify.
- `size`: The new size of data to be transferred.

## See Also

### Miscellaneous
- [AllocatePort](./api-1569283-allocateport.md)
  The method is called when the port should configure its associated hardware to prepare to send or receive isochronous data on the channel number and at the speed specified.
- [GetRefCon](./api-1569219-getrefcon.md)
  Get reference value associated with this port.
- [GetSupported](./api-1569242-getsupported.md)
  The method is called to determine which FireWire isochronous channels and speed this port supports.
- [ModifyJumpDCL](./api-1569296-modifyjumpdcl.md)
  Change the jump target label of a jump DCL.
- [ModifyTransferPacketDCL](./api-1569359-modifytransferpacketdcl.md)
  Modify the transfer size of a transfer packet DCL (send or receive)
- [ModifyTransferPacketDCLBuffer](./api-1569193-modifytransferpacketdclbuffer.md)
  NOT IMPLEMENTED. Modify the transfer size of a transfer packet DCL (send or receive)
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelocalisochportinterface/1569237-modifytransferpacketdclsize)*