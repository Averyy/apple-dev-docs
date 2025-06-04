# WKExtendedRuntimeSessionInvalidationReason.expired

**Framework**: Watchkit  
**Kind**: case

The session used all of its allocated time.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case expired
```

## Overview

Sessions can only run for a limited amount of time. Each session type has a different time limit. For more information, see the session’s [`expirationDate`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate) property.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error))
- [WKExtendedRuntimeSessionInvalidationReason.none](none.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none))
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](sessioninprogress.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/sessioninprogress))
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](resignedfrontmost.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/resignedfrontmost))
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](suppressedbysystem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/expired)*