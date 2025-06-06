# start()

**Framework**: Watchkit  
**Kind**: method

Starts running the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func start()
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md)

#### Discussion

Use [`start()`](wkextendedruntimesession/start().md) to begin a session. You must call this method while your app is running in the foreground.

You can’t use the [`start()`](wkextendedruntimesession/start().md) method to set up a schedulable session (such as a smart alarm session). Call the [`start(at:)`](wkextendedruntimesession/start(at:).md) method instead.

## See Also

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
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start())*