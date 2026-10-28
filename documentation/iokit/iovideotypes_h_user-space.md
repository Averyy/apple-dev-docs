# IOVideoTypes.h User-Space

**Framework**: IOKit  
**Role**: API Collection

## Overview

### Included Headers

- <IOKit/IOTypes.h>
- <mach/message.h>

## Topics

### Data Types
- [IOVideoNotification](./iovideotypes_h_user-space/iovideonotification.md)
  This structure contains an individual notification from the driver.
- [IOVideoDeviceNotificationMessage](./iovideotypes_h_user-space/iovideodevicenotificationmessage.md)
  This structure describes a notification from the driver. Note that the message can contain multiple notifications.
### Constants
- [Control](./api-1503882-control.md)
  Various constants related to controls.
- [Control](./api-1503935-control.md)
  The class IDs that identify the various control base classes.
- [IOVideoBooleanControl](./api-1503876-iovideobooleancontrol.md)
  The four char codes that identify the various standard subclasses of IOVideoBooleanControl.
- [IOVideoFeatureControl Subclass IDs](./api-1503997-iovideofeaturecontrol_subclass_i.md)
  The four char codes that identify the various standard subclasses of IOVideoFeatureControl.
- [IOVideoSelectorControl](./api-1503936-iovideoselectorcontrol.md)
  The four char codes that identify the various standard subclasses of IOVideoSelectorControl.
- [Notification IDs](./api-1503986-notification_ids.md)
  The four char codes used to identify the kind of the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideotypes_h_user-space)*