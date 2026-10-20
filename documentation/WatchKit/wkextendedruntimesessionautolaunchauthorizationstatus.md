# WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- watchOS 9.0+

## Declaration

```swift
enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus
```

```c
enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus.active](./wkextendedruntimesessionautolaunchauthorizationstatus/active.md)
- [WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus.inactive](./wkextendedruntimesessionautolaunchauthorizationstatus/inactive.md)
- [WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus.unknown](./wkextendedruntimesessionautolaunchauthorizationstatus/unknown.md)
### Initializers
- [init?(rawValue: Int)](./wkextendedruntimesessionautolaunchauthorizationstatus/init%28rawvalue%29.md)

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
- [enum WKExtendedRuntimeSessionState](./wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](./wkextendedruntimesession/expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](./wkextendedruntimesession/requestautolaunchauthorizationstatus%28completion%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus)*