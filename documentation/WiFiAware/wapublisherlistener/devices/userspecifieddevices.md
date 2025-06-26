# userSpecifiedDevices

**Framework**: Wi-Fi Aware  
**Kind**: property

Includes only new devices the user pairs via DeviceDiscoveryUI’s `DevicePairingView()`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static let userSpecifiedDevices: WAPublisherListener.Devices
```

#### Discussion

Only applicable to use with the `DevicePairingView()` API. Will throw an error if used with a `NetworkListener`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices/userspecifieddevices)*