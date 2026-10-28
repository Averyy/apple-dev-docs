# WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The app attempted to schedule a session, but the session type does not support scheduling.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notApprovedToSchedule
```

```c
WKExtendedRuntimeSessionErrorNotApprovedToSchedule
```

## Discussion

You can schedule alarm sessions by calling the session’s [`start(at:)`](../wkextendedruntimesession/start%28at%29.md) method. For all other session types, use the [`start()`](../wkextendedruntimesession/start%28%29.md) method instead.

## See Also

### Error Codes
- [WKExtendedRuntimeSessionErrorCode.unknown](./unknown.md)
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](./scheduledtoofarinadvance.md)
  The app attempted to schedule a session too far in the future.
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](./mustbeactivetostartorschedule.md)
  The watchOS app attempted to start or schedule a session while not in an active state.
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](./notyetstarted.md)
  The app invalidated the session before it started.
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](./exceededresourcelimits.md)
  The session exceeded its resource limits.
- [WKExtendedRuntimeSessionErrorCode.barDisabled](./bardisabled.md)
  The user has disabled background app refresh.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](./notapprovedtostartsession.md)
  The app attempted to start a session, but doesn’t have a valid session type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule)*