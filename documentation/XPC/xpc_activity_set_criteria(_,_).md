# xpc_activity_set_criteria(_:_:)

**Framework**: XPC  
**Kind**: func  
**Role**: Function

Modifies the execution criteria of an activity.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func xpc_activity_set_criteria(_ activity: xpc_activity_t, _ criteria: xpc_object_t)
```

```c
extern void xpc_activity_set_criteria(xpc_activity_t activity, xpc_object_t criteria);
```

## See Also

### Execution criteria
- [func xpc_activity_copy_criteria(xpc_activity_t) -> xpc_object_t?](./xpc_activity_copy_criteria%28_%29.md)
  Returns an XPC dictionary that describes the execution criteria of an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_set_criteria(_:_:))*