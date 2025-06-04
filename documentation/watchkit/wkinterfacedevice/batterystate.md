# batteryState

**Framework**: Watchkit  
**Kind**: property

The device’s battery state.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
var batteryState: WKInterfaceDeviceBatteryState { get }
```

## Overview

If battery monitoring is enabled, this property is set to the device’s current battery state. For a list of possible states, see [`WKInterfaceDeviceBatteryState`](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate).

If battery monitoring is disabled, this property is set to [`WKInterfaceDeviceBatteryState.unknown`](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate/unknown).

## See Also

- [var isBatteryMonitoringEnabled: Bool](isbatterymonitoringenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled))
- [var batteryLevel: Float](batterylevel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel))
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate)*