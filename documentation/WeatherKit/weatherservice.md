# WeatherService

**Framework**: Weatherkit  
**Kind**: class

Provides an interface for obtaining weather data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final class WeatherService
```

## Topics

### Creating the object
- [convenience init()](weatherservice/init.md)
  Creates a weather service object.
### Obtaining forecasts
- [func weather(for: CLLocation) async throws -> Weather](weatherservice/weather(for:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>) async throws -> (T1, T2)](weatherservice/weather(for:including:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>) async throws -> (T1, T2, T3)](weatherservice/weather(for:including:_:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>) async throws -> (T1, T2, T3, T4)](weatherservice/weather(for:including:_:_:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4, T5>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>, WeatherQuery<T5>) async throws -> (T1, T2, T3, T4, T5)](weatherservice/weather(for:including:_:_:_:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4, T5, T6>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>, WeatherQuery<T5>, WeatherQuery<T6>) async throws -> (T1, T2, T3, T4, T5, T6)](weatherservice/weather(for:including:_:_:_:_:_:).md)
  Returns the weather forecast for the requested location.
- [static let shared: WeatherService](weatherservice/shared.md)
  A single, shared weather service object.
### Providing attribution
- [var attribution: WeatherAttribution](weatherservice/attribution.md)
  The required attribution which includes a legal attribution page and Apple Weather mark.
### Instance Methods
- [func dailyStatistics<each T>(for: CLLocation, forDaysIn: DateInterval, including: repeat DailyWeatherStatisticsQuery<each T>) async throws -> (repeat DailyWeatherStatistics<each T>)](weatherservice/dailystatistics(for:fordaysin:including:).md)
  Returns daily weather statistics for the requested location, for each day within the specified date interval.
- [func dailyStatistics<each T>(for: CLLocation, including: repeat DailyWeatherStatisticsQuery<each T>) async throws -> (repeat DailyWeatherStatistics<each T>)](weatherservice/dailystatistics(for:including:).md)
  Returns daily weather statistics for the requested location, for each day between 30 days ago and 10 days from now.
- [func dailyStatistics<each T>(for: CLLocation, startDay: Int, endDay: Int, including: repeat DailyWeatherStatisticsQuery<each T>) async throws -> (repeat DailyWeatherStatistics<each T>)](weatherservice/dailystatistics(for:startday:endday:including:).md)
  Returns daily weather statistics for the requested location, for each day from the start day to the end day, inclusively.
- [func dailySummary<each T>(for: CLLocation, forDaysIn: DateInterval, including: repeat DailyWeatherSummaryQuery<each T>) async throws -> (repeat DailyWeatherSummary<each T>)](weatherservice/dailysummary(for:fordaysin:including:).md)
  Returns day weather summaries for the requested location, for each day within the provided date interval.
- [func dailySummary<each T>(for: CLLocation, including: repeat DailyWeatherSummaryQuery<each T>) async throws -> (repeat DailyWeatherSummary<each T>)](weatherservice/dailysummary(for:including:).md)
  Returns day weather summaries for the requested location, for the past 30 days, including the present day.
- [func hourlyStatistics<each T>(for: CLLocation, forHoursIn: DateInterval, including: repeat HourlyWeatherStatisticsQuery<each T>) async throws -> (repeat HourlyWeatherStatistics<each T>)](weatherservice/hourlystatistics(for:forhoursin:including:).md)
  Returns hourly weather statistics for the requested location, for each hour within the specified date interval.
- [func hourlyStatistics<each T>(for: CLLocation, including: repeat HourlyWeatherStatisticsQuery<each T>) async throws -> (repeat HourlyWeatherStatistics<each T>)](weatherservice/hourlystatistics(for:including:).md)
  Returns hourly weather statistics for the requested location, for the 24 hours of the current day.
- [func hourlyStatistics<each T>(for: CLLocation, startHour: Int, endHour: Int, including: repeat HourlyWeatherStatisticsQuery<each T>) async throws -> (repeat HourlyWeatherStatistics<each T>)](weatherservice/hourlystatistics(for:starthour:endhour:including:).md)
  Returns hourly weather statistics for the requested location, for each hour from the start hour to the end hour, inclusively.
- [func monthlyStatistics<each T>(for: CLLocation, forMonthsIn: DateInterval, including: repeat MonthlyWeatherStatisticsQuery<each T>) async throws -> (repeat MonthlyWeatherStatistics<each T>)](weatherservice/monthlystatistics(for:formonthsin:including:).md)
  Returns monthly weather statistics for the requested location, for each month within the specified date interval.
- [func monthlyStatistics<each T>(for: CLLocation, including: repeat MonthlyWeatherStatisticsQuery<each T>) async throws -> (repeat MonthlyWeatherStatistics<each T>)](weatherservice/monthlystatistics(for:including:).md)
  Returns monthly weather statistics for the requested location, for all 12 months of the Gregorian calendar year.
- [func monthlyStatistics<each T>(for: CLLocation, startMonth: Int, endMonth: Int, including: repeat MonthlyWeatherStatisticsQuery<each T>) async throws -> (repeat MonthlyWeatherStatistics<each T>)](weatherservice/monthlystatistics(for:startmonth:endmonth:including:).md)
  Returns monthly weather statistics for the requested location, for each month from the start month to the end month, inclusively.
- [func weather<T>(for: CLLocation, including: WeatherQuery<T>) async throws -> T](weatherservice/weather(for:including:)-3cg1d.md)
  Returns the weather forecast for the requested location.
- [func weather<each T>(for: CLLocation, including: repeat WeatherQuery<each T>) async throws -> (repeat each T)](weatherservice/weather(for:including:)-5jqwy.md)
  Returns the weather forecast for the requested location.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [Fetching weather forecasts with WeatherKit](fetching_weather_forecasts_with_weatherkit.md)
  Request and display weather data for destination airports in a flight-planning app.
- [struct Weather](weather.md)
  A model representing the aggregate weather data the caller requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice)*