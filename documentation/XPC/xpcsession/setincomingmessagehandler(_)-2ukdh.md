# setIncomingMessageHandler(_:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Sets a closure to receive incoming decodable messages for a session.

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
@preconcurrency
func setIncomingMessageHandler<Message>(_ incomingMessageHandler: @escaping @Sendable (Message) -> (any Encodable)?) where Message : Decodable
```

## Discussion

> ❗ **Important**:  Only call this method on an inactive session.

## Parameters

- `incomingMessageHandler`: A closure that the session invokes when it receives messages. The closure has a parameter that contains the message from the client, and optionally returns an encodable reply message to returns to the client. If the closure returns [`nil`](../../ObjectiveC/nil-227m0.md), you can use [`send(message:)`](./send%28message%29.md) to reply asynchronously after the closure completes.

## See Also

### Managing the life cycle
- [func activate() throws](./activate%28%29.md)
  Activates a session so you can send messages.
- [func setIncomingMessageHandler((XPCReceivedMessage) -> (any Encodable)?)](./setincomingmessagehandler%28_%29-5lu26.md)
  Sets a closure to receive incoming received messages for a session.
- [func setIncomingMessageHandler((XPCDictionary) -> XPCDictionary?)](./setincomingmessagehandler%28_%29-75ou9.md)
  Sets a closure to receive incoming dictionary messages for a session.
- [func cancel(reason: String)](./cancel%28reason%29.md)
  Cancels a session, discarding any unsent messages.
- [func setCancellationHandler((XPCRichError) -> Void)](./setcancellationhandler%28_%29.md)
  Sets a closure the session calls when it’s canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/setincomingmessagehandler(_:)-2ukdh)*