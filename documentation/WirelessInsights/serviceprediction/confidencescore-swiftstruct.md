# ServicePrediction.ConfidenceScore

**Framework**: WirelessInsights  
**Kind**: struct

A type that represents the confidence in various aspects of the prediction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

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