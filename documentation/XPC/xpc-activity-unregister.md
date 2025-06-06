# xpc_activity_unregister(_:)

**Framework**: Xpc  
**Kind**: func

Unregisters an activity with the specified identifier.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func xpc_activity_unregister(_ identifier: UnsafePointer<CChar>)
```

#### Discussion

A dynamically registered activity will be deleted in response to this call. Statically registered activity (from a launchd property list) will be reverted to its original criteria if any modifications were made.

Unregistering an activity has no effect on any outstanding [`xpc_activity_t`](xpc_activity_t.md) objects or any currently executing [`xpc_activity_handler_t`](xpc_activity_handler_t.md) blocks; however, no new handler block invocations will be made after it is unregistered.

## Parameters

- `identifier`: The identifier of the activity to unregister.

## See Also

- [func xpc_activity_register(UnsafePointer<CChar>, xpc_object_t, xpc_activity_handler_t)](xpc_activity_register(_:_:_:).md)
  Registers an activity with the system.
- [let XPC_ACTIVITY_CHECK_IN: xpc_object_t](xpc_activity_check_in.md)
  A constant to check in with the system for a previously registered activity using the same identifier.
- [typealias xpc_activity_t](xpc_activity_t.md)
  An XPC activity object.
- [typealias xpc_activity_handler_t](xpc_activity_handler_t.md)
  A block to call when an XPC activity becomes eligible to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_unregister(_:))*