# XPC activities

**Framework**: XPC

Schedule background activities for the system to execute.

## Topics

### Registration
- [func xpc_activity_register(UnsafePointer<CChar>, xpc_object_t, xpc_activity_handler_t)](xpc_activity_register(_:_:_:).md)
  Registers an activity with the system.
- [func xpc_activity_unregister(UnsafePointer<CChar>)](xpc_activity_unregister(_:).md)
  Unregisters an activity with the specified identifier.
- [let XPC_ACTIVITY_CHECK_IN: xpc_object_t](xpc_activity_check_in.md)
  A constant to check in with the system for a previously registered activity using the same identifier.
- [typealias xpc_activity_t](xpc_activity_t.md)
  An XPC activity object.
- [typealias xpc_activity_handler_t](xpc_activity_handler_t.md)
  A block to call when an XPC activity becomes eligible to run.
### State
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
- [var XPC_ACTIVITY_STATE_RUN: Int](xpc_activity_state_run.md)
  The activity is eligible to run according to its criteria.
- [var XPC_ACTIVITY_STATE_DEFER: Int](xpc_activity_state_defer.md)
  The activity needs to wait until it satisfies its criteria again.
- [var XPC_ACTIVITY_STATE_CONTINUE: Int](xpc_activity_state_continue.md)
  The activity continues its operation beyond the return of its handler block.
- [var XPC_ACTIVITY_STATE_DONE: Int](xpc_activity_state_done.md)
  The activity is complete.
### Execution criteria
- [func xpc_activity_copy_criteria(xpc_activity_t) -> xpc_object_t?](xpc_activity_copy_criteria(_:).md)
  Returns an XPC dictionary that describes the execution criteria of an activity.
- [func xpc_activity_set_criteria(xpc_activity_t, xpc_object_t)](xpc_activity_set_criteria(_:_:).md)
  Modifies the execution criteria of an activity.
### Scheduling
- [let XPC_ACTIVITY_REPEATING: UnsafePointer<CChar>](xpc_activity_repeating.md)
  A Boolean property that indicates whether this is a repeating activity.
- [let XPC_ACTIVITY_DELAY: UnsafePointer<CChar>](xpc_activity_delay.md)
  An integer property that indicates the number of seconds to delay before beginning the activity.
- [let XPC_ACTIVITY_GRACE_PERIOD: UnsafePointer<CChar>](xpc_activity_grace_period.md)
  An integer property that indicates the number of seconds to allow as a grace period before the scheduling of the activity becomes more aggressive.
### Time Intervals
- [let XPC_ACTIVITY_INTERVAL: UnsafePointer<CChar>](xpc_activity_interval.md)
  An integer property that indicates the desired time interval of the activity in seconds.
- [let XPC_ACTIVITY_INTERVAL_1_MIN: Int64](xpc_activity_interval_1_min.md)
  A constant that represents a 1-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_5_MIN: Int64](xpc_activity_interval_5_min.md)
  A constant that represents a 5-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_15_MIN: Int64](xpc_activity_interval_15_min.md)
  A constant that represents a 15-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_30_MIN: Int64](xpc_activity_interval_30_min.md)
  A constant that represents a 30-minute time interval.
- [let XPC_ACTIVITY_INTERVAL_1_HOUR: Int64](xpc_activity_interval_1_hour.md)
  A constant that represents a 1-hour time interval.
- [let XPC_ACTIVITY_INTERVAL_4_HOURS: Int64](xpc_activity_interval_4_hours.md)
  A constant that represents a 4-hour time interval.
- [let XPC_ACTIVITY_INTERVAL_8_HOURS: Int64](xpc_activity_interval_8_hours.md)
  A constant that represents an 8-hour time interval.
- [let XPC_ACTIVITY_INTERVAL_1_DAY: Int64](xpc_activity_interval_1_day.md)
  A constant that represents a one-day time interval.
- [let XPC_ACTIVITY_INTERVAL_7_DAYS: Int64](xpc_activity_interval_7_days.md)
  A constant that represents a seven-day time interval.
### Priority
- [let XPC_ACTIVITY_PRIORITY: UnsafePointer<CChar>](xpc_activity_priority.md)
  A string property that indicates the priority of the activity.
- [let XPC_ACTIVITY_PRIORITY_MAINTENANCE: UnsafePointer<CChar>](xpc_activity_priority_maintenance.md)
  A string that indicates an activity is maintenance priority.
- [let XPC_ACTIVITY_PRIORITY_UTILITY: UnsafePointer<CChar>](xpc_activity_priority_utility.md)
  A string that indicates an activity is utility priority.
### Power consumption
- [let XPC_ACTIVITY_ALLOW_BATTERY: UnsafePointer<CChar>](xpc_activity_allow_battery.md)
  A Boolean value that indicates whether to allow the activity to run while the computer is on battery power.
- [let XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP: UnsafePointer<CChar>](xpc_activity_require_screen_sleep.md)
  A Boolean value that indicates whether the activity performs only while the primary screen is in sleep mode.
- [let XPC_ACTIVITY_PREVENT_DEVICE_SLEEP: UnsafePointer<CChar>](xpc_activity_prevent_device_sleep.md)
  A Boolean that indicates whether the activity prevents the system from sleeping while on battery power.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc-activities)*