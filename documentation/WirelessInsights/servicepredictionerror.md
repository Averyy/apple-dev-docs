# ServicePredictionError

**Framework**: WirelessInsights  
**Kind**: enum

A type that represents errors encountered while using the WirelessInsights framework.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

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
### Operators
- [static func == (ServicePredictionError, ServicePredictionError) -> Bool](servicepredictionerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](servicepredictionerror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](servicepredictionerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](servicepredictionerror/equatable-implementations.md)
- [Error Implementations](servicepredictionerror/error-implementations.md)

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