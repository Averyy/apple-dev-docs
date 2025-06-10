# xpc_main(_:)

**Framework**: XPC  
**Kind**: func

Starts listening for incoming connections and processes them with the specified event handler.

**Availability**:
- Mac Catalyst 5.0+
- macOS 10.7+

## Declaration

```swift
func xpc_main(_ handler: xpc_connection_handler_t) -> Never
```

#### Discussion

This is the springboard into the XPC service runtime. This function sets up your service bundle’s listener connection and manages it automatically. After this initial setup, this function calls [`dispatchMain()`](https://developer.apple.com/documentation/Dispatch/dispatchMain()). You may override this behavior by setting the [`RunLoopType`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/XPCService/RunLoopType) key in your XPC service bundle’s `Info.plist` under the `XPCService` dictionary.

## Parameters

- `handler`: The handler to accept new connections with.

## See Also

- [func xpc_connection_activate(xpc_connection_t)](xpc_connection_activate(_:).md)
  Activates a new connection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_main(_:))*