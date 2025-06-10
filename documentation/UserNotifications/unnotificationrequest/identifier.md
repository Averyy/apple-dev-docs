# identifier

**Framework**: User Notifications  
**Kind**: property

The unique identifier for this notification request.

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
var identifier: String { get }
```

#### Discussion

Use this string to identify notifications in your app. For example, you can pass this string to the [`removePendingNotificationRequests(withIdentifiers:)`](unusernotificationcenter/removependingnotificationrequests(withidentifiers:).md) method to cancel a previously scheduled notification.

If you use the same identifier when scheduling a new notification, the system removes the previously scheduled notification with that identifier and replaces it with the new one.

For local notifications, the system sets this property to the value passed to the request’s initializer (see the [`init(identifier:content:trigger:)`](unnotificationrequest/init(identifier:content:trigger:).md) method). For remote notifications, the system sets this property to the value of the `apns-collapse-id` key that you specified in the APNs request header when generating the remote notification. If your app doesn’t set a value, the system automatically assigns an identifier.

## See Also

- [var content: UNNotificationContent](unnotificationrequest/content.md)
  The content associated with the notification.
- [var trigger: UNNotificationTrigger?](unnotificationrequest/trigger.md)
  The conditions that trigger the delivery of the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/identifier)*