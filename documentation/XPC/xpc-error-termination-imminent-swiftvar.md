# XPC_ERROR_TERMINATION_IMMINENT

**Framework**: Xpc  
**Kind**: var

An error that sends to a peer connection’s event handler when the XPC runtime determines that the program needs to exit and that all outstanding transactions must wind down.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
var XPC_ERROR_TERMINATION_IMMINENT: xpc_object_t { get }
```

#### Discussion

This error will be delivered to a peer connection’s event handler when the XPC runtime has determined that the program should exit and that all outstanding transactions must be wound down, and no new transactions can be opened.

After this error has been delivered to the event handler, no more messages will be received by the connection. The runtime will still attempt to deliver outgoing messages, but this error should be treated as an indication that the program will exit very soon, and any outstanding business over the connection should be wrapped up as quickly as possible and the connection canceled shortly thereafter.

This error will only be delivered to peer connections received through a listener or the [`xpc_main(_:)`](xpc_main(_:).md) event handler.

## See Also

- [var XPC_ERROR_CONNECTION_INVALID: xpc_object_t](xpc_error_connection_invalid-swift.var.md)
  An error that sends to the connection’s event handler to indicate that the connection is no longer usable.
- [var XPC_ERROR_CONNECTION_INTERRUPTED: xpc_object_t](xpc_error_connection_interrupted-swift.var.md)
  An error that sends to the connection’s event handler when the remote service exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_error_termination_imminent-swift.var)*