# setTaskCompletedWithSnapshot(_:)

**Framework**: WatchKit  
**Kind**: method

Marks the task as complete and indicates whether the system should take a new snapshot of the app.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
func setTaskCompletedWithSnapshot(_ refreshSnapshot: Bool)
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))

#### Discussion

Call this method as soon as a nonsnapshot background task (any [`WKRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask) subclass except the [`WKSnapshotRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask) class) is complete.

To update the app’s snapshot in response to the current task, pass [`true`](https://developer.apple.com/documentation/swift/true), and the system schedules an immediate snapshot. This request counts against the standard snapshot budget and overwrites any requests made using the [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](https://developer.apple.com/documentation/watchkit/wkextension/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:)) method. As with all snapshots, your app receives a [`WKSnapshotRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask) before the snapshot is taken.

The system provides your extension with a limited amount of time (on the order of seconds) to finish this task. If you do not call [`setTaskCompletedWithSnapshot(_:)`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)) on the task, the system continues to run in the background until all available time is consumed, wasting battery power.

The system suspends the extension as soon as all background tasks are complete.

When completing a snapshot background task, you generally call the [`setTaskCompleted(restoredDefaultState:estimatedSnapshotExpiration:userInfo:)`](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/settaskcompleted(restoreddefaultstate:estimatedsnapshotexpiration:userinfo:))method and explicitly set the date for the next snapshot. You can call [`setTaskCompletedWithSnapshot(_:)`](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:)) as a simpler alternative. If you pass [`true`](https://developer.apple.com/documentation/swift/true), the system schedules a new snapshot task in one hour. If you pass [`false`](https://developer.apple.com/documentation/swift/false), no snapshot is scheduled.

## Parameters

- `refreshSnapshot`: A Boolean value that indicates whether the system should take a new snapshot of the app.

## See Also

- [var expirationHandler: (() -> Void)?](expirationhandler.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/expirationhandler))
  A block that the system calls when the available runtime for a background task is about to expire.
- [func setTaskCompleted()](settaskcompleted().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompleted()))
  Marks the task as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:))*