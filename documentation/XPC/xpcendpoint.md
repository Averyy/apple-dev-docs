# XPCEndpoint

**Framework**: XPC  
**Kind**: struct

An `XPCEndpoint` represents a connection in serialized form. Unlike a connection, an endpoint is an inert object that does not have any runtime activity associated with it. Thus, it is safe to pass an endpoint in a message. Upon receiving an endpoint, the recipient can use `XPCSession(endpoint:targetQueue:options:incomingMessageHandler:cancellationHandler)` to create as many distinct sessions as desired.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct XPCEndpoint
```

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcendpoint)*