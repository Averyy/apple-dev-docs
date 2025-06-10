# xpc_transaction_begin()

**Framework**: XPC  
**Kind**: func

Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func xpc_transaction_begin()
```

#### Discussion

A service with no outstanding transactions may automatically exit due to inactivity as determined by the system.

This function may be used to manually manage transactions in cases where their automatic management (as described below) does not meet the needs of an XPC service. This function also updates the transaction count used for sudden termination, i.e. `vproc_transaction_begin()`, and these two interfaces may be used in combination.

The XPC runtime will automatically begin a transaction on behalf of a service when a new message is received. If no reply message is expected, the transaction is automatically ended when the connection event handler returns. If a reply message is created, the transaction will end when the reply message is sent or released. An XPC service may use [`xpc_transaction_begin()`](xpc_transaction_begin().md) and [`xpc_transaction_end()`](xpc_transaction_end().md) to inform the XPC runtime about activity that occurs outside of this common pattern.

When the XPC runtime has determined that the service should exit, the event handlers for all active listening and peer connections will receive [`XPC_ERROR_TERMINATION_IMMINENT`](xpc_error_termination_imminent-swift.var.md) as an indication that they should unwind their existing transactions. After this error is delivered to a connection’s event handler, no more messages will be delivered to the connection.

## See Also

- [func xpc_main(xpc_connection_handler_t) -> Never](xpc_main(_:).md)
  Starts listening for incoming connections and processes them with the specified event handler.
- [func xpc_connection_activate(xpc_connection_t)](xpc_connection_activate(_:).md)
  Activates a new connection.
- [func xpc_connection_suspend(xpc_connection_t)](xpc_connection_suspend(_:).md)
  Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.
- [func xpc_connection_resume(xpc_connection_t)](xpc_connection_resume(_:).md)
  Resumes a suspended connection.
- [func xpc_connection_cancel(xpc_connection_t)](xpc_connection_cancel(_:).md)
  Cancels the connection and ensures that its event handler doesn’t fire again.
- [func xpc_transaction_end()](xpc_transaction_end().md)
  Informs the XPC runtime when a transaction ends.
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](xpc_connection_copy_invalidation_reason(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_transaction_begin())*