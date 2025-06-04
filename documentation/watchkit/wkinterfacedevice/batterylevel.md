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

## Overview

If battery monitoring is enabled, this property is set to a value between `0.0` (0% charge) and `1.0` (100% charge). When the [`batteryState`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate) property is set to [`WKInterfaceDeviceBatteryState.unknown`](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown) (for example, when battery monitoring is disabled), the value is `-1.0`.

## See Also

- [var isBatteryMonitoringEnabled: Bool](isbatterymonitoringenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled))
- [var batteryState: WKInterfaceDeviceBatteryState](batterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate))
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel)*