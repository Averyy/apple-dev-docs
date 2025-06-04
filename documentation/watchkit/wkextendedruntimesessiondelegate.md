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

- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))

## Overview

Implement these methods to track the changes to your session’s state.

## Topics

### Monitoring State Changes
- [func extendedRuntimeSessionDidStart(WKExtendedRuntimeSession)](extendedruntimesessiondidstart(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:)))
  Indicates that the session has started running.
- [func extendedRuntimeSessionWillExpire(WKExtendedRuntimeSession)](extendedruntimesessionwillexpire(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire(_:)))
  Indicates that the session is about to expire.
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](extendedruntimesession(_:didinvalidatewith:error:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)))
  Indicates that the session has encountered an error or stopped running.
- [enum WKExtendedRuntimeSessionInvalidationReason](wkextendedruntimesessioninvalidationreason.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason))
  The reasons why a session can become invalid.

## Relationships

### Inherits From
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [var delegate: (any WKExtendedRuntimeSessionDelegate)?](delegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/delegate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate)*