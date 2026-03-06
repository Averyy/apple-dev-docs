# Urgency

**Framework**: WeatherKit REST API  
**Kind**: typealias

An indication of urgency of action from the reporting agency.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
string Urgency
```

#### Possible Values

- **immediate**: Take responsive action immediately.
- **expected**: Take responsive action in the next hour.
- **future**: Take responsive action in the near future.
- **past**: Responsive action is no longer required.
- **unknown**: The urgency is unknown.

## See Also

- [GET /api/v1/weatherAlert/{language}/{id}](get-api-v1-weatheralert-_language_-_id_.md)
  Receive an active weather alert.
- [object WeatherAlert](weatheralert.md)
  An official message indicating severe weather from a reporting agency.
- [object WeatherAlertCollection](weatheralertcollection.md)
  A collection of severe weather alerts for a specified location.
- [object WeatherAlertSummary](weatheralertsummary.md)
  Detailed information about the weather alert.
- [type ResponseType](responsetype.md)
  The recommended action from a reporting agency.
- [type Severity](severity.md)
  The level of danger to life and property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/urgency)*