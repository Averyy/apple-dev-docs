# extendedRuntimeSessionDidStart(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates that the session has started running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func extendedRuntimeSessionDidStart(_ extendedRuntimeSession: WKExtendedRuntimeSession)
```

```objc
- (void) extendedRuntimeSessionDidStart:(WKExtendedRuntimeSession *) extendedRuntimeSession;
```

#### Discussion

The system calls this method when your session starts running, in response to the [`start()`](../wkextendedruntimesession/start%28%29.md) method, or because a scheduled session’s start date has arrived.

## Parameters

- `extendedRuntimeSession`: The session that started running.

## See Also

### Monitoring State Changes
- [func extendedRuntimeSessionWillExpire(WKExtendedRuntimeSession)](./extendedruntimesessionwillexpire%28_%29.md)
  Indicates that the session is about to expire.
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](./extendedruntimesession%28_,didinvalidatewith,error%29.md)
  Indicates that the session has encountered an error or stopped running.
- [enum WKExtendedRuntimeSessionInvalidationReason](../wkextendedruntimesessioninvalidationreason.md)
  The reasons why a session can become invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:))*