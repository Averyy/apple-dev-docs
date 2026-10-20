# mNotifications

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

A variable length array of IOVideoNotification structures that carry the actual notification data. The number of elements in this array is denoted by mNumberNotifications, but can also be inferred from the message size in the mach message header.

**Availability**:
- macOS 10.7+

## Declaration

```c
IOVideoDeviceNotification mNotifications[1];
```

## See Also

### Fields
- [mMessageHeader](./api-1411394-mmessageheader.md)
  The mach message header.
- [mClientData](./api-1411358-mclientdata.md)
  The client data that was registered with the mach port.
- [mNumberNotifications](./api-1411444-mnumbernotifications.md)
  The number of IOVideoNotifications in the mNotifications array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevicenotificationmessage/1411390-mnotifications)*