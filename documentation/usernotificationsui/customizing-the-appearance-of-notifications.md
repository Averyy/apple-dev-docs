# Customizing the Appearance of Notifications

**Framework**: User Notifications UI

Customize the appearance of your iOS app’s notification alerts with a notification content app extension.

#### Overview

When an iOS device receives a notification containing an alert, the system displays the contents of the alert in two stages. Initially, it displays an abbreviated banner with the title, subtitle, and two to four lines of body text from the notification. If the user presses the abbreviated banner, iOS displays the full notification interface, including any notification-related actions. The system provides the interface for the abbreviated banner, but you can customize the full interface using a notification content app extension.

![Screenshots showing the abbreviated banner and the full notification.](https://docs-assets.developer.apple.com/published/c8698879eaa065aeed4020fab5318b42/customizing_the_appearance_of_notifications-1%402x.png)

The notification content app extension manages a view controller that displays your custom notification interface. This view controller can supplement or replace the default system interface for your notifications. You can use your view controller to:

- Customize the placement of items, including the alert’s title, subtitle, and body text.
- Substitute different fonts or styling for interface elements.
- Display app-specific data—for example, data stored in app-specific keys of the notification’s payload.
- Include custom images or branding.

Your app extension must configure its view controller using the data immediately available, such as the contents of the notification and the files present in your app extension’s bundle. If you use an app group to share data between your app and your app extension, you may also use any files found in the app group. To ensure your notifications are delivered in a timely manner, configure the views as quickly as possible. Don’t perform any long-running tasks, like trying to retrieve data over the network.

> **Note**: Notification content app extensions are supported only in iOS apps. For information about how to customize the appearance of notifications in watchOS, see [`App Programming Guide for watchOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969).

##### Add the Notification Content App Extension to Your Project

To add a notification content app extension to your iOS app:

1. Choose File > New > Target in Xcode.
2. Select Notification Content Extension from iOS Application Extension.
3. Click Next.
4. Provide a name for your app extension.
5. Click Finish.

> **Note**: You may add more than one notification content app extension to your project, but each one must support a unique set of notification categories. You specify the categories for your app extension in its `Info.plist` file, as described in [`Declare the Supported Notification Types`](customizing-the-appearance-of-notifications#Declare-the-Supported-Notification-Types.md).

##### Add Views to Your View Controller

The template provided by Xcode includes a storyboard and a view controller for you to configure. Build your custom notification interface by adding views to your view controller. For example, use labels to display the title, subtitle, and body text of the notification. You can also add image views and views that display noninteractive content. You don’t need to provide any initial content for your views.

You can add interactive controls (for example, buttons or switches) in iOS 12 and later. For more information, see Support Interactive Controls.

> ❗ **Important**: Don’t add additional view controllers to your app extension or storyboard file. Your app extension must contain exactly one view controller.

##### Configure Your View Controller

Use the [`didReceive(_:)`](unnotificationcontentextension/didreceive(_:).md) method of your view controller to update its labels and other views. The notification payload contains the data to use when configuring your view controller. You can also use data from the other files of your app extension. The code listing below shows a version of this method that retrieves the title and body text from the notification payload and assigns the strings to two [`UILabel`](https://developer.apple.com/documentation/UIKit/UILabel) controls, which are stored as outlets on the view controller.

```swift
func didReceive(_ notification: UNNotification) {
   self.bodyText?.text = notification.request.content.body
   self.headlineText?.text = notification.request.content.title
}
```

If a second notification arrives when your view controller is already visible, the system calls the [`didReceive(_:)`](unnotificationcontentextension/didreceive(_:).md) method again with the new notification payload.

##### Declare the Supported Notification Types

Specify the types of notifications for which your notification content app extension provides an interface. When it receives a notification, the system matches the notification’s category value—its type—with the declared categories of any notification content app extensions in your app. If it finds a match, the system loads the corresponding app extension.

In the `Info.plist` file of your notification content app extension, configure the `UNNotificationExtensionCategory` key with the category strings of the notifications that your extension supports. Category strings are identifiers contained in the [`UNNotificationCategory`](https://developer.apple.com/documentation/UserNotifications/UNNotificationCategory) objects that you register from your iOS app. You use these strings to differentiate the types of notifications that your app can receive. For example, you might include the string `MEETING_INVITE` in any notifications that indicate the arrival of a new meeting invitation. Identifier strings are case sensitive.

The following figure shows the `Info.plist` file of a notification content app extension that supports two different notification types. Because it supports two types, the value for the `UNNotificationExtensionCategory` key consists of an array with the strings `GENERAL` and `PLANE_AVAILABLE`. If a notification with either of those types arrives, the system displays the interface from this notification content app extension.

![A screenshot of the plist editor, showing the UNNotificationExtensionCategory for two notification types.](https://docs-assets.developer.apple.com/published/152e34869924e4cd1a285365566a5a97/customizing_the_appearance_of_notifications-2%402x.png)

> **Note**: Initially, the value of the `UNNotificationExtensionCategory` key is a string, which lets your notification content app extension support only one notification type. To support multiple types, change the type to an array of strings.

For a local notification, put its category string into the [`categoryIdentifier`](https://developer.apple.com/documentation/UserNotifications/UNMutableNotificationContent/categoryIdentifier) property of your [`UNMutableNotificationContent`](https://developer.apple.com/documentation/UserNotifications/UNMutableNotificationContent) object. For a remote notification, put the string into the `category` key of your JSON payload. For information about declaring your app’s notification types, see [`Declaring your actionable notification types`](https://developer.apple.com/documentation/UserNotifications/declaring-your-actionable-notification-types).

For more information about the keys in your `Info.plist` file, see [`UNNotificationContentExtension`](unnotificationcontentextension.md).

##### Hide the Default Notification Interface

The system displays some default information with every notification, including those for which you provide a custom interface. The system always displays a header that includes the app name and icon. The system also displays an interface with the title, subtitle, and body text of the notification, but you can hide this portion of the interface if you prefer.

For example, you might hide the default notification interface if your custom interface displays the same information. The following figure illustrates the layout of the notification interface with and without the default content.

![The default interface displays a header, followed by your custom content, followed by the default system content. If you hide the default system content, only the header and your custom interface are displayed.](https://docs-assets.developer.apple.com/published/a62382090758a2f43ea487b72c5298d5/customizing_the_appearance_of_notifications-3%402x.png)

To remove the default system content, add the `UNNotificationExtensionDefaultContentHidden` key to your extension’s `Info.plist` file and set the value of the key to `true`. For more information about this key, see [`UNNotificationContentExtension`](unnotificationcontentextension.md).

##### Incorporating Media Into Your Interface

To support the playback of audio or video from your custom notifications interface, implement the following:

- In the view controller’s [`mediaPlayPauseButtonType`](unnotificationcontentextension/mediaplaypausebuttontype.md) property, return the type of button you want.
- In the view controller’s [`mediaPlayPauseButtonFrame`](unnotificationcontentextension/mediaplaypausebuttonframe.md) property, return the button’s frame.
- In the  [`mediaPlay()`](unnotificationcontentextension/mediaplay().md) method, start playing your media file.
- in the [`mediaPause()`](unnotificationcontentextension/mediapause().md) button, stop playing your media file.

The system draws a media button for you, handling all user interactions. When the buttons are pressed, it calls the [`mediaPlay()`](unnotificationcontentextension/mediaplay().md) and [`mediaPause()`](unnotificationcontentextension/mediapause().md) methods so that you can start and stop playback.

To programmatically start or stop playback of your media file, call the current [`NSExtensionContext`](https://developer.apple.com/documentation/Foundation/NSExtensionContext) object’s [`mediaPlayingStarted()`](https://developer.apple.com/documentation/Foundation/NSExtensionContext/mediaPlayingStarted()) and [`mediaPlayingPaused()`](https://developer.apple.com/documentation/Foundation/NSExtensionContext/mediaPlayingPaused()) methods. Use your view controller’s [`extensionContext`](https://developer.apple.com/documentation/UIKit/UIViewController/extensionContext) property to access the extension context.

##### Support Interactive Controls

In iOS 12 and later you can enable user interactions in your custom notifications. This lets you add interactive controls, such as buttons and switches to your custom interface.

To enable user interactions:

1. Open your Notification Content Extension’s `Info.plist` file.
2. Add the `UNNotificationExtensionUserInteractionEnabled` key to your extension attributes. Give it a Boolean value, set to `YES`.

The following figure shows the `Info.plist` file, with notifications enabled.

![A screenshot of the plist editor, showing the UNNotificationExtensionUserInteractionEnabled key added to the NSExtensionAttributes dictionary.](https://docs-assets.developer.apple.com/published/56e764232f71daec129a208c72a7d564/customizing_the_appearance_of_notifications-4%402x.png)

## See Also

- [protocol UNNotificationContentExtension](unnotificationcontentextension.md)
  An object that presents a custom interface for a delivered local or remote notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotificationsui/customizing-the-appearance-of-notifications)*