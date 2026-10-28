# WKExtendedRuntimeSessionInvalidationReason.error

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

An error prevented the session from running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
case error
```

```c
WKExtendedRuntimeSessionInvalidationReasonError
```

## Discussion

When the system passes this value to your extension delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](../wkextendedruntimesessiondelegate/extendedruntimesession%28_,didinvalidatewith,error%29.md) method, check the `error` parameter for additional information about the error.

## See Also

### Invalidation Reasons
- [WKExtendedRuntimeSessionInvalidationReason.none](./none.md)
  The session ended normally.
- [WKExtendedRuntimeSessionInvalidationReason.sessionInProgress](./sessioninprogress.md)
  This app already has a running session.
- [WKExtendedRuntimeSessionInvalidationReason.expired](./expired.md)
  The session used all of its allocated time.
- [WKExtendedRuntimeSessionInvalidationReason.resignedFrontmost](./resignedfrontmost.md)
  The app lost its frontmost status.
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](./suppressedbysystem.md)
  The system is in a state that doesn’t allow sessions of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason/error)*