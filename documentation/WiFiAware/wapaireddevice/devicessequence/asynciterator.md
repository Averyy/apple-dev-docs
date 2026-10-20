# WAPairedDevice.DevicesSequence.AsyncIterator

**Framework**: Wi-Fi Aware  
**Kind**: class  
**Role**: Class

An iterator for the sequence of devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class AsyncIterator
```

## Topics

### Getting the next asynchronous update
- [WAPairedDevice.DevicesSequence.AsyncIterator.Element](./asynciterator/element.md)
  A dictionary holding a snapshot of currently paired devices accessible to your app.
- [func next() async throws -> WAPairedDevice.DevicesSequence.AsyncIterator.Element?](./asynciterator/next%28%29.md)
  Returns the next dictionary in the sequence.
### Throwing an error
- [WAPairedDevice.DevicesSequence.AsyncIterator.Failure](./asynciterator/failure.md)
  The type of error that the sequence can produce.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Getting async updates
- [func makeAsyncIterator() -> WAPairedDevice.DevicesSequence.AsyncIterator](./makeasynciterator%28%29.md)
  Makes an asynchronous iterator that provides successive device snapshots when the list of paired devices known to the app changes.
- [WAPairedDevice.DevicesSequence.Element](./element.md)
  A dictionary holding a snapshot of currently paired devices accessible to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence/asynciterator)*