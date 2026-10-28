# WKExtendedRuntimeSessionState.notStarted

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The app has not yet started or scheduled the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notStarted
```

```c
WKExtendedRuntimeSessionStateNotStarted
```

## Discussion

When you instantiate a new session, it stays in the [`WKExtendedRuntimeSessionState.notStarted`](./notstarted.md) state until you call the session’s [`start()`](../wkextendedruntimesession/start%28%29.md) or [`start(at:)`](../wkextendedruntimesession/start%28at%29.md) method.

## See Also

### Session States
- [WKExtendedRuntimeSessionState.scheduled](./scheduled.md)
  The app has scheduled the session to run at a future date.
- [WKExtendedRuntimeSessionState.running](./running.md)
  The session is actively running.
- [WKExtendedRuntimeSessionState.invalid](./invalid.md)
  Either the session has encountered an error, or it has stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted)*