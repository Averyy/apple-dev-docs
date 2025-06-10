# requestAutoLaunchAuthorizationStatus(completion:)

**Framework**: WatchKit  
**Kind**: method

**Availability**:
- watchOS 9.0+

## Declaration

```swift
class func requestAutoLaunchAuthorizationStatus() async throws -> WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus
```

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
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:))*