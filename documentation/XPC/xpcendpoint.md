# XPCEndpoint

**Framework**: XPC  
**Kind**: struct

A connection in serialized form.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct XPCEndpoint
```

#### Overview

An `XPCEndpoint` can be passed around in an XPC message. The recipient of `XPCEndpoint` can use [`init(endpoint:targetQueue:options:cancellationHandler:)`](xpcsession/init(endpoint:targetqueue:options:cancellationhandler:).md) to create as many distinct sessions as desired.

Unlike a connection, the endpoint is an inert object that does not have any runtime activity associated with it.

## Topics

### Initializers
- [init(xpc_endpoint_t)](xpcendpoint/init(_:).md)
  Copy-initialize from a C endpoint object.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcendpoint)*