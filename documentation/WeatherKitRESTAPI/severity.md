# Severity

**Framework**: WeatherKit REST API  
**Kind**: typealias  
**Role**: Type

The level of danger to life and property.

**Availability**:
- Weather API 1.0.0+

## Declaration

```
string Severity
```

## Possible Values

- `extreme`
- `severe`
- `moderate`
- `minor`
- `unknown`

## Possible Values

- **extreme**: Extraordinary threat.
- **severe**: Significant threat.
- **moderate**: Possible threat.
- **minor**: Minimal or no known threat.
- **unknown**: Unknown threat.

## See Also

### Obtaining weather alerts
- [GET /api/v1/weatherAlert/{language}/{id}](./get-api-v1-weatheralert-_language_-_id_.md)
  Receive an active weather alert.
- [object WeatherAlert](./weatheralert.md)
  An official message indicating severe weather from a reporting agency.
- [object WeatherAlertCollection](./weatheralertcollection.md)
  A collection of severe weather alerts for a specified location.
- [object WeatherAlertSummary](./weatheralertsummary.md)
  Detailed information about the weather alert.
- [type ResponseType](./responsetype.md)
  The recommended action from a reporting agency.
- [type Urgency](./urgency.md)
  An indication of urgency of action from the reporting agency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/severity)*