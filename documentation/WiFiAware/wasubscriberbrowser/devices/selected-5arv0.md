# selected(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Includes only the preselected paired devices in the provided list.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func selected(_ pairedDevices: some Sequence<WAPairedDevice>) -> WASubscriberBrowser.Devices
```

#### Return Value

A new `Devices` list that includes the selected devices.

## Parameters

- `pairedDevices`: A sequence holding a snapshot of paired devices to use for this operation.

## See Also

- [static func selected(WAPairedDevice.Devices) -> WASubscriberBrowser.Devices](wasubscriberbrowser/devices/selected(_:)-8myz8.md)
  Includes only the preselected paired devices in the provided dictionary.
- [static let userSpecifiedDevices: WASubscriberBrowser.Devices](wasubscriberbrowser/devices/userspecifieddevices.md)
  Includes only devices the user selects or pairs in DeviceDiscoveryUI’s `DevicePicker()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/devices/selected(_:)-5arv0)*