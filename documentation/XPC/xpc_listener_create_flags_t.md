# xpc_listener_create_flags_t

**Framework**: XPC  
**Kind**: enum  
**Role**: Enumeration

Options that control the listener’s configuration.

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
typedef enum { ... } xpc_listener_create_flags_t;
```

## Topics

### Listener state
- [XPC_LISTENER_CREATE_INACTIVE](./xpc_listener_create_flags_t/xpc_listener_create_inactive.md)
  Prevents the system from automatically activating the listener after creation.
- [XPC_LISTENER_CREATE_NONE](./xpc_listener_create_flags_t/xpc_listener_create_none.md)
  Configures the listener in a default state.
### Enumeration Cases
- [XPC_LISTENER_CREATE_FORCE_MACH](./xpc_listener_create_flags_t/xpc_listener_create_force_mach.md)
- [XPC_LISTENER_CREATE_FORCE_XPCSERVICE](./xpc_listener_create_flags_t/xpc_listener_create_force_xpcservice.md)

## See Also

### Creating a listener
- [xpc_listener_create](./xpc_listener_create.md)
  Creates the server side of an XPC service using the specified service name.
- [typealias xpc_listener_incoming_session_handler_t](./xpc_listener_incoming_session_handler_t.md)
  A block that receives an incoming peer session request from a client.
- [xpc_listener_copy_description](./xpc_listener_copy_description.md)
  Copies the description string of a listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_create_flags_t)*