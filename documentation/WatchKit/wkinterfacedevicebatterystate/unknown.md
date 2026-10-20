# WKInterfaceDeviceBatteryState.unknown

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

An unknown battery-charging state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
case unknown
```

```c
WKInterfaceDeviceBatteryStateUnknown
```

#### Discussion

When the device’s [`isBatteryMonitoringEnabled`](../wkinterfacedevice/isbatterymonitoringenabled.md) property is set to [`false`](../../Swift/false.md), its [`batteryState`](../wkinterfacedevice/batterystate.md) property is set to [`WKInterfaceDeviceBatteryState.unknown`](./unknown.md).

## See Also

### Battery States
- [WKInterfaceDeviceBatteryState.charging](./charging.md)
  The device is connected to a charger, but its battery charge is under 100%.
- [WKInterfaceDeviceBatteryState.full](./full.md)
  The device is connected to a charger, and its battery is charged to 100%.
- [WKInterfaceDeviceBatteryState.unplugged](./unplugged.md)
  The device is not connected to a charger and is running on battery power.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown)*