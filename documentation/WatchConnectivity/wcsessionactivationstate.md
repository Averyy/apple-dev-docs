# WCSessionActivationState

**Framework**: Watch Connectivity  
**Kind**: enum

Constants indicating the activation state of a session.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
enum WCSessionActivationState
```

## Topics

### Constants
- [WCSessionActivationState.notActivated](wcsessionactivationstate/notactivated.md)
  The session is not activated. When in this state, no communication occurs between the Watch app and iOS app. It is a programmer error to try to send data to the counterpart app while in this state.
- [WCSessionActivationState.inactive](wcsessionactivationstate/inactive.md)
  The session was active but is transitioning to the deactivated state. The session’s delegate object may still receive data while in this state, but it is a programmer error to try to send data to the counterpart app.
- [WCSessionActivationState.activated](wcsessionactivationstate/activated.md)
  The session is active and the Watch app and iOS app may communicate with each other freely.
### Initializers
- [init?(rawValue: Int)](wcsessionactivationstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let WCErrorDomain: String](wcerrordomain.md)
  The domain for errors associated with the Watch Connectivity framework.
- [struct WCError](wcerror.md)
  A structure that contains Watch Connectivity error information.
- [WCError.Code](wcerror/code.md)
  Constants for errors during a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate)*