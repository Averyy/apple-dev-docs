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
- [WKApplicationState.active](active.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active))
  The Watch app is running in the foreground and currently receiving events.
- [WKApplicationState.inactive](inactive.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive))
  The Watch app is running in the foreground, but is not yet responding to actions from controls or gestures.
- [WKApplicationState.background](background.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background))
  The Watch app is running in the background.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [var applicationState: WKApplicationState](applicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/applicationstate))
  The runtime state of the watchOS app.
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isapplicationrunningindock))
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationstate)*