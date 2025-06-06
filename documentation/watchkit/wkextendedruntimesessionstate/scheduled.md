# WKExtendedRuntimeSessionState.scheduled

**Framework**: Watchkit  
**Kind**: case

The app has scheduled the session to run at a future date.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case scheduled
```

#### Discussion

The session transitions to the [`WKExtendedRuntimeSessionState.scheduled`](wkextendedruntimesessionstate/scheduled.md) state when you call the [`start(at:)`](wkextendedruntimesession/start(at:).md) method. It remains in this state until the start date arrives. Then it transitions to the running state.

## See Also

- [WKExtendedRuntimeSessionState.notStarted](wkextendedruntimesessionstate/notstarted.md)
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.running](wkextendedruntimesessionstate/running.md)
  The session is actively running.
- [WKExtendedRuntimeSessionState.invalid](wkextendedruntimesessionstate/invalid.md)
  Either the session has encountered an error, or it has stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled)*