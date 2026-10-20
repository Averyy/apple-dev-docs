# watchOnlyApp

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Type Property

An error indicating that the app is a watch-only app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var watchOnlyApp: WCError.Code { get }
```

## See Also

### Understanding Error Codes
- [static var genericError: WCError.Code](./genericerror.md)
  An error that occurs when there is an unknown problem.
- [static var sessionNotSupported: WCError.Code](./sessionnotsupported.md)
  An error indicating that the current device doesn’t support the use of session objects.
- [static var sessionMissingDelegate: WCError.Code](./sessionmissingdelegate.md)
  An error indicating that the WatchKit extension doesn’t have a valid extension delegate to process events.
- [static var sessionNotActivated: WCError.Code](./sessionnotactivated.md)
  An error indicating that the other device doesn’t have an active session.
- [static var deviceNotPaired: WCError.Code](./devicenotpaired.md)
  An error indicating that the current device doesn’t have a paired counterpart.
- [static var watchAppNotInstalled: WCError.Code](./watchappnotinstalled.md)
  An error indicating that the Watch app isn’t an installed app on the user’s Apple Watch.
- [static var notReachable: WCError.Code](./notreachable.md)
  An error indicating that the counterpart app isn’t reachable.
- [static var invalidParameter: WCError.Code](./invalidparameter.md)
  An error indicating that a parameter is invalid.
- [static var payloadTooLarge: WCError.Code](./payloadtoolarge.md)
  An error indicating an attempt to send an item that exceeds the maximum size limit.
- [static var payloadUnsupportedTypes: WCError.Code](./payloadunsupportedtypes.md)
  An error indicating that a dictionary contains nonproperty list types.
- [static var messageReplyFailed: WCError.Code](./messagereplyfailed.md)
  An error that occurs when the system can’t return the reply.
- [static var messageReplyTimedOut: WCError.Code](./messagereplytimedout.md)
  An error that occurs when the counterpart app doesn’t return a reply in time.
- [static var fileAccessDenied: WCError.Code](./fileaccessdenied.md)
  An error indicating that the system can’t transfer a file because it is inaccessible.
- [static var deliveryFailed: WCError.Code](./deliveryfailed.md)
  An error that occurs when the system can’t deliver the payload.
- [static var insufficientSpace: WCError.Code](./insufficientspace.md)
  An error indicating that there isn’t enough space on the receiving side to store the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcerror/watchonlyapp)*