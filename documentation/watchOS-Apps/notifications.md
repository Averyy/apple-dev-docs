# Notifications

**Framework**: watchOS apps

Communicate with users even when your app isn’t running.

#### Overview

Notifications play an integral role in watchOS app design. Apple Watch is ideally suited for short, personal interactions, but you can use notifications to string together longer workflows, for instance to convey a series of short steps. An app for ordering coffee might let users place an order with just a few taps, then drop their wrist and allow the app to finish the transaction on its own. The coffee-ordering app could alert the user with a notification when their order is ready, or notify them if an error occurs.

Apple Watch and iPhone also work together to automatically forward notifications sent to your iOS app to a paired Apple Watch, even if you don’t have a watchOS app; however, you can improve the user experience on Apple Watch by customizing the notifications in your watchOS app.

A watchOS app can customize notifications to:

- Respond to the delivery of local or remote notifications.
- Add support for actionable notifications.
- Provide custom long-look interfaces for notifications.
- Enable interactive long-look notification interfaces.
- Schedule local notifications directly from your watch.
- Receive remote notifications directly from your server.
- Receive background notifications from your server.

For more information, see [`User Notifications`](https://developer.apple.com/documentation/UserNotifications)

## Topics

### Essentials
- [Enabling and receiving notifications](enabling-and-receiving-notifications.md)
  Set up and handle local and remote notifications.
- [Presenting notifications on Apple Watch](presenting-notifications-on-apple-watch.md)
  Understand how the system displays incoming notifications.
### Customizing the user experience
- [Taking advantage of notification forwarding](taking-advantage-of-notification-forwarding.md)
  Deliver notifications to the user’s iPhone or Apple Watch.
- [Customizing your long-look interface](customizing-your-long-look-interface.md)
  Create custom interfaces for your watchOS app’s notifications.
- [Adding actions to notifications on watchOS](adding-actions-to-notifications-on-watchos.md)
  Provide a set of responses to a notification.
- [Grouping notifications](grouping-notifications.md)
  Organize notifications into threads.
### Testing notifications
- [Testing custom notification interfaces](testing-custom-notification-interfaces.md)
  Test your notification interfaces on watchOS using a notification scheme and payload file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/notifications)*