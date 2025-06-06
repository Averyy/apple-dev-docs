# WKExtendedRuntimeSessionInvalidationReason.error

**Framework**: Watchkit  
**Kind**: case

An error prevented the session from running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case error
```

#### Discussion

When the system passes this value to your extension delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:).md) method, check the `error` parameter for additional information about the error.

## See Also

- [WKExtendedRuntimeSessionInvalidationReason.none](wkextendedruntimesessioninvalidationreason/none.md)
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](wkextendedruntimesessioninvalidationreason/sessioninprogress.md)
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](wkextendedruntimesessioninvalidationreason/expired.md)
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](wkextendedruntimesessioninvalidationreason/resignedfrontmost.md)
  The app lost its frontmost status.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](wkextendedruntimesessioninvalidationreason/suppressedbysystem.md)
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error)*