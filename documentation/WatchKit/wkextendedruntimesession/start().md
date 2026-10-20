# start()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Starts running the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func start()
```

```objc
- (void) start;
```

## Mentions

- [Using extended runtime sessions](../using-extended-runtime-sessions.md)

#### Discussion

Use [`start()`](./start%28%29.md) to begin a session. You must call this method while your app is running in the foreground.

You can’t use the [`start()`](./start%28%29.md) method to set up a schedulable session (such as a smart alarm session). Call the [`start(at:)`](./start%28at%29.md) method instead.

## See Also

### Managing the Session State
- [func start(at: Date)](./start%28at%29.md)
  Schedules a session to start running at a future date.
- [func invalidate()](./invalidate%28%29.md)
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](./state.md)
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](../wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](./expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](./requestautolaunchauthorizationstatus%28completion%29.md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](../wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start())*