# Output

**Framework**: XPC  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type that represents a response to an incoming request.

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
associatedtype Output
```

## See Also

### Receiving client messages
- [func handleIncomingRequest(Self.Input) -> Self.Output?](./handleincomingrequest%28_%29.md)
  A closure that receives a message from a client and optionally provides a reply.
- [associatedtype Input](./input.md)
  A type that represents a message from a client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerhandler/output)*