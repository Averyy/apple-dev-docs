# WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem

**Framework**: WatchKit  
**Kind**: case

The system is in a state that doesn’t allow sessions of this type.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case suppressedBySystem
```

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error))
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.none](none.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none))
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](sessioninprogress.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/sessioninprogress))
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](expired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/expired))
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](resignedfrontmost.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/resignedfrontmost))
  The app lost its frontmost status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem)*