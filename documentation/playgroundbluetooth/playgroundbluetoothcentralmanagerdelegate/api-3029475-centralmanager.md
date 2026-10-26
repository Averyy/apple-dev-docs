# centralManager(_:didConnectTo:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029475-centralmanager)*