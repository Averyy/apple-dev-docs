# xpc_listener_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A C type that performs tasks for clients across process boundaries.

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
typealias xpc_listener_t = OS_xpc_listener
```

```c
typedef NSObject<OS_xpc_listener> * xpc_listener_t;
```

#### Discussion

To implement an XPC service, create a listener and respond to incoming session requests.

## Topics

### Creating a listener
- [typealias xpc_listener_incoming_session_handler_t](./xpc_listener_incoming_session_handler_t.md)
  A block that receives an incoming peer session request from a client.
- [xpc_listener_create](./xpc_listener_create.md)
  Creates the server side of an XPC service using the specified service name.
- [xpc_listener_create_flags_t](./xpc_listener_create_flags_t.md)
  Options that control the listener’s configuration.
- [xpc_listener_copy_description](./xpc_listener_copy_description.md)
  Copies the description string of a listener.
### Working with code signing
- [func xpc_listener_set_peer_code_signing_requirement(xpc_listener_t, UnsafePointer<CChar>) -> Int32](./xpc_listener_set_peer_code_signing_requirement%28_,_%29.md)
### Managing the life cycle
- [xpc_listener_activate](./xpc_listener_activate.md)
  Activates an inactive listener.
- [xpc_listener_cancel](./xpc_listener_cancel.md)
  Cancels a listener.
- [xpc_listener_reject_peer](./xpc_listener_reject_peer.md)
  Rejects an incoming peer session request.

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
- [typealias xpc_session_t](./xpc_session_t-10if0.md)
  A C type that sends messages to a server process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_t)*