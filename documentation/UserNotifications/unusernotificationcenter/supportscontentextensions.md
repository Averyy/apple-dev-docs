# supportsContentExtensions

**Framework**: User Notifications  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) BOOL supportsContentExtensions;
```

*macOS*

```objc
@property (atomic, readonly) BOOL supportsContentExtensions;
```

## Discussion

Notification content extensions let you customize the appearance of the alerts displayed for your app’s notifications. The value of this property is [`true`](../../Swift/true.md) for devices that support notification content extensions and [`false`](../../Swift/false.md) for devices that do not support them. For information about how to implement a notification content extension, see [Customizing the Appearance of Notifications](../../UserNotificationsUI/customizing-the-appearance-of-notifications.md).

## See Also

### Processing received notifications
- [var delegate: (any UNUserNotificationCenterDelegate)?](./delegate.md)
  The notification center’s delegate.
- [protocol UNUserNotificationCenterDelegate](../unusernotificationcenterdelegate.md)
  An interface for processing incoming notifications and responding to notification actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/supportscontentextensions)*