# UNNotificationTrigger

**Framework**: Usernotifications  
**Kind**: class

The common behavior for subclasses that trigger the delivery of a local or remote notification.

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
class UNNotificationTrigger
```

#### Overview

The [`UNNotificationTrigger`](unnotificationtrigger.md) class is an abstract class for representing an event that triggers the delivery of a notification. You don’t create instances of this class directly. Instead, you instantiate the concrete subclass that defines the trigger condition you want for your notification. You then assign the resulting object to the [`UNNotificationRequest`](unnotificationrequest.md) object that you use to schedule your notification.

Concrete trigger classes include the following:

- [`UNTimeIntervalNotificationTrigger`](untimeintervalnotificationtrigger.md)
- [`UNCalendarNotificationTrigger`](uncalendarnotificationtrigger.md)
- [`UNLocationNotificationTrigger`](unlocationnotificationtrigger.md)
- [`UNPushNotificationTrigger`](unpushnotificationtrigger.md)

## Topics

### Configuring the Trigger’s Behavior
- [var repeats: Bool](unnotificationtrigger/repeats.md)
  A Boolean value indicating whether the system reschedules the notification after it’s delivered.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md)
- [UNLocationNotificationTrigger](unlocationnotificationtrigger.md)
- [UNPushNotificationTrigger](unpushnotificationtrigger.md)
- [UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md)
  A trigger condition that causes a notification the system delivers at a specific date and time.
- [class UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [class UNLocationNotificationTrigger](unlocationnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [class UNPushNotificationTrigger](unpushnotificationtrigger.md)
  A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationtrigger)*