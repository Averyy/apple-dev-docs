# PlaygroundBluetoothConnectionView.State.connectedPeripheralFirmwareOutOfDate

**Framework**: Playground Bluetooth  
**Kind**: enumelt

The currently connected peripheral has outdated firmware and can't be used.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
case connectedPeripheralFirmwareOutOfDate
```

#### Discussion

The connection view title corresponding to this state should be in the following format:

```swift
"Connect to a Different \(item.name)"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview/state/connectedperipheralfirmwareoutofdate)*