# UITableViewCell.CellStyle

**Framework**: UIKit  
**Kind**: enum

An enumeration for the various styles of cells.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum CellStyle
```

#### Overview

In all these cell styles, the larger of the text labels is accessed using the [`textLabel`](uitableviewcell/textlabel.md) property and the smaller using the [`detailTextLabel`](uitableviewcell/detailtextlabel.md) property.

## Topics

### Cell styles
- [UITableViewCell.CellStyle.default](uitableviewcell/cellstyle/default.md)
  A simple style for a cell with a text label (black and left-aligned) and an optional image view.
- [UITableViewCell.CellStyle.value1](uitableviewcell/cellstyle/value1.md)
  A style for a cell with a label on the left side of the cell with left-aligned and black text; on the right side is a label that has smaller blue text and is right-aligned.
- [UITableViewCell.CellStyle.value2](uitableviewcell/cellstyle/value2.md)
  A style for a cell with a label on the left side of the cell with text that’s right-aligned and blue; on the right side of the cell is another label with smaller text that’s left-aligned and black.
- [UITableViewCell.CellStyle.subtitle](uitableviewcell/cellstyle/subtitle.md)
  A style for a cell with a left-aligned label across the top and a left-aligned label below it in smaller gray text.
### Initializers
- [init?(rawValue: Int)](uitableviewcell/cellstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](uitableviewcell/init(style:reuseidentifier:).md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
- [init?(coder: NSCoder)](uitableviewcell/init(coder:).md)
  Creates a table view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/cellstyle)*