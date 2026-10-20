# WKExtendedRuntimeSessionState.invalid

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

Either the session has encountered an error, or it has stopped running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case invalid
```

```c
WKExtendedRuntimeSessionStateInvalid
```

#### Discussion

The system passes a [`WKExtendedRuntimeSessionInvalidationReason`](../wkextendedruntimesessioninvalidationreason.md) value to the session delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](../wkextendedruntimesessiondelegate/extendedruntimesession%28_,didinvalidatewith,error%29.md) method. Use this value to determine why the session became invalid.

## See Also

### Session States
- [WKExtendedRuntimeSessionState.notStarted](./notstarted.md)
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.scheduled](./scheduled.md)
  The app has scheduled the session to run at a future date.
- [WKExtendedRuntimeSessionState.running](./running.md)
  The session is actively running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid)*