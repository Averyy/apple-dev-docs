# WKSnapshotRefreshBackgroundTask

**Framework**: Watchkit  
**Kind**: class

A background task used to update your app’s user interface in preparation for a snapshot.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKSnapshotRefreshBackgroundTask
```

## Mentions

- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))

## Overview

Using the methods of [`WKSnapshotRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask), you can push, pop, or present other interface controllers, and then update the content of the desired interface controller. The system automatically takes a snapshot of your user interface as soon as this task completes.

Don’t subclass or create instances of this class. Instead, schedule a background snapshot refresh task by calling [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](https://developer.apple.com/documentation/watchkit/wkextension/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:)). When the system triggers this task, it launches your app in the background, instantiates a [`WKSnapshotRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask) object, and passes the task object to your app delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-4vdjo) method.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

 In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

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
- [func setTaskCompleted(restoredDefaultState: Bool, estimatedSnapshotExpiration: Date?, userInfo: (any NSSecureCoding & NSObjectProtocol)?)](settaskcompleted(restoreddefaultstate:estimatedsnapshotexpiration:userinfo:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/settaskcompleted(restoreddefaultstate:estimatedsnapshotexpiration:userinfo:)))
  Marks the task as complete.
### Instance properties
- [var reasonForSnapshot: WKSnapshotReason](reasonforsnapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/reasonforsnapshot))
  The reason for taking the upcoming snapshot.
- [enum WKSnapshotReason](wksnapshotreason.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotreason))
  The reason for a background snapshot task.
- [var returnToDefaultState: Bool](returntodefaultstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/returntodefaultstate))
  A Boolean value indicating that the app should return to its default state.

## Relationships

### Inherits From
- [WKRefreshBackgroundTask](wkrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))
- [class WKApplicationRefreshBackgroundTask](wkapplicationrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask))
- [class WKURLSessionRefreshBackgroundTask](wkurlsessionrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask))
- [class WKWatchConnectivityRefreshBackgroundTask](wkwatchconnectivityrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask))
- [class WKBluetoothAlertRefreshBackgroundTask](wkbluetoothalertrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask))
- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkintentdidrunrefreshbackgroundtask))
- [class WKRelevantShortcutRefreshBackgroundTask](wkrelevantshortcutrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrelevantshortcutrefreshbackgroundtask))
- [class WKRefreshBackgroundTask](wkrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask)*