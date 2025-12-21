# ServicePredictionError

**Framework**: WirelessInsights  
**Kind**: enum

A type that represents errors encountered while using the WirelessInsights framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum ServicePredictionError
```

## Topics

### Handling configuration errors
- [ServicePredictionError.unsupportedDevice](servicepredictionerror/unsupporteddevice.md)
  The device doesn’t currently support service predictions.
### Handling connectivity errors
- [ServicePredictionError.connectionError](servicepredictionerror/connectionerror.md)
  An unexpected error occurred while setting up the event stream.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var servicePredictions: any AsyncSequence<[ServicePrediction], any Error>](servicepredictionprovider/servicepredictions.md)
  An asychronous sequence of current predictions.
- [struct ServicePrediction](serviceprediction.md)
  An individual prediction of anticipated cellular network availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/servicepredictionerror)*