# WeatherAlertSummary

**Framework**: WeatherKit REST API  
**Kind**: dictionary

Detailed information about the weather alert.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
object WeatherAlertSummary
```

## Properties

- `areaId` (string): An official designation of the affected area.
- `areaName` (string): A human-readable name of the affected area.
- `certainty` (Certainty) *(required)*: How likely the event is to occur.
- `countryCode` (string) *(required)*: The ISO code of the reporting country.
- `description` (string) *(required)*: A human-readable description of the event.
- `detailsUrl` (string): The URL to a page containing detailed information about the event.
- `effectiveTime` (date-time) *(required)*: The time the event went into effect.
- `eventEndTime` (date-time): The time when the underlying weather event is projected to end.
- `eventOnsetTime` (date-time): The time when the underlying weather event is projected to start.
- `expireTime` (date-time) *(required)*: The time when the event expires.
- `id` (uuid) *(required)*: A unique identifier of the event.
- `issuedTime` (date-time) *(required)*: The time that event was issued by the reporting agency.
- `responses` ([ResponseType]) *(required)*: An array of recommended actions from the reporting agency.
- `severity` (Severity) *(required)*: The level of danger to life and property.
- `source` (string) *(required)*: The name of the reporting agency.
- `urgency` (Urgency): An indication of urgency of action from the reporting agency.

## Relationships

### Inherited By
- [WeatherAlert](weatheralert.md)

## See Also

- [GET /api/v1/weatherAlert/{language}/{id}](get-api-v1-weatheralert-_language_-_id_.md)
  Receive an active weather alert.
- [object WeatherAlert](weatheralert.md)
  An official message indicating severe weather from a reporting agency.
- [object WeatherAlertCollection](weatheralertcollection.md)
  A collection of severe weather alerts for a specified location.
- [type ResponseType](responsetype.md)
  The recommended action from a reporting agency.
- [type Severity](severity.md)
  The level of danger to life and property.
- [type Urgency](urgency.md)
  An indication of urgency of action from the reporting agency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/weatheralertsummary)*