# isApplicationRunningInDock

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app is running in the dock.

**Availability**:
- watchOS 4.0+ - Deprecated in 9.2

## Declaration

```swift
var isApplicationRunningInDock: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isApplicationRunningInDock;
```

## Mentions

- [Handling Common State Transitions](../handling-common-state-transitions.md)
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)

## Discussion

This property contains [`true`](../../Swift/true.md) if the app is running in the dock; otherwise, [`false`](../../Swift/false.md).

Check this property (for example, in your extension delegate’s [`applicationWillEnterForeground()`](../wkextensiondelegate/applicationwillenterforeground%28%29.md) method) to determine whether your app is running in the dock. You can use this information to customize your user interface in the dock.

## See Also

### Managing the execution state
- [var applicationState: WKApplicationState](./applicationstate.md)
  The runtime state of the Watch app.
- [enum WKApplicationState](../wkapplicationstate.md)
  The running states of the Watch app.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](./schedulebackgroundrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md)
  Schedules a background task to refresh the app’s data.
- [var isFrontmostTimeoutExtended: Bool](./isfrontmosttimeoutextended.md)
  A Boolean value that determines whether the app extends its time as the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock)*