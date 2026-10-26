# SetRefCon

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set reference value associated with this port.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
void (*SetRefCon)(IOFireWireLibIsochPortRef self, void *inRefCon);
```

#### Discussion

Retrieve the reference value with GetRefCon()

## Parameters

- `self`: The isoch port interface to use.
- `inRefCon`: The new reference value.

## See Also

### Miscellaneous
- [AllocatePort](./api-1569309-allocateport.md)
  The method is called when the port should configure its associated hardware to prepare to send or receive isochronous data on the channel number and at the speed specified.
- [GetRefCon](./api-1569245-getrefcon.md)
  Get reference value associated with this port.
- [GetSupported](./api-1569205-getsupported.md)
  The method is called to determine which FireWire isochronous channels and speed this port supports.
- [ReleasePort](./api-1569267-releaseport.md)
  The method is called to release the hardware after the channel has been stopped.
- [Start](./api-1569348-start.md)
  The method is called when the port is to begin talking or listening.
- [Stop](./api-1569292-stop.md)
  The method is called when the port is to stop talking or listening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireisochportinterface/1569301-setrefcon)*