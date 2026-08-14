# HourlyWeatherStatistics

**Framework**: WeatherKit  
**Kind**: struct

A structure that holds a collection of hour weather statistics data.

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
struct HourlyWeatherStatistics<T> where T : Decodable, T : Encodable, T : Equatable, T : Sendable
```

#### Overview

Weather statistics for each hour are derived from data for that hour, collected over all years since the baseline start date.

## Topics

### Instance Properties
- [var baselineStartDate: Date](hourlyweatherstatistics/baselinestartdate.md)
  The date when the statistics collection began.
- [var endIndex: HourlyWeatherStatistics<T>.Index](hourlyweatherstatistics/endindex.md)
  The end index for the hourly weather statistics.
- [var hours: [T]](hourlyweatherstatistics/hours.md)
  An ordered collection of hour weather statistics data of type `T`, for each requested hour.
- [var metadata: WeatherMetadata](hourlyweatherstatistics/metadata.md)
  Descriptive information about the weather statistics data.
- [var startIndex: HourlyWeatherStatistics<T>.Index](hourlyweatherstatistics/startindex.md)
  The start index for the hourly weather statistics.
### Subscripts
- [subscript(HourlyWeatherStatistics<T>.Index) -> HourlyWeatherStatistics<T>.Element](hourlyweatherstatistics/subscript(_:).md)
  The hour weather statistics at the provided index.

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

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourlyweatherstatistics)*