# setCancellationHandler(_:)

**Framework**: XPC  
**Kind**: method

Sets a closure the session calls when it’s canceled.

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
func setCancellationHandler(_ cancellationHandler: @escaping (XPCRichError) -> Void)
```

#### Discussion

> ❗ **Important**:  Only call this method on an inactive session.

## Parameters

- `cancellationHandler`: A closure that receives an error indicating why the session was canceled.

## See Also

- [func activate() throws](xpcsession/activate.md)
  Activates a session so you can send messages.
- [func setIncomingMessageHandler<Message>((Message) -> (any Encodable)?)](xpcsession/setincomingmessagehandler(_:)-2ukdh.md)
  Sets a closure to receive incoming decodable messages for a session.
- [func setIncomingMessageHandler((XPCReceivedMessage) -> (any Encodable)?)](xpcsession/setincomingmessagehandler(_:)-5lu26.md)
  Sets a closure to receive incoming received messages for a session.
- [func setIncomingMessageHandler((XPCDictionary) -> XPCDictionary?)](xpcsession/setincomingmessagehandler(_:)-75ou9.md)
  Sets a closure to receive incoming dictionary messages for a session.
- [func cancel(reason: String)](xpcsession/cancel(reason:).md)
  Cancels a session, discarding any unsent messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/setcancellationhandler(_:))*