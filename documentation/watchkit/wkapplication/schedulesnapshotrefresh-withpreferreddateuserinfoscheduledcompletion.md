# scheduleSnapshotRefresh(withPreferredDate:userInfo:scheduledCompletion:)

**Framework**: WatchKit  
**Kind**: method

Schedules a background task to refresh your app’s snapshot.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
func scheduleSnapshotRefresh(withPreferredDate preferredFireDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: @escaping ((any Error)?) -> Void)
```

## Mentions

- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))

#### Discussion

Call this method to update your app’s snapshot in the background. When the system triggers the task, it wakes your app in the background and calls your app delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-7kiwx) method. Use this task to transition to the interface controller you want to display in the snapshot, and to update that controller’s user interface.

You can only schedule one background snapshot refresh task at a time. If you’ve already scheduled a background snapshot refresh task, scheduling a second task cancels the first. Additionally, the system budgets background snapshot refresh tasks. For more information, see [`WKSnapshotRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask).

The system automatically schedules background snapshot request tasks in the following situations:

- When your device starts up.
- When your app updates the complication timeline.
- When the user interacts with one of the apps notifications.
- When the app transitions from the foreground to the background.
- One hour after the user’s last interaction with the app.

These requests don’t cancel or replace any of your scheduled requests.

## Parameters

- `preferredFireDate`: If you pass the current date and time, the system immediately invalidates your existing snapshot, marking the snapshot as stale in the Dock. The system also schedules the earliest possible background snapshot refresh task.
- `userInfo`: A dictionary of custom information associated with the background snapshot refresh task. Pass   if you don’t need to associate any custom data with the task.
- `scheduledCompletion`: A block that the system calls after the background refresh has completed. This block takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/schedulesnapshotrefresh(withpreferreddate:userinfo:scheduledcompletion:))*