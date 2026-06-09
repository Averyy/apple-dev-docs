# signalStrength

**Framework**: Wi-Fi Aware  
**Kind**: property

The estimated signal strength of the remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let signalStrength: Double?
```

#### Discussion

The resulting value can be between `0.0` (weakest) and `1.0` (strongest), or it can be `nil` if the system can’t measure the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformanceforecast/signalstrength)*