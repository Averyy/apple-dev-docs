# HourWeather

**Framework**: WeatherKit  
**Kind**: struct

A structure that represents the weather conditions for the hour.

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
struct HourWeather
```

## Topics

### Getting temperature and humidity
- [var apparentTemperature: Measurement<UnitTemperature>](hourweather/apparenttemperature.md)
  The apparent, or “feels like” temperature during the hour.
- [var humidity: Double](hourweather/humidity.md)
  The humidity for the hour.
- [var temperature: Measurement<UnitTemperature>](hourweather/temperature.md)
  The temperature during the hour.
- [var dewPoint: Measurement<UnitTemperature>](hourweather/dewpoint.md)
  The amount of moisture in the air.
### Getting pressure
- [var pressure: Measurement<UnitPressure>](hourweather/pressure.md)
  The atmospheric pressure at sea level at a given location.
- [var pressureTrend: PressureTrend](hourweather/pressuretrend.md)
  The kind and amount of atmospheric pressure change over time.
### Getting conditions
- [var cloudCover: Double](hourweather/cloudcover.md)
  The percentage of the sky covered with clouds.
- [var condition: WeatherCondition](hourweather/condition.md)
  A description of the weather condition for this hour.
- [var isDaylight: Bool](hourweather/isdaylight.md)
  The presence or absence of daylight at the requested location and hour.
- [var visibility: Measurement<UnitLength>](hourweather/visibility.md)
  The distance at which an object can be clearly seen.
### Getting the UV index
- [var uvIndex: UVIndex](hourweather/uvindex.md)
  The expected intensity of ultraviolet radiation from the sun.
### Getting the wind
- [var wind: Wind](hourweather/wind.md)
  Wind data describing the wind speed, direction, and gust.
### Getting the date
- [var date: Date](hourweather/date.md)
  The start time of the hour weather.
### Getting the precipitation
- [var precipitation: Precipitation](hourweather/precipitation.md)
  Description of precipitation for this hour.
- [var precipitationChance: Double](hourweather/precipitationchance.md)
  The probability of precipitation during the hour.
### Getting the weather symbol
- [var symbolName: String](hourweather/symbolname.md)
  The SF Symbol icon that represents the hour weather condition and whether it’s daylight on the hour.
### Instance Properties
- [var cloudCoverByAltitude: CloudCoverByAltitude](hourweather/cloudcoverbyaltitude.md)
  The percentage of the sky covered with low altitude, middle altitude and high altitude clouds during the period.
- [var precipitationAmount: Measurement<UnitLength>](hourweather/precipitationamount.md)
  The amount of precipitation for the hour.
- [var snowfallAmount: Measurement<UnitLength>](hourweather/snowfallamount.md)
  The amount of snowfall for the hour.

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
- [struct DayWeather](dayweather.md)
  A structure that represents the weather conditions for the day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourweather)*