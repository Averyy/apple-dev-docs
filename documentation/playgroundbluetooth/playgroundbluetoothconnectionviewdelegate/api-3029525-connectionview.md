# connectionView(_:shouldDisplayDiscovered:withAdvertisementData:rssi:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func connectionView(_ connectionView: PlaygroundBluetoothConnectionView, shouldDisplayDiscovered peripheral: CBPeripheral, withAdvertisementData advertisementData: [String : Any]?, rssi: Double) -> Bool
```

## Return Value

A Boolean value indicating whether the newly discovered peripheral should show up in the connection view.

## Parameters

- `connectionView`: The connection view showing available peripherals.
- `peripheral`: The newly discovered peripheral.
- `advertisementData`: The advertisement data you use to help decide whether or not to display the peripheral.
- `rssi`: The current received signal strength indicator of the peripheral in decibels.

## Default Implementations

### PlaygroundBluetoothConnectionViewDelegate Implementations
- [func connectionView(PlaygroundBluetoothConnectionView, shouldDisplayDiscovered: CBPeripheral, withAdvertisementData: [String : Any]?, rssi: Double) -> Bool](./api-3029526-connectionview.md)
  Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.

## See Also

### Displaying New Peripherals
- [func connectionView(PlaygroundBluetoothConnectionView, shouldConnectTo: CBPeripheral, withAdvertisementData: [String : Any]?) -> Bool](./api-3029523-connectionview.md)
  Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.
- [func connectionView(PlaygroundBluetoothConnectionView, titleFor: PlaygroundBluetoothConnectionView.State) -> String](./api-3029527-connectionview.md)
  Tells the delegate that the connection view needs a title to display for its current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate/3029525-connectionview)*