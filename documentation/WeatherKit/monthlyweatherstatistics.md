# MonthlyWeatherStatistics

**Framework**: WeatherKit  
**Kind**: struct

A structure that holds a collection of month weather statistics data.

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
struct MonthlyWeatherStatistics<T> where T : Decodable, T : Encodable, T : Equatable, T : Sendable
```

#### Overview

Weather statistics for each month are derived from data for that month, collected over all years since the baseline start date.

## Topics

### Instance Properties
- [var baselineStartDate: Date](monthlyweatherstatistics/baselinestartdate.md)
  The year the statistics collection began.
- [var endIndex: MonthlyWeatherStatistics<T>.Index](monthlyweatherstatistics/endindex.md)
  The end index for the monthly weather statistics.
- [var metadata: WeatherMetadata](monthlyweatherstatistics/metadata.md)
  Descriptive information about the weather statistics data.
- [var months: [T]](monthlyweatherstatistics/months.md)
  An ordered collection of month weather statistics data of type `T`, for each requested month.
- [var startIndex: MonthlyWeatherStatistics<T>.Index](monthlyweatherstatistics/startindex.md)
  The start index for the monthly weather statistics.
### Subscripts
- [subscript(MonthlyWeatherStatistics<T>.Index) -> MonthlyWeatherStatistics<T>.Element](monthlyweatherstatistics/subscript(_:).md)
  The month weather statistics at the provided index.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/monthlyweatherstatistics)*