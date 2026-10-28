# XPCListener.IncomingSessionRequest

**Framework**: XPC  
**Kind**: class  
**Role**: Class

A session request from a client that you accept or reject.

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
class IncomingSessionRequest
```

## Mentions

- [Creating XPC services](../creating-xpc-services.md)

## Overview

When a client initiates a connection to a listener, the system passes the incoming session request to the listener. In response, the listener calls one of the `accept` methods to complete the connection with the client, or it rejects the request.

## Topics

### Responding to client sessions requests
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/accept%28_%29-73k8w.md)
  Accepts an incoming session request from a client, delegating incoming encodable messages to a separate object.
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/accept%28_%29-35eh9.md)
  Accepts an incoming session request from a client, delegating incoming received messages to a separate object.
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/accept%28_%29-tkrp.md)
  Accepts an incoming session request from a client, delegating incoming dictionary messages to a separate object.
- [func accept<Message>(incomingMessageHandler: (Message) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/accept%28incomingmessagehandler,cancellationhandler%29-56fch.md)
  Accepts an incoming session request from a client using closures to handle encodable messages or cancellation, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCReceivedMessage) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/accept%28incomingmessagehandler,cancellationhandler%29-9oa3z.md)
  Accepts an incoming session request from a client using closures to handle received messages or cancellation, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCDictionary) -> XPCDictionary?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/accept%28incomingmessagehandler,cancellationhandler%29-8rodk.md)
  Accepts an incoming session request from a client using closures to handle dictionary messages or cancellation, and returns the inactive session.
- [func accept<Message>(incomingMessageHandler: (Message) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](./incomingsessionrequest/accept%28incomingmessagehandler,cancellationhandler%29-50tzb.md)
  Accepts an incoming session request from a client using a closure to handle encodable messages, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCReceivedMessage) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](./incomingsessionrequest/accept%28incomingmessagehandler,cancellationhandler%29-6oelg.md)
  Accepts an incoming session request from a client using a closure to handle received messages, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCDictionary) -> XPCDictionary?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](./incomingsessionrequest/accept%28incomingmessagehandler,cancellationhandler%29-48c3k.md)
  Accepts an incoming session request from a client using a closure to handle dictionary messages, and returns the inactive session.
- [func reject(reason: String) -> XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/reject%28reason%29.md)
  Rejects an incoming client session request.
- [XPCListener.IncomingSessionRequest.Decision](./incomingsessionrequest/decision.md)
  An opaque type that indicates whether a listener accepts or rejects an incoming session request.

## See Also

### Creating a listener
- [init(service: String, targetQueue: DispatchQueue?, options: XPCListener.InitializationOptions, incomingSessionHandler: (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws](./init%28service,targetqueue,options,incomingsessionhandler%29.md)
  Creates the server side of an XPC service using the specified service name.
- [XPCListener.InitializationOptions](./initializationoptions.md)
  Options that control the listener’s configuration, such as if it’s inactive at creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/incomingsessionrequest)*