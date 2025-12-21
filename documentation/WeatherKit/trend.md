# Trend

**Framework**: WeatherKit  
**Kind**: struct

A structure describing an observed pattern in the data for weather at a location for a specific condition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Trend<Dimension> where Dimension : Dimension
```

## Topics

### Instance Properties
- [var baseline: TrendBaseline<Dimension>](trend/baseline.md)
  The manner in which the comparison between the baseline and current values are compared.
- [var currentValue: Measurement<Dimension>](trend/currentvalue.md)
  The current recorded value for the condition in which the trend is compared against.
- [var deviation: Deviation](trend/deviation.md)
  Semantically describes the manner in which the observed trend compares the current value against the baseline value.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/trend)*