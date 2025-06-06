# PlaygroundBluetoothConnectionView.State.noConnection

**Framework**: Playground Bluetooth  
**Kind**: enumelt

The connection to a peripheral has been lost.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case noConnection
```

#### Discussion

The connection view title corresponding to this state should be in the following format:

```swift
"Connect \(item.name)"
```

## See Also

- [PlaygroundBluetoothConnectionView.State.connecting](playgroundbluetoothconnectionview/state/connecting.md)
  The peripheral is in the process of connecting to a connection view’s central manager.
- [PlaygroundBluetoothConnectionView.State.searchingForPeripherals](playgroundbluetoothconnectionview/state/searchingforperipherals.md)
  A connection view’s central manager is scanning for nearby peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/state/noconnection)*