# XPCPeerHandler

**Framework**: XPC  
**Kind**: protocol

A type that handles incoming messages from a client and session cancellation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
protocol XPCPeerHandler : Sendable
```

## Topics

### Receiving client messages
- [func handleIncomingRequest(Self.Input) -> Self.Output?](xpcpeerhandler/handleincomingrequest(_:).md)
  A closure that receives a message from a client and optionally provides a reply.
- [associatedtype Input](xpcpeerhandler/input.md)
  A type that represents a message from a client.
- [associatedtype Output](xpcpeerhandler/output.md)
  A type that represents a response to an incoming request.
### Responding to session cancellation
- [func handleCancellation(error: XPCRichError)](xpcpeerhandler/handlecancellation(error:).md)
  A closure the system invokes when it cancels a session with a client.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerhandler)*