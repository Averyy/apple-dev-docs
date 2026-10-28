# WAAccessCategory.bestEffort

**Framework**: Wi-Fi Aware  
**Kind**: case  
**Role**: Case

A default quality-of-service (QoS) type that provides high throughput for data transfers of any size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case bestEffort
```

## Discussion

This Wi-Fi access category is the default for packets transmitted by a `NetworkConnection`, as well as if you set `serviceClass = .bestEffort` with [`NWParameters`](../../Network/nwparameters.md). Use this category for bulk transfers that are visible to a person using your app.

For more information, refer to [NWParameters.ServiceClass.bestEffort](../../Network/nwparameters/serviceclass-swift.enum/besteffort.md)

## See Also

### Providing throughput
- [WAAccessCategory.background](./background.md)
  A quality-of-service (QoS) type that provides high throughput for delay-tolerant, noninteractive data transfers of any size.
- [WAAccessCategory.interactiveVideo](./interactivevideo.md)
  A quality-of-service (QoS) type that provides low-latency for moderate throughput flows.
- [WAAccessCategory.interactiveVoice](./interactivevoice.md)
  A quality-of-service (QoS) type that provides very low-latency for low-throughput flows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waaccesscategory/besteffort)*