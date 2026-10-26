# IOVideoDeviceNotificationMessage

**Framework**: IOKit  
**Kind**: tag

This structure describes a notification from the driver. Note that the message can contain multiple notifications.

## Declaration

```c
struct IOVideoDeviceNotificationMessage {
   mach_msg_header_t mMessageHeader;
   UInt32 mClientData;
   UInt32 mNumberNotifications;
   IOVideoDeviceNotification mNotifications[1];
};
```

## Topics

### Fields
- [mMessageHeader](../../kernel/iovideodevicenotificationmessage/api-1411394-mmessageheader.md)
  The mach message header.
- [mClientData](../../kernel/iovideodevicenotificationmessage/api-1411358-mclientdata.md)
  The client data that was registered with the mach port.
- [mNumberNotifications](../../kernel/iovideodevicenotificationmessage/api-1411444-mnumbernotifications.md)
  The number of IOVideoNotifications in the mNotifications array.
- [mNotifications](../../kernel/iovideodevicenotificationmessage/api-1411390-mnotifications.md)
  A variable length array of IOVideoNotification structures that carry the actual notification data. The number of elements in this array is denoted by mNumberNotifications, but can also be inferred from the message size in the mach message header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideotypes_h_user-space/iovideodevicenotificationmessage)*