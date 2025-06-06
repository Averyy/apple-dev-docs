# centralManager(_:didConnectTo:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Required**: Yes

Tells the delegate that the central manager established a connection with a peripheral.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func centralManager(_ centralManager: PlaygroundBluetoothCentralManager, didConnectTo peripheral: CBPeripheral)
```

## Parameters

- `centralManager`: The central manager that made the new connection.
- `peripheral`: The newly connected peripheral.

## See Also

- [func centralManager(PlaygroundBluetoothCentralManager, didDiscover: CBPeripheral, withAdvertisementData: [String : Any]?, rssi: Double)](playgroundbluetoothcentralmanagerdelegate/3029478-centralmanager.md)
  Tells the delegate that a peripheral has been discovered during scanning.
- [func centralManager(PlaygroundBluetoothCentralManager, willConnectTo: CBPeripheral)](playgroundbluetoothcentralmanagerdelegate/3029482-centralmanager.md)
  Tells the delegate that the central manager is about to attempt to establish a connection with a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029474-centralmanager)*