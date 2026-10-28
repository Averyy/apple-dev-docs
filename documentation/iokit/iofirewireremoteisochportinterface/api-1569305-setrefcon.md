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

## Discussion

Retrieve the reference value with GetRefCon()

## Parameters

- `self`: The isoch port interface to use.
- `inRefCon`: The new reference value.

## See Also

### Miscellaneous
- [AllocatePort](./api-1569266-allocateport.md)
  The method is called when the port should configure its associated hardware to prepare to send or receive isochronous data on the channel number and at the speed specified.
- [GetRefCon](./api-1569317-getrefcon.md)
  Get reference value associated with this port.
- [GetSupported](./api-1569252-getsupported.md)
  The method is called to determine which FireWire isochronous channels and speed this port supports.
- [ReleasePort](./api-1569201-releaseport.md)
  The method is called to release the hardware after the channel has been stopped.
- [SetAllocatePortHandler](./api-1569327-setallocateporthandler.md)
- [SetGetSupportedHandler](./api-1569273-setgetsupportedhandler.md)
- [SetReleasePortHandler](./api-1569272-setreleaseporthandler.md)
- [SetStartHandler](./api-1569358-setstarthandler.md)
- [SetStopHandler](./api-1569289-setstophandler.md)
- [Start](./api-1569244-start.md)
  The method is called when the port is to begin talking or listening.
- [Stop](./api-1569216-stop.md)
  The method is called when the port is to stop talking or listening.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireremoteisochportinterface/1569305-setrefcon)*