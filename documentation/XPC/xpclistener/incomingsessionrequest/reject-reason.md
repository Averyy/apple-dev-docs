# reject(reason:)

**Framework**: XPC  
**Kind**: method

Rejects an incoming client session request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func reject(reason: String) -> XPCListener.IncomingSessionRequest.Decision
```

#### Return Value

A decision that indicates that the request was canceled.

## Parameters

- `reason`: A description of why the listener rejected the request.

## See Also

- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](xpclistener/incomingsessionrequest/accept(_:)-73k8w.md)
  Accepts an incoming session request from a client, delegating incoming encodable messages to a separate object.
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](xpclistener/incomingsessionrequest/accept(_:)-35eh9.md)
  Accepts an incoming session request from a client, delegating incoming received messages to a separate object.
- [func accept<Handler>((XPCSession) -> Handler) -> XPCListener.IncomingSessionRequest.Decision](xpclistener/incomingsessionrequest/accept(_:)-tkrp.md)
  Accepts an incoming session request from a client, delegating incoming dictionary messages to a separate object.
- [func accept<Message>(incomingMessageHandler: (Message) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-56fch.md)
  Accepts an incoming session request from a client using closures to handle encodable messages or cancellation, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCReceivedMessage) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-9oa3z.md)
  Accepts an incoming session request from a client using closures to handle received messages or cancellation, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCDictionary) -> XPCDictionary?, cancellationHandler: ((XPCRichError) -> Void)?) -> XPCListener.IncomingSessionRequest.Decision](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-8rodk.md)
  Accepts an incoming session request from a client using closures to handle dictionary messages or cancellation, and returns the inactive session.
- [func accept<Message>(incomingMessageHandler: (Message) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-50tzb.md)
  Accepts an incoming session request from a client using a closure to handle encodable messages, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCReceivedMessage) -> (any Encodable)?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-6oelg.md)
  Accepts an incoming session request from a client using a closure to handle received messages, and returns the inactive session.
- [func accept(incomingMessageHandler: (XPCDictionary) -> XPCDictionary?, cancellationHandler: ((XPCRichError) -> Void)?) -> (XPCListener.IncomingSessionRequest.Decision, XPCSession)](xpclistener/incomingsessionrequest/accept(incomingmessagehandler:cancellationhandler:)-48c3k.md)
  Accepts an incoming session request from a client using a closure to handle dictionary messages, and returns the inactive session.
- [XPCListener.IncomingSessionRequest.Decision](xpclistener/incomingsessionrequest/decision.md)
  An opaque type that indicates whether a listener accepts or rejects an incoming session request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/incomingsessionrequest/reject(reason:))*