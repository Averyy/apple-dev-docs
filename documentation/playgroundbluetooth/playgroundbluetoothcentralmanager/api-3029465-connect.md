# connect(toPeripheralWithUUID:timeout:callback:)

**Framework**: Playground Bluetooth  
**Kind**: instm

Attempts to connect the central manager to a peripheral with the specified unique identifier.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func connect(toPeripheralWithUUID uuid: UUID, timeout: TimeInterval = 7, callback: ((CBPeripheral?, Error?) -> Void)? = nil)
```

## Parameters

- `uuid`: The unique identifier of the peripheral to attempt to connect to.
- `timeout`: The amount of time, in seconds, before the connection attempt is aborted. If the timeout value is  , the attempt won’t time out. To cancel a connection attempt, call the   method.
- `callback`: A function that’s called when the connection attempt succeeds or fails.

## See Also

- [func connect(to: CBPeripheral, timeout: TimeInterval?, callback: ((CBPeripheral, Error?) -> Void)?)](playgroundbluetoothcentralmanager/3029464-connect.md)
  Attempts to connect the central manager to the specified peripheral.
- [func connectToLastConnectedPeripheral(timeout: TimeInterval, callback: ((CBPeripheral?, Error?) -> Void)?) -> Bool](playgroundbluetoothcentralmanager/3029466-connecttolastconnectedperipheral.md)
  Attempts to reconnect the central manager to the most recently connected peripheral.
- [enum PlaygroundBluetoothCentralManager.ConnectionError](playgroundbluetoothcentralmanager/connectionerror.md)
  The errors you may encounter when connecting a peripheral to the central manager for the current playground page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/3029465-connect)*