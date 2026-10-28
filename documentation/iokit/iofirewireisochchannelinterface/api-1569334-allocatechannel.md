# AllocateChannel

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Prepare all hardware to begin sending or receiving isochronous data.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
IOReturn (*AllocateChannel)(IOFireWireLibIsochChannelRef self);
```

## Return Value

Returns an IOReturn error code.

## Discussion

Calling this function will result in all listener and talker ports on this isochronous channel having their AllocatePort method called.

## Parameters

- `self`: The isoch channel interface to use.

## See Also

### Miscellaneous
- [AddListener](./api-1569199-addlistener.md)
  Modify the transfer size of a transfer packet DCL (send or receive)
- [ClientCommandIsComplete](./api-1569206-clientcommandiscomplete.md)
- [GetRefCon](./api-1569187-getrefcon.md)
  Set reference value associated with this channel.
- [NotificationIsOn](./api-1569360-notificationison.md)
- [ReleaseChannel](./api-1569255-releasechannel.md)
  Release all hardware after stopping the isochronous channel.
- [SetChannelForceStopHandler](./api-1569347-setchannelforcestophandler.md)
  Set the channel force stop handler.
- [SetRefCon](./api-1569224-setrefcon.md)
  Set reference value associated with this channel.
- [SetTalker](./api-1569194-settalker.md)
  Set the talker port for this channel.
- [Start](./api-1569362-start.md)
  Start the channel.
- [Stop](./api-1569251-stop.md)
  Stop the channel.
- [TurnOffNotification](./api-1569241-turnoffnotification.md)
- [TurnOnNotification](./api-1569227-turnonnotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireisochchannelinterface/1569334-allocatechannel)*