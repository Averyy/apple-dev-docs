# WKBluetoothAlertRefreshBackgroundTask

**Framework**: Watchkit  
**Kind**: class

A task for handling timely Bluetooth alerts in the background.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
class WKBluetoothAlertRefreshBackgroundTask
```

## Mentions

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

## Overview

Your app can receive [`WKBluetoothAlertRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask) tasks to handle timely alerts in the background. Use these tasks to reconnect a peripheral and handle a critical alert. Apps that use timely alerts can also scan for a specific system identifier (UUID) while in the background. You can then perform the initial connection and pair the devices if necessary.

To receive timely alerts, your peripheral must use Generic Attribute Profile (GATT) transactions. Call [`setNotifyValue(_:for:)`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheral/setNotifyValue(_:for:)) to enable notifications for the specified characteristic. Then, any changes to the peripheral’s characteristic wakes your app using a [`WKBluetoothAlertRefreshBackgroundTask`](https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask) task. Use this task to reconnect to the peripheral and handle the critical alert.

> **Note**:  In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

 In watchOS 9 and later, SwiftUI Background tasks are the preferred way to handle background tasks and interactions. For more information, [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/Scene/backgroundTask(_:action:)).

The critical alerts and background scans share a budget. Your app can only use five timely alerts or background scans within a rolling 24-hour window.

When your app receives a timely alert and your budget has only one Bluetooth alert task remaining, the system raises a [`leGattNearBackgroundNotificationLimit`](https://developer.apple.com/documentation/CoreBluetooth/CBError-swift.struct/leGattNearBackgroundNotificationLimit) error. If you exceed the budget, it raises a [`leGattExceededBackgroundNotificationLimit`](https://developer.apple.com/documentation/CoreBluetooth/CBError-swift.struct/leGattExceededBackgroundNotificationLimit) error. The system passes these errors to your [`CBPeripheralDelegate`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheralDelegate), by calling methods like the [`peripheral(_:didUpdateValueFor:error:)`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheralDelegate/peripheral(_:didUpdateValueFor:error:)-1xyna) method.

If you exceed your budget, your app doesn’t receive any timely alerts until additional background budget becomes available. The user can reset this budget by launching your app.

## Relationships

### Inherits From
- [WKRefreshBackgroundTask](wkrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))
- [Preparing to take your watchOS app’s snapshot](preparing-to-take-your-watchos-app-s-snapshot.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/preparing-to-take-your-watchos-app-s-snapshot))
- [class WKApplicationRefreshBackgroundTask](wkapplicationrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask))
- [class WKURLSessionRefreshBackgroundTask](wkurlsessionrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask))
- [class WKWatchConnectivityRefreshBackgroundTask](wkwatchconnectivityrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask))
- [class WKIntentDidRunRefreshBackgroundTask](wkintentdidrunrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkintentdidrunrefreshbackgroundtask))
- [class WKRelevantShortcutRefreshBackgroundTask](wkrelevantshortcutrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrelevantshortcutrefreshbackgroundtask))
- [class WKSnapshotRefreshBackgroundTask](wksnapshotrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask))
- [class WKRefreshBackgroundTask](wkrefreshbackgroundtask.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkbluetoothalertrefreshbackgroundtask)*