# extendedRuntimeSessionWillExpire(_:)

**Framework**: WatchKit  
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

- [func extendedRuntimeSessionDidStart(WKExtendedRuntimeSession)](extendedruntimesessiondidstart(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:)))
  Indicates that the session has started running.
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](extendedruntimesession(_:didinvalidatewith:error:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)))
  Indicates that the session has encountered an error or stopped running.
- [enum WKExtendedRuntimeSessionInvalidationReason](wkextendedruntimesessioninvalidationreason.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason))
  The reasons why a session can become invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire(_:))*