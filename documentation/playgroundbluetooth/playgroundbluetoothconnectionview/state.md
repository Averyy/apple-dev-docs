# PlaygroundBluetoothConnectionView.State

**Framework**: Playground Bluetooth  
**Kind**: enum

The states that tell users how to proceed when connecting to and switching between peripherals in a playground page.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
enum PlaygroundBluetoothConnectionView.State
```

#### Overview

The example below shows how to use the different states as part of adopting the [`PlaygroundBluetoothConnectionViewDelegate`](playgroundbluetoothconnectionviewdelegate.md) protocol.

```swift
extension PageViewDelegate: PlaygroundBluetoothConnectionViewDelegate {
    func connectionView(_ connectionView: PlaygroundBluetoothConnectionView, titleFor state: PlaygroundBluetoothConnectionView.State) -> String {
        // Pick a name that matches the types of peripheral your playground
        // supports, such as "Robot", "Speaker", or "Light".
        let name = "Peripheral"
        switch state {
        case .noConnection:
            return "Connect \(name)"
        case .connecting:
            return "Connecting \(name)"
        case .searchingForPeripherals:
            return "Searching for \(name)s"
        case .selectingPeripherals:
            return "Select a \(name)"
        case .connectedPeripheralFirmwareOutOfDate:
            return "Connect to a Different \(name)"
        }
    }
}
```

## Topics

### Waiting for Connections
- [PlaygroundBluetoothConnectionView.State.connecting](playgroundbluetoothconnectionview/state/connecting.md)
  The peripheral is in the process of connecting to a connection view’s central manager.
- [PlaygroundBluetoothConnectionView.State.noConnection](playgroundbluetoothconnectionview/state/noconnection.md)
  The connection to a peripheral has been lost.
- [PlaygroundBluetoothConnectionView.State.searchingForPeripherals](playgroundbluetoothconnectionview/state/searchingforperipherals.md)
  A connection view’s central manager is scanning for nearby peripherals.
### Selecting Connections
- [PlaygroundBluetoothConnectionView.State.selectingPeripherals](playgroundbluetoothconnectionview/state/selectingperipherals.md)
  One or more peripherals have been discovered and can be selected.
### Handling Old Firmware
- [PlaygroundBluetoothConnectionView.State.connectedPeripheralFirmwareOutOfDate](playgroundbluetoothconnectionview/state/connectedperipheralfirmwareoutofdate.md)
  The currently connected peripheral has outdated firmware and can't be used.
### Comparing Connection States
- [static func != (PlaygroundBluetoothConnectionView.State, PlaygroundBluetoothConnectionView.State) -> Bool](playgroundbluetoothconnectionview/state/3029501.md)
  Compares two connection states and returns [`true`](https://developer.apple.com/documentation/swift/true) if they're different.

## See Also

- [var delegate: PlaygroundBluetoothConnectionViewDelegate?](playgroundbluetoothconnectionview/3029510-delegate.md)
  A delegate you supply to make decisions about which peripherals are displayed in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/state)*