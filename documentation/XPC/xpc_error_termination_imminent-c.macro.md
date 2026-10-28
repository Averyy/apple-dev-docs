# XPC_ERROR_TERMINATION_IMMINENT

**Framework**: XPC  
**Kind**: macro  
**Role**: Macro

An error that sends to a peer connection’s event handler when the XPC runtime determines that the program needs to exit and that all outstanding transactions must wind down.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define XPC_ERROR_TERMINATION_IMMINENT
```

## Discussion

This error will be delivered to a peer connection’s event handler when the XPC runtime has determined that the program should exit and that all outstanding transactions must be wound down, and no new transactions can be opened.

After this error has been delivered to the event handler, no more messages will be received by the connection. The runtime will still attempt to deliver outgoing messages, but this error should be treated as an indication that the program will exit very soon, and any outstanding business over the connection should be wrapped up as quickly as possible and the connection canceled shortly thereafter.

This error will only be delivered to peer connections received through a listener or the [`xpc_main(_:)`](./xpc_main%28_%29.md) event handler.

## See Also

### Errors
- [XPC_ERROR_CONNECTION_INVALID](./xpc_error_connection_invalid-c.macro.md)
  An error that sends to the connection’s event handler to indicate that the connection is no longer usable.
- [XPC_ERROR_CONNECTION_INTERRUPTED](./xpc_error_connection_interrupted-c.macro.md)
  An error that sends to the connection’s event handler when the remote service exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_error_termination_imminent-c.macro)*