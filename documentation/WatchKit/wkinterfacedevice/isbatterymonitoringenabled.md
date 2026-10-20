# isBatteryMonitoringEnabled

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the app can monitor the device’s battery.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var isBatteryMonitoringEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isBatteryMonitoringEnabled) BOOL batteryMonitoringEnabled;
```

#### Discussion

This property defaults to [`false`](../../Swift/false.md). To monitor the device’s battery, set this property to [`true`](../../Swift/true.md). This enables both the [`batteryLevel`](./batterylevel.md) and [`batteryState`](./batterystate.md) properties.

## See Also

### Reading Information About the Battery
- [var batteryLevel: Float](./batterylevel.md)
  The battery’s current percent charge.
- [var batteryState: WKInterfaceDeviceBatteryState](./batterystate.md)
  The device’s battery state.
- [enum WKInterfaceDeviceBatteryState](../wkinterfacedevicebatterystate.md)
  The battery’s charging state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled)*