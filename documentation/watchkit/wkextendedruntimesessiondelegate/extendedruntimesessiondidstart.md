# extendedRuntimeSessionDidStart(_:)

**Framework**: Watchkit  
**Kind**: method  
**Required**: Yes

Indicates that the session has started running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func extendedRuntimeSessionDidStart(_ extendedRuntimeSession: WKExtendedRuntimeSession)
```

## Overview

The system calls this method when your session starts running, in response to the [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) method, or because a scheduled session’s start date has arrived.

## Parameters

- `extendedRuntimeSession`: The session that started running.

## See Also

- [func extendedRuntimeSessionWillExpire(WKExtendedRuntimeSession)](extendedruntimesessionwillexpire(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire(_:)))
- [func extendedRuntimeSession(WKExtendedRuntimeSession, didInvalidateWith: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)](extendedruntimesession(_:didinvalidatewith:error:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:)))
- [enum WKExtendedRuntimeSessionInvalidationReason](wkextendedruntimesessioninvalidationreason.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:))*