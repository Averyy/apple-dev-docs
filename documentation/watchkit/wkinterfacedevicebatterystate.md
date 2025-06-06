# WKInterfaceDeviceBatteryState

**Framework**: Watchkit  
**Kind**: enum

The battery’s charging state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
enum WKInterfaceDeviceBatteryState
```

## Topics

### Battery States
- [WKInterfaceDeviceBatteryState.charging](wkinterfacedevicebatterystate/charging.md)
  The device is connected to a charger, but its battery charge is under 100%.
- [WKInterfaceDeviceBatteryState.full](wkinterfacedevicebatterystate/full.md)
  The device is connected to a charger, and its battery is charged to 100%.
- [WKInterfaceDeviceBatteryState.unknown](wkinterfacedevicebatterystate/unknown.md)
  An unknown battery-charging state.
- [WKInterfaceDeviceBatteryState.unplugged](wkinterfacedevicebatterystate/unplugged.md)
  The device is not connected to a charger and is running on battery power.
### Initializers
- [init?(rawValue: Int)](wkinterfacedevicebatterystate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isBatteryMonitoringEnabled: Bool](wkinterfacedevice/isbatterymonitoringenabled.md)
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryLevel: Float](wkinterfacedevice/batterylevel.md)
  The battery’s current percent charge.
- [var batteryState: WKInterfaceDeviceBatteryState](wkinterfacedevice/batterystate.md)
  The device’s battery state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate)*