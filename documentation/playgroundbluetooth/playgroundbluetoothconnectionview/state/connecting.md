# PlaygroundBluetoothConnectionView.State.connecting

**Framework**: Playground Bluetooth  
**Kind**: enumelt  
**Role**: Enumeration Case

The peripheral is in the process of connecting to a connection view’s central manager.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case connecting
```

#### Discussion

The connection view title corresponding to this state should be in the following format:

```swift
"Connecting \(item.name)"
```

## See Also

### Waiting for Connections
- [PlaygroundBluetoothConnectionView.State.noConnection](./noconnection.md)
  The connection to a peripheral has been lost.
- [PlaygroundBluetoothConnectionView.State.searchingForPeripherals](./searchingforperipherals.md)
  A connection view’s central manager is scanning for nearby peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/state/connecting)*