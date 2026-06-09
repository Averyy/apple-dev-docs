# localThroughputCeiling

**Framework**: Wi-Fi Aware  
**Kind**: property

The highest throughput a connection from the local device to the remote device is capable of under ideal conditions, given the hardware capabilities of the local device. The actual throughput achieved can be lower in the presence of other active connections.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let localThroughputCeiling: Double?
```

#### Discussion

The result is in `Mbps` and can be `nil` if the system can’t calculate it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformanceforecast/localthroughputceiling)*