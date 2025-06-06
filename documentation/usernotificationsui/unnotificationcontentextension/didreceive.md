# didReceive(_:)

**Framework**: User Notifications UI  
**Kind**: method  
**Required**: Yes

Delivers a new notification to your notification content app extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func didReceive(_ notification: UNNotification)
```

## Mentions

- [Customizing the Appearance of Notifications](customizing-the-appearance-of-notifications.md)

#### Discussion

In your implementation of this method, use the contents of `notification` to configure your view controller. This method may be called multiple times while your view controller is visible. Specifically, it is called again when a new notification arrives whose [`threadIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationContent/threadIdentifier) value matches the thread identifier of the notification already being displayed. The method is called on the main thread of your notification content app extension.

If you want to accommodate new content in your interface, you can change the height of your view controller’s view. Change only the height; width values are ignored. You can then add subviews to fill the additional space with your content.

## Parameters

- `notification`: The notification that arrived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension/didreceive(_:))*