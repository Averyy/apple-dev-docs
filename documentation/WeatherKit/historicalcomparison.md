# HistoricalComparison

**Framework**: WeatherKit  
**Kind**: enum

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
- [case highTemperature(Trend<UnitTemperature>)](historicalcomparison/hightemperature(_:).md)
  The comparison relates to the location’s maximum temperature averaged since ~1970.
- [case lowTemperature(Trend<UnitTemperature>)](historicalcomparison/lowtemperature(_:).md)
  The comparison relates to the location’s minimum temperature averaged since ~1970.
- [HistoricalComparison.precipitationAmount(_:)](historicalcomparison/precipitationamount(_:).md)
  The comparison relates to the amount of precipitation at the location averaged over the past 30 days.
- [HistoricalComparison.snowfallAmount(_:)](historicalcomparison/snowfallamount(_:).md)
  The comparison relates to the amount of snowfall at the location averaged over the past 30 days.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/historicalcomparison)*