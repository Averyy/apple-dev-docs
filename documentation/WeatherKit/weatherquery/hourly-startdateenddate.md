# hourly(startDate:endDate:)

**Framework**: Weatherkit  
**Kind**: method

The hourly forecast query that takes a start date and end date for the request, with the following caveats:

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
static func hourly(startDate: Date, endDate: Date) -> WeatherQuery<T>
```

#### Return Value

An hourly forecast query for the specified time range

#### Discussion

- Historical data is available from Aug 1, 2021.
- Forecasts are available up to 10 days (~240 hours) in the future.
- Each request will return a maximum of 10 days (~240 hours).
- Hours in the forecast range from `startDate`(inclussive) to `endDate` (exclusive)

## Parameters

- `startDate`: The lower boundary of the time range for the forecast (inclusive)
- `endDate`: The upper boundary of the time range for the forecast (exclusive)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherquery/hourly(startdate:enddate:))*