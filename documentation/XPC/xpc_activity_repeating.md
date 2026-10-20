# XPC_ACTIVITY_REPEATING

**Framework**: XPC  
**Kind**: var  
**Role**: Global Variable

A Boolean property that indicates whether this is a repeating activity.

**Availability**:
- macOS 10.9+

## Declaration

```swift
let XPC_ACTIVITY_REPEATING: UnsafePointer<CChar>
```

```c
extern const char * const XPC_ACTIVITY_REPEATING;
```

## See Also

### Scheduling
- [let XPC_ACTIVITY_DELAY: UnsafePointer<CChar>](./xpc_activity_delay.md)
  An integer property that indicates the number of seconds to delay before beginning the activity.
- [let XPC_ACTIVITY_GRACE_PERIOD: UnsafePointer<CChar>](./xpc_activity_grace_period.md)
  An integer property that indicates the number of seconds to allow as a grace period before the scheduling of the activity becomes more aggressive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_repeating)*