# PlaygroundBluetoothCentralManager.ConnectionError

**Framework**: Playground Bluetooth  
**Kind**: enum

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
- [PlaygroundBluetoothCentralManager.ConnectionError.connectionFailed](playgroundbluetoothcentralmanager/connectionerror/connectionfailed.md)
  The error that occurs when a peripheral fails to connect to the central manager.
- [PlaygroundBluetoothCentralManager.ConnectionError.connectionLost](playgroundbluetoothcentralmanager/connectionerror/connectionlost.md)
  The error that occurs when a peripheral connection to the central manager fails.
- [PlaygroundBluetoothCentralManager.ConnectionError.excessiveConnections](playgroundbluetoothcentralmanager/connectionerror/excessiveconnections.md)
  The error that occurs when a peripheral rejects a connection to the central manager because there are too many others.
- [PlaygroundBluetoothCentralManager.ConnectionError.invalidState](playgroundbluetoothcentralmanager/connectionerror/invalidstate.md)
  The error that occurs when the central manager is in a state that can’t make connections.
- [PlaygroundBluetoothCentralManager.ConnectionError.timeoutExpired](playgroundbluetoothcentralmanager/connectionerror/timeoutexpired.md)
  The error that occurs when a peripheral fails to connect to the central manager before the timeout period expires.
### Displaying Errors
- [var localizedDescription: String](playgroundbluetoothcentralmanager/connectionerror/3029462-localizeddescription.md)
  A string containing the localized description of the error.
### Comparing Errors
- [static func != (PlaygroundBluetoothCentralManager.ConnectionError, PlaygroundBluetoothCentralManager.ConnectionError) -> Bool](playgroundbluetoothcentralmanager/connectionerror/3029457.md)
  Returns `true` when the two connection errors being compared aren't the same.

## Relationships

### Conforms To
- [Error](../swift/error.md)

## See Also

- [func connect(to: CBPeripheral, timeout: TimeInterval?, callback: ((CBPeripheral, Error?) -> Void)?)](playgroundbluetoothcentralmanager/3029464-connect.md)
  Attempts to connect the central manager to the specified peripheral.
- [func connect(toPeripheralWithUUID: UUID, timeout: TimeInterval, callback: ((CBPeripheral?, Error?) -> Void)?)](playgroundbluetoothcentralmanager/3029465-connect.md)
  Attempts to connect the central manager to a peripheral with the specified unique identifier.
- [func connectToLastConnectedPeripheral(timeout: TimeInterval, callback: ((CBPeripheral?, Error?) -> Void)?) -> Bool](playgroundbluetoothcentralmanager/3029466-connecttolastconnectedperipheral.md)
  Attempts to reconnect the central manager to the most recently connected peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/connectionerror)*