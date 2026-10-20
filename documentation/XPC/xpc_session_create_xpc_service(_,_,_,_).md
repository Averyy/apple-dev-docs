# xpc_session_create_xpc_service(_:_:_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 16.0+ - Deprecated in 17.0 (renamed: XPCSession(xpcService:))
- macOS 13.0+ - Deprecated in 14.0 (renamed: XPCSession(xpcService:))

## Declaration

```swift
func xpc_session_create_xpc_service(_ name: UnsafePointer<CChar>, _ target_queue: dispatch_queue_t?, _ flags: xpc_session_create_flags_t, _ error_out: AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?
```

## See Also

### Creating a session
- [typealias xpc_session_t](./xpc_session_t-49tiv.md)
- [func xpc_session_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](./xpc_session_create_mach_service%28_,_,_,_%29.md)
- [struct xpc_session_create_flags_t](./xpc_session_create_flags_t-swift.struct.md)
- [func xpc_session_copy_description(any OS_xpc_object) -> UnsafeMutablePointer<CChar>?](./xpc_session_copy_description%28_%29.md)
- [func xpc_session_set_target_queue(any OS_xpc_object, dispatch_queue_t?)](./xpc_session_set_target_queue%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_create_xpc_service(_:_:_:_:))*