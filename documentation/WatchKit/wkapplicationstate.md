# WKApplicationState

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

The running states of the Watch app.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
enum WKApplicationState
```

```c
enum WKApplicationState : NSInteger;
```

## Topics

### Constants
- [WKApplicationState.active](./wkapplicationstate/active.md)
  The Watch app is running in the foreground and currently receiving events.
- [WKApplicationState.inactive](./wkapplicationstate/inactive.md)
  The Watch app is running in the foreground, but is not yet responding to actions from controls or gestures.
- [WKApplicationState.background](./wkapplicationstate/background.md)
  The Watch app is running in the background.
### Initializers
- [init?(rawValue: Int)](./wkapplicationstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing the app state
- [var applicationState: WKApplicationState](./wkapplication/applicationstate.md)
  The runtime state of the watchOS app.
- [var isApplicationRunningInDock: Bool](./wkapplication/isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](./wkapplication/schedulebackgroundrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md)
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationstate)*