# scanning

**Framework**: Playground Bluetooth  
**Kind**: instp  
**Role**: Instance Property

A Boolean value that determines whether the central manager is scanning for peripherals.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
var scanning: Bool { get set }
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) to start scanning for peripherals. Upon discovering a peripheral, the central manager calls the delegate’s [`centralManager(_:didDiscover:withAdvertisementData:rssi:)`](../playgroundbluetoothcentralmanagerdelegate/api-3029478-centralmanager.md) method.

## See Also

### Configuring Central Managers
- [init(services: [CBUUID]?, queue: DispatchQueue)](./api-3029470-init.md)
  Creates a central manager that supports communicating with Bluetooth peripherals.
- [var delegate: PlaygroundBluetoothCentralManagerDelegate?](./api-3029468-delegate.md)
  A delegate that can receive messages from the central manager by adopting the [`PlaygroundBluetoothCentralManagerDelegate`](../playgroundbluetoothcentralmanagerdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager/3029471-scanning)*