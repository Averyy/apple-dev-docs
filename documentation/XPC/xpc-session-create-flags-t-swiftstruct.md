# xpc_session_create_flags_t

**Framework**: XPC  
**Kind**: struct

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
struct xpc_session_create_flags_t
```

## Topics

### Type Properties
- [static let inactive: xpc_session_create_flags_t](xpc_session_create_flags_t-swift.struct/inactive.md)
- [static let none: xpc_session_create_flags_t](xpc_session_create_flags_t-swift.struct/none.md)
- [static let privileged: xpc_session_create_flags_t](xpc_session_create_flags_t-swift.struct/privileged.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias xpc_session_t](xpc_session_t-49tiv.md)
- [func xpc_session_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](xpc_session_create_mach_service(_:_:_:_:).md)
- [func xpc_session_create_xpc_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](xpc_session_create_xpc_service(_:_:_:_:).md)
- [func xpc_session_copy_description(any OS_xpc_object) -> UnsafeMutablePointer<CChar>?](xpc_session_copy_description(_:).md)
- [func xpc_session_set_target_queue(any OS_xpc_object, dispatch_queue_t?)](xpc_session_set_target_queue(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_create_flags_t-swift.struct)*