# isBatteryMonitoringEnabled

**Framework**: Watchkit  
**Kind**: property

A Boolean value that determines whether the app can monitor the device’s battery.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var isBatteryMonitoringEnabled: Bool { get set }
```

#### Discussion

This property defaults to [`false`](https://developer.apple.com/documentation/swift/false). To monitor the device’s battery, set this property to [`true`](https://developer.apple.com/documentation/swift/true). This enables both the [`batteryLevel`](wkinterfacedevice/batterylevel.md) and [`batteryState`](wkinterfacedevice/batterystate.md) properties.

## See Also

- [var batteryLevel: Float](wkinterfacedevice/batterylevel.md)
  The battery’s current percent charge.
- [var batteryState: WKInterfaceDeviceBatteryState](wkinterfacedevice/batterystate.md)
  The device’s battery state.
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md)
  The battery’s charging state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled)*