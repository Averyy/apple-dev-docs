# xpc_connection_resume(_:)

**Framework**: Xpc  
**Kind**: func

Resumes a suspended connection.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_resume(_ connection: xpc_connection_t)
```

#### Discussion

In order for a connection to become live, every call to [`xpc_connection_suspend(_:)`](xpc_connection_suspend(_:).md) must be balanced with a call to [`xpc_connection_resume(_:)`](xpc_connection_resume(_:).md) after the initial call to [`xpc_connection_resume(_:)`](xpc_connection_resume(_:).md). After the initial resume of the connection, calling [`xpc_connection_resume(_:)`](xpc_connection_resume(_:).md) more times than [`xpc_connection_suspend(_:)`](xpc_connection_suspend(_:).md) has been called is considered an error.

## Parameters

- `connection`: The connection object which is to be manipulated.

## See Also

- [func xpc_main(xpc_connection_handler_t) -> Never](xpc_main(_:).md)
  Starts listening for incoming connections and processes them with the specified event handler.
- [func xpc_connection_activate(xpc_connection_t)](xpc_connection_activate(_:).md)
  Activates a new connection.
- [func xpc_connection_suspend(xpc_connection_t)](xpc_connection_suspend(_:).md)
  Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.
- [func xpc_connection_cancel(xpc_connection_t)](xpc_connection_cancel(_:).md)
  Cancels the connection and ensures that its event handler doesn’t fire again.
- [func xpc_transaction_begin()](xpc_transaction_begin().md)
  Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.
- [func xpc_transaction_end()](xpc_transaction_end().md)
  Informs the XPC runtime when a transaction ends.
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](xpc_connection_copy_invalidation_reason(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_resume(_:))*