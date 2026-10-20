# WKInterfaceDeviceBatteryState

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

The battery’s charging state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
enum WKInterfaceDeviceBatteryState
```

```c
enum WKInterfaceDeviceBatteryState : NSInteger;
```

## Topics

### Battery States
- [WKInterfaceDeviceBatteryState.charging](./wkinterfacedevicebatterystate/charging.md)
  The device is connected to a charger, but its battery charge is under 100%.
- [WKInterfaceDeviceBatteryState.full](./wkinterfacedevicebatterystate/full.md)
  The device is connected to a charger, and its battery is charged to 100%.
- [WKInterfaceDeviceBatteryState.unknown](./wkinterfacedevicebatterystate/unknown.md)
  An unknown battery-charging state.
- [WKInterfaceDeviceBatteryState.unplugged](./wkinterfacedevicebatterystate/unplugged.md)
  The device is not connected to a charger and is running on battery power.
### Initializers
- [init?(rawValue: Int)](./wkinterfacedevicebatterystate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reading Information About the Battery
- [var isBatteryMonitoringEnabled: Bool](./wkinterfacedevice/isbatterymonitoringenabled.md)
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryLevel: Float](./wkinterfacedevice/batterylevel.md)
  The battery’s current percent charge.
- [var batteryState: WKInterfaceDeviceBatteryState](./wkinterfacedevice/batterystate.md)
  The device’s battery state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate)*