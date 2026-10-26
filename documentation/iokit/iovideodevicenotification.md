# IOVideoDeviceNotification

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
typedef struct IOVideoDeviceNotification {
    ...
} IOVideoDeviceNotification;
```

## Topics

### Instance Properties
- [mNotificationArgument1](./iovideodevicenotification/api-1503991-mnotificationargument1.md)
  A UInt32 whose usage depends on the the specific kind of notification.
- [mNotificationArgument2](./iovideodevicenotification/api-1503960-mnotificationargument2.md)
  A UInt32 whose usage depends on the the specific kind of notification.
- [mNotificationArgument3](./iovideodevicenotification/api-1503903-mnotificationargument3.md)
  A UInt64 whose usage depends on the the specific kind of notification.
- [mNotificationArgument4](./iovideodevicenotification/api-1503923-mnotificationargument4.md)
  A UInt64 whose usage depends on the the specific kind of notification.
- [mNotificationID](./iovideodevicenotification/api-1503872-mnotificationid.md)
  A UInt32 that identifies the kind of the notification.
- [mObjectID](./iovideodevicenotification/api-1503906-mobjectid.md)
  The ID of the object to which the notification pertains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideodevicenotification)*