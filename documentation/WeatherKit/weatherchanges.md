# WeatherChanges

**Framework**: WeatherKit  
**Kind**: struct  
**Role**: Structure

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
- [var changes: [WeatherChange]](./weatherchanges/changes.md)
  A list of forecasted weather changes, in chronological order.
- [var endIndex: WeatherChanges.Index](./weatherchanges/endindex.md)
  The end index for the weather changes.
- [var metadata: WeatherMetadata](./weatherchanges/metadata.md)
  Descriptive information about the weather change data.
- [var startIndex: WeatherChanges.Index](./weatherchanges/startindex.md)
  The start index for the weather changes.
### Subscripts
- [subscript(WeatherChanges.Index) -> WeatherChanges.Element](./weatherchanges/subscript%28_%29.md)
  The weather change at the provided index.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherchanges)*