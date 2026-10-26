# XPC_ERROR_CONNECTION_INTERRUPTED

**Framework**: XPC  
**Kind**: macro  
**Role**: Macro

An error that sends to the connection’s event handler when the remote service exits.

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
#define XPC_ERROR_CONNECTION_INTERRUPTED
```

#### Discussion

Will be delivered to the connection’s event handler if the remote service exited. The connection is still live even in this case, and resending a message will cause the service to be launched on-demand. This error serves as a client’s indication that it should resynchronize any state that it had given the service.

Any messages in the queue to be sent will be unwound and canceled when this error occurs. In the case where a message waiting to be sent has a reply handler, that handler will be invoked with this error. In the context of the reply handler, this error indicates that a reply to the message will never arrive.

Messages that do not have reply handlers associated with them will be silently disposed of. This error will only be given to peer connections.

## See Also

### Errors
- [XPC_ERROR_CONNECTION_INVALID](./xpc_error_connection_invalid-c.macro.md)
  An error that sends to the connection’s event handler to indicate that the connection is no longer usable.
- [XPC_ERROR_TERMINATION_IMMINENT](./xpc_error_termination_imminent-c.macro.md)
  An error that sends to a peer connection’s event handler when the XPC runtime determines that the program needs to exit and that all outstanding transactions must wind down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_error_connection_interrupted-c.macro)*