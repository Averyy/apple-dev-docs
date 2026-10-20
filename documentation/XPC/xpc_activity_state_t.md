# xpc_activity_state_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A type that represents the state of an activity.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias xpc_activity_state_t = Int
```

```c
typedef long xpc_activity_state_t;
```

#### Discussion

An activity is in one of the states that [`xpc_activity_state_t`](./xpc_activity_state_t.md) defines. Apps may check the current state of the activity using [`xpc_activity_get_state(_:)`](./xpc_activity_get_state%28_%29.md) in the handler block that you provide to [`xpc_activity_register(_:_:_:)`](./xpc_activity_register%28_,_,_%29.md).

The app can modify the state of the activity by calling [`xpc_activity_set_state(_:_:)`](./xpc_activity_set_state%28_,_%29.md) with one of the following:

- [`XPC_ACTIVITY_STATE_DEFER`](./xpc_activity_state_defer.md)
- [`XPC_ACTIVITY_STATE_CONTINUE`](./xpc_activity_state_continue.md)
- [`XPC_ACTIVITY_STATE_DONE`](./xpc_activity_state_done.md)

## See Also

### State
- [func xpc_activity_get_state(xpc_activity_t) -> xpc_activity_state_t](./xpc_activity_get_state%28_%29.md)
  Returns the current state of an activity.
- [func xpc_activity_set_state(xpc_activity_t, xpc_activity_state_t) -> Bool](./xpc_activity_set_state%28_,_%29.md)
  Updates the current state of an activity.
- [func xpc_activity_should_defer(xpc_activity_t) -> Bool](./xpc_activity_should_defer%28_%29.md)
  Tests whether to defer an activity.
- [xpc_activity_state_t](./xpc-activity-state-t-swift-consts.md)
  A type that represents the state of an activity.
- [var XPC_ACTIVITY_STATE_CHECK_IN: Int](./xpc_activity_state_check_in.md)
  The activity has completed a check-in with the system.
- [var XPC_ACTIVITY_STATE_WAIT: Int](./xpc_activity_state_wait.md)
  The activity is waiting for an opportunity to run.
- [var XPC_ACTIVITY_STATE_RUN: Int](./xpc_activity_state_run.md)
  The activity is eligible to run according to its criteria.
- [var XPC_ACTIVITY_STATE_DEFER: Int](./xpc_activity_state_defer.md)
  The activity needs to wait until it satisfies its criteria again.
- [var XPC_ACTIVITY_STATE_CONTINUE: Int](./xpc_activity_state_continue.md)
  The activity continues its operation beyond the return of its handler block.
- [var XPC_ACTIVITY_STATE_DONE: Int](./xpc_activity_state_done.md)
  The activity is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_state_t)*