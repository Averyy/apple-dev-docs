# connectionView(_:willDisconnectFrom:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method  
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

## Default Implementations

### PlaygroundBluetoothConnectionViewDelegate Implementations
- [func connectionView(PlaygroundBluetoothConnectionView, willDisconnectFrom: CBPeripheral)](./api-3029529-connectionview.md)
  Tells the delegate that a connected peripheral is about to be disconnected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate/3029528-connectionview)*