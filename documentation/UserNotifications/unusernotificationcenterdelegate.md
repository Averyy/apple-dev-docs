# UNUserNotificationCenterDelegate

**Framework**: User Notifications  
**Kind**: protocol

An interface for processing incoming notifications and responding to notification actions.

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
protocol UNUserNotificationCenterDelegate : NSObjectProtocol
```

#### Overview

Use the methods of the [`UNUserNotificationCenterDelegate`](unusernotificationcenterdelegate.md) protocol to handle user-selected actions from notifications, and to process notifications that arrive when your app is running in the foreground. After implementing these methods in an object, assign that object to the [`delegate`](unusernotificationcenter/delegate.md) property of the shared [`UNUserNotificationCenter`](unusernotificationcenter.md) object. The user notification center object calls the methods of your delegate at appropriate times.

> ❗ **Important**:  You must assign your delegate object to the [`UNUserNotificationCenter`](unusernotificationcenter.md) object before your app finishes launching. For example, in an iOS app, you must assign it in the [`application(_:willFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:willFinishLaunchingWithOptions:)) or [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)) method of your app delegate. Assigning a delegate after the system calls these methods might cause you to miss incoming notifications.

For information about the shared user notification center object, see [`UNUserNotificationCenter`](unusernotificationcenter.md).

## Topics

### First Steps
- [Handling notifications and notification-related actions](handling-notifications-and-notification-related-actions.md)
  Respond to user interactions with the system’s notification interfaces, including handling your app’s custom actions.
### Handling the Selection of Custom Actions
- [func userNotificationCenter(UNUserNotificationCenter, didReceive: UNNotificationResponse, withCompletionHandler: () -> Void)](unusernotificationcenterdelegate/usernotificationcenter(_:didreceive:withcompletionhandler:).md)
  Asks the delegate to process the user’s response to a delivered notification.
### Receiving Notifications
- [func userNotificationCenter(UNUserNotificationCenter, willPresent: UNNotification, withCompletionHandler: (UNNotificationPresentationOptions) -> Void)](unusernotificationcenterdelegate/usernotificationcenter(_:willpresent:withcompletionhandler:).md)
  Asks the delegate how to handle a notification that arrived while the app was running in the foreground.
- [struct UNNotificationPresentationOptions](unnotificationpresentationoptions.md)
  Constants indicating how to present a notification in a foreground app.
### Displaying Notification Settings
- [func userNotificationCenter(UNUserNotificationCenter, openSettingsFor: UNNotification?)](unusernotificationcenterdelegate/usernotificationcenter(_:opensettingsfor:).md)
  Asks the delegate to display the in-app notification settings.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UNUserNotificationCenter](unusernotificationcenter.md)
  The central object for managing notification-related activities for your app or app extension.
- [class UNNotificationSettings](unnotificationsettings.md)
  The object for managing notification-related settings and the authorization status of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)*