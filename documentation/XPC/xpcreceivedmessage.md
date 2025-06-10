# XPCReceivedMessage

**Framework**: XPC  
**Kind**: struct

A type that represents a message sent between a session and a listener.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
struct XPCReceivedMessage
```

## Mentions

- [Creating XPC services](creating-xpc-services.md)

## Topics

### Accessing message content
- [func decode<T>(as: T.Type) throws -> T](xpcreceivedmessage/decode(as:).md)
  Decodes a message as the given type.
- [var isSync: Bool](xpcreceivedmessage/issync.md)
  A Boolean value that indicates if this message is from a synchronous request.
### Replying to messages
- [var expectsReply: Bool](xpcreceivedmessage/expectsreply.md)
  A Boolean value that indicates if the client that sent the message expects a reply.
- [func reply<Message>(Message)](xpcreceivedmessage/reply(_:).md)
  Sends a reply to the originator of the message.
- [func handoffReply(to: DispatchQueue, () -> Void) -> (any Encodable)?](xpcreceivedmessage/handoffreply(to:_:).md)
  Informs the system when message processing and response continues in a separate dispatch queue.
### Instance Methods
- [func senderSatisfies(XPCPeerRequirement) -> Bool](xpcreceivedmessage/sendersatisfies(_:).md)
  Check whether the sender of the received message satisfies the specified requirement.

## See Also

- [Creating XPC services](creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCListener](xpclistener.md)
  A type that performs tasks for clients across process boundaries.
- [class XPCSession](xpcsession.md)
  A type that sends messages to a server process.
- [typealias xpc_listener_t](xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.
- [typealias xpc_session_t](xpc_session_t-10if0.md)
  A C type that sends messages to a server process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcreceivedmessage)*