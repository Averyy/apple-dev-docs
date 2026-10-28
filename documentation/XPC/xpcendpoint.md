# XPCEndpoint

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

A connection in serialized form.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
struct XPCEndpoint
```

## Overview

An `XPCEndpoint` can be passed around in an XPC message. The recipient of `XPCEndpoint` can use [`init(endpoint:targetQueue:options:cancellationHandler:)`](./xpcsession/init%28endpoint,targetqueue,options,cancellationhandler%29.md) to create as many distinct sessions as desired.

Unlike a connection, the endpoint is an inert object that does not have any runtime activity associated with it.

## Topics

### Initializers
- [init(xpc_endpoint_t)](./xpcendpoint/init%28_%29.md)
  Copy-initialize from a C endpoint object.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcendpoint)*