# DayPartForecast

**Framework**: WeatherKit REST API  
**Kind**: dictionary

A summary forecast for a daytime or overnight period.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
object DayPartForecast
```

## Properties

- `cloudCover` (number) *(required)*: The percentage of the sky covered with clouds during the period, from `0` to `1`.
- `conditionCode` (string) *(required)*: An enumeration value indicating the condition at the time.
- `forecastEnd` (date-time) *(required)*: The ending date and time of the forecast.
- `forecastStart` (date-time) *(required)*: The starting date and time of the forecast.
- `humidity` (number) *(required)*: The relative humidity during the period, from `0` to `1`.
- `precipitationAmount` (number) *(required)*: The amount of precipitation forecasted to occur during the period, in millimeters.
- `precipitationChance` (number) *(required)*: The chance of precipitation forecasted to occur during the period.
- `precipitationType` (PrecipitationType) *(required)*: The type of precipitation forecasted to occur during the period.
- `snowfallAmount` (number) *(required)*: The depth of snow as ice crystals forecasted to occur during the period, in millimeters.
- `windDirection` (integer): The direction the wind is forecasted to come from during the period, in degrees.
- `windSpeed` (number) *(required)*: The average speed the wind is forecasted to be during the period, in kilometers per hour.

## See Also

- [object DayWeatherConditions](dayweatherconditions.md)
  The historical or forecasted weather conditions for a specified day.
- [object DailyForecast](dailyforecast.md)
  A collection of day forecasts for a specified range of days.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/daypartforecast)*