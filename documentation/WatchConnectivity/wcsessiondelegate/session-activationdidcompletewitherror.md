# session(_:activationDidCompleteWith:error:)

**Framework**: Watch Connectivity  
**Kind**: method  
**Required**: Yes

Tells the delegate that the session has finished activating.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error: (any Error)?)
```

#### Discussion

You must implement this method to support asynchronous activation and quick watch switching. Your implementation should check the value of the `activationState` parameter to see if communication with the counterpart app is possible. When the state is [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md), you may communicate normally with the other app.

## Parameters

- `session`: The session object whose activation completed.
- `activationState`: The state of the session. Sessions normally move to the   state upon success or the   state when there is an error. On iOS, the session may also move to the   state if there is data waiting to be delivered from a previous session.
- `error`: An error object indicating that a problem occurred or   if activation completed successfully. When the   parameter contains the value  , this parameter contains the error object describing the reason for the failure.

## See Also

- [func sessionDidBecomeInactive(WCSession)](wcsessiondelegate/sessiondidbecomeinactive(_:).md)
  Tells the delegate that the session will stop communicating with the current Apple Watch.
- [func sessionDidDeactivate(WCSession)](wcsessiondelegate/sessiondiddeactivate(_:).md)
  Tells the delegate that the session has delivered all the data from the previous session, and that communication with the Apple Watch has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/session(_:activationdidcompletewith:error:))*