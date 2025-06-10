# TrendBaseline.Kind

**Framework**: WeatherKit  
**Kind**: enum

An enum describing what value is being compared between historical and current readings.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum Kind
```

## Topics

### Operators
- [static func == (TrendBaseline<Dimension>.Kind, TrendBaseline<Dimension>.Kind) -> Bool](trendbaseline/kind-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [TrendBaseline.Kind.mean](trendbaseline/kind-swift.enum/mean.md)
  The baseline value is a mean (or average) of other values.
### Initializers
- [init(from: any Decoder) throws](trendbaseline/kind-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](trendbaseline/kind-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](trendbaseline/kind-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](trendbaseline/kind-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](trendbaseline/kind-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/trendbaseline/kind-swift.enum)*