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

## Overview

This property defaults to [`false`](https://developer.apple.com/documentation/swift/false). To monitor the device’s battery, set this property to [`true`](https://developer.apple.com/documentation/swift/true). This enables both the [`batteryLevel`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel) and [`batteryState`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate) properties.

## See Also

- [var batteryLevel: Float](batterylevel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel))
- [var batteryState: WKInterfaceDeviceBatteryState](batterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate))
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled)*