# WKApplicationState

**Framework**: WatchKit  
**Kind**: enum

The running states of the Watch app.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
enum WKApplicationState
```

## Topics

### Constants
- [WKApplicationState.active](wkapplicationstate/active.md)
  The Watch app is running in the foreground and currently receiving events.
- [WKApplicationState.inactive](wkapplicationstate/inactive.md)
  The Watch app is running in the foreground, but is not yet responding to actions from controls or gestures.
- [WKApplicationState.background](wkapplicationstate/background.md)
  The Watch app is running in the background.
### Initializers
- [init?(rawValue: Int)](wkapplicationstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var applicationState: WKApplicationState](wkapplication/applicationstate.md)
  The runtime state of the watchOS app.
- [var isApplicationRunningInDock: Bool](wkapplication/isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md)
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationstate)*