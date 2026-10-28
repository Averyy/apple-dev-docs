# Certainty

**Framework**: WeatherKit REST API  
**Kind**: typealias  
**Role**: Type

How likely the event is to occur.

**Availability**:
- Weather API 1.0.0+

## Declaration

```
string Certainty
```

## Possible Values

- `observed`
- `likely`
- `possible`
- `unlikely`
- `unknown`

## Possible Values

- **observed**: The event has already occurred or is ongoing.
- **likely**: The event is likely to occur (greater than 50% probability).
- **possible**: The event is unlikley to occur (less than 50% probability).
- **unlikely**: The event is not expected to occur (approximately 0% probability).
- **unknown**: It is unknown if the event will occur.

## See Also

### Obtaining event information
- [object EventText](./eventtext.md)
  The official text describing a severe weather event from the agency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/certainty)*