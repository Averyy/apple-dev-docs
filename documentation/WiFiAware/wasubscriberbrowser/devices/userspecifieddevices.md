# userSpecifiedDevices

**Framework**: Wi-Fi Aware  
**Kind**: property  
**Role**: Type Property

Includes only devices the user selects or pairs in DeviceDiscoveryUI’s `DevicePicker()`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
static let userSpecifiedDevices: WASubscriberBrowser.Devices
```

#### Discussion

Only applicable to use with the `DevicePicker()` API. Will throw an error if used with a `NetworkBrowser`.

## See Also

### Selecting devices to connect to
- [static func selected(WAPairedDevice.Devices) -> WASubscriberBrowser.Devices](./selected%28_%29-8myz8.md)
  Includes only the preselected paired devices in the provided dictionary.
- [static func selected(some Sequence<WAPairedDevice>) -> WASubscriberBrowser.Devices](./selected%28_%29-5arv0.md)
  Includes only the preselected paired devices in the provided list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/devices/userspecifieddevices)*