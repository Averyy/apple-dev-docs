# WAPairedDevice.DevicesSequence.AsyncIterator

**Framework**: Wi-Fi Aware  
**Kind**: class

An iterator for the sequence of devices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
class AsyncIterator
```

## Topics

### Getting the next asynchronous update
- [WAPairedDevice.DevicesSequence.AsyncIterator.Element](wapaireddevice/devicessequence/asynciterator/element.md)
  A dictionary holding a snapshot of currently paired devices accessible to your app.
- [func next() async throws -> WAPairedDevice.DevicesSequence.AsyncIterator.Element?](wapaireddevice/devicessequence/asynciterator/next.md)
  Returns the next dictionary in the sequence.
### Throwing an error
- [WAPairedDevice.DevicesSequence.AsyncIterator.Failure](wapaireddevice/devicessequence/asynciterator/failure.md)
  The type of error that the sequence can produce.
### Default Implementations
- [AsyncIteratorProtocol Implementations](wapaireddevice/devicessequence/asynciterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)

## See Also

- [func makeAsyncIterator() -> WAPairedDevice.DevicesSequence.AsyncIterator](wapaireddevice/devicessequence/makeasynciterator.md)
  Makes an asynchronous iterator that provides successive device snapshots when the list of paired devices known to the app changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence/asynciterator)*