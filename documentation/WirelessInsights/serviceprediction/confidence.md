# ServicePrediction.Confidence

**Framework**: WirelessInsights  
**Kind**: enum

An enumeration of levels of confidence for a prediction or one of its properties.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum Confidence
```

## Topics

### Working with confidence values
- [ServicePrediction.Confidence.high](serviceprediction/confidence/high.md)
  A high confidence level in the prediction.
- [ServicePrediction.Confidence.medium](serviceprediction/confidence/medium.md)
  A medium confidence level in the prediction.
- [ServicePrediction.Confidence.low](serviceprediction/confidence/low.md)
  A low confidence level in the prediction.
### Encoding and decoding
- [init(from: any Decoder) throws](serviceprediction/confidence/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](serviceprediction/confidence/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](serviceprediction/confidence/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](serviceprediction/confidence/hashvalue.md)
  The hash value.
### Comparing confidence values
- [static func == (ServicePrediction.Confidence, ServicePrediction.Confidence) -> Bool](serviceprediction/confidence/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (ServicePrediction.Confidence, ServicePrediction.Confidence) -> Bool](serviceprediction/confidence/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Default Implementations
- [Comparable Implementations](serviceprediction/confidence/comparable-implementations.md)
- [Equatable Implementations](serviceprediction/confidence/equatable-implementations.md)

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

- [let confidenceScore: ServicePrediction.ConfidenceScore](serviceprediction/confidencescore-swift.property.md)
  A score that represents the level of confidence in various aspects of the prediction.
- [ServicePrediction.ConfidenceScore](serviceprediction/confidencescore-swift.struct.md)
  A type that represents the confidence in various aspects of the prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/confidence)*