# HistoricalComparisons

**Framework**: Weatherkit  
**Kind**: struct

A structure that represents the weather condition comparisons for a specific location. It’s a list of comparisons between current readings and historical averages. The list is ordered by significance of deviation.

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
struct HistoricalComparisons
```

## Topics

### Operators
- [static func == (HistoricalComparisons, HistoricalComparisons) -> Bool](historicalcomparisons/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](historicalcomparisons/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var comparisons: [HistoricalComparison]](historicalcomparisons/comparisons.md)
  A list of comparisons between current readings and historical averages, ordered by significance of deviation.
- [var endIndex: HistoricalComparisons.Index](historicalcomparisons/endindex.md)
  The end index for the historical comparisons.
- [var metadata: WeatherMetadata](historicalcomparisons/metadata.md)
  Descriptive information about the weather comparisons data.
- [var startIndex: HistoricalComparisons.Index](historicalcomparisons/startindex.md)
  The start index for the historical comparisons.
### Instance Methods
- [func encode(to: any Encoder) throws](historicalcomparisons/encode(to:).md)
  Encodes this value into the given encoder.
### Subscripts
- [subscript(HistoricalComparisons.Index) -> HistoricalComparisons.Element](historicalcomparisons/subscript(_:).md)
  The historical comparison at the provided index.
### Type Aliases
- [HistoricalComparisons.Element](historicalcomparisons/element.md)
  A type representing the sequence’s elements.
- [HistoricalComparisons.Index](historicalcomparisons/index.md)
  A type that represents a position in the collection.
- [HistoricalComparisons.Indices](historicalcomparisons/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [HistoricalComparisons.Iterator](historicalcomparisons/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [HistoricalComparisons.SubSequence](historicalcomparisons/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](historicalcomparisons/bidirectionalcollection-implementations.md)
- [Collection Implementations](historicalcomparisons/collection-implementations.md)
- [Equatable Implementations](historicalcomparisons/equatable-implementations.md)
- [RandomAccessCollection Implementations](historicalcomparisons/randomaccesscollection-implementations.md)
- [Sequence Implementations](historicalcomparisons/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/historicalcomparisons)*