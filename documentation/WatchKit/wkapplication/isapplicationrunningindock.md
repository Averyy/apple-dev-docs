# isApplicationRunningInDock

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app is running in the dock.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var isApplicationRunningInDock: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isApplicationRunningInDock;
```

#### Discussion

This property contains [`true`](../../Swift/true.md) if the app is running in the dock; otherwise, [`false`](../../Swift/false.md).

Check this property (for example, in your app delegate’s [`applicationWillEnterForeground()`](../wkapplicationdelegate/applicationwillenterforeground%28%29.md) method) to determine whether your app is running in the dock. You can use this information to customize your user interface in the dock.

## See Also

### Managing the app state
- [var applicationState: WKApplicationState](./applicationstate.md)
  The runtime state of the watchOS app.
- [enum WKApplicationState](../wkapplicationstate.md)
  The running states of the Watch app.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](./schedulebackgroundrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md)
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/isapplicationrunningindock)*