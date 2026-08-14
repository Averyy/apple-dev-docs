# Percentiles

**Framework**: WeatherKit  
**Kind**: struct

A structure that describes probability distributions for a measurable weather condition.

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
struct Percentiles<Dimension> where Dimension : Dimension
```

## Topics

### Instance Properties
- [var p10: Measurement<Dimension>](percentiles/p10.md)
  10% of the distribution is less than this value.
- [var p50: Measurement<Dimension>](percentiles/p50.md)
  50% of the distribution is less than this value.
- [var p90: Measurement<Dimension>](percentiles/p90.md)
  90% of the distribution is less than this value.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/percentiles)*