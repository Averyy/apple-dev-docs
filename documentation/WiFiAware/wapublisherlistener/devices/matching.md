# matching(_:)

**Framework**: Wi-Fi Aware  
**Kind**: method

Includes only paired devices matching the provided live filter predicate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static func matching(_ pairedDevicesFilter: Predicate<WAPairedDevice>) -> WAPublisherListener.Devices
```

#### Return Value

A new `Devices` containing the device filter to use.

## Parameters

- `pairedDevicesFilter`: The filter to apply to choose paired devices for this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices/matching(_:))*