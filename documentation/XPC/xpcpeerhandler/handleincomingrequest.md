# handleIncomingRequest(_:)

**Framework**: XPC  
**Kind**: method  
**Required**: Yes

A closure that receives a message from a client and optionally provides a reply.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func handleIncomingRequest(_: Self.Input) -> Self.Output?
```

#### Return Value

A response message, if any, to send back to the client; otherwise [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0).

#### Discussion

If the closure returns [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0), you can still send use [`send(message:)`](xpcsession/send(message:).md) to send an asynchronous reply after handling the message.

## See Also

- [associatedtype Input](xpcpeerhandler/input.md)
  A type that represents a message from a client.
- [associatedtype Output](xpcpeerhandler/output.md)
  A type that represents a response to an incoming request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerhandler/handleincomingrequest(_:))*