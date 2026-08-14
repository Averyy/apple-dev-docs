# WAPerformanceMode

**Framework**: Wi-Fi Aware  
**Kind**: enum

The performance mode that indicates what performance criterion to prioritize.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum WAPerformanceMode
```

#### Overview

> ❗ **Important**: Each service must have the same [`WAPerformanceMode`](waperformancemode.md) on both the `NetworkBrowser` (subscriber) and `NetworkListener` (publisher) sides of the connection, or the performance behavior is undefined. If not specified, the performance mode defaults to [`WAPerformanceMode.bulk`](waperformancemode/bulk.md) on both sides.

## Topics

### Setting performance modes
- [WAPerformanceMode.bulk](waperformancemode/bulk.md)
  A mode that prioritizes throughput, power, and support for other concurrent Wi-Fi use cases and devices.
- [WAPerformanceMode.realtime](waperformancemode/realtime.md)
  A mode that prioritizes latency at the expense of throughput, power, and other concurrent Wi-Fi use cases and devices.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct NWPath](../network/nwpath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [struct WAPath](wapath.md)
  A representation of the current Wi-Fi Aware path.
- [enum WAAccessCategory](waaccesscategory.md)
  The underling quality-of-service (QoS) the Wi-Fi layer uses to transmit data packets from a connection over the air.
- [struct WAPerformanceReport](waperformancereport.md)
  The current performance state of the data path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancemode)*