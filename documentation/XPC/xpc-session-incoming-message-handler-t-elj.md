# xpc_session_incoming_message_handler_t

**Framework**: Xpc  
**Kind**: typealias

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
typealias xpc_session_incoming_message_handler_t = (xpc_object_t) -> Void
```

## See Also

- [func xpc_session_activate(any OS_xpc_object, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> Bool](xpc_session_activate(_:_:).md)
- [func xpc_session_cancel(any OS_xpc_object)](xpc_session_cancel(_:).md)
- [func xpc_session_set_cancel_handler(any OS_xpc_object, xpc_session_cancel_handler_t)](xpc_session_set_cancel_handler(_:_:).md)
- [func xpc_session_set_incoming_message_handler(any OS_xpc_object, xpc_session_incoming_message_handler_t)](xpc_session_set_incoming_message_handler(_:_:).md)
  Sets a handler to receive incoming messages for a session.
- [typealias xpc_session_cancel_handler_t](xpc_session_cancel_handler_t-65b6f.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_incoming_message_handler_t-elj)*