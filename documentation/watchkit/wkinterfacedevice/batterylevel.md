# batteryLevel

**Framework**: Watchkit  
**Kind**: property

The battery’s current percent charge.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var batteryLevel: Float { get }
```

#### Discussion

If battery monitoring is enabled, this property is set to a value between `0.0` (0% charge) and `1.0` (100% charge). When the [`batteryState`](wkinterfacedevice/batterystate.md) property is set to [`WKInterfaceDeviceBatteryState.unknown`](wkinterfacedevicebatterystate/unknown.md) (for example, when battery monitoring is disabled), the value is `-1.0`.

## See Also

- [var isBatteryMonitoringEnabled: Bool](wkinterfacedevice/isbatterymonitoringenabled.md)
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryState: WKInterfaceDeviceBatteryState](wkinterfacedevice/batterystate.md)
  The device’s battery state.
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md)
  The battery’s charging state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel)*