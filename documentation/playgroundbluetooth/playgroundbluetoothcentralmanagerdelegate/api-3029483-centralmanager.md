# centralManager(_:willConnectTo:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method

Tells the delegate that the central manager is about to attempt to establish a connection with a peripheral.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func centralManager(_ centralManager: PlaygroundBluetoothCentralManager, willConnectTo peripheral: CBPeripheral)
```

## Parameters

- `centralManager`: The central manager attempting the new connection.
- `peripheral`: The peripheral that the central manager is attempting to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029483-centralmanager)*