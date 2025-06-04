# WKExtendedRuntimeSessionErrorCode.notYetStarted

**Framework**: Watchkit  
**Kind**: case

The app invalidated the session before it started.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notYetStarted
```

## Overview

The app called the [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()) method on a session before calling its [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) method.

## See Also

- [WKExtendedRuntimeSessionErrorCode.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/unknown))
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](scheduledtoofarinadvance.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/scheduledtoofarinadvance))
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](mustbeactivetostartorschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule))
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](exceededresourcelimits.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits))
- [WKExtendedRuntimeSessionErrorCode.barDisabled](bardisabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/bardisabled))
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](notapprovedtostartsession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtostartsession))
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](notapprovedtoschedule.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notapprovedtoschedule))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/notyetstarted)*