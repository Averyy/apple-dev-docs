# WKExtendedRuntimeSessionState.invalid

**Framework**: WatchKit  
**Kind**: case

Either the session has encountered an error, or it has stopped running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case invalid
```

#### Discussion

The system passes a [`WKExtendedRuntimeSessionInvalidationReason`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason) value to the session delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)) method. Use this value to determine why the session became invalid.

## See Also

- [WKExtendedRuntimeSessionState.notStarted](notstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted))
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.scheduled](scheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled))
  The app has scheduled the session to run at a future date.
- [WKExtendedRuntimeSessionState.running](running.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/running))
  The session is actively running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid)*