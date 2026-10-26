# xpc_session_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A C type that sends messages to a server process.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias xpc_session_t = OS_xpc_session
```

```c
typedef NSObject<OS_xpc_session> * xpc_session_t;
```

#### Discussion

XPC sessions are stateful connections you use to send structured messages to a separate process. Once established, a session remains active until one side of the connection cancels it, at which point the system invalidates the connection. Unlike lower-level `xpc_connection` functions, the system makes no attempt to reestablish a connection or relaunch the service.

## Topics

### Creating a session
- [typealias xpc_session_t](./xpc_session_t-49tiv.md)
- [func xpc_session_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](./xpc_session_create_mach_service%28_,_,_,_%29.md)
- [func xpc_session_create_xpc_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](./xpc_session_create_xpc_service%28_,_,_,_%29.md)
- [struct xpc_session_create_flags_t](./xpc_session_create_flags_t-swift.struct.md)
- [func xpc_session_copy_description(any OS_xpc_object) -> UnsafeMutablePointer<CChar>?](./xpc_session_copy_description%28_%29.md)
- [func xpc_session_set_target_queue(any OS_xpc_object, dispatch_queue_t?)](./xpc_session_set_target_queue%28_,_%29.md)
- [xpc_session_create_xpc_service](./xpc_session_create_xpc_service.md)
  Establishes a connection to an XPC service with the name you specify.
- [xpc_session_create_mach_service](./xpc_session_create_mach_service.md)
  Establishes a connection to a launch agent or launch daemon with the name you specify.
- [xpc_session_create_flags_t](./xpc_session_create_flags_t-c.enum.md)
  Options that specify how to create inactive or privileged sessions.
- [xpc_session_set_target_queue](./xpc_session_set_target_queue.md)
  Sets the target dispatch queue on an inactive session for processing messages.
- [xpc_session_copy_description](./xpc_session_copy_description.md)
  Copies the description string of a session.
### Managing life cycle
- [func xpc_session_activate(any OS_xpc_object, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> Bool](./xpc_session_activate%28_,_%29.md)
- [func xpc_session_cancel(any OS_xpc_object)](./xpc_session_cancel%28_%29.md)
- [func xpc_session_set_cancel_handler(any OS_xpc_object, xpc_session_cancel_handler_t)](./xpc_session_set_cancel_handler%28_,_%29.md)
- [func xpc_session_set_incoming_message_handler(any OS_xpc_object, xpc_session_incoming_message_handler_t)](./xpc_session_set_incoming_message_handler%28_,_%29.md)
  Sets a handler to receive incoming messages for a session.
- [typealias xpc_session_incoming_message_handler_t](./xpc_session_incoming_message_handler_t-elj.md)
- [typealias xpc_session_cancel_handler_t](./xpc_session_cancel_handler_t-65b6f.md)
- [xpc_session_activate](./xpc_session_activate.md)
  Activates a session so you can send messages.
- [xpc_session_set_incoming_message_handler](./xpc_session_set_incoming_message_handler.md)
  Sets a handler to receive incoming messages for a session.
- [xpc_session_incoming_message_handler_t](./xpc_session_incoming_message_handler_t-3eb2a.md)
  A closure that receives an incoming message for a session.
- [xpc_session_cancel](./xpc_session_cancel.md)
  Cancels a session, discarding any unsent messages.
- [xpc_session_set_cancel_handler](./xpc_session_set_cancel_handler.md)
  Sets a handler the session calls when it’s canceled.
- [xpc_session_cancel_handler_t](./xpc_session_cancel_handler_t-7y2lv.md)
  A block the session calls when it’s canceled.
### Sending messages
- [typealias xpc_rich_error_t](./xpc_rich_error_t.md)
  A type that describes an error, and whether you can retry the operation that experienced the error.
- [func xpc_rich_error_can_retry(xpc_rich_error_t) -> Bool](./xpc_rich_error_can_retry%28_%29.md)
  Returns a Boolean that indicates whether you can retry the operation that experienced an error.
- [func xpc_rich_error_copy_description(xpc_rich_error_t) -> UnsafeMutablePointer<CChar>?](./xpc_rich_error_copy_description%28_%29.md)
  Copies the string description of an error.
- [func xpc_session_send_message(any OS_xpc_object, xpc_object_t) -> xpc_rich_error_t?](./xpc_session_send_message%28_,_%29.md)
- [func xpc_session_send_message_with_reply_async(any OS_xpc_object, xpc_object_t, xpc_session_reply_handler_t)](./xpc_session_send_message_with_reply_async%28_,_,_%29.md)
- [typealias xpc_session_reply_handler_t](./xpc_session_reply_handler_t-2hf7c.md)
- [func xpc_session_send_message_with_reply_sync(any OS_xpc_object, xpc_object_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> xpc_object_t?](./xpc_session_send_message_with_reply_sync%28_,_,_%29.md)
- [xpc_session_send_message](./xpc_session_send_message.md)
  Sends a message over the session to the destination service.
- [xpc_session_send_message_with_reply_async](./xpc_session_send_message_with_reply_async.md)
  Sends a message asynchronously over the session to the destination service, calling a handler after receiving a reply.
- [xpc_session_reply_handler_t](./xpc_session_reply_handler_t-7kfe4.md)
  A block that receives the reply to a message a session sends.
- [xpc_session_send_message_with_reply_sync](./xpc_session_send_message_with_reply_sync.md)
  Sends a message over the session to the destination service, blocking the caller until receiving a reply.
### Working with code signing
- [func xpc_session_set_peer_code_signing_requirement(xpc_session_t, UnsafePointer<CChar>) -> Int32](./xpc_session_set_peer_code_signing_requirement%28_,_%29.md)

## See Also

### Interprocess communication
- [Creating XPC services](./creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCListener](./xpclistener.md)
  A type that performs tasks for clients across process boundaries.
- [class XPCSession](./xpcsession.md)
  A type that sends messages to a server process.
- [struct XPCReceivedMessage](./xpcreceivedmessage.md)
  A type that represents a message sent between a session and a listener.
- [typealias xpc_listener_t](./xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_t-10if0)*