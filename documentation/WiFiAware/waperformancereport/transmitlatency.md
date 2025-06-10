# transmitLatency

**Framework**: Wi-Fi Aware  
**Kind**: property

The measured transmit latency per access category that is in use with the remote devices and that the system can measure.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
let transmitLatency: [WAAccessCategory : WAPerformanceReport.TransmitLatencyMetrics]
```

#### Discussion

The system only reports in-use and measurable access categories. The dictionary is empty if there’s no activity, or if the system can’t measure the data.

## See Also

- [WAPerformanceReport.TransmitLatencyMetrics](waperformancereport/transmitlatencymetrics.md)
  A report of the transmit latency to the specified peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancereport/transmitlatency)*