# batteryLevel

**Framework**: WatchKit  
**Kind**: property

The battery’s current percent charge.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var batteryLevel: Float { get }
```

#### Discussion

If battery monitoring is enabled, this property is set to a value between `0.0` (0% charge) and `1.0` (100% charge). When the [`batteryState`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate) property is set to [`WKInterfaceDeviceBatteryState.unknown`](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown) (for example, when battery monitoring is disabled), the value is `-1.0`.

## See Also

- [var isBatteryMonitoringEnabled: Bool](isbatterymonitoringenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled))
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryState: WKInterfaceDeviceBatteryState](batterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate))
  The device’s battery state.
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate))
  The battery’s charging state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel)*