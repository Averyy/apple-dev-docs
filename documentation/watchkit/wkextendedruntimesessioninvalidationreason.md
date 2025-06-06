# WKExtendedRuntimeSessionInvalidationReason

**Framework**: Watchkit  
**Kind**: enum

The reasons why a session can become invalid.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
enum WKExtendedRuntimeSessionInvalidationReason
```

#### Overview

Sessions become invalid when they encounter an error, or when they stop running.

## Topics

### Invalidation Reasons
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
- [WKExtendedRuntimeSessionInvalidationReason.suppressedBySystem](wkextendedruntimesessioninvalidationreason/suppressedbysystem.md)
  The system is in a state that doesn’t allow sessions of this type.
### Initializers
- [init?(rawValue: Int)](wkextendedruntimesessioninvalidationreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func extendedRuntimeSessionDidStart(WKExtendedRuntimeSession)](wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:).md)
  Indicates that the session has started running.
- [func extendedRuntimeSessionWillExpire(WKExtendedRuntimeSession)](wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire(_:).md)
  Indicates that the session is about to expire.
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:).md)
  Indicates that the session has encountered an error or stopped running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason)*