# Preparing to take your watchOS app’s snapshot

**Framework**: Watchkit

Provide a timely, accurate snapshot of your app by using snapshot background tasks.

#### Overview

To provide a placeholder image for your app, watchOS periodically takes snapshots of your app’s user interface. Keeping your app’s snapshot up to date helps produce apps that feel responsive and current. The system uses snapshots in two ways:

- To represent your app in the dock
- As your app’s launch image

The system displays the dock when the user presses the watch’s side button. By default, the dock contains the 10 most-recently used apps, but users can configure the dock to always contain certain apps. If the user lets the dock settle on an app for a moment, the system replaces the snapshot with a running instance of the app. watchOS tries to keep these apps in memory so they can resume quickly. These apps also receive priority for background tasks, helping you keep their content up to date.

When you launch an app, watchOS initially displays the latest snapshot for your app. As soon as the app is active, watchOS replaces the snapshot with the app’s live user interface.

##### Schedule Snapshots

The system automatically schedules snapshots for your app after significant state changes, for example when the app transitions from the foreground to the background, whenever the user interacts with the app’s complications or notifications, and one hour after the last user interaction. Your app can also invalidate its current snapshot and schedule a background snapshot refresh tasks by calling your extension’s [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](wkapplication/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) method.

When using [`WKRefreshBackgroundTask`](wkrefreshbackgroundtask.md) tasks, you can request a new snapshot whenever another background task ends, by calling [`setTaskCompletedWithSnapshot(_:)`](wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:).md) and passing [`true`](https://developer.apple.com/documentation/swift/true). If your app uses the SwiftUI [`BackgroundTask`](https://developer.apple.com/documentation/SwiftUI/BackgroundTask) tasks, the system automatically detects any changes to the user interface and schedules the snapshot task.

The system budgets the number of snapshots you can take per hour. For apps in the dock, you can safely request one snapshot per hour. For apps with an active complication, you can request up to four per hour. If you exceed the available budget, the system may delay your request until additional background execution time is available.

##### Respond to Snapshot Background Tasks

To take a snapshot, the system resumes running your app in the background. It then executes your background task handler. If you’re using SwiftUI [`BackgroundTask`](https://developer.apple.com/documentation/SwiftUI/BackgroundTask) tasks, you can respond using a [`snapshot`](https://developer.apple.com/documentation/SwiftUI/BackgroundTask/snapshot) task. The closure must return a [`SnapshotResponse`](https://developer.apple.com/documentation/SwiftUI/SnapshotResponse). Use the constructor’s `estimatedSnapshotExpieration:` parameter to set the preferred date and time for the next background snapshot refresh task. You can use [`distantFuture`](https://developer.apple.com/documentation/foundation/nsdate/1415385-distantfuture) if you don’t want to schedule the next refresh.

```swift
.backgroundTask(.snapshot) { snapshotData in
    // Update your UI for the snapshot.

    return SnapshotResponse(estimatedSnapshotExpiration: .distantFuture)
}
```

For [`WKSnapshotRefreshBackgroundTask`](wksnapshotrefreshbackgroundtask.md) tasks, the system calls your app delegate’s [`handle(_:)`](wkapplicationdelegate/handle(_:)-4vdjo.md) method and passes an [`WKSnapshotRefreshBackgroundTask`](wksnapshotrefreshbackgroundtask.md) instance.

Use this task to update your user interface before the system takes a snapshot. You can push, pop, or present other interface controllers, and then update the content of the desired interface controller. The system automatically takes a snapshot of your user interface as soon as this task completes.

## See Also

- [Using background tasks](using-background-tasks.md)
  Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.
- [class WKApplicationRefreshBackgroundTask](wkapplicationrefreshbackgroundtask.md)
  A task that updates your app’s state in the background.
- [class WKURLSessionRefreshBackgroundTask](wkurlsessionrefreshbackgroundtask.md)
  A task that responds to background URL sessions.
- [class WKWatchConnectivityRefreshBackgroundTask](wkwatchconnectivityrefreshbackgroundtask.md)
  A background task used to receive background updates from the Watch Connectivity framework.
- [class WKBluetoothAlertRefreshBackgroundTask](wkbluetoothalertrefreshbackgroundtask.md)
  A task for handling timely Bluetooth alerts in the background.
- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md)
  A background task used to update your app after a SiriKit intent runs.
- [class WKRelevantShortcutRefreshBackgroundTask](wkrelevantshortcutrefreshbackgroundtask.md)
  A background task used to periodically donate relevant Siri shortcuts.
- [class WKSnapshotRefreshBackgroundTask](wksnapshotrefreshbackgroundtask.md)
  A background task used to update your app’s user interface in preparation for a snapshot.
- [class WKRefreshBackgroundTask](wkrefreshbackgroundtask.md)
  The abstract superclass for WatchKit’s background task classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot)*