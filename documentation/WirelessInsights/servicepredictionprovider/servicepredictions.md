# servicePredictions

**Framework**: WirelessInsights  
**Kind**: property

An asychronous sequence of current predictions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final var servicePredictions: any AsyncSequence<[ServicePrediction], any Error> { get }
```

#### Discussion

To act on predictions about wireless service changes, use a `for`-`await`-`in` loop to iterate over events produced by this sequence as conditions change. Each update provides either an array of [`ServicePrediction`](serviceprediction.md) instances representing the current set of predictions or throws a [`ServicePredictionError`](servicepredictionerror.md). Only act on the most recent array of predictions received from the sequence.

> **Note**: The framework requires that your app have the `com.apple.developer.wireless-insights.service-predictions` entitlement in order to access predictions.

## See Also

- [struct ServicePrediction](serviceprediction.md)
  An individual prediction of anticipated cellular network availability.
- [enum ServicePredictionError](servicepredictionerror.md)
  A type that represents errors encountered while using the WirelessInsights framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/servicepredictionprovider/servicepredictions)*