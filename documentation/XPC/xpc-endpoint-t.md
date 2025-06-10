# xpc_endpoint_t

**Framework**: XPC  
**Kind**: typealias

A type that represents a connection in serialized form.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_endpoint_t = xpc_object_t
```

#### Discussion

Unlike a connection, an endpoint is an inert object that doesn’t have any associated runtime activity. So, it is safe to pass an endpoint in a message. Upon receiving an endpoint, the recipient can use [`xpc_connection_create_from_endpoint(_:)`](xpc_connection_create_from_endpoint(_:).md) to create as many distinct connections as necessary.

## See Also

- [func xpc_endpoint_create(xpc_connection_t) -> xpc_endpoint_t](xpc_endpoint_create(_:).md)
  Creates a new endpoint from a connection that is suitable for embedding into messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_endpoint_t)*