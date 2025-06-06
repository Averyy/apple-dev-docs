# WeatherChanges

**Framework**: Weatherkit  
**Kind**: struct

A structure that represents the Weather Change forecast. It provides a qualitative assessment of whether upcoming weather is significantly different from prior conditions.

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
struct WeatherChanges
```

## Topics

### Instance Properties
- [var changes: [WeatherChange]](weatherchanges/changes.md)
  A list of forecasted weather changes, in chronological order.
- [var endIndex: WeatherChanges.Index](weatherchanges/endindex.md)
  The end index for the weather changes.
- [var metadata: WeatherMetadata](weatherchanges/metadata.md)
  Descriptive information about the weather change data.
- [var startIndex: WeatherChanges.Index](weatherchanges/startindex.md)
  The start index for the weather changes.
### Subscripts
- [subscript(WeatherChanges.Index) -> WeatherChanges.Element](weatherchanges/subscript(_:).md)
  The weather change at the provided index.
### Type Aliases
- [WeatherChanges.Element](weatherchanges/element.md)
  A type representing the sequence’s elements.
- [WeatherChanges.Index](weatherchanges/index.md)
  A type that represents a position in the collection.
- [WeatherChanges.Indices](weatherchanges/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [WeatherChanges.Iterator](weatherchanges/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [WeatherChanges.SubSequence](weatherchanges/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](weatherchanges/bidirectionalcollection-implementations.md)
- [Collection Implementations](weatherchanges/collection-implementations.md)
- [Decodable Implementations](weatherchanges/decodable-implementations.md)
- [Encodable Implementations](weatherchanges/encodable-implementations.md)
- [Equatable Implementations](weatherchanges/equatable-implementations.md)
- [RandomAccessCollection Implementations](weatherchanges/randomaccesscollection-implementations.md)
- [Sequence Implementations](weatherchanges/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherchanges)*