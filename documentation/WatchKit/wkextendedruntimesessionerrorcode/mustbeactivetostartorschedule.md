# WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The watchOS app attempted to start or schedule a session while not in an active state.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case mustBeActiveToStartOrSchedule
```

```c
WKExtendedRuntimeSessionErrorMustBeActiveToStartOrSchedule
```

## Discussion

You can only start or schedule sessions when the watchOS app is running in the foreground. Specifically, the WatchKit extension’s [`applicationState`](../wkextension/applicationstate.md) must equal [`WKApplicationState.active`](../wkapplicationstate/active.md).

## See Also

### Error Codes
- [WKExtendedRuntimeSessionErrorCode.unknown](./unknown.md)
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](./scheduledtoofarinadvance.md)
  The app attempted to schedule a session too far in the future.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule)*