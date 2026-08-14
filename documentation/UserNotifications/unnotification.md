# UNNotification

**Framework**: User Notifications  
**Kind**: class

The data for a local or remote notification the system delivers to your app.

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
class UNNotification
```

#### Overview

A [`UNNotification`](unnotification.md) object contains the initial notification request, which contains the notification’s payload, and the date that the system delivered the notification.

Don’t create notification objects directly. When handling notifications, the system delivers notification objects to your [`UNUserNotificationCenterDelegate`](unusernotificationcenterdelegate.md) object. The [`UNUserNotificationCenter`](unusernotificationcenter.md) object also maintains the list of notifications that the system delivers, and you use the [`getDeliveredNotifications(completionHandler:)`](unusernotificationcenter/getdeliverednotifications(completionhandler:).md) method to retrieve those objects.

## Topics

### Getting the Notification Details
- [var request: UNNotificationRequest](unnotification/request.md)
  The notification request containing the payload and trigger condition for the notification.
- [var date: Date](unnotification/date.md)
  The delivery date of the notification.
### Initializers
- [init?(coder: NSCoder)](unnotification/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
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

- [Scheduling a notification locally from your app](scheduling-a-notification-locally-from-your-app.md)
  Create and schedule notifications from your app when you want to get the user’s attention.
- [class UNNotificationRequest](unnotificationrequest.md)
  A request to schedule a local notification, which includes the content of the notification and the trigger conditions for delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotification)*