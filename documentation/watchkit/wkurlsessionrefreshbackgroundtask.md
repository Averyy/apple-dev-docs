# WKURLSessionRefreshBackgroundTask

**Framework**: Watchkit  
**Kind**: class

A task that responds to background URL sessions.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKURLSessionRefreshBackgroundTask
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

## Overview

Always upload and download data using a [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) background transfer. Background transfers occur in a separate process and continue to transfer data even after your app terminates. Asynchronous uploads and downloads, on the other hand, suspend with your app. Because watchOS apps have a short runtime, you can’t guarantee that an asynchronous transfer finishes before the app suspends. For more information on background transfers, see [`Downloading files in the background`](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background).

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

If your app has a complication on the active watch face, it can receive up to four [`WKURLSessionRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask) tasks per hour. To avoid throttling, use the [`earliestBeginDate`](https://developer.apple.com/documentation/foundation/urlsessiontask/2873413-earliestbegindate) property to schedule background URL session tasks no closer than 15 minutes apart.

Don’t subclass or create instances of this class. Instead, the system instantiates a [`WKURLSessionRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask) object and passes the task object to your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-4vdjo) method in response to [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) events. Defer calling the background [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) task’s `setTaskCompleted()` method until all the delegate method calls finish processing.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

 In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

The system creates a background [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) task when any of the following events occur:

- The server requires authentication to complete a background transfer.
- All background transfers associated with a session identifier complete (either successfully or unsuccessfully).

To get more information about the transfer, create a background configuration object with the same session identifier. Next, create a session object using the configuration object and a session delegate. The system automatically associates the new session with the transfer and calls the appropriate delegate methods.

## Code Examples

### Example

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

## Topics

### Accessing background task data
- [var sessionIdentifier: String](sessionidentifier.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask/sessionidentifier))
  The identifier for the triggering background transfer.

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
- [class WKWatchConnectivityRefreshBackgroundTask](wkwatchconnectivityrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask))
- [class WKBluetoothAlertRefreshBackgroundTask](wkbluetoothalertrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask))
- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkintentdidrunrefreshbackgroundtask))
- [class WKRelevantShortcutRefreshBackgroundTask](wkrelevantshortcutrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrelevantshortcutrefreshbackgroundtask))
- [class WKSnapshotRefreshBackgroundTask](wksnapshotrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask))
- [class WKRefreshBackgroundTask](wkrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask)*