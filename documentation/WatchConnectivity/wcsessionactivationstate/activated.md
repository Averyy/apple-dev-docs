# WCSessionActivationState.activated

**Framework**: Watchconnectivity  
**Kind**: case

The session is active and the Watch app and iOS app may communicate with each other freely.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
case activated
```

## See Also

- [WCSessionActivationState.notActivated](wcsessionactivationstate/notactivated.md)
  The session is not activated. When in this state, no communication occurs between the Watch app and iOS app. It is a programmer error to try to send data to the counterpart app while in this state.
- [WCSessionActivationState.inactive](wcsessionactivationstate/inactive.md)
  The session was active but is transitioning to the deactivated state. The session’s delegate object may still receive data while in this state, but it is a programmer error to try to send data to the counterpart app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate/activated)*