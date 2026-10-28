# xpc_session_send_message_with_reply_async

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Sends a message asynchronously over the session to the destination service, calling a handler after receiving a reply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
extern void xpc_session_send_message_with_reply_async(xpc_session_t session, xpc_object_t message, xpc_session_reply_handler_t reply_handler);
```

## Discussion

If the system tears down the session’s connection before receiving a reply, it invokes `reply_handler` with an [`xpc_rich_error_t`](./xpc_rich_error_t.md) describing the failure. For example, if the remote service exits prematurely before sending a reply.

> ❗ **Important**:  If you create an inactive session, you must activate it before sending messages. Calling this method with an inactive session crashes.

## Parameters

- `session`: The session that represents the destination service.
- `message`: A dictionary object that contains the message to send.
- `reply_handler`: A closure the session invokes with the reply it receives.

## See Also

### Sending messages
- [xpc_session_send_message](./xpc_session_send_message.md)
  Sends a message over the session to the destination service.
- [xpc_session_reply_handler_t](./xpc_session_reply_handler_t-7kfe4.md)
  A block that receives the reply to a message a session sends.
- [xpc_session_send_message_with_reply_sync](./xpc_session_send_message_with_reply_sync.md)
  Sends a message over the session to the destination service, blocking the caller until receiving a reply.
- [typealias xpc_rich_error_t](./xpc_rich_error_t.md)
  A type that describes an error, and whether you can retry the operation that experienced the error.
- [func xpc_rich_error_can_retry(xpc_rich_error_t) -> Bool](./xpc_rich_error_can_retry%28_%29.md)
  Returns a Boolean that indicates whether you can retry the operation that experienced an error.
- [func xpc_rich_error_copy_description(xpc_rich_error_t) -> UnsafeMutablePointer<CChar>?](./xpc_rich_error_copy_description%28_%29.md)
  Copies the string description of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_send_message_with_reply_async)*