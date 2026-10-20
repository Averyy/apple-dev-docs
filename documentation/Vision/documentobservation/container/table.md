# DocumentObservation.Container.Table

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

A structure that represents a table within a document.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Table
```

## Topics

### Accessing a table
- [DocumentObservation.Container.Table.Cell](./table/cell.md)
  A structure that represents a table cell.
### Inspecting a table
- [var boundingRegion: NormalizedRegion](./table/boundingregion.md)
  A polygon that defines the boundary of the table.
- [var columns: [[DocumentObservation.Container.Table.Cell]]](./table/columns.md)
  The columns in a table.
- [var rows: [[DocumentObservation.Container.Table.Cell]]](./table/rows.md)
  The rows in a table.
### Getting the cell
- [func cell(row: Int, col: Int) -> DocumentObservation.Container.Table.Cell?](./table/cell%28row,col%29.md)
  The cell at the specific row and column index, if it exists.

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
- [DocumentObservation.Container.List](./list.md)
  A structure that represents a list of items within a document.
- [DocumentObservation.Container.Text](./text-swift.struct.md)
  A structure that represents a region of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/table)*