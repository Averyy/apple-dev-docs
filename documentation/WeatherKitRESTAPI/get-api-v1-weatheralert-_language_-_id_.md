# GET /api/v1/weatherAlert/{language}/{id}

**Framework**: WeatherKit REST API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Receive an active weather alert.

**Availability**:
- Weather API 1.0.0+

## Endpoint

`GET https://weatherkit.apple.com/api/v1/weatherAlert/{language}/{id}`

## Parameters

### Path Parameters

- `id` (uuid) *(required)*: The unique identifier for the weather alert.
- `language` (string) *(required)*: The language tag to use for localizing responses.

## Responses

- `200` OK (`WeatherAlert`, `application/json`): The request is successful. The weather alert is in the response.
- `400` Bad Request: The server is unable to process the request due to an invalid parameter value.
- `401` Unauthorized: The request isn’t authorized or doesn’t include the correct authentication information.
- `404` Not Found: There’s no active alert for the specified unique identifier.

## See Also

### Obtaining weather alerts
- [object WeatherAlert](./weatheralert.md)
  An official message indicating severe weather from a reporting agency.
- [object WeatherAlertCollection](./weatheralertcollection.md)
  A collection of severe weather alerts for a specified location.
- [object WeatherAlertSummary](./weatheralertsummary.md)
  Detailed information about the weather alert.
- [type ResponseType](./responsetype.md)
  The recommended action from a reporting agency.
- [type Severity](./severity.md)
  The level of danger to life and property.
- [type Urgency](./urgency.md)
  An indication of urgency of action from the reporting agency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/get-api-v1-weatheralert-_language_-_id_)*