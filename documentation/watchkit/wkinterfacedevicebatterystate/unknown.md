# WKInterfaceDeviceBatteryState.unknown

**Framework**: Watchkit  
**Kind**: case

An unknown battery-charging state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case unknown
```

#### Discussion

When the device’s [`isBatteryMonitoringEnabled`](wkinterfacedevice/isbatterymonitoringenabled.md) property is set to [`false`](https://developer.apple.com/documentation/swift/false), its [`batteryState`](wkinterfacedevice/batterystate.md) property is set to [`WKInterfaceDeviceBatteryState.unknown`](wkinterfacedevicebatterystate/unknown.md).

## See Also

- [WKInterfaceDeviceBatteryState.charging](wkinterfacedevicebatterystate/charging.md)
  The device is connected to a charger, but its battery charge is under 100%.
- [WKInterfaceDeviceBatteryState.full](wkinterfacedevicebatterystate/full.md)
  The device is connected to a charger, and its battery is charged to 100%.
- [WKInterfaceDeviceBatteryState.unplugged](wkinterfacedevicebatterystate/unplugged.md)
  The device is not connected to a charger and is running on battery power.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown)*