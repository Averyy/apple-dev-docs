# WAPairedDevice.Devices

**Framework**: Wi-Fi Aware  
**Kind**: typealias

A dictionary holding a snapshot of currently paired devices accessible and known to your app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
typealias Devices = [WAPairedDevice.ID : WAPairedDevice]
```

## Mentions

- [Connecting devices for peer-to-peer Wi-Fi](connecting-paired-devices.md)

#### Discussion

An empty dictionary indicates that no paired devices are known to your app.

## See Also

- [struct WAPairedDevice](wapaireddevice.md)
  A known Wi-Fi Aware device that your app can connect to.
- [WAPairedDevice.DevicesSequence](wapaireddevice/devicessequence.md)
  A sequence that vends updates to a paired device list, as the list changes.
- [WAPairedDevice.PairingInfo](wapaireddevice/pairinginfo-swift.struct.md)
  A collection of unauthenticated information the system receives from a device before it’s paired for the first time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devices)*