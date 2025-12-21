# WAAccessCategory.background

**Framework**: Wi-Fi Aware  
**Kind**: case

A quality-of-service (QoS) type that provides high throughput for delay-tolerant, noninteractive data transfers of any size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case background
```

#### Discussion

Use this Wi-Fi access category for background data transfers, to prevent background traffic from interfering with other higher-priority flows, and for packets transmitted by a `NetworkConnection` that you set with NWParameter’s `serviceClass = .background`.

For more information, refer to [`NWParameters.ServiceClass.background`](https://developer.apple.comhttps://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum/background)

## See Also

- [WAAccessCategory.bestEffort](waaccesscategory/besteffort.md)
  A default quality-of-service (QoS) type that provides high throughput for data transfers of any size.
- [WAAccessCategory.interactiveVideo](waaccesscategory/interactivevideo.md)
  A quality-of-service (QoS) type that provides low-latency for moderate throughput flows.
- [WAAccessCategory.interactiveVoice](waaccesscategory/interactivevoice.md)
  A quality-of-service (QoS) type that provides very low-latency for low-throughput flows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waaccesscategory/background)*