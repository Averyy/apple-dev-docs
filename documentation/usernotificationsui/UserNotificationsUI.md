# User Notifications UI

**Framework**: User Notifications UI  
**Kind**: module

Customize the interface that displays local and remote notifications.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

#### Overview

Customize how local and remote notifications appear on the user’s device by adding a notification content app extension to the bundle of your iOS app. Your extension manages a custom view controller, which you use to present the content from incoming notifications. When a notification arrives, the system displays your view controller in addition to, or in place of, the default system interface.

## Topics

### Notification Content App Extension
- [Customizing the Appearance of Notifications](customizing-the-appearance-of-notifications.md)
  Customize the appearance of your iOS app’s notification alerts with a notification content app extension.
- [protocol UNNotificationContentExtension](unnotificationcontentextension.md)
  An object that presents a custom interface for a delivered local or remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UserNotificationsUI)*