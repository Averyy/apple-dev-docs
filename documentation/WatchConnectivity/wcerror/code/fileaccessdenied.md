# WCError.Code.fileAccessDenied

**Framework**: Watchconnectivity  
**Kind**: case

An error indicating that the system can’t transfer a file because it is inaccessible.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case fileAccessDenied
```

#### Discussion

This error can occur when the file path is invalid or the app has insufficient privileges to access the file.

## See Also

- [WCError.Code.genericError](wcerror/code/genericerror.md)
  An error that occurs when there is an unknown problem.
- [WCError.Code.sessionNotSupported](wcerror/code/sessionnotsupported.md)
  An error indicating that the current device doesn’t support the use of session objects.
- [WCError.Code.sessionMissingDelegate](wcerror/code/sessionmissingdelegate.md)
  An error indicating that the WatchKit extension doesn’t have a valid extension delegate to process events.
- [WCError.Code.sessionNotActivated](wcerror/code/sessionnotactivated.md)
  An error indicating that the other device doesn’t have an active session.
- [WCError.Code.deviceNotPaired](wcerror/code/devicenotpaired.md)
  An error indicating that the current device doesn’t have a paired counterpart.
- [WCError.Code.watchAppNotInstalled](wcerror/code/watchappnotinstalled.md)
  An error indicating that the Watch app isn’t an installed app on the user’s Apple Watch.
- [WCError.Code.notReachable](wcerror/code/notreachable.md)
  An error indicating that the counterpart app isn’t reachable.
- [WCError.Code.invalidParameter](wcerror/code/invalidparameter.md)
  An error indicating that a parameter is invalid.
- [WCError.Code.payloadTooLarge](wcerror/code/payloadtoolarge.md)
  An error indicating an attempt to send an item that exceeds the maximum size limit.
- [WCError.Code.payloadUnsupportedTypes](wcerror/code/payloadunsupportedtypes.md)
  An error indicating that a dictionary contains nonproperty list types.
- [WCError.Code.messageReplyFailed](wcerror/code/messagereplyfailed.md)
  An error that occurs when the system can’t return the reply.
- [WCError.Code.messageReplyTimedOut](wcerror/code/messagereplytimedout.md)
  An error that occurs when the counterpart app doesn’t return a reply in time.
- [WCError.Code.deliveryFailed](wcerror/code/deliveryfailed.md)
  An error that occurs when the system can’t deliver the payload.
- [WCError.Code.insufficientSpace](wcerror/code/insufficientspace.md)
  An error indicating that there isn’t enough space on the receiving side to store the data.
- [WCError.Code.sessionInactive](wcerror/code/sessioninactive.md)
  An error indicating that the session is inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/fileaccessdenied)*