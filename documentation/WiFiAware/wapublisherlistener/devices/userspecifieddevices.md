# userSpecifiedDevices

**Framework**: Wi-Fi Aware  
**Kind**: property

Includes only new devices the user pairs via DeviceDiscoveryUI’s `DevicePairingView()`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static let userSpecifiedDevices: WAPublisherListener.Devices
```

#### Discussion

Only applicable to use with the `DevicePairingView()` API. Will throw an error if used with a `NetworkListener`.

## See Also

- [static func selected(WAPairedDevice.Devices) -> WAPublisherListener.Devices](wapublisherlistener/devices/selected(_:)-56vig.md)
  Includes only the preselected paired devices in the provided dictionary.
- [static func selected(some Sequence<WAPairedDevice>) -> WAPublisherListener.Devices](wapublisherlistener/devices/selected(_:)-1e2.md)
  Includes only the preselected paired devices in the provided list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices/userspecifieddevices)*