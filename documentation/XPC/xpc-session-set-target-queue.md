# xpc_session_set_target_queue(_:_:)

**Framework**: XPC  
**Kind**: func

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
func xpc_session_set_target_queue(_ session: any OS_xpc_object, _ target_queue: dispatch_queue_t?)
```

## See Also

- [typealias xpc_session_t](xpc_session_t-49tiv.md)
- [func xpc_session_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](xpc_session_create_mach_service(_:_:_:_:).md)
- [func xpc_session_create_xpc_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](xpc_session_create_xpc_service(_:_:_:_:).md)
- [struct xpc_session_create_flags_t](xpc_session_create_flags_t-swift.struct.md)
- [func xpc_session_copy_description(any OS_xpc_object) -> UnsafeMutablePointer<CChar>?](xpc_session_copy_description(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_set_target_queue(_:_:))*