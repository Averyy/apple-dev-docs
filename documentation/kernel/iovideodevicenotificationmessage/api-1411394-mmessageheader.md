# mMessageHeader

**Framework**: Kernel  
**Kind**: structp

The mach message header.

**Availability**:
- macOS 10.7+

## Declaration

```swift
mach_msg_header_t mMessageHeader;
```

## See Also

- [mClientData](iovideodevicenotificationmessage/1411358-mclientdata.md)
  The client data that was registered with the mach port.
- [mNumberNotifications](iovideodevicenotificationmessage/1411444-mnumbernotifications.md)
  The number of IOVideoNotifications in the mNotifications array.
- [mNotifications](iovideodevicenotificationmessage/1411390-mnotifications.md)
  A variable length array of IOVideoNotification structures that carry the actual notification data. The number of elements in this array is denoted by mNumberNotifications, but can also be inferred from the message size in the mach message header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iovideodevicenotificationmessage/1411394-mmessageheader)*