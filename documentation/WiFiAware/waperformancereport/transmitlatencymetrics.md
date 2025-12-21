# WAPerformanceReport.TransmitLatencyMetrics

**Framework**: Wi-Fi Aware  
**Kind**: struct

A report of the transmit latency to the specified peer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct TransmitLatencyMetrics
```

## Topics

### Identifying the Wi-Fi access category
- [let accessCategory: WAAccessCategory](waperformancereport/transmitlatencymetrics/accesscategory.md)
  The Wi-Fi quality-of-service (QoS) category that this latency data tracks.
### Getting the average Latency
- [let average: Duration?](waperformancereport/transmitlatencymetrics/average.md)
  The average per-packet transmit latency measured for this flow’s peers.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let transmitLatency: [WAAccessCategory : WAPerformanceReport.TransmitLatencyMetrics]](waperformancereport/transmitlatency.md)
  The measured transmit latency per access category that is in use with the remote devices and that the system can measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancereport/transmitlatencymetrics)*