# UITableViewCell.CellStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration for the various styles of cells.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum CellStyle
```

```c
enum UITableViewCellStyle : NSInteger;
```

#### Overview

In all these cell styles, the larger of the text labels is accessed using the [`textLabel`](./textlabel.md) property and the smaller using the [`detailTextLabel`](./detailtextlabel.md) property.

## Topics

### Cell styles
- [UITableViewCell.CellStyle.default](./cellstyle/default.md)
  A simple style for a cell with a text label (black and left-aligned) and an optional image view.
- [UITableViewCell.CellStyle.value1](./cellstyle/value1.md)
  A style for a cell with a label on the left side of the cell with left-aligned and black text; on the right side is a label that has smaller blue text and is right-aligned.
- [UITableViewCell.CellStyle.value2](./cellstyle/value2.md)
  A style for a cell with a label on the left side of the cell with text that’s right-aligned and blue; on the right side of the cell is another label with smaller text that’s left-aligned and black.
- [UITableViewCell.CellStyle.subtitle](./cellstyle/subtitle.md)
  A style for a cell with a left-aligned label across the top and a left-aligned label below it in smaller gray text.
### Initializers
- [init?(rawValue: Int)](./cellstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a table view cell
- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](./init%28style,reuseidentifier%29.md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a table view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/cellstyle)*