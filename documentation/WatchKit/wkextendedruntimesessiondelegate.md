# WKExtendedRuntimeSessionDelegate

**Framework**: WatchKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods for monitoring an extended runtime session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
protocol WKExtendedRuntimeSessionDelegate : NSObjectProtocol
```

```objc
@protocol WKExtendedRuntimeSessionDelegate <NSObject>
```

## Mentions

- [Using extended runtime sessions](./using-extended-runtime-sessions.md)

## Overview

Implement these methods to track the changes to your session’s state.

## Topics

### Monitoring State Changes
- [func extendedRuntimeSessionDidStart(WKExtendedRuntimeSession)](./wkextendedruntimesessiondelegate/extendedruntimesessiondidstart%28_%29.md)
  Indicates that the session has started running.
- [func extendedRuntimeSessionWillExpire(WKExtendedRuntimeSession)](./wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire%28_%29.md)
  Indicates that the session is about to expire.
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](./wkextendedruntimesessiondelegate/extendedruntimesession%28_,didinvalidatewith,error%29.md)
  Indicates that the session has encountered an error or stopped running.
- [enum WKExtendedRuntimeSessionInvalidationReason](./wkextendedruntimesessioninvalidationreason.md)
  The reasons why a session can become invalid.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a Session
- [var delegate: (any WKExtendedRuntimeSessionDelegate)?](./wkextendedruntimesession/delegate.md)
  A delegate object for monitoring the session and responding to state changes and errors.
- [+ session](./wkextendedruntimesession/session.md)
  Instantiates a new session object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate)*