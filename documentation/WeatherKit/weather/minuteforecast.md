# minuteForecast

**Framework**: WeatherKit  
**Kind**: property  
**Role**: Instance Property

The minute-by-minute forecast.

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
var minuteForecast: Forecast<MinuteWeather>?
```

## Discussion

Depending upon region support and data availability, this may be `nil`.

## See Also

### Getting the forecast
- [var availability: WeatherAvailability](./availability.md)
  Flags containing information about data availability and attribution.
- [var currentWeather: CurrentWeather](./currentweather.md)
  The current weather forecast.
- [var dailyForecast: Forecast<DayWeather>](./dailyforecast.md)
  The daily forecast.
- [var hourlyForecast: Forecast<HourWeather>](./hourlyforecast.md)
  The hourly forecast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weather/minuteforecast)*