# XPCListener

**Framework**: XPC  
**Kind**: class

A type that performs tasks for clients across process boundaries.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
class XPCListener
```

## Mentions

- [Creating XPC services](creating-xpc-services.md)

#### Overview

To implement an XPC service, create a listener and respond to incoming session requests.

## Topics

### Creating a listener
- [init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](xpclistener/init(service:targetqueue:options:incomingsessionhandler:).md)
  Creates the server side of an XPC service using the specified service name.
- [XPCListener.InitializationOptions](xpclistener/initializationoptions.md)
  Options that control the listener’s configuration, such as if it’s inactive at creation.
- [XPCListener.IncomingSessionRequest](xpclistener/incomingsessionrequest.md)
  A session request from a client that you accept or reject.
### Managing the life cycle
- [func activate() throws](xpclistener/activate.md)
  Activates an inactive listener.
- [func cancel()](xpclistener/cancel.md)
  Cancels a listener.
### Handling incoming messages
- [protocol XPCPeerHandler](xpcpeerhandler.md)
  A type that handles incoming messages from a client and session cancellation.
### Structures
- [XPCListener.Endpoint](xpclistener/endpoint-swift.struct.md)
### Initializers
- [convenience init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, requirement: XPCPeerRequirement, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](xpclistener/init(service:targetqueue:options:requirement:incomingsessionhandler:).md)
  Creates a listener with the service defined by the provided name, and requires that the session peer has the specified requirement.
- [init(targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)](xpclistener/init(targetqueue:options:incomingsessionhandler:).md)
  Creates an anonymous listener
### Instance Properties
- [var endpoint: XPCListener.Endpoint](xpclistener/endpoint-swift.property.md)
  Creates an endpoint from the listener.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating XPC services](creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCSession](xpcsession.md)
  A type that sends messages to a server process.
- [struct XPCReceivedMessage](xpcreceivedmessage.md)
  A type that represents a message sent between a session and a listener.
- [typealias xpc_listener_t](xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.
- [typealias xpc_session_t](xpc_session_t-10if0.md)
  A C type that sends messages to a server process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener)*