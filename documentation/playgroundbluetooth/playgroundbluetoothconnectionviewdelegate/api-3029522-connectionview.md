# connectionView(_:firmwareUpdateInstructionsFor:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Required**: Yes

Tells the delegate that a peripheral has a firmware update available.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func connectionView(_ connectionView: PlaygroundBluetoothConnectionView, firmwareUpdateInstructionsFor peripheral: CBPeripheral) -> String
```

#### Return_value

A localized string that contains firmware update instructions.

## Parameters

- `connectionView`: The central manager that failed to make the new connection.
- `peripheral`: The peripheral that the central manager couldn’t connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate/3029522-connectionview)*