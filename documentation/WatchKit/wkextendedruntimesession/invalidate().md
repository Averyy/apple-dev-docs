# invalidate()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Stops the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidate;
```

## Mentions

- [Using extended runtime sessions](../using-extended-runtime-sessions.md)

#### Discussion

This method stops a running session. If you’ve scheduled a session, it cancels the session. If the session isn’t yet running or scheduled, this method triggers a [`WKExtendedRuntimeSessionErrorCode.notYetStarted`](../wkextendedruntimesessionerrorcode/notyetstarted.md) error.

For sessions started with [`start(at:)`](./start%28at%29.md), you can only call [`invalidate()`](./invalidate%28%29.md) when the app is active. For all other sessions, you can call [`invalidate()`](./invalidate%28%29.md) to end a session at any time.

After calling [`invalidate()`](./invalidate%28%29.md), you can no longer run the session. Create and start a new session instead.

## See Also

### Managing the Session State
- [func start()](./start%28%29.md)
  Starts running the session.
- [func start(at: Date)](./start%28at%29.md)
  Schedules a session to start running at a future date.
- [var state: WKExtendedRuntimeSessionState](./state.md)
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](../wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](./expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](./requestautolaunchauthorizationstatus%28completion%29.md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](../wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate())*