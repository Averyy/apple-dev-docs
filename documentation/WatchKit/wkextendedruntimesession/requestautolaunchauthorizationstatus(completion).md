# requestAutoLaunchAuthorizationStatus(completion:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- watchOS 9.0+

## Declaration

```swift
class func requestAutoLaunchAuthorizationStatus(completion: @escaping @Sendable (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)
```

```swift
class func requestAutoLaunchAuthorizationStatus() async throws -> WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus
```

```objc
+ (void) requestAutoLaunchAuthorizationStatusWithCompletion:(void (^)(WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus authorizationStatus, NSError *error)) completion;
```

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
- [var expirationDate: Date?](./expirationdate.md)
  The time and date when the session expires.
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](../wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:))*