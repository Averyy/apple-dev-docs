# hourlyStatistics(for:including:)

**Framework**: WeatherKit  
**Kind**: method

Returns hourly weather statistics for the requested location, for the 24 hours of the current day.

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
final func hourlyStatistics<each T>(for location: CLLocation, including dataSets: repeat HourlyWeatherStatisticsQuery<each T>) async throws -> (repeat HourlyWeatherStatistics<each T>) where repeat each T : Decodable, repeat each T : Encodable, repeat each T : Equatable, repeat each T : Sendable
```

#### Return Value

The requested hourly weather statistics.

#### Discussion

> **Note**: Weather data error `WeatherError`

The statistics returned for each hour are derived from weather data recorded over the past decades, to the present date. Each item returned represents statistics for a particular hour of the year, in UTC. For example, if the hours of December 31, UTC time, are within the span, the statistics returned for those particular hours will be taken from data recorded over the years for hours 8737 to 8760 of the year, or 8761 to 8784 if December 31 of the span falls on a leap year.

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. Here’s an example:

```swift
let hourlyTemperatureStatistics = try await service.hourlyStatistics(for: newYork, including: .temperature)
```

## Parameters

- `location`: The requested location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/hourlystatistics(for:including:))*