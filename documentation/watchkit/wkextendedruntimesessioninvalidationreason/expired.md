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

Sessions can only run for a limited amount of time. Each session type has a different time limit. For more information, see the session’s [`expirationDate`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate) property.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error))
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.none](none.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none))
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](sessioninprogress.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/sessioninprogress))
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](resignedfrontmost.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/resignedfrontmost))
  The app lost its frontmost status.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](suppressedbysystem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem))
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/expired)*