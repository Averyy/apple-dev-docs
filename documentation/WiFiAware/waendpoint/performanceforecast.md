# performanceForecast

**Framework**: Wi-Fi Aware  
**Kind**: property

The forecasted performance for connections setup to the remote device, per WAPerformanceMode.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let performanceForecast: [WAPerformanceMode : WAPerformanceForecast]
```

#### Discussion

This estimation makes certain worst case assumptions about the remote device when calculating performance. A more accurate performance report is available though WAPerformanceReport after a connection is setup. Returns an empty dictionary if the forecast cannot be estimated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waendpoint/performanceforecast)*