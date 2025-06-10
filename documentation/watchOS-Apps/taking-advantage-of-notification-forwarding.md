# Taking advantage of notification forwarding

**Framework**: watchOS apps

Deliver notifications to the user’s iPhone or Apple Watch.

#### Overview

Apple Watch and iPhone work together to deliver notifications. Instead of appearing on both devices, notifications appear only on the device that’s most likely to have the user’s current focus.

##### Forward Notifications

The system decides which device receives the notification based on the notification’s type, the process that created the notification, and the currently active device.

| Notification type | Source | Destination |
| --- | --- | --- |
| Local | iOS app | Apple Watch or iPhone, depending on the locked/unlocked state of both devices. |
| Local | watchOS app | Apple Watch-only. |
| Remote | Your server | If you send a remote notification to iPhone, it can appear on either Apple Watch or iPhone, depending on the locked/unlocked state of both devices. With watchOS 6 and later, you can also send notifications directly to Apple Watch. These notifications only appear on Apple Watch. |
| Background | Your server | If you send a background notification to iPhone, the phone always handles the notification. It never forwards background notifications to Apple Watch; however, with watchOS 6 and later you can also send background notifications directly to Apple Watch. |

If a notification can be delivered to either device, the system uses the devices’ locked state to determine the best destination.

The system applies the following rules, in the order listed:

1. If the user’s iPhone is unlocked and the screen is on, notifications go to the phone.
2. Otherwise, if the Apple Watch is on the user’s wrist and unlocked, notifications go to the watch.
3. Otherwise, notifications default back to iPhone.

Also, if the user has more than one Apple Watch, local notifications only appear on the device that scheduled it. Remote and background notifications also only appear at the specified watch — so you may need to send notifications to multiple devices.

## See Also

- [Customizing your long-look interface](customizing-your-long-look-interface.md)
  Create custom interfaces for your watchOS app’s notifications.
- [Adding actions to notifications on watchOS](adding-actions-to-notifications-on-watchos.md)
  Provide a set of responses to a notification.
- [Grouping notifications](grouping-notifications.md)
  Organize notifications into threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/taking-advantage-of-notification-forwarding)*