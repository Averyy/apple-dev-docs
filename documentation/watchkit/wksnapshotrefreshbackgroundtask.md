# WKSnapshotRefreshBackgroundTask

**Framework**: WatchKit  
**Kind**: class

A background task used to update your app’s user interface in preparation for a snapshot.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKSnapshotRefreshBackgroundTask
```

## Mentions

- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md)

#### Overview

Using the methods of [`WKSnapshotRefreshBackgroundTask`](wksnapshotrefreshbackgroundtask.md), you can push, pop, or present other interface controllers, and then update the content of the desired interface controller. The system automatically takes a snapshot of your user interface as soon as this task completes.

Don’t subclass or create instances of this class. Instead, schedule a background snapshot refresh task by calling [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](wkextension/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:).md). When the system triggers this task, it launches your app in the background, instantiates a [`WKSnapshotRefreshBackgroundTask`](wksnapshotrefreshbackgroundtask.md) object, and passes the task object to your app delegate’s [`handle(_:)`](wkapplicationdelegate/handle(_:)-4vdjo.md) method.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

Background snapshot tasks are budgeted. In general, the system performs approximately one task per hour for each app in the dock (including the most recently used app). This budget is shared among all apps on the dock. The system performs multiple tasks an hour for each app with a complication on the active watch face. This budget is shared among all complications on the watch face. After you exhaust the budget, the system delays your requests until more time becomes available.

The system automatically schedules background snapshot request tasks when:

- Your device starts up
- Your app updates the complication timeline
- The user interacts with one of the apps notifications
- The app transitions from the foreground to the background
- One hour passes after the user’s last interaction with the app, then the `returnToGlanceableUI` property is set to [`true`](https://developer.apple.com/documentation/swift/true)

These requests don’t cancel or replace any of your scheduled requests.

## Topics

### Completing the background task
- [func setTaskCompleted(restoredDefaultState: Bool, estimatedSnapshotExpiration: Date?, userInfo: (any NSSecureCoding & NSObjectProtocol)?)](wksnapshotrefreshbackgroundtask/settaskcompleted(restoreddefaultstate:estimatedsnapshotexpiration:userinfo:).md)
  Marks the task as complete.
### Instance properties
- [var reasonForSnapshot: WKSnapshotReason](wksnapshotrefreshbackgroundtask/reasonforsnapshot.md)
  The reason for taking the upcoming snapshot.
- [enum WKSnapshotReason](wksnapshotreason.md)
  The reason for a background snapshot task.
- [var returnToDefaultState: Bool](wksnapshotrefreshbackgroundtask/returntodefaultstate.md)
  A Boolean value indicating that the app should return to its default state.

## Relationships

### Inherits From
- [WKRefreshBackgroundTask](wkrefreshbackgroundtask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Using background tasks](using-background-tasks.md)
  Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md)
  Provide a timely, accurate snapshot of your app by using snapshot background tasks.
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
- [class WKRefreshBackgroundTask](wkrefreshbackgroundtask.md)
  The abstract superclass for WatchKit’s background task classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask)*