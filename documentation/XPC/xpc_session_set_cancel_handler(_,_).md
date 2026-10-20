# xpc_session_set_cancel_handler(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 16.0+ - Deprecated in 17.0 (renamed: setCancellationHandler())
- macOS 13.0+ - Deprecated in 14.0 (renamed: setCancellationHandler())

## Declaration

```swift
func xpc_session_set_cancel_handler(_ session: any OS_xpc_object, _ cancel_handler: @escaping xpc_session_cancel_handler_t)
```

## See Also

### Managing life cycle
- [func xpc_session_activate(any OS_xpc_object, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> Bool](./xpc_session_activate%28_,_%29.md)
- [func xpc_session_cancel(any OS_xpc_object)](./xpc_session_cancel%28_%29.md)
- [func xpc_session_set_incoming_message_handler(any OS_xpc_object, xpc_session_incoming_message_handler_t)](./xpc_session_set_incoming_message_handler%28_,_%29.md)
  Sets a handler to receive incoming messages for a session.
- [typealias xpc_session_incoming_message_handler_t](./xpc_session_incoming_message_handler_t-elj.md)
- [typealias xpc_session_cancel_handler_t](./xpc_session_cancel_handler_t-65b6f.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_set_cancel_handler(_:_:))*