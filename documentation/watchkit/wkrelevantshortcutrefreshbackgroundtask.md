# WKRelevantShortcutRefreshBackgroundTask

**Framework**: Watchkit  
**Kind**: class

A background task used to periodically donate relevant Siri shortcuts.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class WKRelevantShortcutRefreshBackgroundTask
```

#### Overview

Relevant shortcut refresh tasks provide background execution time for your app to update its relevant shortcuts. This task lets your app provide up-to-date, glanceable data, without requiring the user to tap the shortcut or launch your app. Use this task to check if your data is updated. If it is, supply new relevant shortcuts as needed.

Don’t subclass or create instances of this class. Instead, the system instantiates a [`WKRelevantShortcutRefreshBackgroundTask`](wkrelevantshortcutrefreshbackgroundtask.md) object and passes the task object to your app delegate’s [`handle(_:)`](wkapplicationdelegate/handle(_:)-4vdjo.md) method.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

The system automatically schedules relevant shortcut refresh tasks based on the user’s engagement with your app’s shortcuts. The more the user glances at or interacts with the shortcuts, the more often the system gives your app a relevant shortcut refresh task.

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
- [class WKSnapshotRefreshBackgroundTask](wksnapshotrefreshbackgroundtask.md)
  A background task used to update your app’s user interface in preparation for a snapshot.
- [class WKRefreshBackgroundTask](wkrefreshbackgroundtask.md)
  The abstract superclass for WatchKit’s background task classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WatchKit/wkrelevantshortcutrefreshbackgroundtask)*