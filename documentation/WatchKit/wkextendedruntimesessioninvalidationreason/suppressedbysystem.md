# WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The system is in a state that doesn’t allow sessions of this type.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case suppressedBySystem
```

```c
WKExtendedRuntimeSessionInvalidationReasonSuppressedBySystem
```

## See Also

### Invalidation Reasons
- [WKExtendedRuntimeSessionInvalidationReason.error](./error.md)
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.none](./none.md)
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](./sessioninprogress.md)
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](./expired.md)
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](./resignedfrontmost.md)
  The app lost its frontmost status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem)*