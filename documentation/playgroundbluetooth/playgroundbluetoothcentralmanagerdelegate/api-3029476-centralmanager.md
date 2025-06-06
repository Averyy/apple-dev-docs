# centralManager(_:didDisconnectFrom:error:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Required**: Yes

Tells the delegate that the central manager disconnected from a peripheral.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func centralManager(_ centralManager: PlaygroundBluetoothCentralManager, didDisconnectFrom peripheral: CBPeripheral, error: Error?)
```

## Parameters

- `centralManager`: The central manager that disconnected from a peripheral.
- `peripheral`: The peripheral that the central manager disconnected from.
- `error`: An error which, if present, describes the reason for the connection failure. The absence of an error indicates that the disconnection was requested via the manager’s   method.

## See Also

- [func centralManager(PlaygroundBluetoothCentralManager, didFailToConnectTo: CBPeripheral, error: Error?)](playgroundbluetoothcentralmanagerdelegate/3029480-centralmanager.md)
  Tells the delegate that the central manager failed to establish a connection with a peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029476-centralmanager)*