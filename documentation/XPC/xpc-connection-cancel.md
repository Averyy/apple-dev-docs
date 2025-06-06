# xpc_connection_cancel(_:)

**Framework**: Xpc  
**Kind**: func

Cancels the connection and ensures that its event handler doesn’t fire again.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_cancel(_ connection: xpc_connection_t)
```

#### Discussion

After this call, any messages that have not yet been sent will be discarded, and the connection will be unwound. If there are messages that are awaiting replies, they will have their reply handlers invoked with the [`XPC_ERROR_CONNECTION_INVALID`](xpc_error_connection_invalid-swift.var.md) error.

Cancellation is asynchronous and non-preemptive and therefore this method will not interrupt the execution of an already-running event handler block. If the event handler is executing at the time of this call, it will finish, and then the connection will be canceled, causing a final invocation of the event handler to be scheduled with the [`XPC_ERROR_CONNECTION_INVALID`](xpc_error_connection_invalid-swift.var.md) error. After that invocation, there will be no further invocations of the event handler.

The XPC runtime guarantees this non-preemptiveness even for concurrent target queues.

## Parameters

- `connection`: The connection object which is to be manipulated.

## See Also

- [func xpc_main(xpc_connection_handler_t) -> Never](xpc_main(_:).md)
  Starts listening for incoming connections and processes them with the specified event handler.
- [func xpc_connection_activate(xpc_connection_t)](xpc_connection_activate(_:).md)
  Activates a new connection.
- [func xpc_connection_suspend(xpc_connection_t)](xpc_connection_suspend(_:).md)
  Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.
- [func xpc_connection_resume(xpc_connection_t)](xpc_connection_resume(_:).md)
  Resumes a suspended connection.
- [func xpc_transaction_begin()](xpc_transaction_begin().md)
  Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.
- [func xpc_transaction_end()](xpc_transaction_end().md)
  Informs the XPC runtime when a transaction ends.
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](xpc_connection_copy_invalidation_reason(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_cancel(_:))*