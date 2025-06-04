# WKExtendedRuntimeSessionState.scheduled

**Framework**: Watchkit  
**Kind**: case

The app has scheduled the session to run at a future date.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case scheduled
```

## Overview

The session transitions to the [`WKExtendedRuntimeSessionState.scheduled`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled) state when you call the [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method. It remains in this state until the start date arrives. Then it transitions to the running state.

## See Also

- [WKExtendedRuntimeSessionState.notStarted](notstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted))
- [WKExtendedRuntimeSessionState.running](running.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/running))
- [WKExtendedRuntimeSessionState.invalid](invalid.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled)*