# XPC_ACTIVITY_REQUIRE_HDD_SPINNING

**Framework**: XPC  
**Kind**: var

A Boolean value indicating whether the activity should only be performed while the hard disk drive (HDD) is spinning.

**Availability**:
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let XPC_ACTIVITY_REQUIRE_HDD_SPINNING: UnsafePointer<CChar>
```

#### Discussion

Computers with flash storage are considered to be equivalent to HDD spinning. Defaults to `NO`.

## See Also

- [let XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL: UnsafePointer<CChar>](xpc_activity_require_battery_level.md)
  An integer percentage of minimum battery charge required to allow the activity to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_require_hdd_spinning)*