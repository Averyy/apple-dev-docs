# UNPushNotificationTrigger

**Framework**: User Notifications  
**Kind**: class  
**Role**: Class

A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class UNPushNotificationTrigger
```

```objc
@interface UNPushNotificationTrigger : UNNotificationTrigger
```

## Overview

You don’t create instances of this class yourself. The system creates [`UNPushNotificationTrigger`](./unpushnotificationtrigger.md) objects and associates them with requests that originated from Apple Push Notification service. You encounter instances of this class when managing your app’s delivered notification requests, which store an object of this type in their [`trigger`](./unnotificationrequest/trigger.md) property.

## Relationships

### Inherits From
- [UNNotificationTrigger](./unnotificationtrigger.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Triggers
- [class UNCalendarNotificationTrigger](./uncalendarnotificationtrigger.md)
  A trigger condition that causes a notification the system delivers at a specific date and time.
- [class UNTimeIntervalNotificationTrigger](./untimeintervalnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [class UNLocationNotificationTrigger](./unlocationnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [class UNNotificationTrigger](./unnotificationtrigger.md)
  The common behavior for subclasses that trigger the delivery of a local or remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unpushnotificationtrigger)*