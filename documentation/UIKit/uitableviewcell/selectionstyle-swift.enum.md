# UITableViewCell.SelectionStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The style of selected cells.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum SelectionStyle
```

```c
enum UITableViewCellSelectionStyle : NSInteger;
```

## Overview

You use these constants to set the value of the [`selectionStyle`](./selectionstyle-swift.property.md) property.

## Topics

### Constants
- [UITableViewCell.SelectionStyle.none](./selectionstyle-swift.enum/none.md)
  The cell has no distinct style for when it’s selected.
- [UITableViewCell.SelectionStyle.blue](./selectionstyle-swift.enum/blue.md)
  The cell has a default background color when it’s selected.
- [UITableViewCell.SelectionStyle.gray](./selectionstyle-swift.enum/gray.md)
  The cell has a gray background when it’s selected.
- [UITableViewCell.SelectionStyle.default](./selectionstyle-swift.enum/default.md)
  The cell selection style to use for tables.
### Initializers
- [init?(rawValue: Int)](./selectionstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing cell selection and highlighting
- [var selectionStyle: UITableViewCell.SelectionStyle](./selectionstyle-swift.property.md)
  The style of selection for a cell.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](./setselected%28_,animated%29.md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](./sethighlighted%28_,animated%29.md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/selectionstyle-swift.enum)*