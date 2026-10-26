# xpc_session_activate

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Activates a session so you can send messages.

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
extern bool xpc_session_activate(xpc_session_t session, xpc_rich_error_t*error_out);
```

#### Return Value

`YES` if the session was activated; otherwise `NO`.

#### Discussion

> ❗ **Important**:  Don’t call [`xpc_session_activate`](./xpc_session_activate.md) with a session that’s already active.

If you create an inactive session using the [`XPC_SESSION_CREATE_INACTIVE`](./xpc_session_create_flags_t-c.enum/xpc_session_create_inactive.md) flag, you must activate it before releasing the last reference to the session. Releasing the last reference to an inactive session causes the process to crash.

If activation fails, the system automatically cancels the session.

## Parameters

- `session`: An inactive session to activate.
- `error_out`: If provided, a pointer that receives an error if activating the session fails.

## See Also

### Managing life cycle
- [xpc_session_set_incoming_message_handler](./xpc_session_set_incoming_message_handler.md)
  Sets a handler to receive incoming messages for a session.
- [xpc_session_incoming_message_handler_t](./xpc_session_incoming_message_handler_t-3eb2a.md)
  A closure that receives an incoming message for a session.
- [xpc_session_cancel](./xpc_session_cancel.md)
  Cancels a session, discarding any unsent messages.
- [xpc_session_set_cancel_handler](./xpc_session_set_cancel_handler.md)
  Sets a handler the session calls when it’s canceled.
- [xpc_session_cancel_handler_t](./xpc_session_cancel_handler_t-7y2lv.md)
  A block the session calls when it’s canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_activate)*