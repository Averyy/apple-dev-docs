# WAAccessCategory.interactiveVideo

**Framework**: Wi-Fi Aware  
**Kind**: case  
**Role**: Case

A quality-of-service (QoS) type that provides low-latency for moderate throughput flows.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
case interactiveVideo
```

#### Discussion

Only use this type if normal Wi-Fi packet transmission delays are directly visible to the person using your app. Use this type for moderate data rate, live, and unbuffered realtime flows that directly interact with the person using your app.

This Wi-Fi access category is used for packets transmitted by a `NetworkConnection` that was set with `NWParameter`’s `serviceClass = .interactiveVideo`.

> ❗ **Important**: This QoS type doesn’t support high throughput.

For more information, refer to [NWParameters.ServiceClass.interactiveVideo](../../Network/nwparameters/serviceclass-swift.enum/interactivevideo.md)

## See Also

### Providing throughput
- [WAAccessCategory.bestEffort](./besteffort.md)
  A default quality-of-service (QoS) type that provides high throughput for data transfers of any size.
- [WAAccessCategory.background](./background.md)
  A quality-of-service (QoS) type that provides high throughput for delay-tolerant, noninteractive data transfers of any size.
- [WAAccessCategory.interactiveVoice](./interactivevoice.md)
  A quality-of-service (QoS) type that provides very low-latency for low-throughput flows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waaccesscategory/interactivevideo)*