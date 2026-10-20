# hourly

**Framework**: WeatherKit  
**Kind**: property  
**Role**: Type Property

The hourly forecast query. This returns 25 contiguous hours, beginning with the current hour.

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
static var hourly: WeatherQuery<Forecast<HourWeather>> { get }
```

## See Also

### Creating queries
- [static var alerts: WeatherQuery<[WeatherAlert]?>](./alerts.md)
  The weather alerts query.
- [static var availability: WeatherQuery<WeatherAvailability>](./availability.md)
  The availability query.
- [static var current: WeatherQuery<CurrentWeather>](./current.md)
  The current weather query.
- [static var daily: WeatherQuery<Forecast<DayWeather>>](./daily.md)
  The daily forecast query. This returns 10 contiguous days, beginning with the current day.
- [static var minute: WeatherQuery<Forecast<MinuteWeather>?>](./minute.md)
  The minute forecast query.
- [static func daily(startDate: Date, endDate: Date) -> WeatherQuery<T>](./daily%28startdate,enddate%29.md)
  Returns weather for an arbitrary range of days, with the following caveats:
- [static func hourly(startDate: Date, endDate: Date) -> WeatherQuery<T>](./hourly%28startdate,enddate%29.md)
  The hourly forecast query that takes a start date and end date for the request, with the following caveats:


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherquery/hourly)*