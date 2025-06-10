# selected(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Includes only the preselected paired devices in the provided list.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static func selected(_ pairedDevices: some Sequence<WAPairedDevice>) -> WAPublisherListener.Devices
```

#### Return Value

A new `Devices` including the selected devices.

## Parameters

- `pairedDevices`: A sequence holding a snapshot of paired devices to use for this operation.

## See Also

- [static func selected(WAPairedDevice.Devices) -> WAPublisherListener.Devices](wapublisherlistener/devices/selected(_:)-56vig.md)
  Includes only the preselected paired devices in the provided dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices/selected(_:)-1e2)*