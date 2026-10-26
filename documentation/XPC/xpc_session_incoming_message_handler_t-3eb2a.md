# xpc_session_incoming_message_handler_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A closure that receives an incoming message for a session.

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
typedef void (^)(NSObject<OS_xpc_object> *) xpc_session_incoming_message_handler_t;
```

## Parameters

- `message`: The message that the session received.

## See Also

### Managing life cycle
- [xpc_session_activate](./xpc_session_activate.md)
  Activates a session so you can send messages.
- [xpc_session_set_incoming_message_handler](./xpc_session_set_incoming_message_handler.md)
  Sets a handler to receive incoming messages for a session.
- [xpc_session_cancel](./xpc_session_cancel.md)
  Cancels a session, discarding any unsent messages.
- [xpc_session_set_cancel_handler](./xpc_session_set_cancel_handler.md)
  Sets a handler the session calls when it’s canceled.
- [xpc_session_cancel_handler_t](./xpc_session_cancel_handler_t-7y2lv.md)
  A block the session calls when it’s canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_incoming_message_handler_t-3eb2a)*