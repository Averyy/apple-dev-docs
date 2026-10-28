# connectionView(_:shouldDisplayDiscovered:withAdvertisementData:rssi:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate/3029526-connectionview)*