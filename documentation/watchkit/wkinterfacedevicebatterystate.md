# WKInterfaceDeviceBatteryState

**Framework**: WatchKit  
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
- [BitwiseCopyable](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [RawRepresentable](https://developer.apple.com/documentation/Swift/RawRepresentable)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [var isBatteryMonitoringEnabled: Bool](wkinterfacedevice/isbatterymonitoringenabled.md)
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryLevel: Float](wkinterfacedevice/batterylevel.md)
  The battery’s current percent charge.
- [var batteryState: WKInterfaceDeviceBatteryState](wkinterfacedevice/batterystate.md)
  The device’s battery state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate)*