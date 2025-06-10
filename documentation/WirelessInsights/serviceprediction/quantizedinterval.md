# ServicePrediction.QuantizedInterval

**Framework**: WirelessInsights  
**Kind**: struct

A type that provides discrete time intervals to express the expected duration of a predicted event.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct QuantizedInterval
```

## Topics

### Working with interval values
- [static let long: Double](serviceprediction/quantizedinterval/long.md)
  An interval for an issue expected to last more than five minutes.
- [static let medium: Double](serviceprediction/quantizedinterval/medium.md)
  An interval for an issue expected to last approximately five minutes.
- [static let short: Double](serviceprediction/quantizedinterval/short.md)
  An interval for an issue expected to last approximately one minute or fewer.
- [static let minimal: Double](serviceprediction/quantizedinterval/minimal.md)
  An interval for an issue expected to last approximately 10 seconds or fewer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let predictedStartTime: Date](serviceprediction/predictedstarttime.md)
  The start time of the predicted event.
- [let predictedInterval: TimeInterval](serviceprediction/predictedinterval.md)
  The expected duration of the predicted event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/serviceprediction/quantizedinterval)*