# xpc_handler_t

**Framework**: XPC  
**Kind**: typealias

The type of block that the XPC connection APIs accept.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_handler_t = (xpc_object_t) -> Void
```

#### Discussion

You aren’t responsible for releasing the event object.

## See Also

- [func xpc_connection_set_event_handler(xpc_connection_t, (xpc_object_t) -> Void)](xpc_connection_set_event_handler(_:_:).md)
  Sets the event handler block for the connection.
- [typealias xpc_connection_handler_t](xpc_connection_handler_t.md)
  The type of the function to invoke for a bundled XPC service when there’s a new connection on the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_handler_t)*