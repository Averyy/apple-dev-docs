# WKExtendedRuntimeSessionState

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

The activation states for an extended runtime session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
enum WKExtendedRuntimeSessionState
```

```c
enum WKExtendedRuntimeSessionState : NSInteger;
```

## Topics

### Session States
- [WKExtendedRuntimeSessionState.notStarted](./wkextendedruntimesessionstate/notstarted.md)
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.scheduled](./wkextendedruntimesessionstate/scheduled.md)
  The app has scheduled the session to run at a future date.
- [WKExtendedRuntimeSessionState.running](./wkextendedruntimesessionstate/running.md)
  The session is actively running.
- [WKExtendedRuntimeSessionState.invalid](./wkextendedruntimesessionstate/invalid.md)
  Either the session has encountered an error, or it has stopped running.
### Initializers
- [init?(rawValue: Int)](./wkextendedruntimesessionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing the Session State
- [func start()](./wkextendedruntimesession/start%28%29.md)
  Starts running the session.
- [func start(at: Date)](./wkextendedruntimesession/start%28at%29.md)
  Schedules a session to start running at a future date.
- [func invalidate()](./wkextendedruntimesession/invalidate%28%29.md)
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](./wkextendedruntimesession/state.md)
  The session’s current state.
- [var expirationDate: Date?](./wkextendedruntimesession/expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](./wkextendedruntimesession/requestautolaunchauthorizationstatus%28completion%29.md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](./wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate)*