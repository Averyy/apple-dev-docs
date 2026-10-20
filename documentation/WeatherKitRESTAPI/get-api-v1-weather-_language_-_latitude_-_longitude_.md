# GET /api/v1/weather/{language}/{latitude}/{longitude}

**Framework**: WeatherKit REST API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Obtain weather data for the specified location.

**Availability**:
- Weather API 1.0.0+

## Endpoint

`GET https://weatherkit.apple.com/api/v1/weather/{language}/{latitude}/{longitude}`

## Parameters

### Path Parameters

- `language` (string) *(required)*: The language tag to use for localizing responses.
- `latitude` (Latitude) *(required)*: The latitude of the desired location.

  **Minimum**: `-90`; **Maximum**: `90`
- `longitude` (Longitude) *(required)*: The longitude of the desired location.

  **Minimum**: `-180`; **Maximum**: `180`

### Query Parameters

- `countryCode` (string): The ISO Alpha-2 country code for the requested location. This parameter is necessary for weather alerts.
- `currentAsOf` (date-time): The time to obtain current conditions. Defaults to `now`.
- `dailyEnd` (date-time): The time to end the daily forecast. If this parameter is absent, daily forecasts run for 10 days.
- `dailyStart` (date-time): The time to start the daily forecast. If this parameter is absent, daily forecasts start on the current day.
- `dataSets` ([DataSet]): A comma-delimited list of data sets to include in the response.
- `hourlyEnd` (date-time): The time to end the hourly forecast. If this parameter is absent, hourly forecasts run 24 hours or the length of the daily forecast, whichever is longer.
- `hourlyStart` (date-time): The time to start the hourly forecast. If this parameter is absent, hourly forecasts start on the current hour.
- `timezone` (string) *(required)*: The name of the timezone to use for rolling up weather forecasts into daily forecasts.

## Responses

- `200` OK (`Weather`, `application/json`): The request is successful. The weather alert is in the response.
- `400` Bad Request: The server is unable to process the request due to an invalid parameter value.
- `401` Unauthorized: The request isn’t authorized or doesn’t include the correct authentication information.

## See Also

### Obtaining weather information for a location
- [GET /api/v1/availability/{latitude}/{longitude}](./get-api-v1-availability-_latitude_-_longitude_.md)
  Determine the data sets available for the specified location.
- [object Weather](./weather.md)
  The collection of all requested weather data.
- [type Latitude](./latitude.md)
  A numeric value indicating the latitude of the coordinate between `-90` and `90`.
- [type Longitude](./longitude.md)
  A numeric value indicating the longitude of the coordinate between `-180` and `180`.
- [type DataSet](./dataset.md)
  The collection of weather information for a location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/get-api-v1-weather-_language_-_latitude_-_longitude_)*