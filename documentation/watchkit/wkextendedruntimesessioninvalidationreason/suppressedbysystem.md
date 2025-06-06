# WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem

**Framework**: Watchkit  
**Kind**: case

The system is in a state that doesn’t allow sessions of this type.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case suppressedBySystem
```

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](wkextendedruntimesessioninvalidationreason/error.md)
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.none](wkextendedruntimesessioninvalidationreason/none.md)
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](wkextendedruntimesessioninvalidationreason/sessioninprogress.md)
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](wkextendedruntimesessioninvalidationreason/expired.md)
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](wkextendedruntimesessioninvalidationreason/resignedfrontmost.md)
  The app lost its frontmost status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem)*