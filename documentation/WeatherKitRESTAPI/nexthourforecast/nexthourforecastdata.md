# NextHourForecast.NextHourForecastData

**Framework**: WeatherKit REST API  
**Kind**: dictionary

The next hour forecast information.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
object NextHourForecast.NextHourForecastData
```

## Properties

- `forecastEnd` (date-time): The time the forecast ends.
- `forecastStart` (date-time): The time the forecast starts.
- `minutes` ([ForecastMinute]) *(required)*: An array of the forecast minutes.
- `summary` ([ForecastPeriodSummary]) *(required)*: An array of the forecast summaries.

## Relationships

### Inherited By
- [NextHourForecast](nexthourforecast.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/nexthourforecast/nexthourforecastdata)*