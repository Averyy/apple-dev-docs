# XPC_SESSION_CREATE_INACTIVE

**Framework**: XPC  
**Kind**: case  
**Role**: Enumeration Case

Configures a new session in an inactive state.

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
XPC_SESSION_CREATE_INACTIVE
```

## Discussion

After creating the session, you must call [`xpc_session_activate`](../xpc_session_activate.md) to activate it before sending messages.

## See Also

### Configuration options
- [XPC_SESSION_CREATE_NONE](./xpc_session_create_none.md)
  Configures a new session with default settings.
- [XPC_SESSION_CREATE_MACH_PRIVILEGED](./xpc_session_create_mach_privileged.md)
  Indicates the session is connecting to a service in the privileged Mach bootstrap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_create_flags_t-c.enum/xpc_session_create_inactive)*