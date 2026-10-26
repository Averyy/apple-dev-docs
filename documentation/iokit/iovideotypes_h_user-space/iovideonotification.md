# IOVideoNotification

**Framework**: IOKit  
**Kind**: tag

This structure contains an individual notification from the driver.

## Declaration

```c
struct IOVideoDeviceNotification {
   UInt32 mObjectID;
   UInt32 mNotificationID;
   UInt32 mNotificationArgument1;
   UInt32 mNotificationArgument2;
   UInt64 mNotificationArgument3;
   UInt64 mNotificationArgument4;
};
```

## Topics

### Fields
- [mObjectID](../../kernel/iovideodevicenotification/api-1411466-mobjectid.md)
  The ID of the object to which the notification pertains.
- [mNotificationID](../../kernel/iovideodevicenotification/api-1411383-mnotificationid.md)
  A UInt32 that identifies the kind of the notification.
- [mNotificationArgument1](../../kernel/iovideodevicenotification/api-1411421-mnotificationargument1.md)
  A UInt32 whose usage depends on the the specific kind of notification.
- [mNotificationArgument2](../../kernel/iovideodevicenotification/api-1411377-mnotificationargument2.md)
  A UInt32 whose usage depends on the the specific kind of notification.
- [mNotificationArgument3](../../kernel/iovideodevicenotification/api-1411448-mnotificationargument3.md)
  A UInt64 whose usage depends on the the specific kind of notification.
- [mNotificationArgument4](../../kernel/iovideodevicenotification/api-1411371-mnotificationargument4.md)
  A UInt64 whose usage depends on the the specific kind of notification.

## See Also

### Related Documentation
- [IOVideoNotification](./iovideonotification.md)
  This structure contains an individual notification from the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideotypes_h_user-space/iovideonotification)*