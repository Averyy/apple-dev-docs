# WAAccessCategory.bestEffort

**Framework**: Wi-Fi Aware  
**Kind**: case

A default quality-of-service (QoS) type that provides high throughput for data transfers of any size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
case bestEffort
```

#### Discussion

This Wi-Fi access category is the default for packets transmitted by a `NetworkConnection`, as well as if you set `serviceClass = .bestEffort` with [`NWParameters`](https://developer.apple.com/documentation/Network/NWParameters). Use this category for bulk transfers that are visible to a person using your app.

For more information, refer to [`NWParameters.ServiceClass.bestEffort`](https://developer.apple.comhttps://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum/besteffort)

## See Also

- [WAAccessCategory.background](waaccesscategory/background.md)
  A quality-of-service (QoS) type that provides high throughput for delay-tolerant, noninteractive data transfers of any size.
- [WAAccessCategory.interactiveVideo](waaccesscategory/interactivevideo.md)
  A quality-of-service (QoS) type that provides low-latency for moderate throughput flows.
- [WAAccessCategory.interactiveVoice](waaccesscategory/interactivevoice.md)
  A quality-of-service (QoS) type that provides very low-latency for low-throughput flows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waaccesscategory/besteffort)*