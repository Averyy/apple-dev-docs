# WKExtendedRuntimeSessionState.notStarted

**Framework**: WatchKit  
**Kind**: case

The app has not yet started or scheduled the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notStarted
```

#### Discussion

When you instantiate a new session, it stays in the [`WKExtendedRuntimeSessionState.notStarted`](wkextendedruntimesessionstate/notstarted.md) state until you call the session’s [`start()`](wkextendedruntimesession/start().md) or [`start(at:)`](wkextendedruntimesession/start(at:).md) method.

## See Also

- [WKExtendedRuntimeSessionState.scheduled](wkextendedruntimesessionstate/scheduled.md)
  The app has scheduled the session to run at a future date.
- [WKExtendedRuntimeSessionState.running](wkextendedruntimesessionstate/running.md)
  The session is actively running.
- [WKExtendedRuntimeSessionState.invalid](wkextendedruntimesessionstate/invalid.md)
  Either the session has encountered an error, or it has stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted)*