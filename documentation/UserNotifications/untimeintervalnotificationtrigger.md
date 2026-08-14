# UNTimeIntervalNotificationTrigger

**Framework**: User Notifications  
**Kind**: class

A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.

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
class UNTimeIntervalNotificationTrigger
```

#### Overview

Create a [`UNTimeIntervalNotificationTrigger`](untimeintervalnotificationtrigger.md) object when you want to schedule the delivery of a local notification after the number of seconds you specify elapses. You use this type of trigger to implement timers.

Listing 1 creates a trigger that delivers its notification one time after 30 minutes have elapsed.

Listing 1. Creating a trigger that fires in 30 minutes

**Swift**:

```swift
// Fire in 30 minutes (60 seconds times 30)
let trigger = UNTimeIntervalNotificationTrigger(timeInterval: (30*60), repeats: false)
```

**Objective-C**:

```objc
// Fire in 30 minutes (60 seconds times 30)
UNTimeIntervalNotificationTrigger* trigger = [UNTimeIntervalNotificationTrigger
                     triggerWithTimeInterval:(30*60) repeats: NO];
```

## Topics

### Creating a Time Interval Trigger
- [convenience init(timeInterval: TimeInterval, repeats: Bool)](untimeintervalnotificationtrigger/init(timeinterval:repeats:).md)
  Creates a time interval trigger using the time value parameter.
### Getting the Trigger Information
- [func nextTriggerDate() -> Date?](untimeintervalnotificationtrigger/nexttriggerdate.md)
  The next date at which the trigger conditions are met.
- [var timeInterval: TimeInterval](untimeintervalnotificationtrigger/timeinterval.md)
  The time interval to create the trigger.

## Relationships

### Inherits From
- [UNNotificationTrigger](unnotificationtrigger.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md)
  A trigger condition that causes a notification the system delivers at a specific date and time.
- [class UNLocationNotificationTrigger](unlocationnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [class UNPushNotificationTrigger](unpushnotificationtrigger.md)
  A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- [class UNNotificationTrigger](unnotificationtrigger.md)
  The common behavior for subclasses that trigger the delivery of a local or remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger)*