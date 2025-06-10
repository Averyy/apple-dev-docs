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

### Operators
- [static func == (HourlyWeatherStatistics<T>, HourlyWeatherStatistics<T>) -> Bool](hourlyweatherstatistics/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](hourlyweatherstatistics/init(from:).md)
  Creates a new instance by decoding from the given decoder.
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
### Instance Methods
- [func encode(to: any Encoder) throws](hourlyweatherstatistics/encode(to:).md)
  Encodes this value into the given encoder.
### Subscripts
- [subscript(HourlyWeatherStatistics<T>.Index) -> HourlyWeatherStatistics<T>.Element](hourlyweatherstatistics/subscript(_:).md)
  The hour weather statistics at the provided index.
### Type Aliases
- [HourlyWeatherStatistics.Element](hourlyweatherstatistics/element.md)
  A type representing the sequence’s elements.
- [HourlyWeatherStatistics.Index](hourlyweatherstatistics/index.md)
  A type that represents a position in the collection.
- [HourlyWeatherStatistics.Indices](hourlyweatherstatistics/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [HourlyWeatherStatistics.Iterator](hourlyweatherstatistics/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [HourlyWeatherStatistics.SubSequence](hourlyweatherstatistics/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](hourlyweatherstatistics/bidirectionalcollection-implementations.md)
- [Collection Implementations](hourlyweatherstatistics/collection-implementations.md)
- [Equatable Implementations](hourlyweatherstatistics/equatable-implementations.md)
- [RandomAccessCollection Implementations](hourlyweatherstatistics/randomaccesscollection-implementations.md)
- [Sequence Implementations](hourlyweatherstatistics/sequence-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourlyweatherstatistics)*