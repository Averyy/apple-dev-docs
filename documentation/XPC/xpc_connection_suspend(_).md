# xpc_connection_suspend(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func xpc_connection_suspend(_ connection: xpc_connection_t)
```

```c
extern void xpc_connection_suspend(xpc_connection_t connection);
```

## Discussion

All calls to [`xpc_connection_suspend(_:)`](./xpc_connection_suspend%28_%29.md) must be balanced with calls to [`xpc_connection_resume(_:)`](./xpc_connection_resume%28_%29.md) before releasing the last reference to the connection.

Suspension is asynchronous and non-preemptive, and therefore this method will not interrupt the execution of an already-running event handler block. If the event handler is executing at the time of this call, it will finish, and then the connection will be suspended before the next scheduled invocation of the event handler. The XPC runtime guarantees this non-preemptiveness even for concurrent target queues.

Connection event handlers are non-reentrant, so it is safe to call [`xpc_connection_suspend(_:)`](./xpc_connection_suspend%28_%29.md) from within the event handler block.

## Parameters

- `connection`: The connection object which is to be manipulated.

## See Also

### Life cycle
- [func xpc_main(xpc_connection_handler_t) -> Never](./xpc_main%28_%29.md)
  Starts listening for incoming connections and processes them with the specified event handler.
- [func xpc_connection_activate(xpc_connection_t)](./xpc_connection_activate%28_%29.md)
  Activates a new connection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_suspend(_:))*