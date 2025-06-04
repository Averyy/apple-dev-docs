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

- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()))
  Starts running the session.
- [func start(at: Date)](start(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)))
  Schedules a session to start running at a future date.
- [func invalidate()](invalidate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()))
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state))
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate))
  The activation states for an extended runtime session.
- [var expirationDate: Date?](expirationdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate))
  The time and date when the session expires.
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:))*