# UNNotificationContentExtension

**Framework**: User Notifications UI  
**Kind**: protocol

An object that presents a custom interface for a delivered local or remote notification.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol UNNotificationContentExtension : NSObjectProtocol
```

## Mentions

- [Customizing the Appearance of Notifications](customizing-the-appearance-of-notifications.md)

#### Overview

The `UNNotificationContentExtension` protocol provides the entry point for a notification content app extension, which displays a custom interface for your app’s notifications. You adopt this protocol in the custom [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) subclass that you use to present your interface. You create this type of extension to improve the way your notifications are presented, possibly by adding custom colors and branding, or by incorporating media and other dynamic content into your notification interface.

To define a notification content app extension, add a notification content extension target to the Xcode project containing your app. The default Xcode template contains a source file and storyboard for your view controller. The `Info.plist` file of the extension comes mostly configured. Specifically, the `NSExtensionPointIdentifier` key is set to the value `com.apple.usernotifications.content-extension`, and the `NSExtensionMainStoryboard` key is set to the name of the project’s storyboard file. However, the `NSExtensionAttribute` key contains a dictionary of additional keys and values, which are listed in the following table.

| Key | Value |
| --- | --- |
| `UNNotificationExtensionCategory` (Required) | A string or an array of strings. Each string contains the identifier of a category declared by the app using the [`UNNotificationCategory`](https://developer.apple.com/documentation/UserNotifications/UNNotificationCategory) class. |
| `UNNotificationExtensionInitialContentSizeRatio` (Required) | A floating-point number that represents the initial size of your view controller’s view expressed as a ratio of its height to its width. The system uses this value to set the initial size of the view controller while your extension is loading. For example, a value of 0.5 results in a view controller whose height is half its width. You can change the size of your view controller after your extension loads. |
| `UNNotificationExtensionDefaultContentHidden` | A Boolean. When set to [`YES`](https://developer.apple.com/documentation/ObjectiveC/YES), the system displays only your custom view controller in the notification interface. When set to [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO), the system displays the default notification content in addition to your view controller’s content. Custom action buttons and the Dismiss button are always displayed, regardless of this setting. If you don’t specify this key, the default value is set to [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO). |
| `UNNotificationExtensionOverridesDefaultTitle` | A Boolean. When set to [`YES`](https://developer.apple.com/documentation/ObjectiveC/YES), the system uses the [`title`](https://developer.apple.com/documentation/UIKit/UIViewController/title) property of your view controller as the title of the notification. When set to [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO), the system sets the notification’s title to the name of your app. If you don’t specify this key, the default value is set to [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO). |

If the notification category includes custom actions, the system automatically adds action buttons to your notification interface; don’t create those buttons yourself. If your view controller implements the optional [`didReceive(_:completionHandler:)`](unnotificationcontentextension/didreceive(_:completionhandler:).md) method, the system calls that method to respond to any selected actions. If your view controller doesn’t implement that method, the system delivers the selected action to your app for handling.

The system prevents the delivery of touch events to your view controller while it is onscreen. Do not install gesture recognizers or rely on touch events in your interface.

For information about how to implement your notification content app extension, see [`Customizing the Appearance of Notifications`](customizing-the-appearance-of-notifications.md).

## Topics

### Processing Notifications
- [func didReceive(UNNotification)](unnotificationcontentextension/didreceive(_:).md)
  Delivers a new notification to your notification content app extension.
### Handling Custom Actions
- [func didReceive(UNNotificationResponse, completionHandler: (UNNotificationContentExtensionResponseOption) -> Void)](unnotificationcontentextension/didreceive(_:completionhandler:).md)
  Handles a notification action selected by the user.
- [enum UNNotificationContentExtensionResponseOption](unnotificationcontentextensionresponseoption.md)
  Constants indicating the preferred response to a notification.
### Supporting Media Playback
- [var mediaPlayPauseButtonType: UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextension/mediaplaypausebuttontype.md)
  The type of media button type to display.
- [enum UNNotificationContentExtensionMediaPlayPauseButtonType](unnotificationcontentextensionmediaplaypausebuttontype.md)
  Constants indicating the type of media button to display.
- [var mediaPlayPauseButtonFrame: CGRect](unnotificationcontentextension/mediaplaypausebuttonframe.md)
  The frame rectangle to use for displaying a media playback button.
- [var mediaPlayPauseButtonTintColor: UIColor](unnotificationcontentextension/mediaplaypausebuttontintcolor.md)
  The tint color for the media playback button.
- [func mediaPlay()](unnotificationcontentextension/mediaplay.md)
  Tells you to begin playback of your media content.
- [func mediaPause()](unnotificationcontentextension/mediapause.md)
  Tells you to pause playback of your media content.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Scheduling a notification locally from your app](../UserNotifications/scheduling-a-notification-locally-from-your-app.md)
  Create and schedule notifications from your app when you want to get the user’s attention.
- [Setting up a remote notification server](../UserNotifications/setting-up-a-remote-notification-server.md)
  Generate notifications and push them to user devices.
- [Customizing the Appearance of Notifications](customizing-the-appearance-of-notifications.md)
  Customize the appearance of your iOS app’s notification alerts with a notification content app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/unnotificationcontentextension)*