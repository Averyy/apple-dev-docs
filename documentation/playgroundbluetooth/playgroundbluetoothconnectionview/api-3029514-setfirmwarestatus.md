# setFirmwareStatus(_:forPeripheral:)

**Framework**: Playground Bluetooth  
**Kind**: instm

Displays whether or not the specified peripheral’s firmware is up-to-date.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func setFirmwareStatus(_ firmwareStatus: PlaygroundBluetoothConnectionView.Item.FirmwareStatus?, forPeripheral peripheral: CBPeripheral)
```

## Parameters

- `firmwareStatus`: A value that indicates whether the specified peripheral needs a firmware update.
- `peripheral`: The peripheral corresponding to the firmware readiness being set.

## See Also

- [func setBatteryLevel(Double?, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029513-setbatterylevel.md)
  Displays the battery level for the specified peripheral.
- [func setIcon(UIImage, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029515-seticon.md)
  Displays an icon representing the specified peripheral.
- [func setIssueIcon(UIImage, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029516-setissueicon.md)
  Displays an icon indicating that the specified peripheral is available but may not be usable.
- [func setName(String, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029518-setname.md)
  Displays the name of the specified peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/3029514-setfirmwarestatus)*