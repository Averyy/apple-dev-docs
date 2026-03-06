# ForecastPeriodSummary

**Framework**: WeatherKit REST API  
**Kind**: dictionary

The summary for a specified period in the minute forecast.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
object ForecastPeriodSummary
```

## Properties

- `condition` (PrecipitationType) *(required)*: The type of precipitation forecasted.
- `endTime` (date-time): The end time of the forecast.
- `precipitationChance` (number) *(required)*: The probability of precipitation during this period.
- `precipitationIntensity` (number) *(required)*: The precipitation intensity in millimeters per hour.
- `startTime` (date-time) *(required)*: The start time of the forecast.

## See Also

- [object ForecastMinute](forecastminute.md)
  The precipitation forecast for a specified minute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/forecastperiodsummary)*