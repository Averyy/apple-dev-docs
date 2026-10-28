# xpc_main(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Starts listening for incoming connections and processes them with the specified event handler.

**Availability**:
- Mac Catalyst 5.0+
- macOS 10.7+

## Declaration

```swift
func xpc_main(_ handler: xpc_connection_handler_t) -> Never
```

```c
extern void xpc_main(xpc_connection_handler_t handler);
```

## Discussion

This is the springboard into the XPC service runtime. This function sets up your service bundle’s listener connection and manages it automatically. After this initial setup, this function calls [`dispatchMain()`](../Dispatch/dispatchmain%28%29.md). You may override this behavior by setting the [`RunLoopType`](../BundleResources/information-property-list/xpcservice/runlooptype.md) key in your XPC service bundle’s `Info.plist` under the `XPCService` dictionary.

## Parameters

- `handler`: The handler to accept new connections with.

## See Also

### Life cycle
- [func xpc_connection_activate(xpc_connection_t)](./xpc_connection_activate%28_%29.md)
  Activates a new connection.
- [func xpc_connection_suspend(xpc_connection_t)](./xpc_connection_suspend%28_%29.md)
  Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.
- [func xpc_connection_resume(xpc_connection_t)](./xpc_connection_resume%28_%29.md)
  Resumes a suspended connection.
- [func xpc_connection_cancel(xpc_connection_t)](./xpc_connection_cancel%28_%29.md)
  Cancels the connection and ensures that its event handler doesn’t fire again.
- [func xpc_transaction_begin()](./xpc_transaction_begin%28%29.md)
  Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.
- [func xpc_transaction_end()](./xpc_transaction_end%28%29.md)
  Informs the XPC runtime when a transaction ends.
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](./xpc_connection_copy_invalidation_reason%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_main(_:))*