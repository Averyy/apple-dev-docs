# XPC_ACTIVITY_PREVENT_DEVICE_SLEEP

**Framework**: Xpc  
**Kind**: var

A Boolean that indicates whether the activity prevents the system from sleeping while on battery power.

**Availability**:
- macOS 12.0+

## Declaration

```swift
let XPC_ACTIVITY_PREVENT_DEVICE_SLEEP: UnsafePointer<CChar>
```

#### Discussion

When set to `true`, the activity scheduler takes the necessary power assertions to keep the device awake, excluding the screen. Only set this property for activities that perform critical system functions, and that system sleep can’t interrupt. Note that setting this property can affect battery life.

## See Also

- [let XPC_ACTIVITY_ALLOW_BATTERY: UnsafePointer<CChar>](xpc_activity_allow_battery.md)
  A Boolean value that indicates whether to allow the activity to run while the computer is on battery power.
- [let XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP: UnsafePointer<CChar>](xpc_activity_require_screen_sleep.md)
  A Boolean value that indicates whether the activity performs only while the primary screen is in sleep mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_activity_prevent_device_sleep)*