# xpc_connection_activate(_:)

**Framework**: Xpc  
**Kind**: func

Activates a new connection.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
func xpc_connection_activate(_ connection: xpc_connection_t)
```

#### Discussion

Connections start in an inactive state, so you must call [`xpc_connection_activate(_:)`](xpc_connection_activate(_:).md) on a connection before it will send or receive any messages.

Calling [`xpc_connection_activate(_:)`](xpc_connection_activate(_:).md) on an active connection has no effect. Releasing the last reference on an inactive connection that was created with a call to one of the `xpc_connection_create` functions is undefined.

For backward compatibility reasons, [`xpc_connection_resume(_:)`](xpc_connection_resume(_:).md) on an inactive and not otherwise suspended XPC connection has the same effect as calling [`xpc_connection_activate(_:)`](xpc_connection_activate(_:).md). For new code, using [`xpc_connection_activate(_:)`](xpc_connection_activate(_:).md) is preferred.

## See Also

- [func xpc_main(xpc_connection_handler_t) -> Never](xpc_main(_:).md)
  Starts listening for incoming connections and processes them with the specified event handler.
- [func xpc_connection_suspend(xpc_connection_t)](xpc_connection_suspend(_:).md)
  Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.
- [func xpc_connection_resume(xpc_connection_t)](xpc_connection_resume(_:).md)
  Resumes a suspended connection.
- [func xpc_connection_cancel(xpc_connection_t)](xpc_connection_cancel(_:).md)
  Cancels the connection and ensures that its event handler doesn’t fire again.
- [func xpc_transaction_begin()](xpc_transaction_begin().md)
  Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.
- [func xpc_transaction_end()](xpc_transaction_end().md)
  Informs the XPC runtime when a transaction ends.
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](xpc_connection_copy_invalidation_reason(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_activate(_:))*