# WKExtendedRuntimeSessionDelegate

**Framework**: Watchkit  
**Kind**: protocol

A set of optional methods for monitoring an extended runtime session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
protocol WKExtendedRuntimeSessionDelegate : NSObjectProtocol
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md)

#### Overview

Implement these methods to track the changes to your session’s state.

## Topics

### Monitoring State Changes
- [func extendedRuntimeSessionDidStart(WKExtendedRuntimeSession)](wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:).md)
  Indicates that the session has started running.
- [func extendedRuntimeSessionWillExpire(WKExtendedRuntimeSession)](wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire(_:).md)
  Indicates that the session is about to expire.
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:).md)
  Indicates that the session has encountered an error or stopped running.
- [enum WKExtendedRuntimeSessionInvalidationReason](wkextendedruntimesessioninvalidationreason.md)
  The reasons why a session can become invalid.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any WKExtendedRuntimeSessionDelegate)?](wkextendedruntimesession/delegate.md)
  A delegate object for monitoring the session and responding to state changes and errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate)*