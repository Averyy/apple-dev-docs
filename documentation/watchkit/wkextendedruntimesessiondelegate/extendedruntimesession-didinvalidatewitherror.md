# extendedRuntimeSession(_:didInvalidateWith:error:)

**Framework**: WatchKit  
**Kind**: method  
**Required**: Yes

Indicates that the session has encountered an error or stopped running.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func extendedRuntimeSession(_ extendedRuntimeSession: WKExtendedRuntimeSession, didInvalidateWith reason: WKExtendedRuntimeSessionInvalidationReason, error: (any Error)?)
```

#### Discussion

The system calls this method both when a session fails to start and when a session stops running. Use the invalidation reason to determine why the session became invalid.

> ❗ **Important**:  If your app terminates immediately after the system invalidates the session, you may not receive this delegate call until the user launches your app again. In that case, the system calls your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-4qxgv) method to resume the session. Then, after you assign the session delegate, the system finally makes this delegate call.

 If your app terminates immediately after the system invalidates the session, you may not receive this delegate call until the user launches your app again. In that case, the system calls your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-4qxgv) method to resume the session. Then, after you assign the session delegate, the system finally makes this delegate call.

## Parameters

- `extendedRuntimeSession`: The session that became invalid.
- `reason`: The reason the session became invalid.
- `error`: If the   parameter is  , then this parameter contains additional information about the error. Otherwise it is set to  .

## See Also

- [func extendedRuntimeSessionDidStart(WKExtendedRuntimeSession)](extendedruntimesessiondidstart(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessiondidstart(_:)))
  Indicates that the session has started running.
- [func extendedRuntimeSessionWillExpire(WKExtendedRuntimeSession)](extendedruntimesessionwillexpire(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesessionwillexpire(_:)))
  Indicates that the session is about to expire.
- [enum WKExtendedRuntimeSessionInvalidationReason](wkextendedruntimesessioninvalidationreason.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessioninvalidationreason))
  The reasons why a session can become invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:))*