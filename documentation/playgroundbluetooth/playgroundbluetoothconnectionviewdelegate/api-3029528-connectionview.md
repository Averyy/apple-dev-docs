# connectionView(_:willDisconnectFrom:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Required**: Yes

Tells the delegate that a connected peripheral is about to be disconnected.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func connectionView(_ connectionView: PlaygroundBluetoothConnectionView, willDisconnectFrom peripheral: CBPeripheral)
```

## Parameters

- `connectionView`: The connection view currently displaying the connection to this peripheral.
- `peripheral`: The peripheral facing emminent disconnection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate/3029528-connectionview)*