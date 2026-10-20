# GET /attribution/{language}

**Framework**: WeatherKit REST API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Receive attribution information.

**Availability**:
- Weather API 1.0.0+

## Endpoint

`GET https://weatherkit.apple.com/attribution/{language}`

## Parameters

### Path Parameters

- `language` (string) *(required)*: The language tag to use for localizing responses.

## Responses

- `200` OK (`Attribution`, `application/json`): The request is successful. The attribution information is in the response.

## See Also

### Performing attribution
- [object Attribution](./attribution.md)
  A list of image asset URLs for attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/get-attribution-_language_)*