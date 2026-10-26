# xpc_session_reply_handler_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A block that receives the reply to a message a session sends.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef void (^)(NSObject<OS_xpc_object> *, NSObject<OS_xpc_object> *) xpc_session_reply_handler_t;
```

## Parameters

- `reply`: The object the destination service sends back.
- `error`: An error, if one occurs while sending a message.

## See Also

### Sending messages
- [xpc_session_send_message](./xpc_session_send_message.md)
  Sends a message over the session to the destination service.
- [xpc_session_send_message_with_reply_async](./xpc_session_send_message_with_reply_async.md)
  Sends a message asynchronously over the session to the destination service, calling a handler after receiving a reply.
- [xpc_session_send_message_with_reply_sync](./xpc_session_send_message_with_reply_sync.md)
  Sends a message over the session to the destination service, blocking the caller until receiving a reply.
- [typealias xpc_rich_error_t](./xpc_rich_error_t.md)
  A type that describes an error, and whether you can retry the operation that experienced the error.
- [func xpc_rich_error_can_retry(xpc_rich_error_t) -> Bool](./xpc_rich_error_can_retry%28_%29.md)
  Returns a Boolean that indicates whether you can retry the operation that experienced an error.
- [func xpc_rich_error_copy_description(xpc_rich_error_t) -> UnsafeMutablePointer<CChar>?](./xpc_rich_error_copy_description%28_%29.md)
  Copies the string description of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_reply_handler_t-7kfe4)*