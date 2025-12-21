# ServicePrediction

**Framework**: WirelessInsights  
**Kind**: struct

An individual prediction of anticipated cellular network availability.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct ServicePrediction
```

#### Overview

Your app receives arrays of curent predictions from the [`servicePredictions`](servicepredictionprovider/servicepredictions.md) asynchronous sequence. Inspect the timing and impact properties of these predictions, and the associated confidence scores, to determine if your app takes action before a possible change in cellular conditions.

## Topics

### Accessing prediction impact
- [let impact: ServicePrediction.Impact](serviceprediction/impact-swift.property.md)
  The expected impact of the predicted event.
- [ServicePrediction.Impact](serviceprediction/impact-swift.enum.md)
  An enumeration of levels of impact for a predicted event.
### Accessing prediction timing
- [let predictedStartTime: Date](serviceprediction/predictedstarttime.md)
  The start time of the predicted event.
- [let predictedInterval: TimeInterval](serviceprediction/predictedinterval.md)
  The expected duration of the predicted event.
- [ServicePrediction.QuantizedInterval](serviceprediction/quantizedinterval.md)
  A type that provides discrete time intervals to express the expected duration of a predicted event.
### Accessing prediction confidence
- [let confidenceScore: ServicePrediction.ConfidenceScore](serviceprediction/confidencescore-swift.property.md)
  A score that represents the level of confidence in various aspects of the prediction.
- [ServicePrediction.ConfidenceScore](serviceprediction/confidencescore-swift.struct.md)
  A type that represents the confidence in various aspects of the prediction.
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

- [var servicePredictions: any AsyncSequence<[ServicePrediction], any Error>](servicepredictionprovider/servicepredictions.md)
  An asychronous sequence of current predictions.
- [enum ServicePredictionError](servicepredictionerror.md)
  A type that represents errors encountered while using the WirelessInsights framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction)*