# centralManager(_:didFailToConnectTo:error:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the central manager failed to establish a connection with a peripheral.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func centralManager(_ centralManager: PlaygroundBluetoothCentralManager, didFailToConnectTo peripheral: CBPeripheral, error: Error?)
```

## Parameters

- `centralManager`: The central manager that failed to make the new connection.
- `peripheral`: The peripheral that the central manager couldn’t connect to.
- `error`: An error which describes the reason for the connection failure.

## Default Implementations

### PlaygroundBluetoothCentralManagerDelegate Implementations
- [func centralManager(PlaygroundBluetoothCentralManager, didFailToConnectTo: CBPeripheral, error: Error?)](./api-3029481-centralmanager.md)
  Tells the delegate that the central manager failed to establish a connection with a peripheral.

## See Also

### Handling Disconnects
- [func centralManager(PlaygroundBluetoothCentralManager, didDisconnectFrom: CBPeripheral, error: Error?)](./api-3029476-centralmanager.md)
  Tells the delegate that the central manager disconnected from a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029480-centralmanager)*