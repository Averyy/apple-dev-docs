# TrendBaseline

**Framework**: WeatherKit  
**Kind**: struct

A type encapsulating everything there is to know about what a trend baseline is.

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
struct TrendBaseline<Dimension> where Dimension : Dimension
```

## Topics

### Instance Properties
- [let kind: TrendBaseline<Dimension>.Kind](trendbaseline/kind-swift.property.md)
  The manner in which the comparison between the baseline and current values are compared.
- [let startDate: Date](trendbaseline/startdate.md)
  The year the statistics collection began.
- [let value: Measurement<Dimension>](trendbaseline/value.md)
  The recorded baseline value for the condition in which the trend is comparing to.
### Enumerations
- [TrendBaseline.Kind](trendbaseline/kind-swift.enum.md)
  An enum describing what value is being compared between historical and current readings.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/trendbaseline)*