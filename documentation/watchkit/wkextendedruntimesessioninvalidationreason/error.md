# WKExtendedRuntimeSessionInvalidationReason.error

**Framework**: Watchkit  
**Kind**: case

An error prevented the session from running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case error
```

## Overview

When the system passes this value to your extension delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)) method, check the `error` parameter for additional information about the error.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.none](none.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none))
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](sessioninprogress.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/sessioninprogress))
- [WKExtendedRuntimeSessionInvalidationReason.expired](expired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/expired))
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](resignedfrontmost.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/resignedfrontmost))
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](suppressedbysystem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error)*