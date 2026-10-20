# PlaygroundBluetoothCentralManager.ConnectionError

**Framework**: Playground Bluetooth  
**Kind**: enum  
**Role**: Enumeration

The errors you may encounter when connecting a peripheral to the central manager for the current playground page.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
enum PlaygroundBluetoothCentralManager.ConnectionError
```

## Topics

### Handling Errors
- [PlaygroundBluetoothCentralManager.ConnectionError.connectionFailed](./connectionerror/connectionfailed.md)
  The error that occurs when a peripheral fails to connect to the central manager.
- [PlaygroundBluetoothCentralManager.ConnectionError.connectionLost](./connectionerror/connectionlost.md)
  The error that occurs when a peripheral connection to the central manager fails.
- [PlaygroundBluetoothCentralManager.ConnectionError.excessiveConnections](./connectionerror/excessiveconnections.md)
  The error that occurs when a peripheral rejects a connection to the central manager because there are too many others.
- [PlaygroundBluetoothCentralManager.ConnectionError.invalidState](./connectionerror/invalidstate.md)
  The error that occurs when the central manager is in a state that can’t make connections.
- [PlaygroundBluetoothCentralManager.ConnectionError.timeoutExpired](./connectionerror/timeoutexpired.md)
  The error that occurs when a peripheral fails to connect to the central manager before the timeout period expires.
### Displaying Errors
- [var localizedDescription: String](./connectionerror/api-3029462-localizeddescription.md)
  A string containing the localized description of the error.
### Comparing Errors
- [static func != (PlaygroundBluetoothCentralManager.ConnectionError, PlaygroundBluetoothCentralManager.ConnectionError) -> Bool](./connectionerror/api-3029457.md)
  Returns `true` when the two connection errors being compared aren't the same.

## Relationships

### Conforms To
- [Error](../../Swift/error.md)

## See Also

### Connecting Peripherals
- [func connect(to: CBPeripheral, timeout: TimeInterval?, callback: ((CBPeripheral, Error?) -> Void)?)](./api-3029464-connect.md)
  Attempts to connect the central manager to the specified peripheral.
- [func connect(toPeripheralWithUUID: UUID, timeout: TimeInterval, callback: ((CBPeripheral?, Error?) -> Void)?)](./api-3029465-connect.md)
  Attempts to connect the central manager to a peripheral with the specified unique identifier.
- [func connectToLastConnectedPeripheral(timeout: TimeInterval, callback: ((CBPeripheral?, Error?) -> Void)?) -> Bool](./api-3029466-connecttolastconnectedperipheral.md)
  Attempts to reconnect the central manager to the most recently connected peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/connectionerror)*