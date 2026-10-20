# XPC_CONNECTION_MACH_SERVICE_PRIVILEGED

**Framework**: XPC  
**Kind**: var  
**Role**: Global Variable

A flag that indicates the job advertising the service name belongs to a launch daemon rather than a launch agent.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var XPC_CONNECTION_MACH_SERVICE_PRIVILEGED: Int32 { get }
```

```c
#define XPC_CONNECTION_MACH_SERVICE_PRIVILEGED
```

#### Discussion

Pass this to [`xpc_connection_create_mach_service(_:_:_:)`](./xpc_connection_create_mach_service%28_,_,_%29.md). This flag indicates that the job advertising the service name in its `launchd.plist` needs to be in the privileged Mach bootstrap. Do this by placing your `launchd.plist` in `/Library/LaunchDaemons`.

If you specify this alongside the [`XPC_CONNECTION_MACH_SERVICE_LISTENER`](./xpc_connection_mach_service_listener.md) flag, this flag is a no-op.

## See Also

### Creation
- [typealias xpc_connection_t](./xpc_connection_t.md)
  A type that represents a connection to a named service.
- [func xpc_connection_create(UnsafePointer<CChar>?, dispatch_queue_t?) -> xpc_connection_t](./xpc_connection_create%28_,_%29.md)
  Creates a new connection object.
- [func xpc_connection_create_from_endpoint(xpc_endpoint_t) -> xpc_connection_t](./xpc_connection_create_from_endpoint%28_%29.md)
  Creates a new connection from the specified endpoint.
- [func xpc_connection_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, UInt64) -> xpc_connection_t](./xpc_connection_create_mach_service%28_,_,_%29.md)
  Creates a new connection object that represents a Mach service.
- [func xpc_connection_set_target_queue(xpc_connection_t, dispatch_queue_t?)](./xpc_connection_set_target_queue%28_,_%29.md)
  Sets the target queue of the connection.
- [var XPC_CONNECTION_MACH_SERVICE_LISTENER: Int32](./xpc_connection_mach_service_listener.md)
  A flag that indicates the caller is the listener for the named service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_connection_mach_service_privileged)*