# PlaygroundBluetoothConnectionView.Item.FirmwareStatus

**Framework**: Playground Bluetooth  
**Kind**: enum  
**Role**: Enumeration

The states you use to indicate whether a peripheral’s firmware is current

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
enum PlaygroundBluetoothConnectionView.Item.FirmwareStatus
```

## Topics

### Determining Firmware Status
- [PlaygroundBluetoothConnectionView.Item.FirmwareStatus.outOfDate](./firmwarestatus/outofdate.md)
  The state that indicates that a peripheral needs a firmware update before it can operate correctly.
- [PlaygroundBluetoothConnectionView.Item.FirmwareStatus.upToDate](./firmwarestatus/uptodate.md)
  The state that indicates that a peripheral doesn’t need a firmware update.
- [static func != (PlaygroundBluetoothConnectionView.Item.FirmwareStatus, PlaygroundBluetoothConnectionView.Item.FirmwareStatus) -> Bool](./firmwarestatus/api-3029491.md)
  Compares two firmware statuses and returns [`true`](../../../Swift/true.md) when they're different.

## See Also

### Displaying Statuses
- [var batteryLevel: Double?](./api-3029494-batterylevel.md)
  A value between 0 and 1.0 indicating a peripheral’s percent battery charge.
- [var firmwareStatus: PlaygroundBluetoothConnectionView.Item.FirmwareStatus?](./api-3029495-firmwarestatus.md)
  A value that indicates whether a peripheral needs a firmware update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/item/firmwarestatus)*