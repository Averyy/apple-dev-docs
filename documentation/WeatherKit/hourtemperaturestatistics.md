# HourTemperatureStatistics

**Framework**: WeatherKit  
**Kind**: struct

A structure that describes temperature statistics for a specific hour.

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
struct HourTemperatureStatistics
```

## Topics

### Instance Properties
- [var hour: Int](hourtemperaturestatistics/hour.md)
  The hour of the year, in UTC.
- [var percentiles: Percentiles<UnitTemperature>](hourtemperaturestatistics/percentiles.md)
  The temperature statistics for the hour.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourtemperaturestatistics)*