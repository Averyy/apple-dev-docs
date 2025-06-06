# delegate

**Framework**: Playground Bluetooth  
**Kind**: instp

A delegate that can receive messages from the central manager by adopting the [`PlaygroundBluetoothCentralManagerDelegate`](playgroundbluetoothcentralmanagerdelegate.md) protocol.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
weak var delegate: PlaygroundBluetoothCentralManagerDelegate?
```

## See Also

- [init(services: [CBUUID]?, queue: DispatchQueue)](playgroundbluetoothcentralmanager/3029470-init.md)
  Creates a central manager that supports communicating with Bluetooth peripherals.
- [var scanning: Bool](playgroundbluetoothcentralmanager/3029471-scanning.md)
  A Boolean value that determines whether the central manager is scanning for peripherals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/3029468-delegate)*