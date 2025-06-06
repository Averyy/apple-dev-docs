# expectsReply

**Framework**: Xpc  
**Kind**: property

A Boolean value that indicates if the client that sent the message expects a reply.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
var expectsReply: Bool { get }
```

## See Also

- [func reply<Message>(Message)](xpcreceivedmessage/reply(_:).md)
  Sends a reply to the originator of the message.
- [func handoffReply(to: DispatchQueue, () -> Void) -> (any Encodable)?](xpcreceivedmessage/handoffreply(to:_:).md)
  Informs the system when message processing and response continues in a separate dispatch queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcreceivedmessage/expectsreply)*