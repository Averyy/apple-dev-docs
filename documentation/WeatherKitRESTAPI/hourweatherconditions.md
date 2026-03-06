# HourWeatherConditions

**Framework**: WeatherKit REST API  
**Kind**: dictionary

The historical or forecasted weather conditions for a specified hour.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
object HourWeatherConditions
```

## Properties

- `cloudCover` (number) *(required)*: The percentage of the sky covered with clouds during the period, from `0` to `1`.
- `conditionCode` (string) *(required)*: An enumeration value indicating the condition at the time.
- `daylight` (boolean): Indicates whether the hour starts during the day or night.
- `forecastStart` (date-time) *(required)*: The starting date and time of the forecast.
- `humidity` (number) *(required)*: The relative humidity at the start of the hour, from `0` to `1`.
- `precipitationChance` (number) *(required)*: The chance of precipitation forecasted to occur during the hour, from `0` to `1`.
- `precipitationType` (PrecipitationType) *(required)*: The type of precipitation forecasted to occur during the period.
- `pressure` (number) *(required)*: The sea-level air pressure, in millibars.
- `pressureTrend` (PressureTrend): The direction of change of the sea-level air pressure.
- `snowfallIntensity` (number): The rate at which snow crystals are falling, in millimeters per hour.
- `temperature` (number) *(required)*: The temperature at the start of the hour, in degrees Celsius.
- `temperatureApparent` (number) *(required)*: The feels-like temperature when considering wind and humidity, at the start of the hour, in degrees Celsius.
- `temperatureDewPoint` (number): The temperature at which relative humidity is 100% at the top of the hour, in degrees Celsius.
- `uvIndex` (integer) *(required)*: The level of ultraviolet radiation at the start of the hour.
- `visibility` (number) *(required)*: The distance at which terrain is visible at the start of the hour, in meters.
- `windDirection` (integer): The direction of the wind at the start of the hour, in degrees.
- `windGust` (number): The maximum wind gust speed during the hour, in kilometers per hour.
- `windSpeed` (number) *(required)*: The wind speed at the start of the hour, in kilometers per hour.
- `precipitationAmount` (number): The amount of precipitation forecasted to occur during period, in millimeters.

## See Also

- [object HourlyForecast](hourlyforecast.md)
  A collection of hour forecasts for a specified range of hours.
- [object NextHourForecast](nexthourforecast.md)
  A minute-by-minute forecast for the next hour.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/hourweatherconditions)*