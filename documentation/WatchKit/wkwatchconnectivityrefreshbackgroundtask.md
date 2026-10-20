# WKWatchConnectivityRefreshBackgroundTask

**Framework**: WatchKit  
**Kind**: class  
**Role**: Class

A background task used to receive background updates from the Watch Connectivity framework.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKWatchConnectivityRefreshBackgroundTask
```

```objc
@interface WKWatchConnectivityRefreshBackgroundTask : WKRefreshBackgroundTask
```

## Mentions

- [Using background tasks](./using-background-tasks.md)

#### Overview

Don’t subclass or create instances of this class. Instead, when this background watch connectivity task is triggered, the system launches your app in the background, instantiates a [`WKWatchConnectivityRefreshBackgroundTask`](./wkwatchconnectivityrefreshbackgroundtask.md) object, and passes the task object to your app delegate’s [`handle(_:)`](./wkapplicationdelegate/handle%28_%29-4vdjo.md) method.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](../SwiftUI/scene/backgroundtask%28_,action%29.md).

Background watch connectivity tasks are triggered whenever the paired device sends data using one of the following [`WCSession`](../WatchConnectivity/wcsession.md) methods:

- [`updateApplicationContext(_:)`](../WatchConnectivity/wcsession/updateapplicationcontext%28_%29.md)
- [`transferUserInfo(_:)`](../WatchConnectivity/wcsession/transferuserinfo%28_%29.md)
- [`transferCurrentComplicationUserInfo(_:)`](../WatchConnectivity/wcsession/transfercurrentcomplicationuserinfo%28_%29.md)
- [`transferFile(_:metadata:)`](../WatchConnectivity/wcsession/transferfile%28_,metadata%29.md)

The background watch connectivity task informs you that your app is given background time. You must use your [`WCSessionDelegate`](../WatchConnectivity/wcsessiondelegate.md) methods to receive this data. Because of the asynchronous nature of these tasks, defer calling your tasks’s [`setTaskCompleted()`](./wkrefreshbackgroundtask/settaskcompleted%28%29.md) method until after you’ve activated your session and received all the pending data. Use the [`hasContentPending`](../WatchConnectivity/wcsession/hascontentpending.md) property to determine whether you still have any pending data.

## Relationships

### Inherits From
- [WKRefreshBackgroundTask](./wkrefreshbackgroundtask.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Background tasks
- [Using background tasks](./using-background-tasks.md)
  Handle scheduled update tasks in the background, and respond to background system interactions including Siri intents and incoming Bluetooth messages.
- [Preparing to take your watchOS app’s snapshot](./preparing-to-take-your-watchos-app-s-snapshot.md)
  Provide a timely, accurate snapshot of your app by using snapshot background tasks.
- [class WKApplicationRefreshBackgroundTask](./wkapplicationrefreshbackgroundtask.md)
  A task that updates your app’s state in the background.
- [class WKURLSessionRefreshBackgroundTask](./wkurlsessionrefreshbackgroundtask.md)
  A task that responds to background URL sessions.
- [class WKBluetoothAlertRefreshBackgroundTask](./wkbluetoothalertrefreshbackgroundtask.md)
  A task for handling timely Bluetooth alerts in the background.
- [class WKIntentDidRunRefreshBackgroundTask](./wkintentdidrunrefreshbackgroundtask.md)
  A background task used to update your app after a SiriKit intent runs.
- [class WKRelevantShortcutRefreshBackgroundTask](./wkrelevantshortcutrefreshbackgroundtask.md)
  A background task used to periodically donate relevant Siri shortcuts.
- [class WKSnapshotRefreshBackgroundTask](./wksnapshotrefreshbackgroundtask.md)
  A background task used to update your app’s user interface in preparation for a snapshot.
- [class WKRefreshBackgroundTask](./wkrefreshbackgroundtask.md)
  The abstract superclass for WatchKit’s background task classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask)*