# MonthTemperatureStatistics

**Framework**: WeatherKit  
**Kind**: struct

A structure that describes temperature statistics for a specific month.

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
struct MonthTemperatureStatistics
```

## Topics

### Operators
- [static func == (MonthTemperatureStatistics, MonthTemperatureStatistics) -> Bool](monthtemperaturestatistics/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](monthtemperaturestatistics/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var averageHighTemperature: Measurement<UnitTemperature>](monthtemperaturestatistics/averagehightemperature.md)
  The average observed high temperature for the month.
- [var averageLowTemperature: Measurement<UnitTemperature>](monthtemperaturestatistics/averagelowtemperature.md)
  The average observed low temperature for the month.
- [var month: Int](monthtemperaturestatistics/month.md)
  The month of the year, in UTC.
### Instance Methods
- [func encode(to: any Encoder) throws](monthtemperaturestatistics/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](monthtemperaturestatistics/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/monthtemperaturestatistics)*