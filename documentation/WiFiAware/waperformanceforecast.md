# WAPerformanceForecast

**Framework**: Wi-Fi Aware  
**Kind**: struct

The performance forecast for a connection setup to the remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct WAPerformanceForecast
```

## Topics

### Instance Properties
- [let localInfrastructureThroughputCapacityRatio: Double?](waperformanceforecast/localinfrastructurethroughputcapacityratio.md)
  The estimated normalized ratio of the local Wi-Fi Infrastructure throughput capacity and the local Wi-Fi Infrastructure throughput ceiling, if a Wi-Fi Aware connection is setup to the remote device.
- [let localThroughputCapacity: Double?](waperformanceforecast/localthroughputcapacity.md)
  The estimated average throughput capacity of the local device for a connection setup to the remote device.
- [let localThroughputCapacityRatio: Double?](waperformanceforecast/localthroughputcapacityratio.md)
  The estimated normalized ratio of the local throughput capacity and the local throughput ceiling.
- [let localThroughputCeiling: Double?](waperformanceforecast/localthroughputceiling.md)
  The highest throughput a connection from the local device to the remote device is capable of under ideal conditions, given the hardware capabilities of the local device. The actual throughput achieved can be lower in the presence of other active connections.
- [let localTimestamp: ContinuousClock.Instant](waperformanceforecast/localtimestamp.md)
  The time the forecast was generated, using a local monotonically increasing clock.
- [let signalStrength: Double?](waperformanceforecast/signalstrength.md)
  The estimated signal strength of the remote device.
- [let timestamp: Date](waperformanceforecast/timestamp.md)
  The time the forecast was generated.
- [let unavailabilityLatencyCeiling: Duration?](waperformanceforecast/unavailabilitylatencyceiling.md)
  The highest forecasted packet latency due to this device’s unavailability.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformanceforecast)*