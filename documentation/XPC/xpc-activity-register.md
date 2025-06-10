# xpc_activity_register(_:_:_:)

**Framework**: XPC  
**Kind**: func

Registers an activity with the system.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func xpc_activity_register(_ identifier: UnsafePointer<CChar>, _ criteria: xpc_object_t, _ handler: @escaping xpc_activity_handler_t)
```

#### Discussion

Registers a new activity with the system. The criteria of the activity are described by the dictionary passed to this function. If an activity with the same identifier already exists, the criteria provided override the existing criteria unless the special dictionary [`XPC_ACTIVITY_CHECK_IN`](xpc_activity_check_in.md) is used. The [`XPC_ACTIVITY_CHECK_IN`](xpc_activity_check_in.md) dictionary instructs the system to first look up an existing activity without modifying its criteria. Once the existing activity is found (or a new one is created with an empty set of criteria) the handler will be called with an activity object in the [`XPC_ACTIVITY_STATE_CHECK_IN`](xpc_activity_state_check_in.md) state.

## Parameters

- `identifier`: A unique identifier for the activity. Each application has its own namespace.
- `criteria`: A dictionary of criteria for the activity.
- `handler`: The handler block is never invoked reentrantly. It will be invoked on a dispatch queue with an appropriate priority to perform the activity.

## See Also

- [func xpc_activity_unregister(UnsafePointer<CChar>)](xpc_activity_unregister(_:).md)
  Unregisters an activity with the specified identifier.
- [let XPC_ACTIVITY_CHECK_IN: xpc_object_t](xpc_activity_check_in.md)
  A constant to check in with the system for a previously registered activity using the same identifier.
- [typealias xpc_activity_t](xpc_activity_t.md)
  An XPC activity object.
- [typealias xpc_activity_handler_t](xpc_activity_handler_t.md)
  A block to call when an XPC activity becomes eligible to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_register(_:_:_:))*