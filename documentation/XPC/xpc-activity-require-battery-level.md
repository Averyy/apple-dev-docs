# XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL

**Framework**: XPC  
**Kind**: var

An integer percentage of minimum battery charge required to allow the activity to run.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL: UnsafePointer<CChar>
```

#### Discussion

A default minimum battery level is determined by the system.

## See Also

- [let XPC_ACTIVITY_REQUIRE_HDD_SPINNING: UnsafePointer<CChar>](xpc_activity_require_hdd_spinning.md)
  A Boolean value indicating whether the activity should only be performed while the hard disk drive (HDD) is spinning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_require_battery_level)*