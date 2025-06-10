# WAPerformanceMode

**Framework**: Wi-Fi Aware  
**Kind**: enum

The performance mode that indicates what performance criterion to prioritize.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum WAPerformanceMode
```

#### Overview

> ❗ **Important**:  Each service must have the same [`WAPerformanceMode`](waperformancemode.md) on both the `NetworkBrowser` (subscriber) and `NetworkListener` (publisher) sides of the connection, or the performance behavior is undefined. If not specified, the performance mode defaults to [`WAPerformanceMode.bulk`](waperformancemode/bulk.md) on both sides.

## Topics

### Setting performance modes
- [WAPerformanceMode.bulk](waperformancemode/bulk.md)
  A mode that prioritizes throughput, power, and support for other concurrent Wi-Fi use cases and devices.
- [WAPerformanceMode.realtime](waperformancemode/realtime.md)
  A mode that prioritizes latency at the expense of throughput, power, and other concurrent Wi-Fi use cases and devices.
### Creating performance modes
- [init(from: any Decoder) throws](waperformancemode/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (WAPerformanceMode, WAPerformanceMode) -> Bool](waperformancemode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](waperformancemode/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](waperformancemode/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](waperformancemode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [WAPerformanceMode.AllCases](waperformancemode/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [WAPerformanceMode]](waperformancemode/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](waperformancemode/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NWPath](../Network/NWPath.md)
  An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [struct WAPath](wapath.md)
  A representation of the current Wi-Fi Aware path.
- [enum WAAccessCategory](waaccesscategory.md)
  The underling quality-of-service (QoS) the Wi-Fi layer uses to transmit data packets from a connection over the air.
- [struct WAPerformanceReport](waperformancereport.md)
  The current performance state of the data path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waperformancemode)*