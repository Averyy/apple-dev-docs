# selectionStyle

**Framework**: UIKit  
**Kind**: property

The style of selection for a cell.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectionStyle: UITableViewCell.SelectionStyle { get set }
```

#### Discussion

The selection style is a [`backgroundView`](uitableviewcell/backgroundview.md) constant that determines the color of a cell when it’s selected. The default value is [`UITableViewCell.SelectionStyle.default`](uitableviewcell/selectionstyle-swift.enum/default.md). See [`UITableViewCell.SelectionStyle`](uitableviewcell/selectionstyle-swift.enum.md) for a description of valid constants.

## See Also

- [UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](uitableviewcell/isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](uitableviewcell/setselected(_:animated:).md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](uitableviewcell/ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](uitableviewcell/sethighlighted(_:animated:).md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/selectionstyle-swift.property)*