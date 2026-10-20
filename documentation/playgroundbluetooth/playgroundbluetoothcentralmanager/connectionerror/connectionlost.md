# PlaygroundBluetoothCentralManager.ConnectionError.connectionLost

**Framework**: Playground Bluetooth  
**Kind**: enumelt  
**Role**: Enumeration Case

The error that occurs when a peripheral connection to the central manager fails.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case connectionLost
```

#### Discussion

This error doesn’t occur when a connection to the central manager is intentionally disconnected.

## See Also

### Handling Errors
- [PlaygroundBluetoothCentralManager.ConnectionError.connectionFailed](./connectionfailed.md)
  The error that occurs when a peripheral fails to connect to the central manager.
- [PlaygroundBluetoothCentralManager.ConnectionError.excessiveConnections](./excessiveconnections.md)
  The error that occurs when a peripheral rejects a connection to the central manager because there are too many others.
- [PlaygroundBluetoothCentralManager.ConnectionError.invalidState](./invalidstate.md)
  The error that occurs when the central manager is in a state that can’t make connections.
- [PlaygroundBluetoothCentralManager.ConnectionError.timeoutExpired](./timeoutexpired.md)
  The error that occurs when a peripheral fails to connect to the central manager before the timeout period expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/connectionerror/connectionlost)*