# WKWatchConnectivityRefreshBackgroundTask

**Framework**: WatchKit  
**Kind**: class

A background task used to receive background updates from the Watch Connectivity framework.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKWatchConnectivityRefreshBackgroundTask
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

#### Overview

Don’t subclass or create instances of this class. Instead, when this background watch connectivity task is triggered, the system launches your app in the background, instantiates a [`WKWatchConnectivityRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask) object, and passes the task object to your app delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-4vdjo) method.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

 In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

Background watch connectivity tasks are triggered whenever the paired device sends data using one of the following [`WCSession`](https://developer.apple.com/documentation/WatchConnectivity/WCSession) methods:

- [`updateApplicationContext(_:)`](https://developer.apple.com/documentation/WatchConnectivity/WCSession/updateApplicationContext(_:))
- [`transferUserInfo(_:)`](https://developer.apple.com/documentation/WatchConnectivity/WCSession/transferUserInfo(_:))
- [`transferCurrentComplicationUserInfo(_:)`](https://developer.apple.com/documentation/WatchConnectivity/WCSession/transferCurrentComplicationUserInfo(_:))
- [`transferFile(_:metadata:)`](https://developer.apple.com/documentation/WatchConnectivity/WCSession/transferFile(_:metadata:))

The background watch connectivity task informs you that your app is given background time. You must use your [`WCSessionDelegate`](https://developer.apple.com/documentation/WatchConnectivity/WCSessionDelegate) methods to receive this data. Because of the asynchronous nature of these tasks, defer calling your tasks’s [`setTaskCompleted()`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompleted()) method until after you’ve activated your session and received all the pending data. Use the [`hasContentPending`](https://developer.apple.com/documentation/WatchConnectivity/WCSession/hasContentPending) property to determine whether you still have any pending data.

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
  Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))
  Provide a timely, accurate snapshot of your app by using snapshot background tasks.
- [class WKApplicationRefreshBackgroundTask](wkapplicationrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask))
  A task that updates your app’s state in the background.
- [class WKURLSessionRefreshBackgroundTask](wkurlsessionrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask))
  A task that responds to background URL sessions.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask)*