# xpc_connection_set_context(_:_:)

**Framework**: Xpc  
**Kind**: func

Sets a context on the connection.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_set_context(_ connection: xpc_connection_t, _ context: UnsafeMutableRawPointer?)
```

#### Discussion

If you must manage the memory of the context object, you must set a finalizer to dispose of it. If this method is called on a connection which already has context associated with it, the finalizer will NOT be invoked. The finalizer is only invoked when the connection is being deallocated.

It is recommended that, instead of changing the actual context pointer associated with the object, you instead change the state of the context object itself.

## Parameters

- `connection`: The connection which is to be manipulated.
- `context`: The context to associate with the connection.

## See Also

- [func xpc_connection_get_context(xpc_connection_t) -> UnsafeMutableRawPointer?](xpc_connection_get_context(_:).md)
  Returns the context for the connection.
- [func xpc_connection_set_finalizer_f(xpc_connection_t, xpc_finalizer_t?)](xpc_connection_set_finalizer_f(_:_:).md)
  Sets the finalizer for the connection.
- [typealias xpc_finalizer_t](xpc_finalizer_t.md)
  A function to invoke when tearing down a connection and freeing its context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_set_context(_:_:))*