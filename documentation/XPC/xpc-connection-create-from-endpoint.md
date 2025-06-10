# xpc_connection_create_from_endpoint(_:)

**Framework**: XPC  
**Kind**: func

Creates a new connection from the specified endpoint.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_create_from_endpoint(_ endpoint: xpc_endpoint_t) -> xpc_connection_t
```

#### Return Value

A new peer connection to the listener represented by the given endpoint.

#### Discussion

The same responsibilities of setting an event handler and resuming the connection after calling [`xpc_connection_create(_:_:)`](xpc_connection_create(_:_:).md) apply to the connection returned by this API. Since the connection yielded by this API is not associated with a name (and therefore is not rediscoverable), this connection will receive [`XPC_ERROR_CONNECTION_INVALID`](xpc_error_connection_invalid-swift.var.md) if the listening side crashes, exits or cancels the listener connection.

## Parameters

- `endpoint`: The endpoint from which to create the new connection.

## See Also

- [typealias xpc_connection_t](xpc_connection_t.md)
  A type that represents a connection to a named service.
- [func xpc_connection_create(UnsafePointer<CChar>?, dispatch_queue_t?) -> xpc_connection_t](xpc_connection_create(_:_:).md)
  Creates a new connection object.
- [func xpc_connection_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, UInt64) -> xpc_connection_t](xpc_connection_create_mach_service(_:_:_:).md)
  Creates a new connection object that represents a Mach service.
- [func xpc_connection_set_target_queue(xpc_connection_t, dispatch_queue_t?)](xpc_connection_set_target_queue(_:_:).md)
  Sets the target queue of the connection.
- [var XPC_CONNECTION_MACH_SERVICE_LISTENER: Int32](xpc_connection_mach_service_listener.md)
  A flag that indicates the caller is the listener for the named service.
- [var XPC_CONNECTION_MACH_SERVICE_PRIVILEGED: Int32](xpc_connection_mach_service_privileged.md)
  A flag that indicates the job advertising the service name belongs to a launch daemon rather than a launch agent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_create_from_endpoint(_:))*