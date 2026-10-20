# makeAsyncIterator()

**Framework**: Wi-Fi Aware  
**Kind**: method  
**Role**: Instance Method

Makes an asynchronous iterator that provides successive device snapshots when the list of paired devices known to the app changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func makeAsyncIterator() -> WAPairedDevice.DevicesSequence.AsyncIterator
```

#### Return Value

A new asynchronous iterator vending [`WAPairedDevice.Devices`](../devices.md) elements when changes occur.

## See Also

### Getting async updates
- [WAPairedDevice.DevicesSequence.AsyncIterator](./asynciterator.md)
  An iterator for the sequence of devices.
- [WAPairedDevice.DevicesSequence.Element](./element.md)
  A dictionary holding a snapshot of currently paired devices accessible to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence/makeasynciterator())*