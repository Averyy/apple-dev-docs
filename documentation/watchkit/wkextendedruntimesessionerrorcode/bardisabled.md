# WKExtendedRuntimeSessionErrorCode.barDisabled

**Framework**: Watchkit  
**Kind**: case

The user has disabled background app refresh.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case barDisabled
```

## Overview

If the user has disabled Background App Refresh for this app, any attempt to schedule a session by calling the [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method fails. The system calls your delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)) method and passes a [`WKExtendedRuntimeSessionInvalidationReason.error`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error) reason with a [`WKExtendedRuntimeSessionErrorCode.barDisabled`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled) error.

Users can turn off Background App Refresh by selecting General > Background App Refresh in the Watch App.

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/unknown))
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](scheduledtoofarinadvance.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance))
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](mustbeactivetostartorschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule))
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](notyetstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted))
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](exceededresourcelimits.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits))
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](notapprovedtoschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled)*