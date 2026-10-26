# centralManager(_:didDisconnectFrom:error:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method

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
- `error`: An error which, if present, describes the reason for the connection failure. The absence of an error indicates that the disconnection was requested via the manager’s [`disconnect(from:)`](../playgroundbluetoothcentralmanager/api-3029469-disconnect.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029477-centralmanager)*