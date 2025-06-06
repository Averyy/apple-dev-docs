# UNLocationNotificationTrigger

**Framework**: Usernotifications  
**Kind**: class

A trigger condition that causes the system to deliver a notification when the user’s device enters or exits a geographic region you specify.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- watchOS 3.0+

## Declaration

```swift
class UNLocationNotificationTrigger
```

#### Overview

Create a [`UNLocationNotificationTrigger`](unlocationnotificationtrigger.md) object when you want to schedule the delivery of a local notification when the device enters or leaves a specific geographic region. The system limits the number of location-based triggers that it schedules at the same time.

> ❗ **Important**:  Before scheduling any notifications using this trigger, your app must have authorization to use Core Location and must have when-in-use permissions. (Because the system actually monitors the regions, you don’t need to request always permissions for your app). For information about how to request authorization, see [`Requesting authorization to use location services`](https://developer.apple.com/documentation/CoreLocation/requesting-authorization-to-use-location-services).

 Before scheduling any notifications using this trigger, your app must have authorization to use Core Location and must have when-in-use permissions. (Because the system actually monitors the regions, you don’t need to request always permissions for your app). For information about how to request authorization, see [`Requesting authorization to use location services`](https://developer.apple.com/documentation/CoreLocation/requesting-authorization-to-use-location-services).

When configuring the region, use the [`notifyOnEntry`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnEntry) and [`notifyOnExit`](https://developer.apple.com/documentation/CoreLocation/CLRegion/notifyOnExit) properties to specify whether you want the system to deliver notifications on entry, on exit, or both. Listing 1 shows the creation of a trigger that fires only once when the user’s device enters a circular region with a 2-kilometer radius.

Listing 1. Creating a location-based trigger

The system doesn’t immediately trigger region-based notifications when the edge of the boundary is crossed. The system applies heuristics to ensure that the boundary crossing represents a deliberate event and isn’t the result of spurious location data. For more information about the heuristics, see [`Monitoring the user’s proximity to geographic regions`](https://developer.apple.com/documentation/CoreLocation/monitoring-the-user-s-proximity-to-geographic-regions).

## Topics

### Creating a Location Trigger
- [convenience init(region: CLRegion, repeats: Bool)](unlocationnotificationtrigger/init(region:repeats:).md)
  Creates a location trigger using the region parameter.
### Accessing the Trigger Region
- [var region: CLRegion](unlocationnotificationtrigger/region.md)
  The region used to determine when the system sends the notification.

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

- [class UNCalendarNotificationTrigger](uncalendarnotificationtrigger.md)
  A trigger condition that causes a notification the system delivers at a specific date and time.
- [class UNTimeIntervalNotificationTrigger](untimeintervalnotificationtrigger.md)
  A trigger condition that causes the system to deliver a notification after the amount of time you specify elapses.
- [class UNPushNotificationTrigger](unpushnotificationtrigger.md)
  A trigger condition that indicates Apple Push Notification Service (APNs) has sent the notification.
- [class UNNotificationTrigger](unnotificationtrigger.md)
  The common behavior for subclasses that trigger the delivery of a local or remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger)*