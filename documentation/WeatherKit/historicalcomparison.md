# HistoricalComparison

**Framework**: WeatherKit  
**Kind**: enum  
**Role**: Enumeration

An enum that represents a recognized comparison in the statistical analysis of a location’s historical weather data.

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
enum HistoricalComparison
```

## Topics

### Enumeration Cases
- [case highTemperature(Trend<UnitTemperature>)](./historicalcomparison/hightemperature%28_%29.md)
  The comparison relates to the location’s maximum temperature averaged since ~1970.
- [case lowTemperature(Trend<UnitTemperature>)](./historicalcomparison/lowtemperature%28_%29.md)
  The comparison relates to the location’s minimum temperature averaged since ~1970.
- [HistoricalComparison.precipitationAmount(_:)](./historicalcomparison/precipitationamount%28_%29.md)
  The comparison relates to the amount of precipitation at the location averaged over the past 30 days.
- [HistoricalComparison.snowfallAmount(_:)](./historicalcomparison/snowfallamount%28_%29.md)
  The comparison relates to the amount of snowfall at the location averaged over the past 30 days.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/historicalcomparison)*