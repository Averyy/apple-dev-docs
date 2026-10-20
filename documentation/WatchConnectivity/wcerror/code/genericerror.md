# WCError.Code.genericError

**Framework**: Watch Connectivity  
**Kind**: case  
**Role**: Case

An error that occurs when there is an unknown problem.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case genericError
```

```c
WCErrorCodeGenericError
```

## See Also

### Error Codes
- [WCError.Code.sessionNotSupported](./sessionnotsupported.md)
  An error indicating that the current device doesn’t support the use of session objects.
- [WCError.Code.sessionMissingDelegate](./sessionmissingdelegate.md)
  An error indicating that the WatchKit extension doesn’t have a valid extension delegate to process events.
- [WCError.Code.sessionNotActivated](./sessionnotactivated.md)
  An error indicating that the other device doesn’t have an active session.
- [WCError.Code.deviceNotPaired](./devicenotpaired.md)
  An error indicating that the current device doesn’t have a paired counterpart.
- [WCError.Code.watchAppNotInstalled](./watchappnotinstalled.md)
  An error indicating that the Watch app isn’t an installed app on the user’s Apple Watch.
- [WCError.Code.notReachable](./notreachable.md)
  An error indicating that the counterpart app isn’t reachable.
- [WCError.Code.invalidParameter](./invalidparameter.md)
  An error indicating that a parameter is invalid.
- [WCError.Code.payloadTooLarge](./payloadtoolarge.md)
  An error indicating an attempt to send an item that exceeds the maximum size limit.
- [WCError.Code.payloadUnsupportedTypes](./payloadunsupportedtypes.md)
  An error indicating that a dictionary contains nonproperty list types.
- [WCError.Code.messageReplyFailed](./messagereplyfailed.md)
  An error that occurs when the system can’t return the reply.
- [WCError.Code.messageReplyTimedOut](./messagereplytimedout.md)
  An error that occurs when the counterpart app doesn’t return a reply in time.
- [WCError.Code.fileAccessDenied](./fileaccessdenied.md)
  An error indicating that the system can’t transfer a file because it is inaccessible.
- [WCError.Code.deliveryFailed](./deliveryfailed.md)
  An error that occurs when the system can’t deliver the payload.
- [WCError.Code.insufficientSpace](./insufficientspace.md)
  An error indicating that there isn’t enough space on the receiving side to store the data.
- [WCError.Code.sessionInactive](./sessioninactive.md)
  An error indicating that the session is inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/genericerror)*