# xpc_activity_handler_t

**Framework**: Xpc  
**Kind**: typealias

A block to call when an XPC activity becomes eligible to run.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_activity_handler_t = (xpc_activity_t) -> Void
```

## See Also

- [func xpc_activity_register(UnsafePointer<CChar>, xpc_object_t, xpc_activity_handler_t)](xpc_activity_register(_:_:_:).md)
  Registers an activity with the system.
- [func xpc_activity_unregister(UnsafePointer<CChar>)](xpc_activity_unregister(_:).md)
  Unregisters an activity with the specified identifier.
- [let XPC_ACTIVITY_CHECK_IN: xpc_object_t](xpc_activity_check_in.md)
  A constant to check in with the system for a previously registered activity using the same identifier.
- [typealias xpc_activity_t](xpc_activity_t.md)
  An XPC activity object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_handler_t)*