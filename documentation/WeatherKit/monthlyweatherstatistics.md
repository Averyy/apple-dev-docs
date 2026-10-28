# MonthlyWeatherStatistics

**Framework**: WeatherKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

Weather statistics for each month are derived from data for that month, collected over all years since the baseline start date.

## Topics

### Instance Properties
- [var baselineStartDate: Date](./monthlyweatherstatistics/baselinestartdate.md)
  The year the statistics collection began.
- [var endIndex: MonthlyWeatherStatistics<T>.Index](./monthlyweatherstatistics/endindex.md)
  The end index for the monthly weather statistics.
- [var metadata: WeatherMetadata](./monthlyweatherstatistics/metadata.md)
  Descriptive information about the weather statistics data.
- [var months: [T]](./monthlyweatherstatistics/months.md)
  An ordered collection of month weather statistics data of type `T`, for each requested month.
- [var startIndex: MonthlyWeatherStatistics<T>.Index](./monthlyweatherstatistics/startindex.md)
  The start index for the monthly weather statistics.
### Subscripts
- [subscript(MonthlyWeatherStatistics<T>.Index) -> MonthlyWeatherStatistics<T>.Element](./monthlyweatherstatistics/subscript%28_%29.md)
  The month weather statistics at the provided index.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/monthlyweatherstatistics)*