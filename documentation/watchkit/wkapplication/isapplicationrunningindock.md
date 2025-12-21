# isApplicationRunningInDock

**Framework**: WatchKit  
**Kind**: property

A Boolean value that indicates whether the app is running in the dock.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
var isApplicationRunningInDock: Bool { get }
```

#### Discussion

This property contains [`true`](https://developer.apple.com/documentation/Swift/true) if the app is running in the dock; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

Check this property (for example, in your app delegate’s [`applicationWillEnterForeground()`](wkapplicationdelegate/applicationwillenterforeground().md) method) to determine whether your app is running in the dock. You can use this information to customize your user interface in the dock.

## See Also

- [var applicationState: WKApplicationState](wkapplication/applicationstate.md)
  The runtime state of the watchOS app.
- [enum WKApplicationState](wkapplicationstate.md)
  The running states of the Watch app.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md)
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/isapplicationrunningindock)*