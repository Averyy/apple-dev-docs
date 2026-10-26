# TurnOnNotification

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Try to turn on packet notifications for this address space.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
Boolean (*TurnOnNotification)(IOFireWireLibPseudoAddressSpaceRef self);
```

#### Return Value

Returns true upon success

## Parameters

- `self`: The address space interface to use.

## See Also

### Miscellaneous
- [ClientCommandIsComplete](./api-1555641-clientcommandiscomplete.md)
  Notify the address space that a packet notification handler has completed.
- [GetBuffer](./api-1556020-getbuffer.md)
  Get a pointer to the backing store for this address space
- [GetBufferSize](./api-1555796-getbuffersize.md)
  Get the size in bytes of this address space.
- [GetFWAddress](./api-1555588-getfwaddress.md)
  Get the FireWire address of this address space
- [GetRefCon](./api-1555864-getrefcon.md)
  Returns the user refCon value for this address space.
- [NotificationIsOn](./api-1555698-notificationison.md)
  Is notification on?
- [SetReadHandler](./api-1555833-setreadhandler.md)
  Set the callback that should be called to handle read accesses to the corresponding address space
- [SetSkippedPacketHandler](./api-1555589-setskippedpackethandler.md)
  Set the callback that should be called when incoming packets are dropped by the address space.
- [SetWriteHandler](./api-1555939-setwritehandler.md)
  Set the callback that should be called to handle write accesses to the corresponding address space
- [TurnOffNotification](./api-1555901-turnoffnotification.md)
  Force packet notification off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirepseudoaddressspaceinterface/1556072-turnonnotification)*