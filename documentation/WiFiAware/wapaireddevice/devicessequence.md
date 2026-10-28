# WAPairedDevice.DevicesSequence

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

A sequence that vends updates to a paired device list, as the list changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct DevicesSequence
```

## Overview

The `DevicesSequence` produces an asynchronous sequence of [`WAPairedDevice.Devices`](./devices.md) items, providing the latest snapshot of the paired devices known to your app.

## Topics

### Getting an initial snapshot
- [func current() async throws -> WAPairedDevice.DevicesSequence.Element?](./devicessequence/current%28%29.md)
  Fetches a one-time snapshot of all paired devices that are currently known and  accessible to your app.
### Getting async updates
- [WAPairedDevice.DevicesSequence.AsyncIterator](./devicessequence/asynciterator.md)
  An iterator for the sequence of devices.
- [func makeAsyncIterator() -> WAPairedDevice.DevicesSequence.AsyncIterator](./devicessequence/makeasynciterator%28%29.md)
  Makes an asynchronous iterator that provides successive device snapshots when the list of paired devices known to the app changes.
- [WAPairedDevice.DevicesSequence.Element](./devicessequence/element.md)
  A dictionary holding a snapshot of currently paired devices accessible to your app.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Paired devices
- [struct WAPairedDevice](../wapaireddevice.md)
  A known Wi-Fi Aware device that your app can connect to.
- [WAPairedDevice.Devices](./devices.md)
  A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- [WAPairedDevice.PairingInfo](./pairinginfo-swift.struct.md)
  A collection of unauthenticated information the system receives from a device before it’s paired for the first time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence)*