# MonthlyWeatherStatisticsQuery

**Framework**: WeatherKit  
**Kind**: struct

A structure that encapsulates a generic monthly weather statistics dataset request.

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
struct MonthlyWeatherStatisticsQuery<T> where T : Decodable, T : Encodable, T : Equatable, T : Sendable
```

#### Overview

Use the properties of this structure to create a monthly weather statistics query. You can combine multiple queries into a single `WeatherService` request.

Here’s how to get monthly weather statistics for New York City:

```None
let (monthlyPrecipitationStatistics, monthlyTemperatureStatistics) = try await service.monthlyStatistics(for: newYork, spanning: interval, including: .precipitation, .temperature)
```

## Topics

### Type Properties
- [static var precipitation: MonthlyWeatherStatisticsQuery<MonthPrecipitationStatistics>](monthlyweatherstatisticsquery/precipitation.md)
  The monthly precipitation statistics query.
- [static var temperature: MonthlyWeatherStatisticsQuery<MonthTemperatureStatistics>](monthlyweatherstatisticsquery/temperature.md)
  The monthly temperature statistics query.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/monthlyweatherstatisticsquery)*