# state

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The session’s current state.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
var state: WKExtendedRuntimeSessionState { get }
```

```objc
@property (nonatomic, readonly) WKExtendedRuntimeSessionState state;
```

## Discussion

For a list of session states, see [`WKExtendedRuntimeSessionState`](../wkextendedruntimesessionstate.md).

## See Also

### Managing the Session State
- [func start()](./start%28%29.md)
  Starts running the session.
- [func start(at: Date)](./start%28at%29.md)
  Schedules a session to start running at a future date.
- [func invalidate()](./invalidate%28%29.md)
  Stops the session.
- [enum WKExtendedRuntimeSessionState](../wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](./expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](./requestautolaunchauthorizationstatus%28completion%29.md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](../wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state)*