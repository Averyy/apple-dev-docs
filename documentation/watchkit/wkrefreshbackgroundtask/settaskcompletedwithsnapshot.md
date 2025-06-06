# setTaskCompletedWithSnapshot(_:)

**Framework**: Watchkit  
**Kind**: method

Marks the task as complete and indicates whether the system should take a new snapshot of the app.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
func setTaskCompletedWithSnapshot(_ refreshSnapshot: Bool)
```

## Mentions

- [Using background tasks](using-background-tasks.md)
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md)

#### Discussion

Call this method as soon as a nonsnapshot background task (any [`WKRefreshBackgroundTask`](wkrefreshbackgroundtask.md) subclass except the [`WKSnapshotRefreshBackgroundTask`](wksnapshotrefreshbackgroundtask.md) class) is complete.

To update the app’s snapshot in response to the current task, pass [`true`](https://developer.apple.com/documentation/swift/true), and the system schedules an immediate snapshot. This request counts against the standard snapshot budget and overwrites any requests made using the [`scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)`](wkextension/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) method. As with all snapshots, your app receives a [`WKSnapshotRefreshBackgroundTask`](wksnapshotrefreshbackgroundtask.md) before the snapshot is taken.

The system provides your extension with a limited amount of time (on the order of seconds) to finish this task. If you do not call [`setTaskCompletedWithSnapshot(_:)`](wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:).md) on the task, the system continues to run in the background until all available time is consumed, wasting battery power.

The system suspends the extension as soon as all background tasks are complete.

When completing a snapshot background task, you generally call the [`setTaskCompleted(restoredDefaultState:estimatedSnapshotExpiration:userInfo:)`](wksnapshotrefreshbackgroundtask/settaskcompleted(restoreddefaultstate:estimatedsnapshotexpiration:userinfo:).md)method and explicitly set the date for the next snapshot. You can call [`setTaskCompletedWithSnapshot(_:)`](wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:).md) as a simpler alternative. If you pass [`true`](https://developer.apple.com/documentation/swift/true), the system schedules a new snapshot task in one hour. If you pass [`false`](https://developer.apple.com/documentation/swift/false), no snapshot is scheduled.

## Parameters

- `refreshSnapshot`: A Boolean value that indicates whether the system should take a new snapshot of the app.

## See Also

- [var expirationHandler: (() -> Void)?](wkrefreshbackgroundtask/expirationhandler.md)
  A block that the system calls when the available runtime for a background task is about to expire.
- [func setTaskCompleted()](wkrefreshbackgroundtask/settaskcompleted.md)
  Marks the task as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/settaskcompletedwithsnapshot(_:))*