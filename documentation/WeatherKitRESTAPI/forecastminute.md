# ForecastMinute

**Framework**: WeatherKit REST API  
**Kind**: dictionary

The precipitation forecast for a specified minute.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
object ForecastMinute
```

## Properties

- `precipitationChance` (number) *(required)*: The probability of precipitation during this minute.
- `precipitationIntensity` (number) *(required)*: The precipitation intensity in millimeters per hour.
- `startTime` (date-time) *(required)*: The start time of the minute.

## See Also

- [object ForecastPeriodSummary](forecastperiodsummary.md)
  The summary for a specified period in the minute forecast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/forecastminute)*