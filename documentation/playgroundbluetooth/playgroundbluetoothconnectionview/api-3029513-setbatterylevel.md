# setBatteryLevel(_:forPeripheral:)

**Framework**: Playground Bluetooth  
**Kind**: instm  
**Role**: Instance Method

Displays the battery level for the specified peripheral.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func setBatteryLevel(_ batteryLevel: Double?, forPeripheral peripheral: CBPeripheral)
```

## Parameters

- `batteryLevel`: A value between 0 and 1.0 indicating the peripheral’s percent battery charge.
- `peripheral`: The peripheral corresponding to the battery level being displayed.

## See Also

### Displaying Individual Details
- [func setFirmwareStatus(PlaygroundBluetoothConnectionView.Item.FirmwareStatus?, forPeripheral: CBPeripheral)](./api-3029514-setfirmwarestatus.md)
  Displays whether or not the specified peripheral’s firmware is up-to-date.
- [func setIcon(UIImage, forPeripheral: CBPeripheral)](./api-3029515-seticon.md)
  Displays an icon representing the specified peripheral.
- [func setIssueIcon(UIImage, forPeripheral: CBPeripheral)](./api-3029516-setissueicon.md)
  Displays an icon indicating that the specified peripheral is available but may not be usable.
- [func setName(String, forPeripheral: CBPeripheral)](./api-3029518-setname.md)
  Displays the name of the specified peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/3029513-setbatterylevel)*