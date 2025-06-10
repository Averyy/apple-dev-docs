# DayWeather

**Framework**: WeatherKit  
**Kind**: struct

A structure that represents the weather conditions for the day.

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
struct DayWeather
```

## Topics

### Getting temperature
- [var highTemperature: Measurement<UnitTemperature>](dayweather/hightemperature.md)
  The daytime high temperature.
- [var lowTemperature: Measurement<UnitTemperature>](dayweather/lowtemperature.md)
  The overnight low temperature.
### Getting precipitation
- [var precipitation: Precipitation](dayweather/precipitation.md)
  The description of precipitation for this day.
- [var precipitationChance: Double](dayweather/precipitationchance.md)
  The probability of precipitation during the day.
- [var rainfallAmount: Measurement<UnitLength>](dayweather/rainfallamount.md)
  The amount of liquid precipitation for the day.
- [var snowfallAmount: Measurement<UnitLength>](dayweather/snowfallamount.md)
  The amount of snowfall for the day.
### Getting celestial information
- [var moon: MoonEvents](dayweather/moon.md)
  The lunar events for the day.
- [var sun: SunEvents](dayweather/sun.md)
  The solar events for the day.
### Getting the wind
- [var wind: Wind](dayweather/wind.md)
  The wind speed, direction, and gust.
### Getting the date
- [var date: Date](dayweather/date.md)
  The start time of the day weather.
### Getting condition and UV index
- [var condition: WeatherCondition](dayweather/condition.md)
  A description of the weather condition on this day.
- [var uvIndex: UVIndex](dayweather/uvindex.md)
  The expected intensity of ultraviolet radiation from the sun.
### Getting the weather symbol
- [var symbolName: String](dayweather/symbolname.md)
  The SF Symbol icon that represents the day weather condition.
### Instance Properties
- [var daytimeForecast: DayPartForecast](dayweather/daytimeforecast.md)
  The weather forecast from 7AM - 7PM on this day.
- [var highTemperatureTime: Date?](dayweather/hightemperaturetime.md)
  The time at which the high temperature occurs on this day.
- [var highWindSpeed: Measurement<UnitSpeed>?](dayweather/highwindspeed.md)
  The maximum sustained wind speed.
- [var lowTemperatureTime: Date?](dayweather/lowtemperaturetime.md)
  The time at which the low temperature occurs on this day.
- [var maximumHumidity: Double](dayweather/maximumhumidity.md)
  The maximum amount of water vapor in the air for the day.
- [var maximumVisibility: Double](dayweather/maximumvisibility.md)
  The maximum distance, in meters, at which terrain is visible for the day.
- [var minimumHumidity: Double](dayweather/minimumhumidity.md)
  The minimum amount of water vapor in the air for the day.
- [var minimumVisibility: Double](dayweather/minimumvisibility.md)
  The minimum distance, in meters, at which terrain is visible for the day.
- [var overnightForecast: DayPartForecast](dayweather/overnightforecast.md)
  The weather forecast for 7PM on this day until 7AM the following day.
- [var precipitationAmount: Measurement<UnitLength>](dayweather/precipitationamount.md)
  The amount of liquid precipitation for the day.
- [var precipitationAmountByType: PrecipitationAmountByType](dayweather/precipitationamountbytype.md)
  A breakdown of amounts of all forms of precipitation forecasted for the day.
- [var restOfDayForecast: DayPartForecast?](dayweather/restofdayforecast.md)
  The forecast from now until midnight local time.
### Default Implementations
- [Decodable Implementations](dayweather/decodable-implementations.md)
- [Encodable Implementations](dayweather/encodable-implementations.md)
- [Equatable Implementations](dayweather/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WeatherAlert](weatheralert.md)
  A weather alert issued for the requested  location by a governmental authority.
- [struct WeatherAvailability](weatheravailability.md)
  A structure that indicates the availability of data at the requested location.
- [struct Forecast](forecast.md)
  A forecast collection for minute, hourly, and daily forecasts.
- [struct MinuteWeather](minuteweather.md)
  A structure that represents the next hour minute forecasts.
- [struct HourWeather](hourweather.md)
  A structure that represents the weather conditions for the hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dayweather)*