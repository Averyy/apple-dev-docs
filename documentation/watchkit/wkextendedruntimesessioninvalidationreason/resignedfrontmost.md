# WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost

**Framework**: Watchkit  
**Kind**: case

The app lost its frontmost status.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case resignedFrontmost
```

## Overview

If the session type doesn’t grant background execution time, the session stops as soon as the app loses its frontmost app status. Users can dismiss the frontmost app by pressing the Digital Crown, tapping a notification, or launching another app. For more information, see `Understand Frontmost App State`.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error))
- [WKExtendedRuntimeSessionInvalidationReason.none](none.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none))
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](sessioninprogress.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/sessioninprogress))
- [WKExtendedRuntimeSessionInvalidationReason.expired](expired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/expired))
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](suppressedbysystem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/resignedfrontmost)*