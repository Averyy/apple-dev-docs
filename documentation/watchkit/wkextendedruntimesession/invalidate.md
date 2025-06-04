# invalidate()

**Framework**: WatchKit  
**Kind**: method

Stops the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func invalidate()
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))

#### Discussion

This method stops a running session. If you’ve scheduled a session, it cancels the session. If the session isn’t yet running or scheduled, this method triggers a [`WKExtendedRuntimeSessionErrorCode.notYetStarted`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted) error.

For sessions started with [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)), you can only call [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()) when the app is active. For all other sessions, you can call [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()) to end a session at any time.

After calling [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()), you can no longer run the session. Create and start a new session instead.

## See Also

- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()))
  Starts running the session.
- [func start(at: Date)](start(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)))
  Schedules a session to start running at a future date.
- [var state: WKExtendedRuntimeSessionState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state))
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate))
  The activation states for an extended runtime session.
- [var expirationDate: Date?](expirationdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate))
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](requestautolaunchauthorizationstatus(completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:)))
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate())*