# selected(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method  
**Role**: Type Method

Includes only the preselected paired devices in the provided dictionary.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
static func selected(_ pairedDevices: WAPairedDevice.Devices) -> WAPublisherListener.Devices
```

#### Return Value

A new `Devices` including the selected devices.

## Parameters

- `pairedDevices`: A [`WAPublisherListener.Devices`](../devices.md) dictionary holding a snapshot  of paired devices to use for this operation.

## See Also

### Selecting specific devices
- [static func selected(some Sequence<WAPairedDevice>) -> WAPublisherListener.Devices](./selected%28_%29-1e2.md)
  Includes only the preselected paired devices in the provided list.
- [static let userSpecifiedDevices: WAPublisherListener.Devices](./userspecifieddevices.md)
  Includes only new devices the user pairs via DeviceDiscoveryUI’s `DevicePairingView()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices/selected(_:)-56vig)*