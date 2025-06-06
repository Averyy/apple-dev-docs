# dailyStatistics(for:startDay:endDay:including:)

**Framework**: Weatherkit  
**Kind**: method

Returns daily weather statistics for the requested location, for each day from the start day to the end day, inclusively.

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
final func dailyStatistics<each T>(for location: CLLocation, startDay: Int, endDay: Int, including dataSets: repeat DailyWeatherStatisticsQuery<each T>) async throws -> (repeat DailyWeatherStatistics<each T>) where repeat each T : Decodable, repeat each T : Encodable, repeat each T : Equatable, repeat each T : Sendable
```

#### Return Value

The requested daily weather statistics

#### Discussion

> **Note**: Weather data error `WeatherError`

The statistics returned for each day are derived from weather data recorded over the past decades, to the present date. Each item returned represents statistics for a particular day of the year, in UTC.

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. The following example will return statistics for the first 10 days of the year.

```None
let (dailyPrecipitationStatistics, dailyTemperatureStatistics) = try await service.dailyStatistics(for: newYork, startDay: 1, endDay: 10, including: .precipitation, .temperature)
```

If `startDay` is greater than `endDay`, then a wrap around will occur. This next example will return statistics for days 365, 366, 1, and 2.

```swift
let (dailyPrecipitationStatistics, dailyTemperatureStatistics) = try await service.dailyStatistics(for: newYork, startDay: 365, endDay: 2, including: .precipitation, .temperature)
```

> **Note**: `startDay in 1...366 && endDay in 1...366`

## Parameters

- `location`: The requested location.
- `startDay`: The first day of the span, between 1 and 366.
- `endDay`: The last day of the span, between 1 and 366.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/dailystatistics(for:startday:endday:including:))*