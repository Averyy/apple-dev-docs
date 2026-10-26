# IOVideoDeviceNotificationMessage

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
typedef struct IOVideoDeviceNotificationMessage {
    ...
} IOVideoDeviceNotificationMessage;
```

## Topics

### Instance Properties
- [mClientData](./iovideodevicenotificationmessage/api-1503868-mclientdata.md)
  The client data that was registered with the mach port.
- [mMessageHeader](./iovideodevicenotificationmessage/api-1503932-mmessageheader.md)
  The mach message header.
- [mNotifications](./iovideodevicenotificationmessage/api-1503948-mnotifications.md)
  A variable length array of IOVideoNotification structures that carry the actual notification data. The number of elements in this array is denoted by mNumberNotifications, but can also be inferred from the message size in the mach message header.
- [mNumberNotifications](./iovideodevicenotificationmessage/api-1503922-mnumbernotifications.md)
  The number of IOVideoNotifications in the mNotifications array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideodevicenotificationmessage)*