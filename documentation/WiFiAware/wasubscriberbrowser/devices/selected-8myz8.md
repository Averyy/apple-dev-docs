# selected(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Includes only the preselected paired devices in the provided dictionary.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func selected(_ pairedDevices: WAPairedDevice.Devices) -> WASubscriberBrowser.Devices
```

#### Return Value

A new `WASubscriber/Devices` including the selected devices.

## Parameters

- `pairedDevices`: A   dictionary holding a snapshot  of paired devices to use for this operation.

## See Also

- [static func selected(some Sequence<WAPairedDevice>) -> WASubscriberBrowser.Devices](wasubscriberbrowser/devices/selected(_:)-5arv0.md)
  Includes only the preselected paired devices in the provided list.
- [static let userSpecifiedDevices: WASubscriberBrowser.Devices](wasubscriberbrowser/devices/userspecifieddevices.md)
  Includes only devices the user selects or pairs in DeviceDiscoveryUI’s `DevicePicker()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/devices/selected(_:)-8myz8)*