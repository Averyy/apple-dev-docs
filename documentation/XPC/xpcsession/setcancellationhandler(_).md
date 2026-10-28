# setCancellationHandler(_:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method

Sets a closure the session calls when it’s canceled.

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
func setCancellationHandler(_ cancellationHandler: @escaping @Sendable (XPCRichError) -> Void)
```

## Discussion

> ❗ **Important**:  Only call this method on an inactive session.

## Parameters

- `cancellationHandler`: A closure that receives an error indicating why the session was canceled.

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
- [func cancel(reason: String)](./cancel%28reason%29.md)
  Cancels a session, discarding any unsent messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/setcancellationhandler(_:))*