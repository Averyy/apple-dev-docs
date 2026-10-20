# GET /api/v1/availability/{latitude}/{longitude}

**Framework**: WeatherKit REST API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Determine the data sets available for the specified location.

**Availability**:
- Weather API 1.0.0+

## Endpoint

`GET https://weatherkit.apple.com/api/v1/availability/{latitude}/{longitude}`

## Parameters

### Path Parameters

- `latitude` (Latitude) *(required)*: The latitude of the desired location.

  **Minimum**: `-90`; **Maximum**: `90`
- `longitude` (Longitude) *(required)*: The longitude of the desired location.

  **Minimum**: `-180`; **Maximum**: `180`

### Query Parameters

- `country` (string) *(required)*: The ISO Alpha-2 country code for the requested location. This parameter is necessary for air quality and weather alerts.

## Responses

- `200` OK (`[DataSet]`, `application/json`): The request is successful. The data sets are in the response.
- `400` Bad Request: The server is unable to process the request due to an invalid parameter value.
- `401` Unauthorized: The request isn’t authorized or doesn’t include the correct authentication information.

## See Also

### Obtaining weather information for a location
- [GET /api/v1/weather/{language}/{latitude}/{longitude}](./get-api-v1-weather-_language_-_latitude_-_longitude_.md)
  Obtain weather data for the specified location.
- [object Weather](./weather.md)
  The collection of all requested weather data.
- [type Latitude](./latitude.md)
  A numeric value indicating the latitude of the coordinate between `-90` and `90`.
- [type Longitude](./longitude.md)
  A numeric value indicating the longitude of the coordinate between `-180` and `180`.
- [type DataSet](./dataset.md)
  The collection of weather information for a location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/get-api-v1-availability-_latitude_-_longitude_)*