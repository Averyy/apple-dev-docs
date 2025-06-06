# Presenting notifications on Apple Watch

**Framework**: Watchos Apps

Understand how the system displays incoming notifications.

#### Overview

When the Apple Watch displays a notification, the system first presents the short-look interface. If the user continues to look at the notification, the system transitions quickly from the short-look interface to the long-look interface

##### Display a Short Look Interface

The  interface is a nonscrolling screen that the system creates automatically.

![A screenshot of the short-look interface, with the icon, title, and app name called out.](https://docs-assets.developer.apple.com/published/fbdc2b8c06214de181743202132c954a/presenting-notifications-on-apple-watch-1%402x.png)

The system uses a template to display the app name and icon along with the title string from the notification payload, and you can’t customize this interface. For local notifications, you specify the title string using the [`UNMutableNotificationContent`](https://developer.apple.com/documentation/UserNotifications/UNMutableNotificationContent) object’s [`title`](https://developer.apple.com/documentation/UserNotifications/UNMutableNotificationContent/title) property. For remote notifications, you specify it using the `alert` dictionary’s `title` key inside the notification’s payload.

##### Transition to the Long Look Interface

The  interface is a scrollable screen that displays the notification’s content and any associated action buttons. The system’s default long-look interface includes your app icon, the notification’s title string, and the alert message; however, your app can customize this interface.

![A screenshot of the short-look interface, with the sash, content, actions, and dismiss button called out.](https://docs-assets.developer.apple.com/published/b25d67717c5060cc02ff768fb3d58e0b/presenting-notifications-on-apple-watch-2%402x.png)

The long-look notification includes the following sections:

- The sash is an overlay that contains the app icon and app name. The system automatically generates the sash, but you can configure the appearance using the hosting controller’s [`sashColor`](https://developer.apple.com/documentation/SwiftUI/WKUserNotificationHostingController/sashColor), [`titleColor`](https://developer.apple.com/documentation/SwiftUI/WKUserNotificationHostingController/titleColor), [`subtitleColor`](https://developer.apple.com/documentation/SwiftUI/WKUserNotificationHostingController/subtitleColor), and [`wantsSashBlur`](https://developer.apple.com/documentation/SwiftUI/WKUserNotificationHostingController/wantsSashBlur) properties.
- The content area contains detailed information about the incoming notification. If you provide a dynamic interactive interface for the notification, the content area can contain controls, like buttons or switches. For information on customizing the long-look interface, see [`Customizing your long-look interface`](customizing-your-long-look-interface.md).
- The bottom contains a Dismiss button and any registered action buttons. For more information, see [`Adding actions to notifications on watchOS`](adding-actions-to-notifications-on-watchos.md).

By default, the system dismisses the long-look interface, launches your app, and calls your notification center delegate’s [`userNotificationCenter(_:didReceive:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:didReceive:withCompletionHandler:)) method when the user taps the notification. The response parameter’s [`actionIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationResponse/actionIdentifier) property varies, as shown below.

| Interface element | Action identifier |
| --- | --- |
| Action button | The identifier for the selected action |
| Dismiss button | [`UNNotificationDismissActionIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationDismissActionIdentifier) |
| Anywhere else | [`UNNotificationDefaultActionIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNNotificationDefaultActionIdentifier) |

For dynamic interactive interfaces, tapping the app content doesn’t launch your watchOS app. Instead, the user can interact with any controls placed in the interface, and the system calls the corresponding action method. The system only dismisses the notification and launches your app if the user taps the app icon or sash, or if you explicitly call the notification controller’s [`performNotificationDefaultAction()`](https://developer.apple.com/documentation/WatchKit/WKUserNotificationInterfaceController/performNotificationDefaultAction()) method.

## See Also

- [Enabling and receiving notifications](enabling-and-receiving-notifications.md)
  Set up and handle local and remote notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/presenting-notifications-on-apple-watch)*