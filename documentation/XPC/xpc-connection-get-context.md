# xpc_connection_get_context(_:)

**Framework**: XPC  
**Kind**: func

Returns the context for the connection.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_get_context(_ connection: xpc_connection_t) -> UnsafeMutableRawPointer?
```

#### Return Value

The context associated with the connection. `NULL` if there has been no context associated with the object.

## Parameters

- `connection`: The connection which is to be examined.

## See Also

- [func xpc_connection_set_context(xpc_connection_t, UnsafeMutableRawPointer?)](xpc_connection_set_context(_:_:).md)
  Sets a context on the connection.
- [func xpc_connection_set_finalizer_f(xpc_connection_t, xpc_finalizer_t?)](xpc_connection_set_finalizer_f(_:_:).md)
  Sets the finalizer for the connection.
- [typealias xpc_finalizer_t](xpc_finalizer_t.md)
  A function to invoke when tearing down a connection and freeing its context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_get_context(_:))*