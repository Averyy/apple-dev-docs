# xpc_listener_create

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Creates the server side of an XPC service using the specified service name.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```c
extern xpc_listener_txpc_listener_create(const char *service, dispatch_queue_t target_queue, xpc_listener_create_flags_t flags, xpc_listener_incoming_session_handler_t incoming_session_handler, xpc_rich_error_t*error_out);
```

## Return Value

If successful, an activated listener ready to accept incoming session requests; otherwise [`nil`](../ObjectiveC/nil-227m0.md).

## Discussion

Listener creation fails if the XPC service is either not found or is unavailable.

Before returning from `incoming_session_handler`, you must do one of the following:

- Call [`xpc_session_set_incoming_message_handler`](./xpc_session_set_incoming_message_handler.md) to set a handler for incoming messages.
- Call [`xpc_session_cancel`](./xpc_session_cancel.md) to cancel the session.

> ❗ **Important**:  Failure to take one of these actions results in an API misuse crash.

When the `incoming_session_handler` returns, the system automatically activates the peer session unless you explicitly cancel it.

You must call [`xpc_release`](./xpc_release.md) and pass the listener when it’s no longer needed.

## Parameters

- `service`: The Mach service or XPC service name that clients use to connect to the service.
- `target_queue`: The dispatch queue that events arrive on. This may be a concurrent queue. If [`nil`](../ObjectiveC/nil-227m0.md), the listeners uses `DISPATCH_TARGET_QUEUE_DEFAULT`.
- `flags`: Configuration options for the listener, such as creating it in an inactive state.
- `incoming_session_handler`: A handler that the system calls when a client connects to the XPC service.
- `error_out`: A pointer that receives an error object if one occurs during creation.

## See Also

### Creating a listener
- [xpc_listener_create_flags_t](./xpc_listener_create_flags_t.md)
  Options that control the listener’s configuration.
- [typealias xpc_listener_incoming_session_handler_t](./xpc_listener_incoming_session_handler_t.md)
  A block that receives an incoming peer session request from a client.
- [xpc_listener_copy_description](./xpc_listener_copy_description.md)
  Copies the description string of a listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_create)*