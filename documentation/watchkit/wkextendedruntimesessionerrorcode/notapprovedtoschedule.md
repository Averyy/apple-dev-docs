# WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule

**Framework**: Watchkit  
**Kind**: case

The app attempted to schedule a session, but the session type does not support scheduling.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notApprovedToSchedule
```

## Overview

You can schedule alarm sessions by calling the session’s [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method. For all other session types, use the [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) method instead.

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/unknown))
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](scheduledtoofarinadvance.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance))
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](mustbeactivetostartorschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule))
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](notyetstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted))
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](exceededresourcelimits.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits))
- [WKExtendedRuntimeSessionErrorCode.barDisabled](bardisabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled))
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule)*