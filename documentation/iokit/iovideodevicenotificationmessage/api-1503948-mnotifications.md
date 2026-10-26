# mNotifications

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

A variable length array of IOVideoNotification structures that carry the actual notification data. The number of elements in this array is denoted by mNumberNotifications, but can also be inferred from the message size in the mach message header.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
IOVideoDeviceNotification mNotifications[1];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideodevicenotificationmessage/1503948-mnotifications)*