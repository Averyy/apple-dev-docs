# dailyStatistics(for:forDaysIn:including:)

**Framework**: WeatherKit  
**Kind**: method

Returns daily weather statistics for the requested location, for each day within the specified date interval.

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
final func dailyStatistics<each T>(for location: CLLocation, forDaysIn interval: DateInterval, including dataSets: repeat DailyWeatherStatisticsQuery<each T>) async throws -> (repeat DailyWeatherStatistics<each T>) where repeat each T : Decodable, repeat each T : Encodable, repeat each T : Equatable, repeat each T : Sendable
```

#### Return Value

The requested daily weather statistics.

#### Discussion

> **Note**: Weather data error `WeatherError`

The statistics returned for each day are derived from weather data recorded over the past decades, to the present date. Each item returned represents statistics for a particular day of the year, in UTC. For example, if December 31, UTC time, is within the span, the statistics returned for that particular day will be taken from data recorded over the years for day 365 of the year, or 366 if December 31 of the span falls on a leap year.

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. Here’s an example:

```None
let (dailyPrecipitationStatistics, dailyTemperatureStatistics) = try await service.dailyStatistics(for: newYork, forDaysIn: timeInterval, including: .precipitation, .temperature)
```

## Parameters

- `location`: The requested location.
- `interval`: The date interval for which to obtain daily weather statistics. The end date of the interval will be capped at 1 year after the start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/dailystatistics(for:fordaysin:including:))*