# supportsContentExtensions

**Framework**: User Notifications  
**Kind**: property

A Boolean value that indicates whether the device supports notification content extensions.

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
var supportsContentExtensions: Bool { get }
```

#### Discussion

Notification content extensions let you customize the appearance of the alerts displayed for your app’s notifications. The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) for devices that support notification content extensions and [`false`](https://developer.apple.com/documentation/swift/false) for devices that do not support them. For information about how to implement a notification content extension, see [`Customizing the Appearance of Notifications`](https://developer.apple.com/documentation/UserNotificationsUI/customizing-the-appearance-of-notifications).

## See Also

- [var delegate: (any UNUserNotificationCenterDelegate)?](unusernotificationcenter/delegate.md)
  The notification center’s delegate.
- [protocol UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md)
  An interface for processing incoming notifications and responding to notification actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/supportscontentextensions)*