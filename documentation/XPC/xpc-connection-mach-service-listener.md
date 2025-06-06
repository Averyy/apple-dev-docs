# XPC_CONNECTION_MACH_SERVICE_LISTENER

**Framework**: Xpc  
**Kind**: var

A flag that indicates the caller is the listener for the named service.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var XPC_CONNECTION_MACH_SERVICE_LISTENER: Int32 { get }
```

#### Discussion

Pass this to [`xpc_connection_create_mach_service(_:_:_:)`](xpc_connection_create_mach_service(_:_:_:).md). This flag indicates that the caller is the listener for the named service. Only pass this flag for services in the process’s `launchd.plist`. You may not use this flag to dynamically add services to the Mach bootstrap namespace.

## See Also

- [typealias xpc_connection_t](xpc_connection_t.md)
  A type that represents a connection to a named service.
- [func xpc_connection_create(UnsafePointer<CChar>?, dispatch_queue_t?) -> xpc_connection_t](xpc_connection_create(_:_:).md)
  Creates a new connection object.
- [func xpc_connection_create_from_endpoint(xpc_endpoint_t) -> xpc_connection_t](xpc_connection_create_from_endpoint(_:).md)
  Creates a new connection from the specified endpoint.
- [func xpc_connection_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, UInt64) -> xpc_connection_t](xpc_connection_create_mach_service(_:_:_:).md)
  Creates a new connection object that represents a Mach service.
- [func xpc_connection_set_target_queue(xpc_connection_t, dispatch_queue_t?)](xpc_connection_set_target_queue(_:_:).md)
  Sets the target queue of the connection.
- [var XPC_CONNECTION_MACH_SERVICE_PRIVILEGED: Int32](xpc_connection_mach_service_privileged.md)
  A flag that indicates the job advertising the service name belongs to a launch daemon rather than a launch agent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_mach_service_listener)*