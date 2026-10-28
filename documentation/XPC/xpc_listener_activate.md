# xpc_listener_activate

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Activates an inactive listener.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```c
extern bool xpc_listener_activate(xpc_listener_t listener, xpc_rich_error_t*error_out);
```

## Return Value

`YES` if the listener was activated; otherwise `NO`.

## Discussion

> ❗ **Important**:  Don’t call [`xpc_listener_activate`](./xpc_listener_activate.md) with a listener that’s already active.

If you create an inactive listener using the [`XPC_LISTENER_CREATE_INACTIVE`](./xpc_listener_create_flags_t/xpc_listener_create_inactive.md) flag, be sure to activate it before releasing the last reference to the listener. Releasing the last reference to an inactive listener crashes.

If activation fails, the system automatically cancels the listener.

## Parameters

- `listener`: The inactive listener to activate.
- `error_out`: If provided, a pointer that receives an error if activation fails.

## See Also

### Managing the life cycle
- [xpc_listener_cancel](./xpc_listener_cancel.md)
  Cancels a listener.
- [xpc_listener_reject_peer](./xpc_listener_reject_peer.md)
  Rejects an incoming peer session request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_activate)*