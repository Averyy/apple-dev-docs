# XPCSession

**Framework**: Xpc  
**Kind**: class

A type that sends messages to a server process.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
class XPCSession
```

#### Overview

XPC sessions are stateful connections you use to send structured messages to a separate process. Once established, a session remains active until one side of the connection cancels it, at which point the system invalidates the connection.

## Topics

### Creating a session
- [convenience init<Message>(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((Message) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-407h2.md)
  Establishes a connection to an XPC service with the name and decodable message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-9f4u0.md)
  Establishes a connection to an XPC service with the name and received message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-bel3.md)
  Establishes a connection to an XPC service with the name and dictionary message handler you specify.
- [convenience init(xpcService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(xpcservice:targetqueue:options:cancellationhandler:).md)
  Establishes a connection to an XPC service with the name you specify.
- [convenience init<Message>(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((Message) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-l3rz.md)
  Establishes a connection to a launch agent or launch daemon with the name and decodable message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCReceivedMessage) -> (any Encodable)?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-2xuyi.md)
  Establishes a connection to a launch agent or launch daemon with the name and received message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, incomingMessageHandler: ((XPCDictionary) -> XPCDictionary?)?, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:incomingmessagehandler:cancellationhandler:)-6jz7y.md)
  Establishes a connection to a launch agent or launch daemon with the name and dictionary message handler you specify.
- [convenience init(machService: String, targetQueue: DispatchQueue?, options: XPCSession.InitializationOptions, cancellationHandler: ((XPCRichError) -> Void)?) throws](xpcsession/init(machservice:targetqueue:options:cancellationhandler:).md)
  Establishes a connection to a launch agent or launch daemon with the name you specify.
- [XPCSession.InitializationOptions](xpcsession/initializationoptions.md)
  Options that control the session’s configuration.
- [func setTargetQueue(DispatchQueue)](xpcsession/settargetqueue(_:).md)
  Sets the target dispatch queue on an inactive session for processing messages.
### Managing the life cycle
- [func activate() throws](xpcsession/activate.md)
  Activates a session so you can send messages.
- [func setIncomingMessageHandler<Message>((Message) -> (any Encodable)?)](xpcsession/setincomingmessagehandler(_:)-2ukdh.md)
  Sets a closure to receive incoming decodable messages for a session.
- [func setIncomingMessageHandler((XPCReceivedMessage) -> (any Encodable)?)](xpcsession/setincomingmessagehandler(_:)-5lu26.md)
  Sets a closure to receive incoming received messages for a session.
- [func setIncomingMessageHandler((XPCDictionary) -> XPCDictionary?)](xpcsession/setincomingmessagehandler(_:)-75ou9.md)
  Sets a closure to receive incoming dictionary messages for a session.
- [func cancel(reason: String)](xpcsession/cancel(reason:).md)
  Cancels a session, discarding any unsent messages.
- [func setCancellationHandler((XPCRichError) -> Void)](xpcsession/setcancellationhandler(_:).md)
  Sets a closure the session calls when it’s canceled.
### Sending messages
- [func send<Message>(Message) throws](xpcsession/send(_:).md)
  Sends an encodable message over the session to the destination service.
- [func send<Message>(Message, replyHandler: (Result<XPCReceivedMessage, XPCRichError>) -> Void) throws](xpcsession/send(_:replyhandler:)-3wjln.md)
  Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply and rich error.
- [func send<Message, Reply>(Message, replyHandler: (Result<Reply, any Error>) -> Void) throws](xpcsession/send(_:replyhandler:)-9an0u.md)
  Sends an encodable message over the session to the destination service, using the closure you specify to handle a reply.
- [func send(message: XPCDictionary) throws](xpcsession/send(message:).md)
  Sends a dictionary message over the session to the destination service.
- [func send(message: XPCDictionary, replyHandler: (Result<XPCDictionary, XPCRichError>) -> Void)](xpcsession/send(message:replyhandler:).md)
  Sends a message asynchronously over the session to the destination service, calling a closure after receiving a reply.
- [func sendSync<Message>(Message) throws -> XPCReceivedMessage](xpcsession/sendsync(_:)-8a284.md)
  Sends an encodable message over the session to the destination service, blocking the caller until receiving a reply message.
- [func sendSync<Message, Reply>(Message) throws -> Reply](xpcsession/sendsync(_:)-88u0s.md)
  Sends an encodable message over the session to the destination service, blocking the caller until receiving an encodable reply message.
- [func sendSync(message: XPCDictionary) throws -> XPCDictionary](xpcsession/sendsync(message:).md)
  Sends a dictionary message over the session to the destination service, blocking the caller until receiving a reply.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)

## See Also

- [Creating XPC services](creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCListener](xpclistener.md)
  A type that performs tasks for clients across process boundaries.
- [struct XPCReceivedMessage](xpcreceivedmessage.md)
  A type that represents a message sent between a session and a listener.
- [typealias xpc_listener_t](xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.
- [typealias xpc_session_t](xpc_session_t-10if0.md)
  A C type that sends messages to a server process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession)*