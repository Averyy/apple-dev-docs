# ServicePrediction.Impact

**Framework**: WirelessInsights  
**Kind**: enum

An enumeration of levels of impact for a predicted event.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum Impact
```

## Topics

### Working with impact values
- [ServicePrediction.Impact.high](serviceprediction/impact-swift.enum/high.md)
  An impact level for severe interruption, including substantially lowered throughput and the potential to lose data capability.
- [ServicePrediction.Impact.medium](serviceprediction/impact-swift.enum/medium.md)
  An impact level for moderately lower throughput and service interruption.
- [ServicePrediction.Impact.low](serviceprediction/impact-swift.enum/low.md)
  An impact level for slightly lower throughput and possibly some service interruption.
### Encoding and decoding
- [init(from: any Decoder) throws](serviceprediction/impact-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](serviceprediction/impact-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](serviceprediction/impact-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](serviceprediction/impact-swift.enum/hashvalue.md)
  The hash value.
### Comparing impact values
- [static func == (ServicePrediction.Impact, ServicePrediction.Impact) -> Bool](serviceprediction/impact-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Operators
- [static func < (ServicePrediction.Impact, ServicePrediction.Impact) -> Bool](serviceprediction/impact-swift.enum/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Default Implementations
- [Comparable Implementations](serviceprediction/impact-swift.enum/comparable-implementations.md)
- [Equatable Implementations](serviceprediction/impact-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let impact: ServicePrediction.Impact](serviceprediction/impact-swift.property.md)
  The expected impact of the predicted event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/impact-swift.enum)*