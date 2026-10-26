# ClientCommandIsComplete

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Notify the PHY packet listener object that a packet notification handler has completed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
void (*ClientCommandIsComplete)(IOFireWireLibPHYPacketListenerRef self, FWClientCommandID commandID);
```

#### Discussion

Packet notifications are received one at a time, in order. This function must be called after a packet handler has completed its work.

## Parameters

- `self`: The PHY packet listener object.
- `commandID`: The ID of the packet notification being completed. This is the same ID that was passed when a packet notification handler is called.

## See Also

### Miscellaneous
- [GetFlags](./api-1555866-getflags.md)
  get the flags of listener.
- [GetRefCon](./api-1555627-getrefcon.md)
  Returns the user refCon value for thisinterface.
- [NotificationIsOn](./api-1556004-notificationison.md)
  Is notification on?
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelibphypacketlistenerinterface/1555760-clientcommandiscomplete)*