# DocumentObservation.Container.List

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A structure that represents a list of items within a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct List
```

## Topics

### Accessing a list
- [DocumentObservation.Container.List.Item](./list/item.md)
  A single element of a list.
### Inspecting a list
- [var boundingRegion: NormalizedRegion](./list/boundingregion.md)
  A polygon that defines the boundary of the list.
- [var items: [DocumentObservation.Container.List.Item]](./list/items.md)
  The elements of the list.
- [DocumentObservation.Container.List.Marker](./list/marker.md)
  The symbol or character at the beginning of each list item.

## Relationships

### Conforms To
- [BoundingRegionProviding](../../boundingregionproviding.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the sections in a document
- [DocumentObservation.Container.Table](./table.md)
  A structure that represents a table within a document.
- [DocumentObservation.Container.Text](./text-swift.struct.md)
  A structure that represents a region of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/list)*