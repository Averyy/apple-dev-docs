# userSpecifiedDevices

**Framework**: Wi-Fi Aware  
**Kind**: property

Includes only devices the user selects or pairs in DeviceDiscoveryUI’s `DevicePicker()`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static let userSpecifiedDevices: WASubscriberBrowser.Devices
```

#### Discussion

Only applicable to use with the `DevicePicker()` API. Will throw an error if used with a `NetworkBrowser`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/devices/userspecifieddevices)*