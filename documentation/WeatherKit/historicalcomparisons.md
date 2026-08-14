# HistoricalComparisons

**Framework**: WeatherKit  
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

### Instance Properties
- [var comparisons: [HistoricalComparison]](historicalcomparisons/comparisons.md)
  A list of comparisons between current readings and historical averages, ordered by significance of deviation.
- [var endIndex: HistoricalComparisons.Index](historicalcomparisons/endindex.md)
  The end index for the historical comparisons.
- [var metadata: WeatherMetadata](historicalcomparisons/metadata.md)
  Descriptive information about the weather comparisons data.
- [var startIndex: HistoricalComparisons.Index](historicalcomparisons/startindex.md)
  The start index for the historical comparisons.
### Subscripts
- [subscript(HistoricalComparisons.Index) -> HistoricalComparisons.Element](historicalcomparisons/subscript(_:).md)
  The historical comparison at the provided index.

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

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/historicalcomparisons)*