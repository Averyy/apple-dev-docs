# WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule

**Framework**: WatchKit  
**Kind**: case

The watchOS app attempted to start or schedule a session while not in an active state.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case mustBeActiveToStartOrSchedule
```

#### Discussion

You can only start or schedule sessions when the watchOS app is running in the foreground. Specifically, the WatchKit extension’s [`applicationState`](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate) must equal [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active).

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/unknown))
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](scheduledtoofarinadvance.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance))
  The app attempted to schedule a session too far in the future.
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](notyetstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted))
  The app invalidated the session before it started.
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](exceededresourcelimits.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits))
  The session exceeded its resource limits.
- [WKExtendedRuntimeSessionErrorCode.barDisabled](bardisabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled))
  The user has disabled background app refresh.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))
  The app attempted to start a session, but doesn’t have a valid session type.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](notapprovedtoschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule))
  The app attempted to schedule a session, but the session type does not support scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule)*