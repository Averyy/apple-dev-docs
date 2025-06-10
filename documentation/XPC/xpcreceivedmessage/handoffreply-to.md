# handoffReply(to:_:)

**Framework**: XPC  
**Kind**: method

Informs the system when message processing and response continues in a separate dispatch queue.

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
func handoffReply(to queue: DispatchQueue, _ continuation: @escaping () -> Void) -> (any Encodable)?
```

#### Return Value

This method always returns `nil`, allowing a message handler closure to return a value.

#### Discussion

You can only call this method from the context of a message handler closure, or from a continuation closure passed to [`handoffReply(to:_:)`](xpcreceivedmessage/handoffreply(to:_:).md).

## Parameters

- `queue`: The dispatch queue where message processing continues. The queue must be an immutible queue hierarchy.
- `continuation`: The closure to perform on  .

## See Also

- [var expectsReply: Bool](xpcreceivedmessage/expectsreply.md)
  A Boolean value that indicates if the client that sent the message expects a reply.
- [func reply<Message>(Message)](xpcreceivedmessage/reply(_:).md)
  Sends a reply to the originator of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcreceivedmessage/handoffreply(to:_:))*