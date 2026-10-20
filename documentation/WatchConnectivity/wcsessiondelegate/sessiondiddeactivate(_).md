# sessionDidDeactivate(_:)

**Framework**: Watch Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the session has delivered all the data from the previous session, and that communication with the Apple Watch has ended.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func sessionDidDeactivate(_ session: WCSession)
```

```objc
- (void) sessionDidDeactivate:(WCSession *) session;
```

#### Discussion

You must implement this method to support quick switching between Apple Watch devices in your iOS app. The session calls this method when there is no more pending data to deliver to your app and the previous session can be formally closed.

When this method is called, call the [`activate()`](../wcsession/activate%28%29.md) method again to initiate a session with the new Apple Watch, as shown in Listing 1. You can also perform any final cleanup tasks related to closing out the previous session.

Listing 1. Handling the deactivation of the session

**Swift**:

```swift
func sessionDidDeactivate(session: WCSession) {
    // Begin the activation process for the new Apple Watch.
    WCSession.defaultSession().activateSession()
}
```

**Objective-C**:

```objc
- (void)sessionDidDeactivate:(WCSession *)session {
   // Begin the activation process for the new Apple Watch.
   [[WCSession defaultSession] activateSession];
}
```

## Parameters

- `session`: The session object whose activation state changed.

## See Also

### Managing Session Activation
- [func session(WCSession, activationDidCompleteWith: WCSessionActivationState, error: (any Error)?)](./session%28_,activationdidcompletewith,error%29.md)
  Tells the delegate that the session has finished activating.
- [func sessionDidBecomeInactive(WCSession)](./sessiondidbecomeinactive%28_%29.md)
  Tells the delegate that the session will stop communicating with the current Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/sessiondiddeactivate(_:))*