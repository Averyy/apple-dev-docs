# PlaygroundBluetoothConnectionViewDelegate

**Framework**: Playground Bluetooth  
**Kind**: intf

A delegate you use to respond to user- and system-initiated interactions with the central manager’s connection view.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
protocol PlaygroundBluetoothConnectionViewDelegate : AnyObject
```

## Topics

### Displaying New Peripherals
- [func connectionView(PlaygroundBluetoothConnectionView, shouldConnectTo: CBPeripheral, withAdvertisementData: [String : Any]?) -> Bool](playgroundbluetoothconnectionviewdelegate/3029523-connectionview.md)
  Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.
- [func connectionView(PlaygroundBluetoothConnectionView, shouldDisplayDiscovered: CBPeripheral, withAdvertisementData: [String : Any]?, rssi: Double) -> Bool](playgroundbluetoothconnectionviewdelegate/3029525-connectionview.md)
  Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.
- [func connectionView(PlaygroundBluetoothConnectionView, titleFor: PlaygroundBluetoothConnectionView.State) -> String](playgroundbluetoothconnectionviewdelegate/3029527-connectionview.md)
  Tells the delegate that the connection view needs a title to display for its current state.
### Displaying Firmware Update Information
- [func connectionView(PlaygroundBluetoothConnectionView, firmwareUpdateInstructionsFor: CBPeripheral) -> String](playgroundbluetoothconnectionviewdelegate/3029522-connectionview.md)
  Tells the delegate that a peripheral has a firmware update available.
### Disconnecting from Peripherals
- [func connectionView(PlaygroundBluetoothConnectionView, willDisconnectFrom: CBPeripheral)](playgroundbluetoothconnectionviewdelegate/3029528-connectionview.md)
  Tells the delegate that a connected peripheral is about to be disconnected.

## See Also

- [class PlaygroundBluetoothConnectionView](playgroundbluetoothconnectionview.md)
  A view that displays the connection status of a peripheral to the central manager for the current page and manages connections to other peripherals.
- [protocol PlaygroundBluetoothConnectionViewDataSource](playgroundbluetoothconnectionviewdatasource.md)
  The protocol you adopt to display an available peripheral in a playground page’s connection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate)*