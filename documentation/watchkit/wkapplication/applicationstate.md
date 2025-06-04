# applicationState

**Framework**: WatchKit  
**Kind**: property

The runtime state of the watchOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
var applicationState: WKApplicationState { get }
```

#### Discussion

The watchOS app may be active, inactive, or running in the background. Use this property to get the current state. To receive notifications about state changes, implement the appropriate methods of the [`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate) object, or create a SwiftUI view that updates based on changes to the [`ScenePhase`](https://developer.apple.com/documentation/SwiftUI/ScenePhase) environment value.

## See Also

- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isapplicationrunningindock))
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/applicationstate)*