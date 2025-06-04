# WKExtendedRuntimeSessionState.notStarted

**Framework**: Watchkit  
**Kind**: case

The app has not yet started or scheduled the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case notStarted
```

## Overview

When you instantiate a new session, it stays in the [`WKExtendedRuntimeSessionState.notStarted`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted) state until you call the session’s [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) or [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method.

## See Also

- [WKExtendedRuntimeSessionState.scheduled](scheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled))
- [WKExtendedRuntimeSessionState.running](running.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/running))
- [WKExtendedRuntimeSessionState.invalid](invalid.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted)*