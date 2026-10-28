# WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The app attempted to schedule a session too far in the future.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case scheduledTooFarInAdvance
```

```c
WKExtendedRuntimeSessionErrorScheduledTooFarInAdvance
```

## Discussion

You can’t schedule alarm sessions more than 36 hours in advance. Other session types do not support scheduling.

## See Also

### Error Codes
- [WKExtendedRuntimeSessionErrorCode.unknown](./unknown.md)
  An unknown error occurred.
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
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](./notapprovedtoschedule.md)
  The app attempted to schedule a session, but the session type does not support scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance)*