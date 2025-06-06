# connectionView(_:itemForPeripheral:withAdvertisementData:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Required**: Yes

Tells the delegate that a new peripheral was discovered and can be displayed in the connection view.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func connectionView(_ connectionView: PlaygroundBluetoothConnectionView, itemForPeripheral peripheral: CBPeripheral, withAdvertisementData advertisementData: [String : Any]?) -> PlaygroundBluetoothConnectionView.Item
```

#### Return_value

A [`PlaygroundBluetoothConnectionView.Item`](playgroundbluetoothconnectionview/item.md) instance that's displayed within a [`PlaygroundBluetoothConnectionView`](playgroundbluetoothconnectionview.md).

## Parameters

- `connectionView`: The connection view showing available peripherals.
- `peripheral`: The peripheral to display in the connection view.
- `advertisementData`: The advertisement data you use to help decide how to display the peripheral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdatasource/3029520-connectionview)*