# batteryState

**Framework**: WatchKit  
**Kind**: property

The device’s battery state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var batteryState: WKInterfaceDeviceBatteryState { get }
```

#### Discussion

If battery monitoring is enabled, this property is set to the device’s current battery state. For a list of possible states, see [`WKInterfaceDeviceBatteryState`](wkinterfacedevicebatterystate.md).

If battery monitoring is disabled, this property is set to [`WKInterfaceDeviceBatteryState.unknown`](wkinterfacedevicebatterystate/unknown.md).

## See Also

- [var isBatteryMonitoringEnabled: Bool](wkinterfacedevice/isbatterymonitoringenabled.md)
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryLevel: Float](wkinterfacedevice/batterylevel.md)
  The battery’s current percent charge.
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md)
  The battery’s charging state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate)*