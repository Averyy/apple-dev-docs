# PlaygroundBluetoothCentralManagerDelegate

**Framework**: Playground Bluetooth  
**Kind**: intf

A delegate you use to respond to peripheral discovery and manage the lifecycle of connections.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
protocol PlaygroundBluetoothCentralManagerDelegate : AnyObject
```

## Topics

### Discovering Peripherals
- [func centralManager(PlaygroundBluetoothCentralManager, didDiscover: CBPeripheral, withAdvertisementData: [String : Any]?, rssi: Double)](playgroundbluetoothcentralmanagerdelegate/3029478-centralmanager.md)
  Tells the delegate that a peripheral has been discovered during scanning.
- [func centralManager(PlaygroundBluetoothCentralManager, willConnectTo: CBPeripheral)](playgroundbluetoothcentralmanagerdelegate/3029482-centralmanager.md)
  Tells the delegate that the central manager is about to attempt to establish a connection with a peripheral.
- [func centralManager(PlaygroundBluetoothCentralManager, didConnectTo: CBPeripheral)](playgroundbluetoothcentralmanagerdelegate/3029474-centralmanager.md)
  Tells the delegate that the central manager established a connection with a peripheral.
### Handling State Changes
- [func centralManagerStateDidChange(PlaygroundBluetoothCentralManager)](playgroundbluetoothcentralmanagerdelegate/3029484-centralmanagerstatedidchange.md)
  Tells the delegate that the state of the central manager has changed.
### Handling Disconnects
- [func centralManager(PlaygroundBluetoothCentralManager, didDisconnectFrom: CBPeripheral, error: Error?)](playgroundbluetoothcentralmanagerdelegate/3029476-centralmanager.md)
  Tells the delegate that the central manager disconnected from a peripheral.
- [func centralManager(PlaygroundBluetoothCentralManager, didFailToConnectTo: CBPeripheral, error: Error?)](playgroundbluetoothcentralmanagerdelegate/3029480-centralmanager.md)
  Tells the delegate that the central manager failed to establish a connection with a peripheral.

## See Also

- [Connecting to Bluetooth Peripherals in Swift Playgrounds](connecting_to_bluetooth_peripherals_in_swift_playgrounds.md)
  Scan for peripherals and display them in your playground's live view.
- [class PlaygroundBluetoothCentralManager](playgroundbluetoothcentralmanager.md)
  A streamlined interface for connecting the central manager for the current playground page to nearby Bluetooth peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate)*