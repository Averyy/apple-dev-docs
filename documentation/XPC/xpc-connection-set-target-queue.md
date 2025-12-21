# xpc_connection_set_target_queue(_:_:)

**Framework**: XPC  
**Kind**: func

Sets the target queue of the connection.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_set_target_queue(_ connection: xpc_connection_t, _ targetq: dispatch_queue_t?)
```

#### Discussion

Setting the target queue is asynchronous and non-preemptive and therefore this method will not interrupt the execution of an already-running event handler block. Setting the target queue may be likened to issuing a barrier to the connection which does the actual work of changing the target queue.

The XPC runtime guarantees this non-preemptiveness even for concurrent target queues. If the target queue is a concurrent queue, then XPC still guarantees that there will never be more than one invocation of the connection’s event handler block executing concurrently. If you wish to process events concurrently, you can [`dispatch_async`](https://developer.apple.com/documentation/Dispatch/dispatch_async) to a concurrent queue from within the event handler.

> ❗ **Important**:  When called from within the event handler block, [`dispatch_get_current_queue()`](https://developer.apple.com/documentation/Dispatch/dispatch_get_current_queue()) is NOT guaranteed to return a pointer to the queue set with this method.

Despite this seeming inconsistency, the XPC runtime guarantees that, when the target queue is a serial queue, the event handler block will execute synchonously with respect to other blocks submitted to that same queue. When the target queue is a concurrent queue, the event handler block may run concurrently with other blocks submitted to that queue, but it will never run concurrently with other invocations of itself for the same connection, as discussed previously.

## Parameters

- `connection`: The connection object which is to be manipulated.
- `targetq`: The GCD queue to which the event handler block will be submitted. This parameter may be  , in which case the connection’s target queue will be the default target queue of  , defined as  .

## See Also

- [typealias xpc_connection_t](xpc_connection_t.md)
  A type that represents a connection to a named service.
- [func xpc_connection_create(UnsafePointer<CChar>?, dispatch_queue_t?) -> xpc_connection_t](xpc_connection_create(_:_:).md)
  Creates a new connection object.
- [func xpc_connection_create_from_endpoint(xpc_endpoint_t) -> xpc_connection_t](xpc_connection_create_from_endpoint(_:).md)
  Creates a new connection from the specified endpoint.
- [func xpc_connection_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, UInt64) -> xpc_connection_t](xpc_connection_create_mach_service(_:_:_:).md)
  Creates a new connection object that represents a Mach service.
- [var XPC_CONNECTION_MACH_SERVICE_LISTENER: Int32](xpc_connection_mach_service_listener.md)
  A flag that indicates the caller is the listener for the named service.
- [var XPC_CONNECTION_MACH_SERVICE_PRIVILEGED: Int32](xpc_connection_mach_service_privileged.md)
  A flag that indicates the job advertising the service name belongs to a launch daemon rather than a launch agent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_set_target_queue(_:_:))*