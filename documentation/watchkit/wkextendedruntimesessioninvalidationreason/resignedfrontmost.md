# WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost

**Framework**: WatchKit  
**Kind**: case

The app lost its frontmost status.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case resignedFrontmost
```

#### Discussion

If the session type doesn’t grant background execution time, the session stops as soon as the app loses its frontmost app status. Users can dismiss the frontmost app by pressing the Digital Crown, tapping a notification, or launching another app. For more information, see `Understand Frontmost App State`.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.error](error.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error))
  An error prevented the session from running.
- [WKExtendedRuntimeSessionInvalidationReason.none](none.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/none))
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](sessioninprogress.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/sessioninprogress))
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](expired.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/expired))
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](suppressedbysystem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/suppressedbysystem))
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/resignedfrontmost)*