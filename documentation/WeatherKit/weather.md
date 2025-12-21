# Weather

**Framework**: WeatherKit  
**Kind**: struct

A model representing the aggregate weather data the caller requests.

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
struct Weather
```

## Topics

### Getting the forecast
- [var availability: WeatherAvailability](weather/availability.md)
  Flags containing information about data availability and attribution.
- [var currentWeather: CurrentWeather](weather/currentweather.md)
  The current weather forecast.
- [var dailyForecast: Forecast<DayWeather>](weather/dailyforecast.md)
  The daily forecast.
- [var hourlyForecast: Forecast<HourWeather>](weather/hourlyforecast.md)
  The hourly forecast.
- [var minuteForecast: Forecast<MinuteWeather>?](weather/minuteforecast.md)
  The minute-by-minute forecast.
### Getting weather alerts
- [var weatherAlerts: [WeatherAlert]?](weather/weatheralerts.md)
  A list of severe weather alerts.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Fetching weather forecasts with WeatherKit](fetching_weather_forecasts_with_weatherkit.md)
  Request and display weather data for destination airports in a flight-planning app.
- [class WeatherService](weatherservice.md)
  Provides an interface for obtaining weather data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weather)*