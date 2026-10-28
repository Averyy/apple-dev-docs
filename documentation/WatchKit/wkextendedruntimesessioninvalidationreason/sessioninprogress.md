# WKExtendedRuntimeSessionInvalidationReason.sessionInProgress

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

This app already has a running session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case sessionInProgress
```

```c
WKExtendedRuntimeSessionInvalidationReasonSessionInProgress
```

## Discussion

Each app can only run one extended runtime session at a time.

## See Also

### Invalidation Reasons
- [WKExtendedRuntimeSessionInvalidationReason.error](./error.md)
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.none](./none.md)
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.expired](./expired.md)
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](./resignedfrontmost.md)
  The app lost its frontmost status.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](./suppressedbysystem.md)
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/sessioninprogress)*