# batteryLevel

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The battery’s current percent charge.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var batteryLevel: Float { get }
```

```objc
@property (nonatomic, readonly) float batteryLevel;
```

## Discussion

If battery monitoring is enabled, this property is set to a value between `0.0` (0% charge) and `1.0` (100% charge). When the [`batteryState`](./batterystate.md) property is set to [`WKInterfaceDeviceBatteryState.unknown`](../wkinterfacedevicebatterystate/unknown.md) (for example, when battery monitoring is disabled), the value is `-1.0`.

## See Also

### Reading Information About the Battery
- [var isBatteryMonitoringEnabled: Bool](./isbatterymonitoringenabled.md)
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryState: WKInterfaceDeviceBatteryState](./batterystate.md)
  The device’s battery state.
- [enum WKInterfaceDeviceBatteryState](../wkinterfacedevicebatterystate.md)
  The battery’s charging state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel)*