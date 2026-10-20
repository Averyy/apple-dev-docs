# xpc_transaction_end()

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Informs the XPC runtime when a transaction ends.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func xpc_transaction_end()
```

```c
extern void xpc_transaction_end();
```

#### Discussion

As described in [`xpc_transaction_begin()`](./xpc_transaction_begin%28%29.md), this API may be used interchangeably with `vproc_transaction_end()`.

See the discussion for [`xpc_transaction_begin()`](./xpc_transaction_begin%28%29.md) for details regarding the XPC runtime’s idle-exit policy.

## See Also

### Life cycle
- [func xpc_main(xpc_connection_handler_t) -> Never](./xpc_main%28_%29.md)
  Starts listening for incoming connections and processes them with the specified event handler.
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
- [func xpc_connection_copy_invalidation_reason(xpc_connection_t) -> UnsafeMutablePointer<CChar>?](./xpc_connection_copy_invalidation_reason%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_transaction_end())*