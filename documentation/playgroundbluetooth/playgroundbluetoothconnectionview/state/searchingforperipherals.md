# PlaygroundBluetoothConnectionView.State.searchingForPeripherals

**Framework**: Playground Bluetooth  
**Kind**: enumelt

A connection view’s central manager is scanning for nearby peripherals.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case searchingForPeripherals
```

#### Discussion

The connection view title corresponding to this state should be in one of the following formats:

```swift
"Searching for \(item.name)"

// Or:
"Searching for \(item.name)s"
```

## See Also

- [PlaygroundBluetoothConnectionView.State.connecting](playgroundbluetoothconnectionview/state/connecting.md)
  The peripheral is in the process of connecting to a connection view’s central manager.
- [PlaygroundBluetoothConnectionView.State.noConnection](playgroundbluetoothconnectionview/state/noconnection.md)
  The connection to a peripheral has been lost.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/state/searchingforperipherals)*