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

The app called the [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()) method on a session before calling its [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) method.

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/unknown))
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](scheduledtoofarinadvance.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance))
  The app attempted to schedule a session too far in the future.
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](mustbeactivetostartorschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule))
  The watchOS app attempted to start or schedule a session while not in an active state.
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](exceededresourcelimits.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits))
  The session exceeded its resource limits.
- [WKExtendedRuntimeSessionErrorCode.barDisabled](bardisabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled))
  The user has disabled background app refresh.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))
  The app attempted to start a session, but doesn’t have a valid session type.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](notapprovedtoschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule))
  The app attempted to schedule a session, but the session type does not support scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted)*