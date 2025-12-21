# xpc_connection_send_barrier(_:_:)

**Framework**: XPC  
**Kind**: func

Issues a barrier against the connection’s message-send activity.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_send_barrier(_ connection: xpc_connection_t, _ barrier: @escaping () -> Void)
```

#### Discussion

XPC guarantees that, even if the connection’s target queue is a concurrent queue, there are no other messages being sent concurrently while the barrier block is executing. XPC does not guarantee that the receipt of messages (either through the connection’s event handler or through reply handlers) will be suspended while the barrier is executing.

A barrier is issued relative to the message-send queue. So, if you call [`xpc_connection_send_message(_:_:)`](xpc_connection_send_message(_:_:).md) five times and then call [`xpc_connection_send_barrier(_:_:)`](xpc_connection_send_barrier(_:_:).md), the barrier will be invoked after the fifth message has been sent and its memory disposed of. You may safely cancel a connection from within a barrier block.

If a barrier is issued after sending a message which expects a reply, the behavior is the same as described above. The receipt of a reply message will not influence when the barrier runs.

A barrier block can be useful for throttling resource consumption on the connected side of a connection. For example, if your connection sends many large messages, you can use a barrier to limit the number of messages that are inflight at any given time. This can be particularly useful for messages that contain kernel resources (like file descriptors) which have a systemwide limit.

If a barrier is issued on a canceled connection, it will be invoked immediately. If a connection has been canceled and still has outstanding barriers, those barriers will be invoked as part of the connection’s unwinding process.

It is important to note that a barrier block’s execution order is not guaranteed with respect to other blocks that have been scheduled on the target queue of the connection. Or said differently, [`xpc_connection_send_barrier(_:_:)`](xpc_connection_send_barrier(_:_:).md) is not equivalent to [`dispatch_async`](https://developer.apple.com/documentation/Dispatch/dispatch_async).

## Parameters

- `connection`: The connection against which the barrier is to be issued.
- `barrier`: The barrier block to issue. This barrier prevents concurrent message-send activity on the connection. No messages will be sent while the barrier block is executing.

## See Also

- [func xpc_connection_send_message(xpc_connection_t, xpc_object_t)](xpc_connection_send_message(_:_:).md)
  Sends a message over the connection to the destination service.
- [func xpc_connection_send_message_with_reply(xpc_connection_t, xpc_object_t, dispatch_queue_t?, (xpc_object_t) -> Void)](xpc_connection_send_message_with_reply(_:_:_:_:).md)
  Sends a message over the connection to the destination service and associates a handler to invoke when the remote service sends a reply message.
- [func xpc_connection_send_message_with_reply_sync(xpc_connection_t, xpc_object_t) -> xpc_object_t](xpc_connection_send_message_with_reply_sync(_:_:).md)
  Sends a message over the connection and blocks the caller until it receives a reply.
- [func xpc_main(xpc_connection_handler_t) -> Never](xpc_main(_:).md)
  Starts listening for incoming connections and processes them with the specified event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_send_barrier(_:_:))*