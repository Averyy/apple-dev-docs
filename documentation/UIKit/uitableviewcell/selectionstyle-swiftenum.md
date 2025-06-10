# UITableViewCell.SelectionStyle

**Framework**: UIKit  
**Kind**: enum

The style of selected cells.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum SelectionStyle
```

#### Overview

You use these constants to set the value of the [`selectionStyle`](uitableviewcell/selectionstyle-swift.property.md) property.

## Topics

### Constants
- [UITableViewCell.SelectionStyle.none](uitableviewcell/selectionstyle-swift.enum/none.md)
  The cell has no distinct style for when it’s selected.
- [UITableViewCell.SelectionStyle.blue](uitableviewcell/selectionstyle-swift.enum/blue.md)
  The cell has a default background color when it’s selected.
- [UITableViewCell.SelectionStyle.gray](uitableviewcell/selectionstyle-swift.enum/gray.md)
  The cell has a gray background when it’s selected.
- [UITableViewCell.SelectionStyle.default](uitableviewcell/selectionstyle-swift.enum/default.md)
  The cell selection style to use for tables.
### Initializers
- [init?(rawValue: Int)](uitableviewcell/selectionstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var selectionStyle: UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.property.md)
  The style of selection for a cell.
- [var isSelected: Bool](uitableviewcell/isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](uitableviewcell/setselected(_:animated:).md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](uitableviewcell/ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](uitableviewcell/sethighlighted(_:animated:).md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/selectionstyle-swift.enum)*