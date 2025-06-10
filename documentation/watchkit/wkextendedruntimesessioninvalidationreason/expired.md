# WKExtendedRuntimeSessionInvalidationReason.expired

**Framework**: WatchKit  
**Kind**: case

The session used all of its allocated time.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case expired
```

#### Discussion

Sessions can only run for a limited amount of time. Each session type has a different time limit. For more information, see the session’s [`expirationDate`](wkextendedruntimesession/expirationdate.md) property.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](wkextendedruntimesessioninvalidationreason/error.md)
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.none](wkextendedruntimesessioninvalidationreason/none.md)
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](wkextendedruntimesessioninvalidationreason/sessioninprogress.md)
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](wkextendedruntimesessioninvalidationreason/resignedfrontmost.md)
  The app lost its frontmost status.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](wkextendedruntimesessioninvalidationreason/suppressedbysystem.md)
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/expired)*