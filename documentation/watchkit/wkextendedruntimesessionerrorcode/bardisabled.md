# WKExtendedRuntimeSessionErrorCode.barDisabled

**Framework**: WatchKit  
**Kind**: case

The user has disabled background app refresh.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case barDisabled
```

#### Discussion

If the user has disabled Background App Refresh for this app, any attempt to schedule a session by calling the [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method fails. The system calls your delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)) method and passes a [`WKExtendedRuntimeSessionInvalidationReason.error`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error) reason with a [`WKExtendedRuntimeSessionErrorCode.barDisabled`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled) error.

Users can turn off Background App Refresh by selecting General > Background App Refresh in the Watch App.

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
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))
  The app attempted to start a session, but doesn’t have a valid session type.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](notapprovedtoschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule))
  The app attempted to schedule a session, but the session type does not support scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled)*