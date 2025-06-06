# DailyWeatherStatistics

**Framework**: Weatherkit  
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

### Operators
- [static func == (DailyWeatherStatistics<T>, DailyWeatherStatistics<T>) -> Bool](dailyweatherstatistics/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](dailyweatherstatistics/init(from:).md)
  Creates a new instance by decoding from the given decoder.
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
### Instance Methods
- [func encode(to: any Encoder) throws](dailyweatherstatistics/encode(to:).md)
  Encodes this value into the given encoder.
### Subscripts
- [subscript(DailyWeatherStatistics<T>.Index) -> DailyWeatherStatistics<T>.Element](dailyweatherstatistics/subscript(_:).md)
  The day weather statistics at the provided index.
### Type Aliases
- [DailyWeatherStatistics.Element](dailyweatherstatistics/element.md)
  A type representing the sequence’s elements.
- [DailyWeatherStatistics.Index](dailyweatherstatistics/index.md)
  A type that represents a position in the collection.
- [DailyWeatherStatistics.Indices](dailyweatherstatistics/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [DailyWeatherStatistics.Iterator](dailyweatherstatistics/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [DailyWeatherStatistics.SubSequence](dailyweatherstatistics/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](dailyweatherstatistics/bidirectionalcollection-implementations.md)
- [Collection Implementations](dailyweatherstatistics/collection-implementations.md)
- [Equatable Implementations](dailyweatherstatistics/equatable-implementations.md)
- [RandomAccessCollection Implementations](dailyweatherstatistics/randomaccesscollection-implementations.md)
- [Sequence Implementations](dailyweatherstatistics/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweatherstatistics)*