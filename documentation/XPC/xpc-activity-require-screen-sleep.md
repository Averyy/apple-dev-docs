# XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP

**Framework**: Xpc  
**Kind**: var

A Boolean value that indicates whether the activity performs only while the primary screen is in sleep mode.

**Availability**:
- macOS 10.9+

## Declaration

```swift
let XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP: UnsafePointer<CChar>
```

#### Discussion

Defaults to `false`.

## See Also

- [let XPC_ACTIVITY_ALLOW_BATTERY: UnsafePointer<CChar>](xpc_activity_allow_battery.md)
  A Boolean value that indicates whether to allow the activity to run while the computer is on battery power.
- [let XPC_ACTIVITY_PREVENT_DEVICE_SLEEP: UnsafePointer<CChar>](xpc_activity_prevent_device_sleep.md)
  A Boolean that indicates whether the activity prevents the system from sleeping while on battery power.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_require_screen_sleep)*