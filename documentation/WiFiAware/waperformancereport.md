# WAPerformanceReport

**Framework**: Wi-Fi Aware  
**Kind**: struct

The current performance state of the data path.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct WAPerformanceReport
```

## Topics

### Reporting the data collection time
- [let timestamp: Date](waperformancereport/timestamp.md)
  The time that the framework generates the report.
- [let localTimestamp: ContinuousClock.Instant](waperformancereport/localtimestamp.md)
  The time the report was generated, using a local monotonically increasing clock.
### Getting the throughput metrics
- [let throughputCeiling: Double?](waperformancereport/throughputceiling.md)
  The highest throughput the connection is capable of under ideal conditions, given the hardware capabilities of both devices.
- [let throughputCapacity: Double?](waperformancereport/throughputcapacity.md)
  The current estimated average throughput capacity of the data path, given the current radio conditions and concurrent Wi-Fi use cases.
- [var throughputCapacityRatio: Double?](waperformancereport/throughputcapacityratio.md)
  The current normalized ratio of the throughput capacity and throughput ceiling.
### Getting the latency metrics
- [let transmitLatency: [WAAccessCategory : WAPerformanceReport.TransmitLatencyMetrics]](waperformancereport/transmitlatency.md)
  The measured transmit latency per access category that is in use with the remote devices and that the system can measure.
- [WAPerformanceReport.TransmitLatencyMetrics](waperformancereport/transmitlatencymetrics.md)
  A report of the transmit latency to the specified peer.
### Getting the radio metrics
- [let signalStrength: Double?](waperformancereport/signalstrength.md)
  The current signal strength of the remote device.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NWPath](../Network/NWPath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [struct WAPath](wapath.md)
  A representation of the current Wi-Fi Aware path.
- [enum WAPerformanceMode](waperformancemode.md)
  The performance mode that indicates what performance criterion to prioritize.
- [enum WAAccessCategory](waaccesscategory.md)
  The underling quality-of-service (QoS) the Wi-Fi layer uses to transmit data packets from a connection over the air.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancereport)*