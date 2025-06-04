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

If the user has disabled Background App Refresh for this app, any attempt to schedule a session by calling the [`start(at:)`](wkextendedruntimesession/start(at:).md) method fails. The system calls your delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:).md) method and passes a [`WKExtendedRuntimeSessionInvalidationReason.error`](wkextendedruntimesessioninvalidationreason/error.md) reason with a [`WKExtendedRuntimeSessionErrorCode.barDisabled`](wkextendedruntimesessionerrorcode/bardisabled.md) error.

Users can turn off Background App Refresh by selecting General > Background App Refresh in the Watch App.

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
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](wkextendedruntimesessionerrorcode/notapprovedtostartsession.md)
  The app attempted to start a session, but doesn’t have a valid session type.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](wkextendedruntimesessionerrorcode/notapprovedtoschedule.md)
  The app attempted to schedule a session, but the session type does not support scheduling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled)*