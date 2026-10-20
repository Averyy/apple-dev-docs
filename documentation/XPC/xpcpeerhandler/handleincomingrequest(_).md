# handleIncomingRequest(_:)

**Framework**: XPC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A closure that receives a message from a client and optionally provides a reply.

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
func handleIncomingRequest(_: Self.Input) -> Self.Output?
```

#### Return Value

A response message, if any, to send back to the client; otherwise [`nil`](../../ObjectiveC/nil-227m0.md).

#### Discussion

If the closure returns [`nil`](../../ObjectiveC/nil-227m0.md), you can still send use [`send(message:)`](../xpcsession/send%28message%29.md) to send an asynchronous reply after handling the message.

## See Also

### Receiving client messages
- [associatedtype Input](./input.md)
  A type that represents a message from a client.
- [associatedtype Output](./output.md)
  A type that represents a response to an incoming request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerhandler/handleincomingrequest(_:))*