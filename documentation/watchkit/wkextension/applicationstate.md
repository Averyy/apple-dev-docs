# applicationState

**Framework**: WatchKit  
**Kind**: property

The runtime state of the Watch app.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor
var applicationState: WKApplicationState { get }
```

#### Discussion

The Watch app may be active, inactive, or running in the background. Use this property to get the current state. To be notified of state changes, implement the appropriate methods of the [`delegate`](https://developer.apple.com/documentation/watchkit/wkextension/delegate) object.

## See Also

- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock))
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh the app’s data.
- [var isFrontmostTimeoutExtended: Bool](isfrontmosttimeoutextended.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended))
  A Boolean value that determines whether the app extends its time as the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate)*