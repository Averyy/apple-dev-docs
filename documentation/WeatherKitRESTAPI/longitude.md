# Longitude

**Framework**: WeatherKit REST API  
**Kind**: typealias

A numeric value indicating the longitude of the coordinate between `-180` and `180`.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
number Longitude
```

#### Discussion

Negative values indicate west of the prime meridian; positive values indicate east of the prime meridian.

## See Also

- [GET /api/v1/availability/{latitude}/{longitude}](get-api-v1-availability-_latitude_-_longitude_.md)
  Determine the data sets available for the specified location.
- [GET /api/v1/weather/{language}/{latitude}/{longitude}](get-api-v1-weather-_language_-_latitude_-_longitude_.md)
  Obtain weather data for the specified location.
- [object Weather](weather.md)
  The collection of all requested weather data.
- [type Latitude](latitude.md)
  A numeric value indicating the latitude of the coordinate between `-90` and `90`.
- [type DataSet](dataset.md)
  The collection of weather information for a location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/longitude)*