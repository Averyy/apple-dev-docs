# ServicePrediction.ConfidenceScore

**Framework**: WirelessInsights  
**Kind**: struct

A type that represents the confidence in various aspects of the prediction.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct ConfidenceScore
```

## Topics

### Accessing prediction confidence scores
- [let prediction: ServicePrediction.Confidence](serviceprediction/confidencescore-swift.struct/prediction.md)
  Confidence that the predicted event will occur.
- [let startTime: ServicePrediction.Confidence](serviceprediction/confidencescore-swift.struct/starttime.md)
  Confidence of the start time if the predicted event occurs.
- [let duration: ServicePrediction.Confidence](serviceprediction/confidencescore-swift.struct/duration.md)
  Confidence of the duration if the predicted event occurs.
- [ServicePrediction.Confidence](serviceprediction/confidence.md)
  An enumeration of levels of confidence for a prediction or one of its properties.
### Encoding and decoding
- [init(from: any Decoder) throws](serviceprediction/confidencescore-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](serviceprediction/confidencescore-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](serviceprediction/confidencescore-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](serviceprediction/confidencescore-swift.struct/hashvalue.md)
  The hash value.
### Comparing confidence scores
- [static func == (ServicePrediction.ConfidenceScore, ServicePrediction.ConfidenceScore) -> Bool](serviceprediction/confidencescore-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](serviceprediction/confidencescore-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let confidenceScore: ServicePrediction.ConfidenceScore](serviceprediction/confidencescore-swift.property.md)
  A score that represents the level of confidence in various aspects of the prediction.
- [ServicePrediction.Confidence](serviceprediction/confidence.md)
  An enumeration of levels of confidence for a prediction or one of its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/confidencescore-swift.struct)*