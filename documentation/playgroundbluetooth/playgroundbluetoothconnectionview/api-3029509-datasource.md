# dataSource

**Framework**: Playground Bluetooth  
**Kind**: instp  
**Role**: Instance Property

A data source that provides subviews for available peripherals.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
weak var dataSource: PlaygroundBluetoothConnectionViewDataSource?
```

## See Also

### Creating Connection Views
- [init(centralManager: PlaygroundBluetoothCentralManager, delegate: PlaygroundBluetoothConnectionViewDelegate?, dataSource: PlaygroundBluetoothConnectionViewDataSource?)](./api-3029511-init.md)
  Creates a new, empty view that can be populated with items when peripherals are connected to the central manager.
- [init?(coder: NSCoder)](./api-3029512-init.md)
  Creates a connection view initialized from data you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/3029509-datasource)*