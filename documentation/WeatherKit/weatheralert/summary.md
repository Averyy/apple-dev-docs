# summary

**Framework**: WeatherKit  
**Kind**: property  
**Role**: Instance Property

The summary of the event type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var summary: String
```

#### Discussion

The summary may or may not contain localized descriptions, depending on what is available from the source.

## See Also

### Getting the properties
- [var metadata: WeatherMetadata](./metadata.md)
  Descriptive information about the weather alert data.
- [var region: String?](./region.md)
  The name of the affected area.
- [var severity: WeatherSeverity](./severity.md)
  The severity of the weather alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatheralert/summary)*