# ServicePrediction.QuantizedInterval

**Framework**: WirelessInsights  
**Kind**: struct  
**Role**: Structure

A type that provides discrete time intervals to express the expected duration of a predicted event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct QuantizedInterval
```

## Topics

### Working with interval values
- [static let long: Double](./quantizedinterval/long.md)
  An interval for an issue expected to last more than five minutes.
- [static let medium: Double](./quantizedinterval/medium.md)
  An interval for an issue expected to last approximately five minutes.
- [static let short: Double](./quantizedinterval/short.md)
  An interval for an issue expected to last approximately one minute or fewer.
- [static let minimal: Double](./quantizedinterval/minimal.md)
  An interval for an issue expected to last approximately 10 seconds or fewer.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing prediction timing
- [let predictedStartTime: Date](./predictedstarttime.md)
  The start time of the predicted event.
- [let predictedInterval: TimeInterval](./predictedinterval.md)
  The expected duration of the predicted event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/quantizedinterval)*