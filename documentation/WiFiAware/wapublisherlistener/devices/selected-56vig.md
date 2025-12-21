# selected(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Includes only the preselected paired devices in the provided dictionary.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func selected(_ pairedDevices: WAPairedDevice.Devices) -> WAPublisherListener.Devices
```

#### Return Value

A new `Devices` including the selected devices.

## Parameters

- `pairedDevices`: A   dictionary holding a snapshot  of paired devices to use for this operation.

## See Also

- [static func selected(some Sequence<WAPairedDevice>) -> WAPublisherListener.Devices](wapublisherlistener/devices/selected(_:)-1e2.md)
  Includes only the preselected paired devices in the provided list.
- [static let userSpecifiedDevices: WAPublisherListener.Devices](wapublisherlistener/devices/userspecifieddevices.md)
  Includes only new devices the user pairs via DeviceDiscoveryUI’s `DevicePairingView()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices/selected(_:)-56vig)*