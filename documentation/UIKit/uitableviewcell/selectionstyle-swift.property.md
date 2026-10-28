# selectionStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style of selection for a cell.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var selectionStyle: UITableViewCell.SelectionStyle { get set }
```

```objc
@property (nonatomic) UITableViewCellSelectionStyle selectionStyle;
```

## Discussion

The selection style is a [`backgroundView`](./backgroundview.md) constant that determines the color of a cell when it’s selected. The default value is [`UITableViewCell.SelectionStyle.default`](./selectionstyle-swift.enum/default.md). See [`UITableViewCell.SelectionStyle`](./selectionstyle-swift.enum.md) for a description of valid constants.

## See Also

### Managing cell selection and highlighting
- [UITableViewCell.SelectionStyle](./selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](./setselected%28_,animated%29.md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](./sethighlighted%28_,animated%29.md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/selectionstyle-swift.property)*