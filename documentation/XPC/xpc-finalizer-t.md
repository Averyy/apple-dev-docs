# xpc_finalizer_t

**Framework**: XPC  
**Kind**: typealias

A function to invoke when tearing down a connection and freeing its context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_finalizer_t = (UnsafeMutableRawPointer?) -> Void
```

#### Discussion

It is not safe to reference the connection from within this function.

## Parameters

- `value`: The context object that is to be disposed of.

## See Also

- [func xpc_connection_set_context(xpc_connection_t, UnsafeMutableRawPointer?)](xpc_connection_set_context(_:_:).md)
  Sets a context on the connection.
- [func xpc_connection_get_context(xpc_connection_t) -> UnsafeMutableRawPointer?](xpc_connection_get_context(_:).md)
  Returns the context for the connection.
- [func xpc_connection_set_finalizer_f(xpc_connection_t, xpc_finalizer_t?)](xpc_connection_set_finalizer_f(_:_:).md)
  Sets the finalizer for the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_finalizer_t)*