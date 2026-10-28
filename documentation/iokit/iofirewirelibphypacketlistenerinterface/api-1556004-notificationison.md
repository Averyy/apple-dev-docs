# NotificationIsOn

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Is notification on?

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
Boolean (*NotificationIsOn)(IOFireWireLibPHYPacketListenerRef self);
```

## Return Value

Returns true if packet notifications for this listener are active

## Parameters

- `self`: The PHY packet listener object.

## See Also

### Miscellaneous
- [ClientCommandIsComplete](./api-1555760-clientcommandiscomplete.md)
  Notify the PHY packet listener object that a packet notification handler has completed.
- [GetFlags](./api-1555866-getflags.md)
  get the flags of listener.
- [GetRefCon](./api-1555627-getrefcon.md)
  Returns the user refCon value for thisinterface.
- [SetFlags](./api-1556083-setflags.md)
  set flags for the listener.
- [SetListenerCallback](./api-1556119-setlistenercallback.md)
  Set the callback that should be called to handle incoming phy packets
- [SetRefCon](./api-1555962-setrefcon.md)
  Sets the user refCon value for this interface.
- [SetSkippedPacketCallback](./api-1555813-setskippedpacketcallback.md)
  Set the callback that should be called when incoming phy packets are dropped by the listener space.
- [TurnOffNotification](./api-1555738-turnoffnotification.md)
  Turn packet notification off.
- [TurnOnNotification](./api-1555787-turnonnotification.md)
  Try to turn on packet notifications for this listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelibphypacketlistenerinterface/1556004-notificationison)*