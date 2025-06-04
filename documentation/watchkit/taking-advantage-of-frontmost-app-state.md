# Taking Advantage of Frontmost App State

**Framework**: Watchkit

Understand the frontmost app state, and the features it provides to your app.

## Overview

Apps running in watchOS quickly become inactive when the user stops interacting with the watch or lowers their wrist. On Apple Watch SE and Apple Watch Series 4 and earlier, the screen turns off when the app becomes inactive. On Apple Watch Series 5 and later, the system blurs the app’s user interface and displays the time over it.

Whether the screen is off or blurred, the app transitions to an inactive state. Its user interface is no longer shown, and it doesn’t receive actions from controls or gestures. However, the app is still in the foreground, and may respond to other events.

An app in this extended, inactive state is the frontmost app. The system can have at most one frontmost app at a time. When the user raises their wrist, the system automatically activates and displays the frontmost app. The frontmost app can perform the following tasks:

- Play haptic feedback.
- Receive notifications.
- Respond immediately to the completion of a background transfer from a task or Watch Connectivity session.
- Receive up to four background app refresh tasks per hour—similar to an app with a complication on the active watch face.

For example, when the frontmost app receives a notification, the system calls your notification delegate’s [`userNotificationCenter(_:willPresent:withCompletionHandler:)`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate/userNotificationCenter(_:willPresent:withCompletionHandler:)) method, rather than displaying the notification alert. Your app can then respond by playing a haptic feedback or custom sound, and updating the user interface.

> **Note**:  If the user explicitly closes the app by pressing the digital crown or covering the screen, the app doesn’t become the frontmost app and doesn’t remain in the inactive state, but transitions quickly to the background instead.

 If the user explicitly closes the app by pressing the digital crown or covering the screen, the app doesn’t become the frontmost app and doesn’t remain in the inactive state, but transitions quickly to the background instead.

By default, the frontmost app remains in the foreground for two minutes before transitioning to the background and then becoming suspended. If the user dismisses the app (for example, by pressing the crown or by covering the screen), the app transitions immediately to the background, and doesn’t become the frontmost app.

Users can configure how long apps remain as the frontmost app using Settings > General > Wake Screen. The Return to Clock setting sets the default duration for all apps.

Users can also set a custom duration for a specific app by scrolling down to the list of apps and selecting the app to customize.

> **Note**:  In watchOS 6 and earlier, apps could request additional frontmost app time by setting the extension’s [`isFrontmostTimeoutExtended`](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended) property to [`true`](https://developer.apple.com/documentation/swift/true); however, starting with watchOS 7, the user controls the duration of an app’s frontmost state.

 In watchOS 6 and earlier, apps could request additional frontmost app time by setting the extension’s [`isFrontmostTimeoutExtended`](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended) property to [`true`](https://developer.apple.com/documentation/swift/true); however, starting with watchOS 7, the user controls the duration of an app’s frontmost state.

Workout, location, background audio, and audio-recording apps appear to behave similarly to the frontmost app. However, these apps continue to run in the background throughout the entire workout, location, or audio session. If the user navigates to the watch face during a session, the system displays a glyph at the top of the watch face. If the user taps the glyph, the associated app resumes running in the foreground. For more information, see [`HKWorkoutSession`](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession).

## See Also

- [Handling Common State Transitions](handling-common-state-transitions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions))
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [Handling User Activity](handling-user-activity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-user-activity))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/taking-advantage-of-frontmost-app-state)*