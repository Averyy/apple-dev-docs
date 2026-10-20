# xpc_session_create_flags_t

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 16.0+ - Deprecated in 17.0 (renamed: XPCSession.InitializationOptions)
- macOS 13.0+ - Deprecated in 14.0 (renamed: XPCSession.InitializationOptions)

## Declaration

```swift
struct xpc_session_create_flags_t
```

## Topics

### Type Properties
- [static let inactive: xpc_session_create_flags_t](./xpc_session_create_flags_t-swift.struct/inactive.md)
- [static let none: xpc_session_create_flags_t](./xpc_session_create_flags_t-swift.struct/none.md)
- [static let privileged: xpc_session_create_flags_t](./xpc_session_create_flags_t-swift.struct/privileged.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Creating a session
- [typealias xpc_session_t](./xpc_session_t-49tiv.md)
- [func xpc_session_create_mach_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](./xpc_session_create_mach_service%28_,_,_,_%29.md)
- [func xpc_session_create_xpc_service(UnsafePointer<CChar>, dispatch_queue_t?, xpc_session_create_flags_t, AutoreleasingUnsafeMutablePointer<xpc_rich_error_t?>?) -> (any OS_xpc_object)?](./xpc_session_create_xpc_service%28_,_,_,_%29.md)
- [func xpc_session_copy_description(any OS_xpc_object) -> UnsafeMutablePointer<CChar>?](./xpc_session_copy_description%28_%29.md)
- [func xpc_session_set_target_queue(any OS_xpc_object, dispatch_queue_t?)](./xpc_session_set_target_queue%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_create_flags_t-swift.struct)*