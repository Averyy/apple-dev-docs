# DailyWeatherSummary

**Framework**: WeatherKit  
**Kind**: struct

A structure that holds a collection of day weather summaries.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct DailyWeatherSummary<T> where T : Decodable, T : Encodable, T : Equatable, T : Sendable
```

## Topics

### Instance Properties
- [var days: [T]](dailyweathersummary/days.md)
  An ordered collection of day weather summaries of type `T`, for each requested day.
- [var endIndex: DailyWeatherSummary<T>.Index](dailyweathersummary/endindex.md)
  The end index for the daily weather summaries.
- [var metadata: WeatherMetadata](dailyweathersummary/metadata.md)
  Descriptive information about the weather statistics data.
- [var startIndex: DailyWeatherSummary<T>.Index](dailyweathersummary/startindex.md)
  The start index for the daily weather summaries.
### Subscripts
- [subscript(DailyWeatherSummary<T>.Index) -> DailyWeatherSummary<T>.Element](dailyweathersummary/subscript(_:).md)
  The day weather summary at the provided index.

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummary)*