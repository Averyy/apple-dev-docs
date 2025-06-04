# WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule

**Framework**: Watchkit  
**Kind**: case

The watchOS app attempted to start or schedule a session while not in an active state.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case mustBeActiveToStartOrSchedule
```

## Overview

You can only start or schedule sessions when the watchOS app is running in the foreground. Specifically, the WatchKit extension’s [`applicationState`](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate) must equal [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active).

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/unknown))
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](scheduledtoofarinadvance.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance))
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](notyetstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted))
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](exceededresourcelimits.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits))
- [WKExtendedRuntimeSessionErrorCode.barDisabled](bardisabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled))
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](notapprovedtoschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule)*