# UNNotificationRequest

**Framework**: Usernotifications  
**Kind**: class

A request to schedule a local notification, which includes the content of the notification and the trigger conditions for delivery.

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
class UNNotificationRequest
```

#### Overview

Create a [`UNNotificationRequest`](unnotificationrequest.md) object when you want to schedule the delivery of a local notification. A notification request object contains a [`UNNotificationContent`](unnotificationcontent.md) object with the payload and the [`UNNotificationTrigger`](unnotificationtrigger.md) object with the conditions that trigger the delivery of the notification. To schedule the delivery of your notification, pass your request object to the [`add(_:withCompletionHandler:)`](unusernotificationcenter/add(_:withcompletionhandler:).md) method of the shared user notification center object.

After scheduling a request, you interact with `UNNotificationRequest` objects in the following ways:

- View your app’s pending notifications by calling the [`getPendingNotificationRequests(completionHandler:)`](unusernotificationcenter/getpendingnotificationrequests(completionhandler:).md) method of your shared user notification center object.
- When the system delivers a notification to your app, the provided [`UNNotification`](unnotification.md) object contains a `UNNotificationRequest` object that you can inspect to get the notification details.
- Use the request’s [`identifier`](unnotificationrequest/identifier.md) to remove delivered notifications from Notification Center.

When receiving a local or remote notification, use the provided [`UNNotificationRequest`](unnotificationrequest.md) object to fetch details about the notification.

```swift
// Create a content object with the message to convey.
let content = UNMutableNotificationContent()
content.title = "Lunch time"
content.body = "Food is cooked... let's eat!"
// Create a notification trigger for 60 seconds in the future.
let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 60.0, repeats: false)
// Create the request with the content and the trigger.
let request = UNNotificationRequest(identifier: "com.example.mynotification", content: content, trigger: trigger)
```

## Topics

### Creating a Notification Request
- [convenience init(identifier: String, content: UNNotificationContent, trigger: UNNotificationTrigger?)](unnotificationrequest/init(identifier:content:trigger:).md)
  Creates a notification request object that you use to schedule a notification.
### Getting the Request Details
- [var identifier: String](unnotificationrequest/identifier.md)
  The unique identifier for this notification request.
- [var content: UNNotificationContent](unnotificationrequest/content.md)
  The content associated with the notification.
- [var trigger: UNNotificationTrigger?](unnotificationrequest/trigger.md)
  The conditions that trigger the delivery of the notification.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [Scheduling a notification locally from your app](scheduling-a-notification-locally-from-your-app.md)
  Create and schedule notifications from your app when you want to get the user’s attention.
- [class UNNotification](unnotification.md)
  The data for a local or remote notification the system delivers to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationrequest)*