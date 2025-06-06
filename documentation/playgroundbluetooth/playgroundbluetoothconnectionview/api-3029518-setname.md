# setName(_:forPeripheral:)

**Framework**: Playground Bluetooth  
**Kind**: instm

Displays the name of the specified peripheral.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func setName(_ name: String, forPeripheral peripheral: CBPeripheral)
```

## Parameters

- `name`: The user-facing name of the specified peripheral.
- `peripheral`: The peripheral corresponding to the name.

## See Also

- [func setBatteryLevel(Double?, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029513-setbatterylevel.md)
  Displays the battery level for the specified peripheral.
- [func setFirmwareStatus(PlaygroundBluetoothConnectionView.Item.FirmwareStatus?, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029514-setfirmwarestatus.md)
  Displays whether or not the specified peripheral’s firmware is up-to-date.
- [func setIcon(UIImage, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029515-seticon.md)
  Displays an icon representing the specified peripheral.
- [func setIssueIcon(UIImage, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029516-setissueicon.md)
  Displays an icon indicating that the specified peripheral is available but may not be usable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/3029518-setname)*