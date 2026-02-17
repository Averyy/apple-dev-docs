# WKExtendedRuntimeSessionErrorCode.notYetStarted

**Framework**: WatchKit  
**Kind**: case

The app invalidated the session before it started.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notYetStarted
```

#### Discussion

The app called the [`invalidate()`](wkextendedruntimesession/invalidate().md) method on a session before calling its [`start()`](wkextendedruntimesession/start().md) method.

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](wkextendedruntimesessionerrorcode/unknown.md)
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](wkextendedruntimesessionerrorcode/scheduledtoofarinadvance.md)
  The app attempted to schedule a session too far in the future.
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule.md)
  The watchOS app attempted to start or schedule a session while not in an active state.
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](wkextendedruntimesessionerrorcode/exceededresourcelimits.md)
  The session exceeded its resource limits.
- [WKExtendedRuntimeSessionErrorCode.barDisabled](wkextendedruntimesessionerrorcode/bardisabled.md)
  The user has disabled background app refresh.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](wkextendedruntimesessionerrorcode/notapprovedtostartsession.md)
  The app attempted to start a session, but doesn’t have a valid session type.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](wkextendedruntimesessionerrorcode/notapprovedtoschedule.md)
  The app attempted to schedule a session, but the session type does not support scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted)*