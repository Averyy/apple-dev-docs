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
- [AllocatePort](./api-1569309-allocateport.md)
  The method is called when the port should configure its associated hardware to prepare to send or receive isochronous data on the channel number and at the speed specified.
- [GetRefCon](./api-1569245-getrefcon.md)
  Get reference value associated with this port.
- [ReleasePort](./api-1569267-releaseport.md)
  The method is called to release the hardware after the channel has been stopped.
- [SetRefCon](./api-1569301-setrefcon.md)
  Set reference value associated with this port.
- [Start](./api-1569348-start.md)
  The method is called when the port is to begin talking or listening.
- [Stop](./api-1569292-stop.md)
  The method is called when the port is to stop talking or listening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireisochportinterface/1569205-getsupported)*