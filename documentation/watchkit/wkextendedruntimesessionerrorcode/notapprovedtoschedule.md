# WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule

**Framework**: Watchkit  
**Kind**: case

The app attempted to schedule a session, but the session type does not support scheduling.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notApprovedToSchedule
```

#### Discussion

You can schedule alarm sessions by calling the session’s [`start(at:)`](wkextendedruntimesession/start(at:).md) method. For all other session types, use the [`start()`](wkextendedruntimesession/start().md) method instead.

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](wkextendedruntimesessionerrorcode/unknown.md)
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](wkextendedruntimesessionerrorcode/scheduledtoofarinadvance.md)
  The app attempted to schedule a session too far in the future.
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule.md)
  The watchOS app attempted to start or schedule a session while not in an active state.
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](wkextendedruntimesessionerrorcode/notyetstarted.md)
  The app invalidated the session before it started.
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](wkextendedruntimesessionerrorcode/exceededresourcelimits.md)
  The session exceeded its resource limits.
- [WKExtendedRuntimeSessionErrorCode.barDisabled](wkextendedruntimesessionerrorcode/bardisabled.md)
  The user has disabled background app refresh.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](wkextendedruntimesessionerrorcode/notapprovedtostartsession.md)
  The app attempted to start a session, but doesn’t have a valid session type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule)*