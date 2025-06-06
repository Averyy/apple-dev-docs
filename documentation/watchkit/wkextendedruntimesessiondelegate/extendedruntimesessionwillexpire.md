# extendedRuntimeSessionWillExpire(_:)

**Framework**: Watchkit  
**Kind**: method  
**Required**: Yes

Indicates that the session is about to expire.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func extendedRuntimeSessionWillExpire(_ extendedRuntimeSession: WKExtendedRuntimeSession)
```

#### Discussion

The system only grants each session a limited amount of time to run. The system calls this method just before reaching that limit. Implement this method to finish any tasks and clean up before the session ends.

## Parameters

- `extendedRuntimeSession`: The session that is about to expire.

## See Also

- [func extendedRuntimeSessionDidStart(WKExtendedRuntimeSession)](wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:).md)
  Indicates that the session has started running.
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:).md)
  Indicates that the session has encountered an error or stopped running.
- [enum WKExtendedRuntimeSessionInvalidationReason](wkextendedruntimesessioninvalidationreason.md)
  The reasons why a session can become invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire(_:))*