# WAAccessCategory

**Framework**: Wi-Fi Aware  
**Kind**: enum

The underling quality-of-service (QoS) the Wi-Fi layer uses to transmit data packets from a connection over the air.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum WAAccessCategory
```

#### Overview

A given `NetworkConnection` is bound to a single access category at the Wi-Fi layer, based on the configuration of `NWParameter`’s  `serviceClass` property. This allows your app to specify how the Wi-Fi layer transmits the `NetworkConnection`’s data packets, selecting the performance characteristics that are relevant to the data flow.

Wi-Fi is a shared medium, so all Wi-Fi devices, networks, apps, and  `NetworkConnection`s share the overall Wi-Fi capacity between them. An app can improve the performance of its data flows, and that of all other nearby devices and Wi-Fi networks, by choosing the lowest QoS category that meets the requirements of each of its flows. When in doubt, use the default `.bestEffort` category.

For more information, refer to [`NWParameters.ServiceClass`](https://developer.apple.comhttps://developer.apple.com/documentation/network/nwparameters/serviceclass-swift.enum) and [`NWParameters`](https://developer.apple.comhttps://developer.apple.com/documentation/network/nwparameters).

Access categories are typically created by the system on behalf of the client, so they usually don’t need to be instantiated directly.

## Topics

### Providing throughput
- [WAAccessCategory.bestEffort](waaccesscategory/besteffort.md)
  A default quality-of-service (QoS) type that provides high throughput for data transfers of any size.
- [WAAccessCategory.background](waaccesscategory/background.md)
  A quality-of-service (QoS) type that provides high throughput for delay-tolerant, noninteractive data transfers of any size.
- [WAAccessCategory.interactiveVideo](waaccesscategory/interactivevideo.md)
  A quality-of-service (QoS) type that provides low-latency for moderate throughput flows.
- [WAAccessCategory.interactiveVoice](waaccesscategory/interactivevoice.md)
  A quality-of-service (QoS) type that provides very low latency for low-throughput flows.
### Creating an access category
- [init(from: any Decoder) throws](waaccesscategory/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (WAAccessCategory, WAAccessCategory) -> Bool](waaccesscategory/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](waaccesscategory/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](waaccesscategory/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](waaccesscategory/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [WAAccessCategory.AllCases](waaccesscategory/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [WAAccessCategory]](waaccesscategory/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [Equatable Implementations](waaccesscategory/equatable-implementations.md)

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
- [enum WAPerformanceMode](waperformancemode.md)
  The performance mode that indicates what performance criterion to prioritize.
- [struct WAPerformanceReport](waperformancereport.md)
  The current performance state of the data path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waaccesscategory)*