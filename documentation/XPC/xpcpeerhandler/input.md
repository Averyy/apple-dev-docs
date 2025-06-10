# Input

**Framework**: XPC  
**Kind**: associatedtype  
**Required**: Yes

A type that represents a message from a client.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
associatedtype Input
```

## See Also

- [func handleIncomingRequest(Self.Input) -> Self.Output?](xpcpeerhandler/handleincomingrequest(_:).md)
  A closure that receives a message from a client and optionally provides a reply.
- [associatedtype Output](xpcpeerhandler/output.md)
  A type that represents a response to an incoming request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerhandler/input)*