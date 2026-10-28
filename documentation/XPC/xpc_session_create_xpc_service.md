# xpc_session_create_xpc_service

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Establishes a connection to an XPC service with the name you specify.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```c
extern xpc_session_txpc_session_create_xpc_service(const char *name, dispatch_queue_t target_queue, xpc_session_create_flags_t flags, xpc_rich_error_t*error_out);
```

## Return Value

A new session object if the connection succeeds; otherwise [`nil`](../ObjectiveC/nil-227m0.md) if the service isn’t found or is unavailable. If the connection fails, this method populates the `error_out` parameter, if set, with an error that describes the failure.

## Discussion

By default, the session object this method returns is activated and is ready to accept messages. To create an inactive session, specify [`XPC_SESSION_CREATE_INACTIVE`](./xpc_session_create_flags_t-c.enum/xpc_session_create_inactive.md) in the `flags` parameter.

> ❗ **Important**:  You’re responsible for calling [`xpc_release`](./xpc_release.md) to dispose of the session when it’s no longer needed.

## Parameters

- `name`: The name of the XPC service to connect to.
- `target_queue`: The dispatch queue to use for session events. You can specify a concurrent dispatch queue. If you specify [`nil`](../ObjectiveC/nil-227m0.md), the session uses `DISPATCH_TARGET_QUEUE_DEFAULT`.
- `flags`: Attributes the session uses when establishing the connection.
- `error_out`: If provided, a pointer that receives an error if the connection fails.

## See Also

### Creating a session
- [xpc_session_create_mach_service](./xpc_session_create_mach_service.md)
  Establishes a connection to a launch agent or launch daemon with the name you specify.
- [xpc_session_create_flags_t](./xpc_session_create_flags_t-c.enum.md)
  Options that specify how to create inactive or privileged sessions.
- [xpc_session_set_target_queue](./xpc_session_set_target_queue.md)
  Sets the target dispatch queue on an inactive session for processing messages.
- [xpc_session_copy_description](./xpc_session_copy_description.md)
  Copies the description string of a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_create_xpc_service)*