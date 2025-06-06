# xpc_session_t

**Framework**: Xpc  
**Kind**: typealias

A C type that sends messages to a server process.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_session_t = OS_xpc_session
```

#### Discussion

XPC sessions are stateful connections you use to send structured messages to a separate process. Once established, a session remains active until one side of the connection cancels it, at which point the system invalidates the connection. Unlike lower-level `xpc_connection` functions, the system makes no attempt to reestablish a connection or relaunch the service.

## Topics

### Creating a session
- [typealias xpc_session_t](xpc_session_t-49tiv.md)
- [func xpc_session_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](xpc_session_create_mach_service(_:_:_:_:).md)
- [func xpc_session_create_xpc_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](xpc_session_create_xpc_service(_:_:_:_:).md)
- [struct xpc_session_create_flags_t](xpc_session_create_flags_t-swift.struct.md)
- [func xpc_session_copy_description(any OS_xpc_object) -> UnsafeMutablePointer<CChar>?](xpc_session_copy_description(_:).md)
- [func xpc_session_set_target_queue(any OS_xpc_object, dispatch_queue_t?)](xpc_session_set_target_queue(_:_:).md)
### Managing life cycle
- [func xpc_session_activate(any OS_xpc_object, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> Bool](xpc_session_activate(_:_:).md)
- [func xpc_session_cancel(any OS_xpc_object)](xpc_session_cancel(_:).md)
- [func xpc_session_set_cancel_handler(any OS_xpc_object, xpc_session_cancel_handler_t)](xpc_session_set_cancel_handler(_:_:).md)
- [func xpc_session_set_incoming_message_handler(any OS_xpc_object, xpc_session_incoming_message_handler_t)](xpc_session_set_incoming_message_handler(_:_:).md)
  Sets a handler to receive incoming messages for a session.
- [typealias xpc_session_incoming_message_handler_t](xpc_session_incoming_message_handler_t-elj.md)
- [typealias xpc_session_cancel_handler_t](xpc_session_cancel_handler_t-65b6f.md)
### Sending messages
- [typealias xpc_rich_error_t](xpc_rich_error_t.md)
  A type that describes an error, and whether you can retry the operation that experienced the error.
- [func xpc_rich_error_can_retry(xpc_rich_error_t) -> Bool](xpc_rich_error_can_retry(_:).md)
  Returns a Boolean that indicates whether you can retry the operation that experienced an error.
- [func xpc_rich_error_copy_description(xpc_rich_error_t) -> UnsafeMutablePointer<CChar>?](xpc_rich_error_copy_description(_:).md)
  Copies the string description of an error.
- [func xpc_session_send_message(any OS_xpc_object, xpc_object_t) -> xpc_rich_error_t?](xpc_session_send_message(_:_:).md)
- [func xpc_session_send_message_with_reply_async(any OS_xpc_object, xpc_object_t, xpc_session_reply_handler_t)](xpc_session_send_message_with_reply_async(_:_:_:).md)
- [typealias xpc_session_reply_handler_t](xpc_session_reply_handler_t-2hf7c.md)
- [func xpc_session_send_message_with_reply_sync(any OS_xpc_object, xpc_object_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> xpc_object_t?](xpc_session_send_message_with_reply_sync(_:_:_:).md)
### Working with code signing
- [func xpc_session_set_peer_code_signing_requirement(xpc_session_t, UnsafePointer<CChar>) -> Int32](xpc_session_set_peer_code_signing_requirement(_:_:).md)

## See Also

- [Creating XPC services](creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCListener](xpclistener.md)
  A type that performs tasks for clients across process boundaries.
- [class XPCSession](xpcsession.md)
  A type that sends messages to a server process.
- [struct XPCReceivedMessage](xpcreceivedmessage.md)
  A type that represents a message sent between a session and a listener.
- [typealias xpc_listener_t](xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_t-10if0)*