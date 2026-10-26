# xpc_session_cancel

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Cancels a session, discarding any unsent messages.

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
extern void xpc_session_cancel(xpc_session_t session);
```

#### Discussion

When you cancel a session, it discards any unsent messages and invalidates its connection. If there are messages awaiting replies, the session calls the reply handlers with an appropriate [`xpc_rich_error_t`](./xpc_rich_error_t.md).

## Parameters

- `session`: The session to cancel.

## See Also

### Managing life cycle
- [xpc_session_activate](./xpc_session_activate.md)
  Activates a session so you can send messages.
- [xpc_session_set_incoming_message_handler](./xpc_session_set_incoming_message_handler.md)
  Sets a handler to receive incoming messages for a session.
- [xpc_session_incoming_message_handler_t](./xpc_session_incoming_message_handler_t-3eb2a.md)
  A closure that receives an incoming message for a session.
- [xpc_session_set_cancel_handler](./xpc_session_set_cancel_handler.md)
  Sets a handler the session calls when it’s canceled.
- [xpc_session_cancel_handler_t](./xpc_session_cancel_handler_t-7y2lv.md)
  A block the session calls when it’s canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_cancel)*