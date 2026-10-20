# XPC_ACTIVITY_REQUIRE_HDD_SPINNING

**Framework**: XPC  
**Kind**: var  
**Role**: Global Variable

A Boolean value indicating whether the activity should only be performed while the hard disk drive (HDD) is spinning.

**Availability**:
- iOS 7.0+ - Deprecated in 7.0
- iPadOS 7.0+ - Deprecated in 7.0
- Mac Catalyst 7.0+ - Deprecated in 7.0
- tvOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: REQUIRE_HDD_SPINNING is not implemented

## Declaration

```swift
let XPC_ACTIVITY_REQUIRE_HDD_SPINNING: UnsafePointer<CChar>
```

```c
extern const char * const XPC_ACTIVITY_REQUIRE_HDD_SPINNING;
```

#### Discussion

Computers with flash storage are considered to be equivalent to HDD spinning. Defaults to `NO`.

## See Also

### Deprecated
- [let XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL: UnsafePointer<CChar>](./xpc_activity_require_battery_level.md)
  An integer percentage of minimum battery charge required to allow the activity to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_require_hdd_spinning)*