# XPC_ACTIVITY_STATE_RUN

**Framework**: Xpc  
**Kind**: var

The activity is eligible to run according to its criteria.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var XPC_ACTIVITY_STATE_RUN: Int { get }
```

## See Also

- [func xpc_activity_get_state(xpc_activity_t) -> xpc_activity_state_t](xpc_activity_get_state(_:).md)
  Returns the current state of an activity.
- [func xpc_activity_set_state(xpc_activity_t, xpc_activity_state_t) -> Bool](xpc_activity_set_state(_:_:).md)
  Updates the current state of an activity.
- [func xpc_activity_should_defer(xpc_activity_t) -> Bool](xpc_activity_should_defer(_:).md)
  Tests whether to defer an activity.
- [xpc_activity_state_t](xpc-activity-state-t-swift-consts.md)
  A type that represents the state of an activity.
- [typealias xpc_activity_state_t](xpc_activity_state_t.md)
  A type that represents the state of an activity.
- [var XPC_ACTIVITY_STATE_CHECK_IN: Int](xpc_activity_state_check_in.md)
  The activity has completed a check-in with the system.
- [var XPC_ACTIVITY_STATE_WAIT: Int](xpc_activity_state_wait.md)
  The activity is waiting for an opportunity to run.
- [var XPC_ACTIVITY_STATE_DEFER: Int](xpc_activity_state_defer.md)
  The activity needs to wait until it satisfies its criteria again.
- [var XPC_ACTIVITY_STATE_CONTINUE: Int](xpc_activity_state_continue.md)
  The activity continues its operation beyond the return of its handler block.
- [var XPC_ACTIVITY_STATE_DONE: Int](xpc_activity_state_done.md)
  The activity is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_state_run)*