# WKExtendedRuntimeSessionState.invalid

**Framework**: Watchkit  
**Kind**: case

Either the session has encountered an error, or it has stopped running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case invalid
```

## Overview

The system passes a [`WKExtendedRuntimeSessionInvalidationReason`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason) value to the session delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)) method. Use this value to determine why the session became invalid.

## See Also

- [WKExtendedRuntimeSessionState.notStarted](notstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted))
- [WKExtendedRuntimeSessionState.scheduled](scheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled))
- [WKExtendedRuntimeSessionState.running](running.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/running))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid)*