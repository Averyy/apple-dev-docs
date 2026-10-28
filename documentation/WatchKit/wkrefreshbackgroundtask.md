# WKRefreshBackgroundTask

**Framework**: WatchKit  
**Kind**: class  
**Role**: Class

The abstract superclass for WatchKit’s background task classes.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKRefreshBackgroundTask
```

```objc
@interface WKRefreshBackgroundTask : NSObject
```

## Mentions

- [Preparing to take your watchOS app’s snapshot](./preparing-to-take-your-watchos-app-s-snapshot.md)
- [Using background tasks](./using-background-tasks.md)

## Overview

Don’t subclass or create instances of this class. The system automatically creates an appropriate background task object whenever it triggers a background task. This object is passed to your app delegate’s [`handle(_:)`](./wkapplicationdelegate/handle%28_%29-4vdjo.md) method. Use the provided background task object to identify and manage the background task.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, see [`backgroundTask(_:action:)`](../SwiftUI/scene/backgroundtask%28_,action%29.md).

## Topics

### Accessing background task data
- [var userInfo: (any NSSecureCoding & NSObjectProtocol)?](./wkrefreshbackgroundtask/userinfo.md)
  Custom information associated with the background task.
### Completing the background task
- [var expirationHandler: (() -> Void)?](./wkrefreshbackgroundtask/expirationhandler.md)
  A block that the system calls when the available runtime for a background task is about to expire.
- [func setTaskCompletedWithSnapshot(Bool)](./wkrefreshbackgroundtask/settaskcompletedwithsnapshot%28_%29.md)
  Marks the task as complete and indicates whether the system should take a new snapshot of the app.
- [func setTaskCompleted()](./wkrefreshbackgroundtask/settaskcompleted%28%29.md)
  Marks the task as complete.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [WKApplicationRefreshBackgroundTask](./wkapplicationrefreshbackgroundtask.md)
- [WKBluetoothAlertRefreshBackgroundTask](./wkbluetoothalertrefreshbackgroundtask.md)
- [WKIntentDidRunRefreshBackgroundTask](./wkintentdidrunrefreshbackgroundtask.md)
- [WKRelevantShortcutRefreshBackgroundTask](./wkrelevantshortcutrefreshbackgroundtask.md)
- [WKSnapshotRefreshBackgroundTask](./wksnapshotrefreshbackgroundtask.md)
- [WKURLSessionRefreshBackgroundTask](./wkurlsessionrefreshbackgroundtask.md)
- [WKWatchConnectivityRefreshBackgroundTask](./wkwatchconnectivityrefreshbackgroundtask.md)
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
- [class WKWatchConnectivityRefreshBackgroundTask](./wkwatchconnectivityrefreshbackgroundtask.md)
  A background task used to receive background updates from the Watch Connectivity framework.
- [class WKBluetoothAlertRefreshBackgroundTask](./wkbluetoothalertrefreshbackgroundtask.md)
  A task for handling timely Bluetooth alerts in the background.
- [class WKIntentDidRunRefreshBackgroundTask](./wkintentdidrunrefreshbackgroundtask.md)
  A background task used to update your app after a SiriKit intent runs.
- [class WKRelevantShortcutRefreshBackgroundTask](./wkrelevantshortcutrefreshbackgroundtask.md)
  A background task used to periodically donate relevant Siri shortcuts.
- [class WKSnapshotRefreshBackgroundTask](./wksnapshotrefreshbackgroundtask.md)
  A background task used to update your app’s user interface in preparation for a snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask)*