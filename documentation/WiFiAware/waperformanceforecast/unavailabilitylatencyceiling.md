# unavailabilityLatencyCeiling

**Framework**: Wi-Fi Aware  
**Kind**: property

The highest forecasted packet latency due to this device’s unavailability.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let unavailabilityLatencyCeiling: Duration?
```

#### Discussion

This only considers the latency caused by time periods where this local device is not able to communicate to the other device via Wi-Fi Aware. Additional latency can be caused by channel or RF conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformanceforecast/unavailabilitylatencyceiling)*