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

### Operators
- [static func == (MonthlyWeatherStatistics<T>, MonthlyWeatherStatistics<T>) -> Bool](monthlyweatherstatistics/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](monthlyweatherstatistics/init(from:).md)
  Creates a new instance by decoding from the given decoder.
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
### Instance Methods
- [func encode(to: any Encoder) throws](monthlyweatherstatistics/encode(to:).md)
  Encodes this value into the given encoder.
### Subscripts
- [subscript(MonthlyWeatherStatistics<T>.Index) -> MonthlyWeatherStatistics<T>.Element](monthlyweatherstatistics/subscript(_:).md)
  The month weather statistics at the provided index.
### Type Aliases
- [MonthlyWeatherStatistics.Element](monthlyweatherstatistics/element.md)
  A type representing the sequence’s elements.
- [MonthlyWeatherStatistics.Index](monthlyweatherstatistics/index.md)
  A type that represents a position in the collection.
- [MonthlyWeatherStatistics.Indices](monthlyweatherstatistics/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [MonthlyWeatherStatistics.Iterator](monthlyweatherstatistics/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [MonthlyWeatherStatistics.SubSequence](monthlyweatherstatistics/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](monthlyweatherstatistics/bidirectionalcollection-implementations.md)
- [Collection Implementations](monthlyweatherstatistics/collection-implementations.md)
- [Equatable Implementations](monthlyweatherstatistics/equatable-implementations.md)
- [RandomAccessCollection Implementations](monthlyweatherstatistics/randomaccesscollection-implementations.md)
- [Sequence Implementations](monthlyweatherstatistics/sequence-implementations.md)

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