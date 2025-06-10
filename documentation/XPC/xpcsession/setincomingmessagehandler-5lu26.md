# setIncomingMessageHandler(_:)

**Framework**: XPC  
**Kind**: method

Sets a closure to receive incoming received messages for a session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
func setIncomingMessageHandler(_ incomingMessageHandler: @escaping (XPCReceivedMessage) -> (any Encodable)?)
```

#### Discussion

> ❗ **Important**:  Only call this method on an inactive session.

## Parameters

- `incomingMessageHandler`: A closure that the session invokes when it receives messages. The closure has a parameter that contains the message from the client, and optionally returns an encodable reply message to returns to the client. If the closure returns  , you can use   to reply asynchronously after the closure completes.

## See Also

- [func activate() throws](xpcsession/activate.md)
  Activates a session so you can send messages.
- [func setIncomingMessageHandler<Message>((Message) -> (any Encodable)?)](xpcsession/setincomingmessagehandler(_:)-2ukdh.md)
  Sets a closure to receive incoming decodable messages for a session.
- [func setIncomingMessageHandler((XPCDictionary) -> XPCDictionary?)](xpcsession/setincomingmessagehandler(_:)-75ou9.md)
  Sets a closure to receive incoming dictionary messages for a session.
- [func cancel(reason: String)](xpcsession/cancel(reason:).md)
  Cancels a session, discarding any unsent messages.
- [func setCancellationHandler((XPCRichError) -> Void)](xpcsession/setcancellationhandler(_:).md)
  Sets a closure the session calls when it’s canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/setincomingmessagehandler(_:)-5lu26)*