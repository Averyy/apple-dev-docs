# xpc_connection_resume(_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Resumes a suspended connection.

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
func xpc_connection_resume(_ connection: xpc_connection_t)
```

```c
extern void xpc_connection_resume(xpc_connection_t connection);
```

## Discussion

In order for a connection to become live, every call to [`xpc_connection_suspend(_:)`](./xpc_connection_suspend%28_%29.md) must be balanced with a call to [`xpc_connection_resume(_:)`](./xpc_connection_resume%28_%29.md) after the initial call to [`xpc_connection_resume(_:)`](./xpc_connection_resume%28_%29.md). After the initial resume of the connection, calling [`xpc_connection_resume(_:)`](./xpc_connection_resume%28_%29.md) more times than [`xpc_connection_suspend(_:)`](./xpc_connection_suspend%28_%29.md) has been called is considered an error.

## Parameters

- `connection`: The connection object which is to be manipulated.

## See Also

### Life cycle
- [func xpc_main(xpc_connection_handler_t) -> Never](./xpc_main%28_%29.md)
  Starts listening for incoming connections and processes them with the specified event handler.
- [func xpc_connection_activate(xpc_connection_t)](./xpc_connection_activate%28_%29.md)
  Activates a new connection.
- [func xpc_connection_suspend(xpc_connection_t)](./xpc_connection_suspend%28_%29.md)
  Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.
- [func xpc_connection_cancel(xpc_connection_t)](./xpc_connection_cancel%28_%29.md)
  Cancels the connection and ensures that its event handler doesn’t fire again.
- [func xpc_transaction_begin()](./xpc_transaction_begin%28%29.md)
  Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.
- [func xpc_transaction_end()](./xpc_transaction_end%28%29.md)
  Informs the XPC runtime when a transaction ends.
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](./xpc_connection_copy_invalidation_reason%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_resume(_:))*