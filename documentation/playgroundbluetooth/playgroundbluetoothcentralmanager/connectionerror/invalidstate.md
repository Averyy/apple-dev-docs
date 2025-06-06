# PlaygroundBluetoothCentralManager.ConnectionError.invalidState

**Framework**: Playground Bluetooth  
**Kind**: enumelt

The error that occurs when the central manager is in a state that can’t make connections.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case invalidState
```

#### Discussion

For example, the central manager is in an invalid state for connections when it’s powered off.

## See Also

- [PlaygroundBluetoothCentralManager.ConnectionError.connectionFailed](playgroundbluetoothcentralmanager/connectionerror/connectionfailed.md)
  The error that occurs when a peripheral fails to connect to the central manager.
- [PlaygroundBluetoothCentralManager.ConnectionError.connectionLost](playgroundbluetoothcentralmanager/connectionerror/connectionlost.md)
  The error that occurs when a peripheral connection to the central manager fails.
- [PlaygroundBluetoothCentralManager.ConnectionError.excessiveConnections](playgroundbluetoothcentralmanager/connectionerror/excessiveconnections.md)
  The error that occurs when a peripheral rejects a connection to the central manager because there are too many others.
- [PlaygroundBluetoothCentralManager.ConnectionError.timeoutExpired](playgroundbluetoothcentralmanager/connectionerror/timeoutexpired.md)
  The error that occurs when a peripheral fails to connect to the central manager before the timeout period expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/connectionerror/invalidstate)*