# DailyWeatherSummary

**Framework**: Weatherkit  
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

### Operators
- [static func == (DailyWeatherSummary<T>, DailyWeatherSummary<T>) -> Bool](dailyweathersummary/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](dailyweathersummary/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var days: [T]](dailyweathersummary/days.md)
  An ordered collection of day weather summaries of type `T`, for each requested day.
- [var endIndex: DailyWeatherSummary<T>.Index](dailyweathersummary/endindex.md)
  The end index for the daily weather summaries.
- [var metadata: WeatherMetadata](dailyweathersummary/metadata.md)
  Descriptive information about the weather statistics data.
- [var startIndex: DailyWeatherSummary<T>.Index](dailyweathersummary/startindex.md)
  The start index for the daily weather summaries.
### Instance Methods
- [func encode(to: any Encoder) throws](dailyweathersummary/encode(to:).md)
  Encodes this value into the given encoder.
### Subscripts
- [subscript(DailyWeatherSummary<T>.Index) -> DailyWeatherSummary<T>.Element](dailyweathersummary/subscript(_:).md)
  The day weather summary at the provided index.
### Type Aliases
- [DailyWeatherSummary.Element](dailyweathersummary/element.md)
  A type representing the sequence’s elements.
- [DailyWeatherSummary.Index](dailyweathersummary/index.md)
  A type that represents a position in the collection.
- [DailyWeatherSummary.Indices](dailyweathersummary/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [DailyWeatherSummary.Iterator](dailyweathersummary/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [DailyWeatherSummary.SubSequence](dailyweathersummary/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](dailyweathersummary/bidirectionalcollection-implementations.md)
- [Collection Implementations](dailyweathersummary/collection-implementations.md)
- [Equatable Implementations](dailyweathersummary/equatable-implementations.md)
- [RandomAccessCollection Implementations](dailyweathersummary/randomaccesscollection-implementations.md)
- [Sequence Implementations](dailyweathersummary/sequence-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummary)*