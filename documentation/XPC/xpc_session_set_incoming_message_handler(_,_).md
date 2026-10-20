# xpc_session_set_incoming_message_handler(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Sets a handler to receive incoming messages for a session.

**Availability**:
- Mac Catalyst 16.0+ - Deprecated in 17.0 (renamed: setIncomingMessageHandler())
- macOS 13.0+ - Deprecated in 14.0 (renamed: setIncomingMessageHandler())

## Declaration

```swift
func xpc_session_set_incoming_message_handler(_ session: any OS_xpc_object, _ handler: @escaping xpc_session_incoming_message_handler_t)
```

## Parameters

- `session`: The session that receives messages.
- `handler`: A block that the session invokes when it receives messages.

## See Also

### Managing life cycle
- [func xpc_session_activate(any OS_xpc_object, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> Bool](./xpc_session_activate%28_,_%29.md)
- [func xpc_session_cancel(any OS_xpc_object)](./xpc_session_cancel%28_%29.md)
- [func xpc_session_set_cancel_handler(any OS_xpc_object, xpc_session_cancel_handler_t)](./xpc_session_set_cancel_handler%28_,_%29.md)
- [typealias xpc_session_incoming_message_handler_t](./xpc_session_incoming_message_handler_t-elj.md)
- [typealias xpc_session_cancel_handler_t](./xpc_session_cancel_handler_t-65b6f.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_set_incoming_message_handler(_:_:))*