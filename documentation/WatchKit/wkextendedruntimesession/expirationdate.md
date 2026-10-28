# expirationDate

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The time and date when the session expires.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
var expirationDate: Date? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDate * expirationDate;
```

## Mentions

- [Using extended runtime sessions](../using-extended-runtime-sessions.md)

## Discussion

Use this property to determine how much time remains before the session stops running.

This property starts set to `nil`. The system assigns a date as soon as the session starts running. This property remains valid, even after the session becomes invalid.

## See Also

### Managing the Session State
- [func start()](./start%28%29.md)
  Starts running the session.
- [func start(at: Date)](./start%28at%29.md)
  Schedules a session to start running at a future date.
- [func invalidate()](./invalidate%28%29.md)
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](./state.md)
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](../wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](./requestautolaunchauthorizationstatus%28completion%29.md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](../wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate)*