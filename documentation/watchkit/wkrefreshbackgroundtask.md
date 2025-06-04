# WKRefreshBackgroundTask

**Framework**: WatchKit  
**Kind**: class

The abstract superclass for WatchKit’s background task classes.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKRefreshBackgroundTask
```

## Mentions

- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))
- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

#### Overview

Don’t subclass or create instances of this class. The system automatically creates an appropriate background task object whenever it triggers a background task. This object is passed to your app delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-4vdjo) method. Use the provided background task object to identify and manage the background task.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, see [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

 In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, see [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

## Topics

### Accessing background task data
- [var userInfo: (any NSSecureCoding & NSObjectProtocol)?](userinfo.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/userinfo))
  Custom information associated with the background task.
### Completing the background task
- [var expirationHandler: (() -> Void)?](expirationhandler.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/expirationhandler))
  A block that the system calls when the available runtime for a background task is about to expire.
- [func setTaskCompletedWithSnapshot(Bool)](settaskcompletedwithsnapshot(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)))
  Marks the task as complete and indicates whether the system should take a new snapshot of the app.
- [func setTaskCompleted()](settaskcompleted().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompleted()))
  Marks the task as complete.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Inherited By
- [WKApplicationRefreshBackgroundTask](wkapplicationrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask))
- [WKBluetoothAlertRefreshBackgroundTask](wkbluetoothalertrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask))
- [WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkintentdidrunrefreshbackgroundtask))
- [WKRelevantShortcutRefreshBackgroundTask](wkrelevantshortcutrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrelevantshortcutrefreshbackgroundtask))
- [WKSnapshotRefreshBackgroundTask](wksnapshotrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask))
- [WKURLSessionRefreshBackgroundTask](wkurlsessionrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask))
- [WKWatchConnectivityRefreshBackgroundTask](wkwatchconnectivityrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask))
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask)*