# UNCalendarNotificationTrigger

**Framework**: User Notifications  
**Kind**: class

A trigger condition that causes a notification the system delivers at a specific date and time.

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
class UNCalendarNotificationTrigger
```

#### Overview

Create a [`UNCalendarNotificationTrigger`](uncalendarnotificationtrigger.md) object when you want to schedule the delivery of a local notification at the date and time you specify. You use an [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) object to specify only the time values that you want the system to use to determine the matching date and time.

Listing 1 creates a trigger that delivers its notification every morning at 8:30. The repeating behavior is achieved by specifying `true` for the `repeats` parameter when creating the trigger.

Listing 1. Creating a trigger that repeats at a specific time

## Topics

### Creating a Calendar Trigger
- [convenience init(dateMatching: DateComponents, repeats: Bool)](uncalendarnotificationtrigger/init(datematching:repeats:).md)
  Creates a calendar trigger using the date components parameter.
### Getting the Trigger Information
- [func nextTriggerDate() -> Date?](uncalendarnotificationtrigger/nexttriggerdate.md)
  The next date at which the trigger conditions are met.
- [var dateComponents: DateComponents](uncalendarnotificationtrigger/datecomponents.md)
  The date components to construct this object.

## Relationships

### Inherits From
- [UNNotificationTrigger](unnotificationtrigger.md)
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

- [class UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [class UNLocationNotificationTrigger](unlocationnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [class UNPushNotificationTrigger](unpushnotificationtrigger.md)
  A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- [class UNNotificationTrigger](unnotificationtrigger.md)
  The common behavior for subclasses that trigger the delivery of a local or remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger)*