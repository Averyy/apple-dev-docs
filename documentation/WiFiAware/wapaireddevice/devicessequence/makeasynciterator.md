# makeAsyncIterator()

**Framework**: Wi-Fi Aware  
**Kind**: method

Makes an asynchronous iterator that provides successive device snapshots when the list of paired devices known to the app changes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func makeAsyncIterator() -> WAPairedDevice.DevicesSequence.AsyncIterator
```

#### Discussion

This method returns a new asynchronous iterator vending [`WAPairedDevice.Devices`](wapaireddevice/devices.md) elements when changes occur.

## See Also

- [WAPairedDevice.DevicesSequence.AsyncIterator](wapaireddevice/devicessequence/asynciterator.md)
  An iterator for the sequence of devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence/makeasynciterator())*