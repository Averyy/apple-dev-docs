# setItem(_:forPeripheral:)

**Framework**: Playground Bluetooth  
**Kind**: instm  
**Role**: Instance Method

Sets all of the information about the specified peripheral at once.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
func setItem(_ item: PlaygroundBluetoothConnectionView.Item, forPeripheral peripheral: CBPeripheral)
```

## Parameters

- `item`: A [`PlaygroundBluetoothConnectionView.Item`](./item.md) that holds information about the specified peripheral.
- `peripheral`: The peripheral corresponding to the [`PlaygroundBluetoothConnectionView.Item`](./item.md) being displayed.

## See Also

### Displaying Peripherals
- [struct PlaygroundBluetoothConnectionView.Item](./item.md)
  A value that holds information about a peripheral displayed in a connection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/3029517-setitem)*