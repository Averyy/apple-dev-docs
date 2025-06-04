# WKInterfaceDeviceBatteryState.unknown

**Framework**: WatchKit  
**Kind**: case

An unknown battery-charging state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case unknown
```

#### Discussion

When the device’s [`isBatteryMonitoringEnabled`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled) property is set to [`false`](https://developer.apple.com/documentation/swift/false), its [`batteryState`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate) property is set to [`WKInterfaceDeviceBatteryState.unknown`](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown).

## See Also

- [WKInterfaceDeviceBatteryState.charging](charging.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/charging))
  The device is connected to a charger, but its battery charge is under 100%.
- [WKInterfaceDeviceBatteryState.full](full.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/full))
  The device is connected to a charger, and its battery is charged to 100%.
- [WKInterfaceDeviceBatteryState.unplugged](unplugged.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unplugged))
  The device is not connected to a charger and is running on battery power.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown)*