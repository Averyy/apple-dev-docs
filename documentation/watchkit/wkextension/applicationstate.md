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

The Watch app may be active, inactive, or running in the background. Use this property to get the current state. To be notified of state changes, implement the appropriate methods of the [`delegate`](wkextension/delegate.md) object.

## See Also

- [enum WKApplicationState](wkapplicationstate.md)
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](wkextension/isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md)
  Schedules a background task to refresh the app’s data.
- [var isFrontmostTimeoutExtended: Bool](wkextension/isfrontmosttimeoutextended.md)
  A Boolean value that determines whether the app extends its time as the frontmost app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate)*