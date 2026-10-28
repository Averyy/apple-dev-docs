# selected(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method  
**Role**: Type Method

Includes only the preselected paired devices in the provided list.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
static func selected(_ pairedDevices: some Sequence<WAPairedDevice>) -> WAPublisherListener.Devices
```

## Return Value

A new `Devices` including the selected devices.

## Parameters

- `pairedDevices`: A sequence holding a snapshot of paired devices to use for this operation.

## See Also

### Selecting specific devices
- [static func selected(WAPairedDevice.Devices) -> WAPublisherListener.Devices](./selected%28_%29-56vig.md)
  Includes only the preselected paired devices in the provided dictionary.
- [static let userSpecifiedDevices: WAPublisherListener.Devices](./userspecifieddevices.md)
  Includes only new devices the user pairs via DeviceDiscoveryUI’s `DevicePairingView()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices/selected(_:)-1e2)*