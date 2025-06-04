# WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus

**Framework**: WatchKit  
**Kind**: enum

**Availability**:
- watchOS 9.0+

## Declaration

```swift
enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus
```

## Topics

### Enumeration Cases
- [WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus.active](wkextendedruntimesessionautolaunchauthorizationstatus/active.md)
- [WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus.inactive](wkextendedruntimesessionautolaunchauthorizationstatus/inactive.md)
- [WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus.unknown](wkextendedruntimesessionautolaunchauthorizationstatus/unknown.md)
### Initializers
- [init?(rawValue: Int)](wkextendedruntimesessionautolaunchauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [RawRepresentable](https://developer.apple.com/documentation/Swift/RawRepresentable)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [func start()](wkextendedruntimesession/start.md)
  Starts running the session.
- [func start(at: Date)](wkextendedruntimesession/start(at:).md)
  Schedules a session to start running at a future date.
- [func invalidate()](wkextendedruntimesession/invalidate.md)
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](wkextendedruntimesession/state.md)
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](wkextendedruntimesession/expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus)*