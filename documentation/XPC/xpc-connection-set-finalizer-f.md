# xpc_connection_set_finalizer_f(_:_:)

**Framework**: XPC  
**Kind**: func

Sets the finalizer for the connection.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_set_finalizer_f(_ connection: xpc_connection_t, _ finalizer: xpc_finalizer_t?)
```

#### Discussion

For many uses of context objects, this API allows for a convenient shorthand for freeing them. For example, for a context object allocated with `malloc(3)`:

```swift
xpc_connection_set_finalizer_f(object, free);
```

## Parameters

- `connection`: The connection on which to set the finalizer.
- `finalizer`: The function that will be invoked when the connection’s retain count has dropped to zero and is being torn down.

## See Also

- [func xpc_connection_set_context(xpc_connection_t, UnsafeMutableRawPointer?)](xpc_connection_set_context(_:_:).md)
  Sets a context on the connection.
- [func xpc_connection_get_context(xpc_connection_t) -> UnsafeMutableRawPointer?](xpc_connection_get_context(_:).md)
  Returns the context for the connection.
- [typealias xpc_finalizer_t](xpc_finalizer_t.md)
  A function to invoke when tearing down a connection and freeing its context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_set_finalizer_f(_:_:))*