# xpc_activity_copy_criteria(_:)

**Framework**: Xpc  
**Kind**: func

Returns an XPC dictionary that describes the execution criteria of an activity.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func xpc_activity_copy_criteria(_ activity: xpc_activity_t) -> xpc_object_t?
```

#### Discussion

Returns `NULL` in cases where the activity has already completed, for example, when checking in to an event that finished and wasn’t rescheduled.

## See Also

- [func xpc_activity_set_criteria(xpc_activity_t, xpc_object_t)](xpc_activity_set_criteria(_:_:).md)
  Modifies the execution criteria of an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_copy_criteria(_:))*