# xpc_session_create_flags_t

**Framework**: XPC  
**Kind**: enum  
**Role**: Enumeration

Options that specify how to create inactive or privileged sessions.

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
typedef enum { ... } xpc_session_create_flags_t;
```

## Topics

### Configuration options
- [XPC_SESSION_CREATE_NONE](./xpc_session_create_flags_t-c.enum/xpc_session_create_none.md)
  Configures a new session with default settings.
- [XPC_SESSION_CREATE_INACTIVE](./xpc_session_create_flags_t-c.enum/xpc_session_create_inactive.md)
  Configures a new session in an inactive state.
- [XPC_SESSION_CREATE_MACH_PRIVILEGED](./xpc_session_create_flags_t-c.enum/xpc_session_create_mach_privileged.md)
  Indicates the session is connecting to a service in the privileged Mach bootstrap.

## See Also

### Creating a session
- [xpc_session_create_xpc_service](./xpc_session_create_xpc_service.md)
  Establishes a connection to an XPC service with the name you specify.
- [xpc_session_create_mach_service](./xpc_session_create_mach_service.md)
  Establishes a connection to a launch agent or launch daemon with the name you specify.
- [xpc_session_set_target_queue](./xpc_session_set_target_queue.md)
  Sets the target dispatch queue on an inactive session for processing messages.
- [xpc_session_copy_description](./xpc_session_copy_description.md)
  Copies the description string of a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_create_flags_t-c.enum)*