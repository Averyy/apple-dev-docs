# ServicePrediction.ConfidenceScore

**Framework**: WirelessInsights  
**Kind**: struct  
**Role**: Structure

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
- [let prediction: ServicePrediction.Confidence](./confidencescore-swift.struct/prediction.md)
  Confidence that the predicted event will occur.
- [let startTime: ServicePrediction.Confidence](./confidencescore-swift.struct/starttime.md)
  Confidence of the start time if the predicted event occurs.
- [let duration: ServicePrediction.Confidence](./confidencescore-swift.struct/duration.md)
  Confidence of the duration if the predicted event occurs.
- [ServicePrediction.Confidence](./confidence.md)
  An enumeration of levels of confidence for a prediction or one of its properties.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing prediction confidence
- [let confidenceScore: ServicePrediction.ConfidenceScore](./confidencescore-swift.property.md)
  A score that represents the level of confidence in various aspects of the prediction.
- [ServicePrediction.Confidence](./confidence.md)
  An enumeration of levels of confidence for a prediction or one of its properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/confidencescore-swift.struct)*