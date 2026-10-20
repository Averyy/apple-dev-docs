# WKExtendedRuntimeSessionState.scheduled

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The app has scheduled the session to run at a future date.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case scheduled
```

```c
WKExtendedRuntimeSessionStateScheduled
```

#### Discussion

The session transitions to the [`WKExtendedRuntimeSessionState.scheduled`](./scheduled.md) state when you call the [`start(at:)`](../wkextendedruntimesession/start%28at%29.md) method. It remains in this state until the start date arrives. Then it transitions to the running state.

## See Also

### Session States
- [WKExtendedRuntimeSessionState.notStarted](./notstarted.md)
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.running](./running.md)
  The session is actively running.
- [WKExtendedRuntimeSessionState.invalid](./invalid.md)
  Either the session has encountered an error, or it has stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled)*