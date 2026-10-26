# AllocatePort

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

The method is called when the port should configure its associated hardware to prepare to send or receive isochronous data on the channel number and at the speed specified.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
IOReturn (*AllocatePort)(IOFireWireLibIsochPortRef self, IOFWSpeed speed, UInt32 chan);
```

#### Return Value

Return kIOReturnSuccess on success, other return any other IOReturn error code.

#### Discussion

This method is called by the channel object to which a port has been added. Subclasses of IOFireWireIsochPortInterface override this method to support specific hardware. Do not call this method directly.

## Parameters

- `self`: The isoch port interface to use.
- `speed`: Channel speed
- `chan`: Channel number (-63)

## See Also

### Miscellaneous
- [GetRefCon](./api-1569245-getrefcon.md)
  Get reference value associated with this port.
- [GetSupported](./api-1569205-getsupported.md)
  The method is called to determine which FireWire isochronous channels and speed this port supports.
- [ReleasePort](./api-1569267-releaseport.md)
  The method is called to release the hardware after the channel has been stopped.
- [SetRefCon](./api-1569301-setrefcon.md)
  Set reference value associated with this port.
- [Start](./api-1569348-start.md)
  The method is called when the port is to begin talking or listening.
- [Stop](./api-1569292-stop.md)
  The method is called when the port is to stop talking or listening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireisochportinterface/1569309-allocateport)*