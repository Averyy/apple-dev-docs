# WAAccessCategory.interactiveVoice

**Framework**: Wi-Fi Aware  
**Kind**: case

A quality-of-service (QoS) type that provides very low latency for low-throughput flows.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case interactiveVoice
```

#### Discussion

Only use this type if normal Wi-Fi packet transmission delays would be directly visible to the person using your app. Use this type for low data rate, live, unbuffered realtime flows that directly interact with the person using your app.

Use this Wi-Fi access category for packets transmitted by a `NetworkConnection` that was set with `NWParameter`’s `serviceClass = .interactiveVoice`.

> ❗ **Important**:  This QoS type doesn’t support high throughput.

For more information, refer to [`NWParameters.ServiceClass.interactiveVoice`](https://developer.apple.comhttps://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum/interactivevoice)

## See Also

- [WAAccessCategory.bestEffort](waaccesscategory/besteffort.md)
  A default quality-of-service (QoS) type that provides high throughput for data transfers of any size.
- [WAAccessCategory.background](waaccesscategory/background.md)
  A quality-of-service (QoS) type that provides high throughput for delay-tolerant, noninteractive data transfers of any size.
- [WAAccessCategory.interactiveVideo](waaccesscategory/interactivevideo.md)
  A quality-of-service (QoS) type that provides low-latency for moderate throughput flows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waaccesscategory/interactivevoice)*