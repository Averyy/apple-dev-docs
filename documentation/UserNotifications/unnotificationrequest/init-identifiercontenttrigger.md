# init(identifier:content:trigger:)

**Framework**: Usernotifications  
**Kind**: init

Creates a notification request object that you use to schedule a notification.

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
convenience init(identifier: String, content: UNNotificationContent, trigger: UNNotificationTrigger?)
```

#### Return Value

A new notification request object.

#### Discussion

Use this method when you want to schedule the delivery of a local notification. This method creates the request object that you subsequently pass to the [`add(_:withCompletionHandler:)`](unusernotificationcenter/add(_:withcompletionhandler:).md) method.

The system uses the `identifier` parameter to determine how to handle the request:

-  the system creates a new notification.
-  the system alerts the user again, replaces the old notification with the new one, and places the new notification at the top of the list.
-  the new request replaces the pending request.

## Parameters

- `identifier`: An identifier for the request; this parameter must not be  . You can use this identifier to cancel the request if it’s still pending (see the   method).
- `content`: The content of the notification. This parameter must not be  .
- `trigger`: The condition that causes the system to deliver the notification. Specify   to deliver the notification right away.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/init(identifier:content:trigger:))*