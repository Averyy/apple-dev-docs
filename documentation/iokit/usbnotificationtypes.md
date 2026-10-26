# USBNotificationTypes

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.9+

## Declaration

```c
typedef enum USBNotificationTypes : unsigned int {
    ...
} USBNotificationTypes;
```

#### Overview

Used to register for USB notifications. These types may be OR'd together if more than one notification is desired. These notification are expected to be acknowledged before the process (e.g. system sleep or system wake) can be continued. See RegisterForNotification and AcknowledgeNotification in IOUSBDeviceInterface and IOUSBInterfaceInterface.

## Topics

### Constants
- [kUSBNotificationPreForcedSuspend](./usbnotificationtypes/kusbnotificationpreforcedsuspend.md)
- [kUSBNotificationPostForcedSuspend](./usbnotificationtypes/kusbnotificationpostforcedsuspend.md)
- [kUSBNotificationPreForcedResume](./usbnotificationtypes/kusbnotificationpreforcedresume.md)
- [kUSBNotificationPostForcedResume](./usbnotificationtypes/kusbnotificationpostforcedresume.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbnotificationtypes)*