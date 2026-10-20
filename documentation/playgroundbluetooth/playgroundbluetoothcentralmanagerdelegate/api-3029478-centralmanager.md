# centralManager(_:didDiscover:withAdvertisementData:rssi:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that a peripheral has been discovered during scanning.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func centralManager(_ centralManager: PlaygroundBluetoothCentralManager, didDiscover peripheral: CBPeripheral, withAdvertisementData advertisementData: [String : Any]?, rssi: Double)
```

## Parameters

- `centralManager`: The central manager providing this information.
- `peripheral`: The newly discovered peripheral.
- `advertisementData`: A dictionary containing any advertisement data that the peripheral provides.
- `rssi`: The current received signal strength indicator of the peripheral in decibels.

## Default Implementations

### PlaygroundBluetoothCentralManagerDelegate Implementations
- [func centralManager(PlaygroundBluetoothCentralManager, didDiscover: CBPeripheral, withAdvertisementData: [String : Any]?, rssi: Double)](./api-3029479-centralmanager.md)
  Tells the delegate that a peripheral has been discovered during scanning.

## See Also

### Discovering Peripherals
- [func centralManager(PlaygroundBluetoothCentralManager, willConnectTo: CBPeripheral)](./api-3029482-centralmanager.md)
  Tells the delegate that the central manager is about to attempt to establish a connection with a peripheral.
- [func centralManager(PlaygroundBluetoothCentralManager, didConnectTo: CBPeripheral)](./api-3029474-centralmanager.md)
  Tells the delegate that the central manager established a connection with a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029478-centralmanager)*