# predictedInterval

**Framework**: WirelessInsights  
**Kind**: property  
**Role**: Instance Property

The expected duration of the predicted event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
let predictedInterval: TimeInterval
```

## Discussion

The value of this property is one of the defined values of the [`ServicePrediction.QuantizedInterval`](./quantizedinterval.md) type.

## See Also

### Accessing prediction timing
- [let predictedStartTime: Date](./predictedstarttime.md)
  The start time of the predicted event.
- [ServicePrediction.QuantizedInterval](./quantizedinterval.md)
  A type that provides discrete time intervals to express the expected duration of a predicted event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/predictedinterval)*