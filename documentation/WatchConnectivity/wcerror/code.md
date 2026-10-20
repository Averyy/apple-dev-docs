# WCError.Code

**Framework**: Watch Connectivity  
**Kind**: enum  
**Role**: Enumeration

Constants for errors during a session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Code
```

```c
enum WCErrorCode : NSInteger;
```

## Topics

### Error Codes
- [WCError.Code.genericError](./code/genericerror.md)
  An error that occurs when there is an unknown problem.
- [WCError.Code.sessionNotSupported](./code/sessionnotsupported.md)
  An error indicating that the current device doesn’t support the use of session objects.
- [WCError.Code.sessionMissingDelegate](./code/sessionmissingdelegate.md)
  An error indicating that the WatchKit extension doesn’t have a valid extension delegate to process events.
- [WCError.Code.sessionNotActivated](./code/sessionnotactivated.md)
  An error indicating that the other device doesn’t have an active session.
- [WCError.Code.deviceNotPaired](./code/devicenotpaired.md)
  An error indicating that the current device doesn’t have a paired counterpart.
- [WCError.Code.watchAppNotInstalled](./code/watchappnotinstalled.md)
  An error indicating that the Watch app isn’t an installed app on the user’s Apple Watch.
- [WCError.Code.notReachable](./code/notreachable.md)
  An error indicating that the counterpart app isn’t reachable.
- [WCError.Code.invalidParameter](./code/invalidparameter.md)
  An error indicating that a parameter is invalid.
- [WCError.Code.payloadTooLarge](./code/payloadtoolarge.md)
  An error indicating an attempt to send an item that exceeds the maximum size limit.
- [WCError.Code.payloadUnsupportedTypes](./code/payloadunsupportedtypes.md)
  An error indicating that a dictionary contains nonproperty list types.
- [WCError.Code.messageReplyFailed](./code/messagereplyfailed.md)
  An error that occurs when the system can’t return the reply.
- [WCError.Code.messageReplyTimedOut](./code/messagereplytimedout.md)
  An error that occurs when the counterpart app doesn’t return a reply in time.
- [WCError.Code.fileAccessDenied](./code/fileaccessdenied.md)
  An error indicating that the system can’t transfer a file because it is inaccessible.
- [WCError.Code.deliveryFailed](./code/deliveryfailed.md)
  An error that occurs when the system can’t deliver the payload.
- [WCError.Code.insufficientSpace](./code/insufficientspace.md)
  An error indicating that there isn’t enough space on the receiving side to store the data.
- [WCError.Code.sessionInactive](./code/sessioninactive.md)
  An error indicating that the session is inactive.
- [WCError.Code.transferTimedOut](./code/transfertimedout.md)
  An error that occurs when the transfer reaches the timeout limit before it completes.
- [WCError.Code.companionAppNotInstalled](./code/companionappnotinstalled.md)
  An error indicating that the companion hasn’t installed the app.
- [WCError.Code.watchOnlyApp](./code/watchonlyapp.md)
  An error indicating that the app is a watch-only app.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum WCSessionActivationState](../wcsessionactivationstate.md)
  Constants indicating the activation state of a session.
- [let WCErrorDomain: String](../wcerrordomain.md)
  The domain for errors associated with the Watch Connectivity framework.
- [struct WCError](../wcerror.md)
  A structure that contains Watch Connectivity error information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcerror/code)*