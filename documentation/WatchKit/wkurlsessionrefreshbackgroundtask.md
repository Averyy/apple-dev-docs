# WKURLSessionRefreshBackgroundTask

**Framework**: WatchKit  
**Kind**: class  
**Role**: Class

A task that responds to background URL sessions.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKURLSessionRefreshBackgroundTask
```

```objc
@interface WKURLSessionRefreshBackgroundTask : WKRefreshBackgroundTask
```

## Mentions

- [Using background tasks](./using-background-tasks.md)

#### Overview

Always upload and download data using a [`URLSession`](../Foundation/urlsession.md) background transfer. Background transfers occur in a separate process and continue to transfer data even after your app terminates. Asynchronous uploads and downloads, on the other hand, suspend with your app. Because watchOS apps have a short runtime, you can’t guarantee that an asynchronous transfer finishes before the app suspends. For more information on background transfers, see [Downloading files in the background](../Foundation/downloading-files-in-the-background.md).

Schedule a background URL session to download an item as shown below.

```swift
// Create a background session configuration.
let config = URLSessionConfiguration.background(withIdentifier: myRequestID)
config.isDiscretionary = true
config.sessionSendsLaunchEvents = true

// Create the background download task and schedule it to run in 15 minutes.
let urlSession = URLSession(configuration: config,
                            delegate: self,
                            delegateQueue: nil)


let backgroundTask = urlSession.downloadTask(with: url)
backgroundTask.earliestBeginDate = Date().addingTimeInterval(15 * 60)

// Run the task.
backgroundTask.resume()
```

If your app has a complication on the active watch face, it can receive up to four [`WKURLSessionRefreshBackgroundTask`](./wkurlsessionrefreshbackgroundtask.md) tasks per hour. To avoid throttling, use the [`earliestBeginDate`](../Foundation/urlsessiontask/earliestbegindate.md) property to schedule background URL session tasks no closer than 15 minutes apart.

Don’t subclass or create instances of this class. Instead, the system instantiates a [`WKURLSessionRefreshBackgroundTask`](./wkurlsessionrefreshbackgroundtask.md) object and passes the task object to your extension delegate’s [`handle(_:)`](./wkapplicationdelegate/handle%28_%29-4vdjo.md) method in response to [`URLSession`](../Foundation/urlsession.md) events. Defer calling the background [`URLSession`](../Foundation/urlsession.md) task’s `setTaskCompleted()` method until all the delegate method calls finish processing.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](../SwiftUI/scene/backgroundtask%28_,action%29.md).

The system creates a background [`URLSession`](../Foundation/urlsession.md) task when any of the following events occur:

- The server requires authentication to complete a background transfer.
- All background transfers associated with a session identifier complete (either successfully or unsuccessfully).

To get more information about the transfer, create a background configuration object with the same session identifier. Next, create a session object using the configuration object and a session delegate. The system automatically associates the new session with the transfer and calls the appropriate delegate methods.

## Topics

### Accessing background task data
- [var sessionIdentifier: String](./wkurlsessionrefreshbackgroundtask/sessionidentifier.md)
  The identifier for the triggering background transfer.

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
- [class WKRefreshBackgroundTask](./wkrefreshbackgroundtask.md)
  The abstract superclass for WatchKit’s background task classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask)*