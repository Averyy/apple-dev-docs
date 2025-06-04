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

The system passes a [`WKExtendedRuntimeSessionInvalidationReason`](wkextendedruntimesessioninvalidationreason.md) value to the session delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:).md) method. Use this value to determine why the session became invalid.

## See Also

- [WKExtendedRuntimeSessionState.notStarted](wkextendedruntimesessionstate/notstarted.md)
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.scheduled](wkextendedruntimesessionstate/scheduled.md)
  The app has scheduled the session to run at a future date.
- [WKExtendedRuntimeSessionState.running](wkextendedruntimesessionstate/running.md)
  The session is actively running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid)*