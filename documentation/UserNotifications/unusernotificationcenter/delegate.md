# delegate

**Framework**: User Notifications  
**Kind**: property

The notification center’s delegate.

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
weak var delegate: (any UNUserNotificationCenterDelegate)? { get set }
```

#### Discussion

Use the delegate object to respond to user-selected actions and to process incoming notifications when your app is in the foreground. For example, you might use your delegate to silence notifications when your app is in the foreground.

To guarantee that your app responds to all actionable notifications, you must set the value of this property before your app finishes launching. For an iOS app, this means updating this property in the [`application(_:willFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:willFinishLaunchingWithOptions:)) or [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)) method of the app delegate. Notifications that cause your app to be launched or delivered shortly after these methods finish executing.

For more information about implementing the delegate methods, see [`UNUserNotificationCenterDelegate`](unusernotificationcenterdelegate.md).

## See Also

- [protocol UNUserNotificationCenterDelegate](unusernotificationcenterdelegate.md)
  An interface for processing incoming notifications and responding to notification actions.
- [var supportsContentExtensions: Bool](unusernotificationcenter/supportscontentextensions.md)
  A Boolean value that indicates whether the device supports notification content extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/delegate)*