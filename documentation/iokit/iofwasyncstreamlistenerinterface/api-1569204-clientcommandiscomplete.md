# ClientCommandIsComplete

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Notify the async stream object that a packet notification handler has completed.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
void (*ClientCommandIsComplete)(IOFWAsyncStreamListenerInterfaceRef self, FWClientCommandID commandID, IOReturn status);
```

#### Discussion

Packet notifications are received one at a time, in order. This function must be called after a packet handler has completed its work.

## Parameters

- `self`: The async stream interface to use.
- `commandID`: The ID of the packet notification being completed. This is the same ID that was passed when a packet notification handler is called.
- `status`: The completion status of the packet handler

## See Also

### Miscellaneous
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
- [SetSkippedPacketHandler](./api-1569256-setskippedpackethandler.md)
  Set the callback that should be called when incoming packets are dropped by the address space.
- [TurnOffNotification](./api-1569306-turnoffnotification.md)
  Force packet notification off.
- [TurnOnNotification](./api-1569192-turnonnotification.md)
  Try to turn on packet notifications for this channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofwasyncstreamlistenerinterface/1569204-clientcommandiscomplete)*