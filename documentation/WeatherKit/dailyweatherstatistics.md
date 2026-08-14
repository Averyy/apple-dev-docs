# DailyWeatherStatistics

**Framework**: WeatherKit  
**Kind**: struct

A structure that holds a collection of day weather statistics data.

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
struct DailyWeatherStatistics<T> where T : Decodable, T : Encodable, T : Equatable, T : Sendable
```

#### Overview

Weather statistics for each day are derived from data for that day, collected over all years since the baseline start date.

## Topics

### Instance Properties
- [var baselineStartDate: Date](dailyweatherstatistics/baselinestartdate.md)
  The year the statistics collection began.
- [var days: [T]](dailyweatherstatistics/days.md)
  An ordered collection of day weather statistics data of type `T`, for each requested day.
- [var endIndex: DailyWeatherStatistics<T>.Index](dailyweatherstatistics/endindex.md)
  The end index for the daily weather statistics.
- [var metadata: WeatherMetadata](dailyweatherstatistics/metadata.md)
  Descriptive information about the weather statistics data.
- [var startIndex: DailyWeatherStatistics<T>.Index](dailyweatherstatistics/startindex.md)
  The start index for the daily weather statistics.
### Subscripts
- [subscript(DailyWeatherStatistics<T>.Index) -> DailyWeatherStatistics<T>.Element](dailyweatherstatistics/subscript(_:).md)
  The day weather statistics at the provided index.

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

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweatherstatistics)*