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
- [WKInterfaceDeviceBatteryState.charging](charging.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/charging))
  The device is connected to a charger, but its battery charge is under 100%.
- [WKInterfaceDeviceBatteryState.full](full.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/full))
  The device is connected to a charger, and its battery is charged to 100%.
- [WKInterfaceDeviceBatteryState.unknown](unknown.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown))
  An unknown battery-charging state.
- [WKInterfaceDeviceBatteryState.unplugged](unplugged.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unplugged))
  The device is not connected to a charger and is running on battery power.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [var isBatteryMonitoringEnabled: Bool](isbatterymonitoringenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled))
- [var batteryLevel: Float](batterylevel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel))
- [var batteryState: WKInterfaceDeviceBatteryState](batterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate)*