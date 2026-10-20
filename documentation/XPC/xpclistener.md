# XPCListener

**Framework**: XPC  
**Kind**: class  
**Role**: Class

A type that performs tasks for clients across process boundaries.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
class XPCListener
```

## Mentions

- [Creating XPC services](./creating-xpc-services.md)

#### Overview

To implement an XPC service, create a listener and respond to incoming session requests.

## Topics

### Creating a listener
- [init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](./xpclistener/init%28service,targetqueue,options,incomingsessionhandler%29.md)
  Creates the server side of an XPC service using the specified service name.
- [XPCListener.InitializationOptions](./xpclistener/initializationoptions.md)
  Options that control the listener’s configuration, such as if it’s inactive at creation.
- [XPCListener.IncomingSessionRequest](./xpclistener/incomingsessionrequest.md)
  A session request from a client that you accept or reject.
### Managing the life cycle
- [func activate() throws](./xpclistener/activate%28%29.md)
  Activates an inactive listener.
- [func cancel()](./xpclistener/cancel%28%29.md)
  Cancels a listener.
### Handling incoming messages
- [protocol XPCPeerHandler](./xpcpeerhandler.md)
  A type that handles incoming messages from a client and session cancellation.
### Initializers
- [convenience init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, requirement: XPCPeerRequirement, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](./xpclistener/init%28service,targetqueue,options,requirement,incomingsessionhandler%29.md)
  Creates a listener with the service defined by the provided name, and requires that the session peer has the specified requirement.
- [init(targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision)](./xpclistener/init%28targetqueue,options,incomingsessionhandler%29.md)
  Creates an anonymous listener
### Instance Properties
- [var endpoint: XPCEndpoint](./xpclistener/endpoint.md)
  Creates an endpoint from the listener.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interprocess communication
- [Creating XPC services](./creating-xpc-services.md)
  Configure a listener, establish a client session, and exchange messages between processes.
- [class XPCSession](./xpcsession.md)
  A type that sends messages to a server process.
- [struct XPCReceivedMessage](./xpcreceivedmessage.md)
  A type that represents a message sent between a session and a listener.
- [typealias xpc_listener_t](./xpc_listener_t.md)
  A C type that performs tasks for clients across process boundaries.
- [typealias xpc_session_t](./xpc_session_t-10if0.md)
  A C type that sends messages to a server process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener)*