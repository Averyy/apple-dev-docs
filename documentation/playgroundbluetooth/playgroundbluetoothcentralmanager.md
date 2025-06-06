# PlaygroundBluetoothCentralManager

**Framework**: Playground Bluetooth  
**Kind**: cl

A streamlined interface for connecting the central manager for the current playground page to nearby Bluetooth peripherals.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
class PlaygroundBluetoothCentralManager
```

## Topics

### Configuring Central Managers
- [init(services: [CBUUID]?, queue: DispatchQueue)](playgroundbluetoothcentralmanager/3029470-init.md)
  Creates a central manager that supports communicating with Bluetooth peripherals.
- [var delegate: PlaygroundBluetoothCentralManagerDelegate?](playgroundbluetoothcentralmanager/3029468-delegate.md)
  A delegate that can receive messages from the central manager by adopting the [`PlaygroundBluetoothCentralManagerDelegate`](playgroundbluetoothcentralmanagerdelegate.md) protocol.
- [var scanning: Bool](playgroundbluetoothcentralmanager/3029471-scanning.md)
  A Boolean value that determines whether the central manager is scanning for peripherals.
### Connecting Peripherals
- [func connect(to: CBPeripheral, timeout: TimeInterval?, callback: ((CBPeripheral, Error?) -> Void)?)](playgroundbluetoothcentralmanager/3029464-connect.md)
  Attempts to connect the central manager to the specified peripheral.
- [func connect(toPeripheralWithUUID: UUID, timeout: TimeInterval, callback: ((CBPeripheral?, Error?) -> Void)?)](playgroundbluetoothcentralmanager/3029465-connect.md)
  Attempts to connect the central manager to a peripheral with the specified unique identifier.
- [func connectToLastConnectedPeripheral(timeout: TimeInterval, callback: ((CBPeripheral?, Error?) -> Void)?) -> Bool](playgroundbluetoothcentralmanager/3029466-connecttolastconnectedperipheral.md)
  Attempts to reconnect the central manager to the most recently connected peripheral.
- [enum PlaygroundBluetoothCentralManager.ConnectionError](playgroundbluetoothcentralmanager/connectionerror.md)
  The errors you may encounter when connecting a peripheral to the central manager for the current playground page.
### Disconnecting Peripherals
- [func disconnect(from: CBPeripheral)](playgroundbluetoothcentralmanager/3029469-disconnect.md)
  Disconnects the central manager from the specified, connected peripheral.
### Inspecting Central Managers
- [var connectedPeripherals: [CBPeripheral]](playgroundbluetoothcentralmanager/3029467-connectedperipherals.md)
  An array of the peripherals currently connected to the central manager.
- [var state: CBManagerState](playgroundbluetoothcentralmanager/3029472-state.md)
  The current state of the central manager.

## See Also

- [Connecting to Bluetooth Peripherals in Swift Playgrounds](connecting_to_bluetooth_peripherals_in_swift_playgrounds.md)
  Scan for peripherals and display them in your playground's live view.
- [protocol PlaygroundBluetoothCentralManagerDelegate](playgroundbluetoothcentralmanagerdelegate.md)
  A delegate you use to respond to peripheral discovery and manage the lifecycle of connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager)*