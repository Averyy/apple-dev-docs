# xpc_activity_should_defer(_:)

**Framework**: Xpc  
**Kind**: func

Tests whether to defer an activity.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func xpc_activity_should_defer(_ activity: xpc_activity_t) -> Bool
```

#### Return Value

Returns true if the activity should be deferred.

#### Discussion

Use this function to test whether the criteria of a long-running activity are still satisfied. If not, the system indicates that the application should defer the activity. The application may acknowledge the deferral by calling [`xpc_activity_set_state(_:_:)`](xpc_activity_set_state(_:_:).md) with [`XPC_ACTIVITY_STATE_DEFER`](xpc_activity_state_defer.md). Once deferred, the system places the activity back into the WAIT state and invokes the handler block again at the earliest opportunity when the criteria are once again satisfied.

## See Also

- [func xpc_activity_get_state(xpc_activity_t) -> xpc_activity_state_t](xpc_activity_get_state(_:).md)
  Returns the current state of an activity.
- [func xpc_activity_set_state(xpc_activity_t, xpc_activity_state_t) -> Bool](xpc_activity_set_state(_:_:).md)
  Updates the current state of an activity.
- [xpc_activity_state_t](xpc-activity-state-t-swift-consts.md)
  A type that represents the state of an activity.
- [typealias xpc_activity_state_t](xpc_activity_state_t.md)
  A type that represents the state of an activity.
- [var XPC_ACTIVITY_STATE_CHECK_IN: Int](xpc_activity_state_check_in.md)
  The activity has completed a check-in with the system.
- [var XPC_ACTIVITY_STATE_WAIT: Int](xpc_activity_state_wait.md)
  The activity is waiting for an opportunity to run.
- [var XPC_ACTIVITY_STATE_RUN: Int](xpc_activity_state_run.md)
  The activity is eligible to run according to its criteria.
- [var XPC_ACTIVITY_STATE_DEFER: Int](xpc_activity_state_defer.md)
  The activity needs to wait until it satisfies its criteria again.
- [var XPC_ACTIVITY_STATE_CONTINUE: Int](xpc_activity_state_continue.md)
  The activity continues its operation beyond the return of its handler block.
- [var XPC_ACTIVITY_STATE_DONE: Int](xpc_activity_state_done.md)
  The activity is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_should_defer(_:))*