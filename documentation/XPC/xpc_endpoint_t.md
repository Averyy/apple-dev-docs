# xpc_endpoint_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A type that represents a connection in serialized form.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias xpc_endpoint_t = xpc_object_t
```

```c
typedef xpc_object_t xpc_endpoint_t;
```

#### Discussion

Unlike a connection, an endpoint is an inert object that doesn’t have any associated runtime activity. So, it is safe to pass an endpoint in a message. Upon receiving an endpoint, the recipient can use [`xpc_connection_create_from_endpoint(_:)`](./xpc_connection_create_from_endpoint%28_%29.md) to create as many distinct connections as necessary.

## See Also

### Endpoints
- [func xpc_endpoint_create(xpc_connection_t) -> xpc_endpoint_t](./xpc_endpoint_create%28_%29.md)
  Creates a new endpoint from a connection that is suitable for embedding into messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_endpoint_t)*