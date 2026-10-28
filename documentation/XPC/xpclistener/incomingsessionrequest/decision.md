# XPCListener.IncomingSessionRequest.Decision

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

An opaque type that indicates whether a listener accepts or rejects an incoming session request.

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
struct Decision
```

## Overview

When you create an [`XPCListener`](../../xpclistener.md), you specify a closure that receives an [`XPCListener.IncomingSessionRequest`](../incomingsessionrequest.md). In that closure, you receive a `Decision` from the call to the request’s accept or reject methods. You don’t have to do anything with the decision other than return it from the closure.

## See Also

### Responding to client sessions requests
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](./accept%28_%29-73k8w.md)
  Accepts an incoming session request from a client, delegating incoming encodable messages to a separate object.
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](./accept%28_%29-35eh9.md)
  Accepts an incoming session request from a client, delegating incoming received messages to a separate object.
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](./accept%28_%29-tkrp.md)
  Accepts an incoming session request from a client, delegating incoming dictionary messages to a separate object.
- [func accept<Message>(incomingMessageHandler: (Message) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](./accept%28incomingmessagehandler,cancellationhandler%29-56fch.md)
  Accepts an incoming session request from a client using closures to handle encodable messages or cancellation, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCReceivedMessage) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](./accept%28incomingmessagehandler,cancellationhandler%29-9oa3z.md)
  Accepts an incoming session request from a client using closures to handle received messages or cancellation, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCDictionary) -> XPCDictionary?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](./accept%28incomingmessagehandler,cancellationhandler%29-8rodk.md)
  Accepts an incoming session request from a client using closures to handle dictionary messages or cancellation, and returns the inactive session.
- [func accept<Message>(incomingMessageHandler: (Message) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](./accept%28incomingmessagehandler,cancellationhandler%29-50tzb.md)
  Accepts an incoming session request from a client using a closure to handle encodable messages, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCReceivedMessage) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](./accept%28incomingmessagehandler,cancellationhandler%29-6oelg.md)
  Accepts an incoming session request from a client using a closure to handle received messages, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCDictionary) -> XPCDictionary?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](./accept%28incomingmessagehandler,cancellationhandler%29-48c3k.md)
  Accepts an incoming session request from a client using a closure to handle dictionary messages, and returns the inactive session.
- [func reject(reason: String) -> XPCListener.IncomingSessionRequest.Decision](./reject%28reason%29.md)
  Rejects an incoming client session request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/incomingsessionrequest/decision)*