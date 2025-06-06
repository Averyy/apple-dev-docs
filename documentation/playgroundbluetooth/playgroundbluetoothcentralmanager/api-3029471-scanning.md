# scanning

**Framework**: Playground Bluetooth  
**Kind**: instp

A Boolean value that determines whether the central manager is scanning for peripherals.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
var scanning: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to start scanning for peripherals. Upon discovering a peripheral, the central manager calls the delegate’s [`centralManager(_:didDiscover:withAdvertisementData:rssi:)`](playgroundbluetoothcentralmanagerdelegate/3029478-centralmanager.md) method.

## See Also

- [init(services: [CBUUID]?, queue: DispatchQueue)](playgroundbluetoothcentralmanager/3029470-init.md)
  Creates a central manager that supports communicating with Bluetooth peripherals.
- [var delegate: PlaygroundBluetoothCentralManagerDelegate?](playgroundbluetoothcentralmanager/3029468-delegate.md)
  A delegate that can receive messages from the central manager by adopting the [`PlaygroundBluetoothCentralManagerDelegate`](playgroundbluetoothcentralmanagerdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/3029471-scanning)*