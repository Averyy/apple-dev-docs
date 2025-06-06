# XPC_ACTIVITY_CHECK_IN

**Framework**: Xpc  
**Kind**: var

A constant to check in with the system for a previously registered activity using the same identifier.

**Availability**:
- macOS 10.9+

## Declaration

```swift
let XPC_ACTIVITY_CHECK_IN: xpc_object_t
```

#### Discussion

Pass this constant to [`xpc_activity_register(_:_:_:)`](xpc_activity_register(_:_:_:).md) as the criteria dictionary to check in with the system for previously registered activity using the same identifier (for example, an activity from a launchd property list).

## See Also

- [func xpc_activity_register(UnsafePointer<CChar>, xpc_object_t, xpc_activity_handler_t)](xpc_activity_register(_:_:_:).md)
  Registers an activity with the system.
- [func xpc_activity_unregister(UnsafePointer<CChar>)](xpc_activity_unregister(_:).md)
  Unregisters an activity with the specified identifier.
- [typealias xpc_activity_t](xpc_activity_t.md)
  An XPC activity object.
- [typealias xpc_activity_handler_t](xpc_activity_handler_t.md)
  A block to call when an XPC activity becomes eligible to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_check_in)*