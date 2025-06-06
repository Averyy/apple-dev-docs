# WKApplicationRefreshBackgroundTask

**Framework**: Watchkit  
**Kind**: class

A task that updates your app’s state in the background.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKApplicationRefreshBackgroundTask
```

## Mentions

- [Using background tasks](using-background-tasks.md)

#### Overview

Don’t subclass or create instances of this class. Instead, schedule a background app refresh task by calling [`scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md). When the system triggers the background task, it launches your app in the background, instantiates a [`WKApplicationRefreshBackgroundTask`](wkapplicationrefreshbackgroundtask.md) object, and passes the task object to your app delegate’s [`handle(_:)`](wkextensiondelegate/handle(_:)-92ulv.md) method.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

The system budgets the number of background refresh tasks available to an app. In general, the system performs approximately four tasks per hour for each app with a complication on the active watch face. All the complications on the current watch face share this budget. After you exhaust the budget, the system delays your requests until more time becomes available.

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

## See Also

- [Using background tasks](using-background-tasks.md)
  Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md)
  Provide a timely, accurate snapshot of your app by using snapshot background tasks.
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

*[View on Apple Developer](https://developer.apple.com/documentation/WatchKit/wkapplicationrefreshbackgroundtask)*