# xpc_listener_incoming_session_handler_t

**Framework**: Xpc  
**Kind**: typealias

A block that receives an incoming peer session request from a client.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_listener_incoming_session_handler_t = (xpc_session_t) -> Void
```

#### Discussion

When a client connects to your service, the system invokes this block with a session that represents the server’s connection to the client. Before returning from this block, you must do one of the following:

- Call [`xpc_session_set_incoming_message_handler`](xpc_session_set_incoming_message_handler.md) to set a handler for incoming messages.
- Call [`xpc_session_cancel`](xpc_session_cancel.md) to cancel the session.

> ❗ **Important**:  Failure to take one of these actions results in an API misuse crash.

 Failure to take one of these actions results in an API misuse crash.

When the `incoming_session_handler` returns, the system automatically activates the peer session unless you explicitly cancel it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_incoming_session_handler_t)*