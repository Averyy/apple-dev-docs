# WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule

**Framework**: WatchKit  
**Kind**: case

The app attempted to schedule a session, but the session type does not support scheduling.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notApprovedToSchedule
```

#### Discussion

You can schedule alarm sessions by calling the session’s [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method. For all other session types, use the [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) method instead.

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/unknown))
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](scheduledtoofarinadvance.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance))
  The app attempted to schedule a session too far in the future.
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](mustbeactivetostartorschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule))
  The watchOS app attempted to start or schedule a session while not in an active state.
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](notyetstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted))
  The app invalidated the session before it started.
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](exceededresourcelimits.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits))
  The session exceeded its resource limits.
- [WKExtendedRuntimeSessionErrorCode.barDisabled](bardisabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled))
  The user has disabled background app refresh.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))
  The app attempted to start a session, but doesn’t have a valid session type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule)*