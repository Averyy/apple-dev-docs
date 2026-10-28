# SetSkippedPacketHandler

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set the callback that should be called when incoming packets are dropped by the address space.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
const IOFWAsyncStreamListenerSkippedPacketHandler (*SetSkippedPacketHandler)(IOFWAsyncStreamListenerInterfaceRef self, IOFWAsyncStreamListenerSkippedPacketHandler inHandler);
```

## Return Value

Returns the callback that was previously set or nil for none.

## Parameters

- `self`: The address space interface to use.
- `inHandler`: The callback to set.

## See Also

### Miscellaneous
- [ClientCommandIsComplete](./api-1569204-clientcommandiscomplete.md)
  Notify the async stream object that a packet notification handler has completed.
- [GetFlags](./api-1569264-getflags.md)
  get the flags of listener.
- [GetOverrunCounter](./api-1569355-getoverruncounter.md)
  get overrun counter from the DCL program.
- [GetRefCon](./api-1569191-getrefcon.md)
  Returns the user refCon value for this async stream interface.
- [NotificationIsOn](./api-1569341-notificationison.md)
  Is notification on?
- [SetFlags](./api-1569319-setflags.md)
  set flags for the listener.
- [SetListenerHandler](./api-1569284-setlistenerhandler.md)
  Set the callback that should be called to handle incoming async stream packets
- [TurnOffNotification](./api-1569306-turnoffnotification.md)
  Force packet notification off.
- [TurnOnNotification](./api-1569192-turnonnotification.md)
  Try to turn on packet notifications for this channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofwasyncstreamlistenerinterface/1569256-setskippedpackethandler)*