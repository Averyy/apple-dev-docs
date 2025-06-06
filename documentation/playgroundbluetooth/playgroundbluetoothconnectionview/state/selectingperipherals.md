# PlaygroundBluetoothConnectionView.State.selectingPeripherals

**Framework**: Playground Bluetooth  
**Kind**: enumelt

One or more peripherals have been discovered and can be selected.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case selectingPeripherals
```

#### Discussion

The connection view title corresponding to this state should be in one of the following formats:

```swift
"Select a \(item.name)"

// Or:
"Select several \(item.name)s"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/state/selectingperipherals)*