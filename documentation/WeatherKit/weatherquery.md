# WeatherQuery

**Framework**: WeatherKit  
**Kind**: struct

A structure that encapsulates a generic weather dataset request.

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
struct WeatherQuery<T>
```

#### Overview

Use the properties of this structure to create a weather query. You can combine multiple weather queries into a single [`WeatherService`](weatherservice.md) request.

Here’s how to get the weather for New York City:

```swift
let (hourly, daily, alerts) = try await service.weather(for: newYork, including: .hourly, .daily, .alerts)
```

## Topics

### Creating queries
- [static var alerts: WeatherQuery<[WeatherAlert]?>](weatherquery/alerts.md)
  The weather alerts query.
- [static var availability: WeatherQuery<WeatherAvailability>](weatherquery/availability.md)
  The availability query.
- [static var current: WeatherQuery<CurrentWeather>](weatherquery/current.md)
  The current weather query.
- [static var daily: WeatherQuery<Forecast<DayWeather>>](weatherquery/daily.md)
  The daily forecast query. This returns 10 contiguous days, beginning with the current day.
- [static var hourly: WeatherQuery<Forecast<HourWeather>>](weatherquery/hourly.md)
  The hourly forecast query. This returns 25 contiguous hours, beginning with the current hour.
- [static var minute: WeatherQuery<Forecast<MinuteWeather>?>](weatherquery/minute.md)
  The minute forecast query.
- [static func daily(startDate: Date, endDate: Date) -> WeatherQuery<T>](weatherquery/daily(startdate:enddate:).md)
  Returns weather for an arbitrary range of days, with the following caveats:
- [static func hourly(startDate: Date, endDate: Date) -> WeatherQuery<T>](weatherquery/hourly(startdate:enddate:).md)
  The hourly forecast query that takes a start date and end date for the request, with the following caveats:
### Type Properties
- [static var changes: WeatherQuery<WeatherChanges?>](weatherquery/changes.md)
  The weather changes query.
- [static var historicalComparisons: WeatherQuery<HistoricalComparisons?>](weatherquery/historicalcomparisons.md)
  The weather historical comparison query.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CurrentWeather](currentweather.md)
  A structure that describes the current conditions observed at a location.
- [struct WeatherAttribution](weatherattribution.md)
  A structure that  defines the necessary information for attributing a weather data provider.
- [struct WeatherMetadata](weathermetadata.md)
  A structure that provides additional weather information.
- [enum WeatherSeverity](weatherseverity.md)
  A description of the severity of the severe weather event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherquery)*