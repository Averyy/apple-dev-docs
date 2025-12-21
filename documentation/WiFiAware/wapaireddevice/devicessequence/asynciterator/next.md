# next()

**Framework**: Wi-Fi Aware  
**Kind**: method

Returns the next dictionary in the sequence.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func next() async throws -> WAPairedDevice.DevicesSequence.AsyncIterator.Element?
```

#### Return Value

The next [`WAPairedDevice.Devices`](wapaireddevice/devices.md) snapshot, or `nil` if it’s at the end of the sequence.

#### Discussion

The [`WAPairedDevice.Devices`](wapaireddevice/devices.md) dictionary holds the latest snapshot of the currently paired devices that are known and accessible to your app.

> **Note**: An error if the system can’t read the sequence, or if your app isn’t permitted to access Wi-Fi Aware devices.

## See Also

- [WAPairedDevice.DevicesSequence.AsyncIterator.Element](wapaireddevice/devicessequence/asynciterator/element.md)
  A dictionary holding a snapshot of currently paired devices accessible to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence/asynciterator/next())*