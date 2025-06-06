# connectionView(_:titleFor:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Required**: Yes

Tells the delegate that the connection view needs a title to display for its current state.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func connectionView(_ connectionView: PlaygroundBluetoothConnectionView, titleFor state: PlaygroundBluetoothConnectionView.State) -> String
```

#### Return_value

A localized string corresponding to the current state of the view.

## Parameters

- `connectionView`: The connection view that’s entering this state.
- `state`: The state of the view. The state is one of the cases of the   enumeration.

## See Also

- [func connectionView(PlaygroundBluetoothConnectionView, shouldConnectTo: CBPeripheral, withAdvertisementData: [String : Any]?) -> Bool](playgroundbluetoothconnectionviewdelegate/3029523-connectionview.md)
  Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.
- [func connectionView(PlaygroundBluetoothConnectionView, shouldDisplayDiscovered: CBPeripheral, withAdvertisementData: [String : Any]?, rssi: Double) -> Bool](playgroundbluetoothconnectionviewdelegate/3029525-connectionview.md)
  Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate/3029527-connectionview)*