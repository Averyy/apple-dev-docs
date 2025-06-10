# xpc_connection_create_mach_service(_:_:_:)

**Framework**: XPC  
**Kind**: func

Creates a new connection object that represents a Mach service.

**Availability**:
- Mac Catalyst 5.0+
- macOS 10.7+

## Declaration

```swift
func xpc_connection_create_mach_service(_ name: UnsafePointer<CChar>, _ targetq: dispatch_queue_t?, _ flags: UInt64) -> xpc_connection_t
```

#### Return Value

A new connection object.

#### Discussion

If the [`XPC_CONNECTION_MACH_SERVICE_LISTENER`](xpc_connection_mach_service_listener.md) flag is given to this method, then the connection returned will be a listener connection. Otherwise, a peer connection will be returned. See the documentation for [`xpc_connection_set_event_handler(_:_:)`](xpc_connection_set_event_handler(_:_:).md) for the semantics of listener connections versus peer connections.

This method will succeed even if the named service does not exist. This is because the Mach namespace is not queried for the service name until the first call to [`xpc_connection_resume(_:)`](xpc_connection_resume(_:).md).

## Parameters

- `name`: The name of the remote service with which to connect. The service name must exist in a Mach bootstrap that is accessible to the process and be advertised in a  .
- `targetq`: The GCD queue to which the event handler block will be submitted. This parameter may be  , in which case the connection’s target queue will be the default target queue of  , defined as  . The target queue may be changed later with a call to  .
- `flags`: Additional attributes with which to create the connection.

## See Also

- [typealias xpc_connection_t](xpc_connection_t.md)
  A type that represents a connection to a named service.
- [func xpc_connection_create(UnsafePointer<CChar>?, dispatch_queue_t?) -> xpc_connection_t](xpc_connection_create(_:_:).md)
  Creates a new connection object.
- [func xpc_connection_create_from_endpoint(xpc_endpoint_t) -> xpc_connection_t](xpc_connection_create_from_endpoint(_:).md)
  Creates a new connection from the specified endpoint.
- [func xpc_connection_set_target_queue(xpc_connection_t, dispatch_queue_t?)](xpc_connection_set_target_queue(_:_:).md)
  Sets the target queue of the connection.
- [var XPC_CONNECTION_MACH_SERVICE_LISTENER: Int32](xpc_connection_mach_service_listener.md)
  A flag that indicates the caller is the listener for the named service.
- [var XPC_CONNECTION_MACH_SERVICE_PRIVILEGED: Int32](xpc_connection_mach_service_privileged.md)
  A flag that indicates the job advertising the service name belongs to a launch daemon rather than a launch agent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_create_mach_service(_:_:_:))*