# DocumentObservation.Container.List

**Framework**: Vision  
**Kind**: struct

A structure that represents a list of items within a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct List
```

## Topics

### Accessing a list
- [DocumentObservation.Container.List.Item](documentobservation/container/list/item.md)
  A single element of a list.
### Inspecting a list
- [var boundingRegion: NormalizedRegion](documentobservation/container/list/boundingregion.md)
  A polygon that defines the boundary of the list.
- [var items: [DocumentObservation.Container.List.Item]](documentobservation/container/list/items.md)
  The elements of the list.
- [DocumentObservation.Container.List.Marker](documentobservation/container/list/marker.md)
  The symbol or character at the beginning of each list item.

## Relationships

### Conforms To
- [BoundingRegionProviding](boundingregionproviding.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DocumentObservation.Container.Table](documentobservation/container/table.md)
  A structure that represents a table within a document.
- [DocumentObservation.Container.Text](documentobservation/container/text-swift.struct.md)
  A structure that represents a region of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/list)*