# setIssueIcon(_:forPeripheral:)

**Framework**: Playground Bluetooth  
**Kind**: instm

Displays an icon indicating that the specified peripheral is available but may not be usable.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func setIssueIcon(_ issueIcon: UIImage, forPeripheral peripheral: CBPeripheral)
```

#### Discussion

Use an issue icon to indicate problems such as outdated firmware or a lost connection.

## Parameters

- `issueIcon`: An icon indicating that the specified peripheral may not function correctly.
- `peripheral`: The problematic peripheral.

## See Also

- [func setBatteryLevel(Double?, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029513-setbatterylevel.md)
  Displays the battery level for the specified peripheral.
- [func setFirmwareStatus(PlaygroundBluetoothConnectionView.Item.FirmwareStatus?, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029514-setfirmwarestatus.md)
  Displays whether or not the specified peripheral’s firmware is up-to-date.
- [func setIcon(UIImage, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029515-seticon.md)
  Displays an icon representing the specified peripheral.
- [func setName(String, forPeripheral: CBPeripheral)](playgroundbluetoothconnectionview/3029518-setname.md)
  Displays the name of the specified peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/3029516-setissueicon)*