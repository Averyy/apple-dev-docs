# Enabling and receiving notifications

**Framework**: Watchos Apps

Set up and handle local and remote notifications.

#### Overview

You have a variety of options when sending notifications to a watchOS app:

- Schedule local notifications directly in your watchOS app, specifying a time or location to trigger the notification’s delivery.
- Send remote notifications, including background updates, from your server to the user’s Apple Watch using the Apple Push Notification Service (APNs).
- Schedule local or send remote notifications to the iOS companion app (if one exists), and let the system forward the notifications to the user’s Apple Watch. For more information, see [`Taking advantage of notification forwarding`](taking-advantage-of-notification-forwarding.md).

In your watchOS app, schedule local notifications and handle both local and remote notifications using the [`User Notifications`](https://developer.apple.com/documentation/UserNotifications) framework.

##### Request Notifications

Before the system can post alerts or play sounds for your app’s notifications, your watchOS app or iOS app must request authorization to interact with the user.

To request authorization:

1. Access the shared [`UNUserNotificationCenter`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter) object by calling the [`current()`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter/current()) class method.
2. Call the notification center’s [`requestAuthorization(options:completionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter/requestAuthorization(options:completionHandler:)) method. You must call this method before performing any operations that involve local or remote notifications.

For example, you might call [`requestAuthorization(options:completionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenter/requestAuthorization(options:completionHandler:)) during your app’s launch cycle.

If you explicitly request permission, the first time the user launches your app, this method prompts them to grant authorization. After the user responds to this prompt, subsequent launches won’t prompt them again. However, users can always change their authorization in the Settings app.

If you request provisional authorization, the system doesn’t prompt the user for permission to recieve notifications. Instead, the system delivers provisional notifications quietly — the notifications don’t interrupt the user with a sound or banner, or appear on the lock screen. Instead, they only appear in the notification center’s history. The notifications also include buttons, prompting the user to either keep or turn off the notification. The user can then choose whether to receive the notifications after seeing one.

For detailed instructions, see [`Asking permission to use notifications`](https://developer.apple.com/documentation/UserNotifications/asking-permission-to-use-notifications).

##### Handle Notifications in Your App

If your watchOS app is running on screen, or is the frontmost app when a notification arrives, the system calls the [`userNotificationCenter(_:willPresent:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:willPresent:withCompletionHandler:)) method on your notification center delegate. The value you pass to the completion handler determines how the system responds. Pass [`UNNotificationPresentationOptionNone`](https://developer.apple.com/documentation/UserNotifications/UNNotificationPresentationOptionNone) to silence the notification. Otherwise, the system presents the notification using the specified options.

> **Note**: If you don’t implement the [`userNotificationCenter(_:willPresent:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:willPresent:withCompletionHandler:)) method, the system silences the notification and doesn’t deliver it to your watchOS app.

If you don’t implement the [`userNotificationCenter(_:willPresent:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:willPresent:withCompletionHandler:)) method, the system silences the notification and doesn’t deliver it to your watchOS app.

##### Send Notifications Directly to Apple Watch

With watchOS 6 and later, you can send remote notifications directly to Apple Watch. Before sending a notification, you must register your watchOS app, as described in [`Registering your app with APNs`](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns). Registering your app creates a unique device token for the watch. Use that token to send notifications directly to the watch.

The recommended notification strategy depends on your watchOS app, as shown in the table below.

| Type of app | Notification strategy |
| --- | --- |
| Apple Watch-only app | Always send remote notifications to Apple Watch. |
| Independent watchOS app with an iOS app | Because the app may not be installed on both devices, you should always send the notification to both iPhone and Apple Watch. The system ensures that the user only receives one notification at the best destination. |
| Dependent watchOS app with an iOS app | You can either send the notification just to iPhone, or send it to both devices. In either case, the system ensures that the user only receives one notification at the best destination. |

For more information on watchOS app types, see [`Creating independent watchOS apps`](creating-independent-watchos-apps.md).

## See Also

- [Presenting notifications on Apple Watch](presenting-notifications-on-apple-watch.md)
  Understand how the system displays incoming notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/enabling-and-receiving-notifications)*