# UNCalendarNotificationTrigger

**Framework**: User Notifications  
**Kind**: class  
**Role**: Class

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

```objc
@interface UNCalendarNotificationTrigger : UNNotificationTrigger
```

#### Overview

Create a [`UNCalendarNotificationTrigger`](./uncalendarnotificationtrigger.md) object when you want to schedule the delivery of a local notification at the date and time you specify. You use an [`NSDateComponents`](../Foundation/nsdatecomponents.md) object to specify only the time values that you want the system to use to determine the matching date and time.

Listing 1 creates a trigger that delivers its notification every morning at 8:30. The repeating behavior is achieved by specifying `true` for the `repeats` parameter when creating the trigger.

Listing 1. Creating a trigger that repeats at a specific time

**Swift**:

```swift
var date = DateComponents()
date.hour = 8
date.minute = 30 
let trigger = UNCalendarNotificationTrigger(dateMatching: date, repeats: true)
```

**Objective-C**:

```objc
NSDateComponents* date = [[NSDateComponents alloc] init];
date.hour = 8;
date.minute = 30; 
UNCalendarNotificationTrigger* trigger = [UNCalendarNotificationTrigger
                     triggerWithDateMatchingComponents:date repeats:YES];
```

## Topics

### Creating a Calendar Trigger
- [convenience init(dateMatching: DateComponents, repeats: Bool)](./uncalendarnotificationtrigger/init%28datematching,repeats%29.md)
  Creates a calendar trigger using the date components parameter.
### Getting the Trigger Information
- [func nextTriggerDate() -> Date?](./uncalendarnotificationtrigger/nexttriggerdate%28%29.md)
  The next date at which the trigger conditions are met.
- [var dateComponents: DateComponents](./uncalendarnotificationtrigger/datecomponents.md)
  The date components to construct this object.
### Initializers
- [convenience init(dateMatchingComponents: DateComponents, repeats: Bool)](./uncalendarnotificationtrigger/init%28datematchingcomponents,repeats%29.md)

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
- [class UNTimeIntervalNotificationTrigger](./untimeintervalnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [class UNLocationNotificationTrigger](./unlocationnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.
- [class UNPushNotificationTrigger](./unpushnotificationtrigger.md)
  A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- [class UNNotificationTrigger](./unnotificationtrigger.md)
  The common behavior for subclasses that trigger the delivery of a local or remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger)*