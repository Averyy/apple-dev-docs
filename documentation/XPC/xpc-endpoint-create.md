# xpc_endpoint_create(_:)

**Framework**: Xpc  
**Kind**: func

Creates a new endpoint from a connection that is suitable for embedding into messages.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_endpoint_create(_ connection: xpc_connection_t) -> xpc_endpoint_t
```

#### Return Value

A new endpoint object.

## Parameters

- `connection`: Only connections obtained through calls to one of the   functions may be given to this API. Passing any other type of connection is not supported and will result in undefined behavior.

## See Also

- [typealias xpc_endpoint_t](xpc_endpoint_t.md)
  A type that represents a connection in serialized form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_endpoint_create(_:))*