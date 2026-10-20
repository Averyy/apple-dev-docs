# WKExtendedRuntimeSessionInvalidationReason.none

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The session ended normally.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case none
```

```c
WKExtendedRuntimeSessionInvalidationReasonNone
```

#### Discussion

The system uses this reason when you stop a session by calling its [`invalidate()`](../wkextendedruntimesession/invalidate%28%29.md) method.

## See Also

### Invalidation Reasons
- [WKExtendedRuntimeSessionInvalidationReason.error](./error.md)
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](./sessioninprogress.md)
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](./expired.md)
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](./resignedfrontmost.md)
  The app lost its frontmost status.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](./suppressedbysystem.md)
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none)*