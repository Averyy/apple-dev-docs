# setIcon(_:forPeripheral:)

**Framework**: Playground Bluetooth  
**Kind**: instm  
**Role**: Instance Method

Displays an icon representing the specified peripheral.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func setIcon(_ icon: UIImage, forPeripheral peripheral: CBPeripheral)
```

## Parameters

- `icon`: An icon that represents the specified peripheral.
- `peripheral`: The peripheral corresponding to the icon being displayed.

## See Also

### Displaying Individual Details
- [func setBatteryLevel(Double?, forPeripheral: CBPeripheral)](./api-3029513-setbatterylevel.md)
  Displays the battery level for the specified peripheral.
- [func setFirmwareStatus(PlaygroundBluetoothConnectionView.Item.FirmwareStatus?, forPeripheral: CBPeripheral)](./api-3029514-setfirmwarestatus.md)
  Displays whether or not the specified peripheral’s firmware is up-to-date.
- [func setIssueIcon(UIImage, forPeripheral: CBPeripheral)](./api-3029516-setissueicon.md)
  Displays an icon indicating that the specified peripheral is available but may not be usable.
- [func setName(String, forPeripheral: CBPeripheral)](./api-3029518-setname.md)
  Displays the name of the specified peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/3029515-seticon)*