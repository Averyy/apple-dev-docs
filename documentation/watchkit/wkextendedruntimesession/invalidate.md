# invalidate()

**Framework**: Watchkit  
**Kind**: method

Stops the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func invalidate()
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md)

#### Discussion

This method stops a running session. If you’ve scheduled a session, it cancels the session. If the session isn’t yet running or scheduled, this method triggers a [`WKExtendedRuntimeSessionErrorCode.notYetStarted`](wkextendedruntimesessionerrorcode/notyetstarted.md) error.

For sessions started with [`start(at:)`](wkextendedruntimesession/start(at:).md), you can only call [`invalidate()`](wkextendedruntimesession/invalidate().md) when the app is active. For all other sessions, you can call [`invalidate()`](wkextendedruntimesession/invalidate().md) to end a session at any time.

After calling [`invalidate()`](wkextendedruntimesession/invalidate().md), you can no longer run the session. Create and start a new session instead.

## See Also

- [func start()](wkextendedruntimesession/start.md)
  Starts running the session.
- [func start(at: Date)](wkextendedruntimesession/start(at:).md)
  Schedules a session to start running at a future date.
- [var state: WKExtendedRuntimeSessionState](wkextendedruntimesession/state.md)
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](wkextendedruntimesession/expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:).md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate())*