# DocumentObservation.Container.Table

**Framework**: Vision  
**Kind**: struct

A structure that represents a table within a document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Table
```

## Topics

### Accessing a table
- [DocumentObservation.Container.Table.Cell](documentobservation/container/table/cell.md)
  A structure that represents a table cell.
### Inspecting a table
- [var boundingRegion: NormalizedRegion](documentobservation/container/table/boundingregion.md)
  A polygon that defines the boundary of the table.
- [var columns: [[DocumentObservation.Container.Table.Cell]]](documentobservation/container/table/columns.md)
  The columns in a table.
- [var rows: [[DocumentObservation.Container.Table.Cell]]](documentobservation/container/table/rows.md)
  The rows in a table.
### Getting the cell
- [func cell(row: Int, col: Int) -> DocumentObservation.Container.Table.Cell?](documentobservation/container/table/cell(row:col:).md)
  The cell at the specific row and column index, if it exists.

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

- [DocumentObservation.Container.List](documentobservation/container/list.md)
  A structure that represents a list of items within a document.
- [DocumentObservation.Container.Text](documentobservation/container/text-swift.struct.md)
  A structure that represents a region of text in a document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/container/table)*