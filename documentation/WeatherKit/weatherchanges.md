# WeatherChanges

**Framework**: WeatherKit  
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

## Relationships

### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [Collection](../swift/collection.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherchanges)*