# centralManager(_:didDiscover:withAdvertisementData:rssi:)

**Framework**: Playground Bluetooth  
**Kind**: intfm  
**Role**: Instance Method

Tells the delegate that a peripheral has been discovered during scanning.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func centralManager(_ centralManager: PlaygroundBluetoothCentralManager, didDiscover peripheral: CBPeripheral, withAdvertisementData advertisementData: [String : Any]?, rssi: Double)
```

## Parameters

- `centralManager`: The central manager providing this information.
- `peripheral`: The newly discovered peripheral.
- `advertisementData`: A dictionary containing any advertisement data that the peripheral provides.
- `rssi`: The current received signal strength indicator of the peripheral in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate/3029479-centralmanager)*