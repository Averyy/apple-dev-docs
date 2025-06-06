# isApplicationRunningInDock

**Framework**: Watchkit  
**Kind**: property

A Boolean value that indicates whether the app is running in the dock.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
var isApplicationRunningInDock: Bool { get }
```

## Mentions

- [Handling Common State Transitions](handling-common-state-transitions.md)
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)

#### Discussion

This property contains [`true`](https://developer.apple.com/documentation/swift/true) if the app is running in the dock; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

Check this property (for example, in your extension delegate’s [`applicationWillEnterForeground()`](wkextensiondelegate/applicationwillenterforeground().md) method) to determine whether your app is running in the dock. You can use this information to customize your user interface in the dock.

## See Also

- [var applicationState: WKApplicationState](wkextension/applicationstate.md)
  The runtime state of the Watch app.
- [enum WKApplicationState](wkapplicationstate.md)
  The running states of the Watch app.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md)
  Schedules a background task to refresh the app’s data.
- [var isFrontmostTimeoutExtended: Bool](wkextension/isfrontmosttimeoutextended.md)
  A Boolean value that determines whether the app extends its time as the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock)*