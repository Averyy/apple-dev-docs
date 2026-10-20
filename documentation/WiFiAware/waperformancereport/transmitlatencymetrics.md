# WAPerformanceReport.TransmitLatencyMetrics

**Framework**: Wi-Fi Aware  
**Kind**: struct  
**Role**: Structure

A report of the transmit latency to the specified peer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct TransmitLatencyMetrics
```

## Topics

### Identifying the Wi-Fi access category
- [let accessCategory: WAAccessCategory](./transmitlatencymetrics/accesscategory.md)
  The Wi-Fi quality-of-service (QoS) category that this latency data tracks.
### Getting the average Latency
- [let average: Duration?](./transmitlatencymetrics/average.md)
  The average per-packet transmit latency measured for this flow’s peers.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the latency metrics
- [let transmitLatency: [WAAccessCategory : WAPerformanceReport.TransmitLatencyMetrics]](./transmitlatency.md)
  The measured transmit latency per access category that is in use with the remote devices and that the system can measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancereport/transmitlatencymetrics)*