# Background execution

**Framework**: WatchKit

Manage background sessions and tasks.

#### Overview

Apps on watchOS primarily run in the foreground to limit the impact on system resources. However, sometimes an app needs to perform an action when it’s not the foreground app. For a limited number of cases, watchOS provides options for running in the background.

##### Handle Background Notifications

When the system launches your app in the background, you can:

- Handle background notifications from local or remote notifications with a [`UNUserNotificationCenterDelegate`](https://developer.apple.com/documentation/UserNotifications/UNUserNotificationCenterDelegate) delegate. For more information, see [`Handling notifications and notification-related actions`](https://developer.apple.com/documentation/UserNotifications/handling-notifications-and-notification-related-actions).
- Receive push notifications to update your app’s complications with a [`PKPushRegistryDelegate`](https://developer.apple.com/documentation/PushKit/PKPushRegistryDelegate) delegate. For more information, see [`PushKit`](https://developer.apple.com/documentation/PushKit).

##### Schedule and Handle Background Refresh Tasks

A watchOS app uses a  to perform work in the background. If your app requires background operations, use one of the following techniques to respond to the task:

- Add a [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)) modifier to respond to the background task in your SwiftUI scene.
- Implement your app delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-4vdjo) method to receive and respond to the task. You need to call the task’s [`setTaskCompletedWithSnapshot(_:)`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)) method to indicate that you’re done.

In both cases, the system launches your app and gives it a few seconds of background execution time to perform the task. Complete the background task as quickly as possible. For more information, see [`Using background tasks`](https://developer.apple.com/documentation/watchkit/using-background-tasks).

##### Start Background Sessions

Apps that support workouts, audio playback, or location updates can continue to run in the background until the current session ends. Your app must enable the appropriate background mode in your project’s capabilities, and then start the session while your app is running in the foreground.

- Use an [`HKWorkoutSession`](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession) object to start and stop workouts. For more information, see [`Running workout sessions`](https://developer.apple.com/documentation/HealthKit/running-workout-sessions).
- Use the [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) class to play extended audio files in the background. For more information, see [`Playing Background Audio`](https://developer.apple.com/documentation/watchkit/playing-background-audio).
- Use a [`CLLocationManager`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager) object to start a continuous background location session. For more information, see [`allowsBackgroundLocationUpdates`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/allowsBackgroundLocationUpdates).

##### Set Up Extended Runtime Sessions

Extended runtime sessions give your app additional time to run while the session is active. Extended runtime sessions provide support for the following session types:

- Self care
- Mindfulness
- Physical therapy
- Smart alarm

Extended runtime sessions let the app continue to communicate with a Bluetooth device, process data, or play sounds or haptics, even after the watch’s screen turns off. While most extended runtime sessions run your app as the frontmost app, some sessions run your app in the background. Select a session type based on the app’s intended use — not based on the features that the session provides.

For more information, see [`Using extended runtime sessions`](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions).

## Topics

### Background tasks
- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))
  Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))
  Provide a timely, accurate snapshot of your app by using snapshot background tasks.
- [class WKApplicationRefreshBackgroundTask](wkapplicationrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask))
  A task that updates your app’s state in the background.
- [class WKURLSessionRefreshBackgroundTask](wkurlsessionrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask))
  A task that responds to background URL sessions.
- [class WKWatchConnectivityRefreshBackgroundTask](wkwatchconnectivityrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask))
  A background task used to receive background updates from the Watch Connectivity framework.
- [class WKBluetoothAlertRefreshBackgroundTask](wkbluetoothalertrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask))
  A task for handling timely Bluetooth alerts in the background.
- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkintentdidrunrefreshbackgroundtask))
  A background task used to update your app after a SiriKit intent runs.
- [class WKRelevantShortcutRefreshBackgroundTask](wkrelevantshortcutrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrelevantshortcutrefreshbackgroundtask))
  A background task used to periodically donate relevant Siri shortcuts.
- [class WKSnapshotRefreshBackgroundTask](wksnapshotrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask))
  A background task used to update your app’s user interface in preparation for a snapshot.
- [class WKRefreshBackgroundTask](wkrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask))
  The abstract superclass for WatchKit’s background task classes.
### Background sessions
- [Enabling Background Sessions](enabling-background-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/enabling-background-sessions))
  Enable the background mode for audio, location updates, remote notifications, or workouts.
- [Playing Background Audio](playing-background-audio.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/playing-background-audio))
  Enable background audio in your app to provide a seamless playback experience.
- WKBackgroundModes ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKBackgroundModes))
  The services a watchOS app provides that require it to continue running in the background.
- UIBackgroundModes ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes))
  Services provided by an app that require it to run in the background.

## See Also

- [Life cycles](life-cycles.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/life-cycles))
  Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))
  Create an extended runtime session that continues running your app after the user stops interacting with it.
- [class WKExtendedRuntimeSession](wkextendedruntimesession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession))
  A session that continues to run your app after the user has stopped interacting.
- [Interacting with Bluetooth peripherals during background app refresh](interacting-with-bluetooth-peripherals-during-background-app-refresh.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh))
  Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/background-execution)*