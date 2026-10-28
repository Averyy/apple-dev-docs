# applicationState

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The runtime state of the watchOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var applicationState: WKApplicationState { get }
```

```objc
@property (nonatomic, readonly) WKApplicationState applicationState;
```

## Discussion

The watchOS app may be active, inactive, or running in the background. Use this property to get the current state. To receive notifications about state changes, implement the appropriate methods of the [`WKApplicationDelegate`](../wkapplicationdelegate.md) object, or create a SwiftUI view that updates based on changes to the [`ScenePhase`](../../SwiftUI/scenephase.md) environment value.

## See Also

### Managing the app state
- [enum WKApplicationState](../wkapplicationstate.md)
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](./isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](./schedulebackgroundrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md)
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/applicationstate)*