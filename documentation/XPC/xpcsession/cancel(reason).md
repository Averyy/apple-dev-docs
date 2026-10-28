# cancel(reason:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Cancels a session, discarding any unsent messages.

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
func cancel(reason: String)
```

## Discussion

When you cancel a session, it discards any unsent messages and invalidates its connection. If there are messages awaiting replies, the session calls the reply handlers with an appropriate [`XPCRichError`](../xpcricherror.md).

## Parameters

- `reason`: A description that explains why cancellation occured.

## See Also

### Managing the life cycle
- [func activate() throws](./activate%28%29.md)
  Activates a session so you can send messages.
- [func setIncomingMessageHandler<Message>((Message) -> (any Encodable)?)](./setincomingmessagehandler%28_%29-2ukdh.md)
  Sets a closure to receive incoming decodable messages for a session.
- [func setIncomingMessageHandler((XPCReceivedMessage) -> (any Encodable)?)](./setincomingmessagehandler%28_%29-5lu26.md)
  Sets a closure to receive incoming received messages for a session.
- [func setIncomingMessageHandler((XPCDictionary) -> XPCDictionary?)](./setincomingmessagehandler%28_%29-75ou9.md)
  Sets a closure to receive incoming dictionary messages for a session.
- [func setCancellationHandler((XPCRichError) -> Void)](./setcancellationhandler%28_%29.md)
  Sets a closure the session calls when it’s canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/cancel(reason:))*