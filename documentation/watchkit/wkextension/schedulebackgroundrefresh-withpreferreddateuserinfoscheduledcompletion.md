# scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)

**Framework**: WatchKit  
**Kind**: method

Schedules a background task to refresh the app’s data.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor
func scheduleBackgroundRefresh(withPreferredDate preferredFireDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: @escaping ((any Error)?) -> Void)
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

#### Discussion

Call this method to update the contents of your app in the background. Background refresh tasks only trigger when the app is in the background. If the app is still running in the foreground at the scheduled time, the system ignores the task.

When the system triggers the task, it wakes your app in the background and execute your background task handler. The system also calls your active interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) and [`didActivate()`](https://developer.apple.com/documentation/SecurityInterface/SFAuthorizationPluginView/didActivate()) methods. You can check your extension’s [`applicationState`](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate) during these methods to determine whether your app is running in the foreground or in the background.

Use this task to update your application’s state. You can only schedule one background app refresh task at a time; scheduling a second task cancels the first. Additionally, the system budgets background app refresh tasks. For more information, see [`WKApplicationRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask).

## Parameters

- `preferredFireDate`: The date and time of the next background app refresh task. The system attempts to wake your app in the background shortly after the scheduled time, but may delay the background task due to the system’s current state or if your app exceeds its budget for background tasks.
- `userInfo`: A dictionary of custom information associated with the background app refresh task. Pass   if you don’t need to associate any custom data with the task.
- `scheduledCompletion`: A block that the system calls after scheduling the background app refresh task. This block takes the following parameter:

## See Also

- [var applicationState: WKApplicationState](applicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate))
  The runtime state of the Watch app.
- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock))
  A Boolean value that indicates whether the app is running in the dock.
- [var isFrontmostTimeoutExtended: Bool](isfrontmosttimeoutextended.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended))
  A Boolean value that determines whether the app extends its time as the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:))*