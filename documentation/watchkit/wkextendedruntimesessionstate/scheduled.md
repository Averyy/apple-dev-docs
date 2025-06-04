# WKExtendedRuntimeSessionState.scheduled

**Framework**: WatchKit  
**Kind**: case

The app has scheduled the session to run at a future date.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case scheduled
```

#### Discussion

The session transitions to the [`WKExtendedRuntimeSessionState.scheduled`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled) state when you call the [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method. It remains in this state until the start date arrives. Then it transitions to the running state.

## See Also

- [WKExtendedRuntimeSessionState.notStarted](notstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted))
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.running](running.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/running))
  The session is actively running.
- [WKExtendedRuntimeSessionState.invalid](invalid.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid))
  Either the session has encountered an error, or it has stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled)*