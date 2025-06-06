# WKExtendedRuntimeSessionInvalidationReason.none

**Framework**: Watchkit  
**Kind**: case

The session ended normally.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case none
```

#### Discussion

The system uses this reason when you stop a session by calling its [`invalidate()`](wkextendedruntimesession/invalidate().md) method.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](wkextendedruntimesessioninvalidationreason/error.md)
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](wkextendedruntimesessioninvalidationreason/sessioninprogress.md)
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](wkextendedruntimesessioninvalidationreason/expired.md)
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](wkextendedruntimesessioninvalidationreason/resignedfrontmost.md)
  The app lost its frontmost status.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](wkextendedruntimesessioninvalidationreason/suppressedbysystem.md)
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none)*