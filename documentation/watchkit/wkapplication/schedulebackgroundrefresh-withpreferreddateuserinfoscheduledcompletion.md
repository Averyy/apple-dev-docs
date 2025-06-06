# scheduleBackgroundRefresh(withPreferredDate:userInfo:scheduledCompletion:)

**Framework**: Watchkit  
**Kind**: method

Schedules a background task to refresh the app’s data.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
func scheduleBackgroundRefresh(withPreferredDate preferredFireDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: @escaping ((any Error)?) -> Void)
```

## Mentions

- [Using background tasks](using-background-tasks.md)

#### Discussion

Call this method to update the contents of your app in the background. Background refresh tasks only trigger when the app is in the background. If the app is still running in the foreground at the scheduled time, the system ignores the task.

When the system triggers the task, it wakes your app in the background and execute your background task handler. The system also calls your active interface controller’s [`willActivate()`](wkinterfacecontroller/willactivate().md) and [`didActivate()`](https://developer.apple.com/documentation/SecurityInterface/SFAuthorizationPluginView/didActivate()) methods. You can check your app’s [`applicationState`](wkapplication/applicationstate.md) during these methods to determine whether your app is running in the foreground or in the background.

Use this task to update your application’s state. You can only schedule one background app refresh task at a time; scheduling a second task cancels the first. Additionally, the system budgets background app refresh tasks. For more information, see [`WKApplicationRefreshBackgroundTask`](wkapplicationrefreshbackgroundtask.md).

## Parameters

- `preferredFireDate`: The date and time of the next background app refresh task. The system attempts to wake your app in the background shortly after the scheduled time, but may delay the background task due to the system’s current state or if your app exceeds its budget for background tasks.
- `userInfo`: A dictionary of custom information associated with the background app refresh task. Pass   if you don’t need to associate any custom data with the task.
- `scheduledCompletion`: A block that the system calls after scheduling the background app refresh task. This block takes the following parameter:

## See Also

- [var applicationState: WKApplicationState](wkapplication/applicationstate.md)
  The runtime state of the watchOS app.
- [enum WKApplicationState](wkapplicationstate.md)
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](wkapplication/isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:))*