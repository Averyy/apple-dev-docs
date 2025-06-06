# monthlyStatistics(for:forMonthsIn:including:)

**Framework**: Weatherkit  
**Kind**: method

Returns monthly weather statistics for the requested location, for each month within the specified date interval.

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
final func monthlyStatistics<each T>(for location: CLLocation, forMonthsIn interval: DateInterval, including dataSets: repeat MonthlyWeatherStatisticsQuery<each T>) async throws -> (repeat MonthlyWeatherStatistics<each T>) where repeat each T : Decodable, repeat each T : Encodable, repeat each T : Equatable, repeat each T : Sendable
```

#### Return Value

The requested monthly weather statistics.

#### Discussion

> **Note**: Weather data error `WeatherError`

Weather data error `WeatherError`

The statistics returned for each month are derived from weather data recorded over the past decades, to the present date. Each item returned represents statistics for a particular Gregorian Calendar month of the year.

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. Here’s an example:

```swift
let (monthlyPrecipitationStatistics, monthlyTemperatureStatistics) = try await service.monthlyStatistics(for: newYork, forMonthsIn: interval, including: .precipitation, .temperature)
```

## Parameters

- `location`: The requested location.
- `interval`: The date interval for which to obtain monthly weather statistics. The end date of the interval will be capped at 1 year after the start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/monthlystatistics(for:formonthsin:including:))*