# PlaygroundBluetoothConnectionView.Item

**Framework**: Playground Bluetooth  
**Kind**: struct

A value that holds information about a peripheral displayed in a connection view.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
struct PlaygroundBluetoothConnectionView.Item
```

## Topics

### Displaying Peripheral Information
- [init(name: String, icon: UIImage, issueIcon: UIImage, firmwareStatus: PlaygroundBluetoothConnectionView.Item.FirmwareStatus?, batteryLevel: Double?)](playgroundbluetoothconnectionview/item/3029497-init.md)
  Creates a structure that holds information about a peripheral displayed in a connection view.
- [var name: String](playgroundbluetoothconnectionview/item/3029499-name.md)
  The name of a peripheral as it should appear in a connection view.
### Displaying Icons
- [var icon: UIImage](playgroundbluetoothconnectionview/item/3029496-icon.md)
  An image that represents a peripheral.
- [var issueIcon: UIImage](playgroundbluetoothconnectionview/item/3029498-issueicon.md)
  An image indicating that a peripheral may not function correctly.
### Displaying Statuses
- [var batteryLevel: Double?](playgroundbluetoothconnectionview/item/3029494-batterylevel.md)
  A value between 0 and 1.0 indicating a peripheral’s percent battery charge.
- [var firmwareStatus: PlaygroundBluetoothConnectionView.Item.FirmwareStatus?](playgroundbluetoothconnectionview/item/3029495-firmwarestatus.md)
  A value that indicates whether a peripheral needs a firmware update.
- [enum PlaygroundBluetoothConnectionView.Item.FirmwareStatus](playgroundbluetoothconnectionview/item/firmwarestatus.md)
  The states you use to indicate whether a peripheral’s firmware is current

## See Also

- [func setItem(PlaygroundBluetoothConnectionView.Item, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029517-setitem.md)
  Sets all of the information about the specified peripheral at once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/item)*