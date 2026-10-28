# xpc_listener_copy_description

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Copies the description string of a listener.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```c
extern char *xpc_listener_copy_description(xpc_listener_t listener);
```

## Return Value

A string that describes the listener.

## Discussion

To dispose of the string when it’s no longer needed, call `free()`.

## Parameters

- `listener`: The listener to get the description from.

## See Also

### Creating a listener
- [xpc_listener_create](./xpc_listener_create.md)
  Creates the server side of an XPC service using the specified service name.
- [xpc_listener_create_flags_t](./xpc_listener_create_flags_t.md)
  Options that control the listener’s configuration.
- [typealias xpc_listener_incoming_session_handler_t](./xpc_listener_incoming_session_handler_t.md)
  A block that receives an incoming peer session request from a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_copy_description)*