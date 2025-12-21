# isSelected

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the cell is selected.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isSelected: Bool { get set }
```

#### Discussion

The selection affects the appearance of labels, image, and background. When the selected state of a cell is set to [`true`](https://developer.apple.com/documentation/Swift/true), it draws the background for selected cells with its title in white. The default value is [`false`](https://developer.apple.com/documentation/Swift/false). If you set the selection state to [`true`](https://developer.apple.com/documentation/Swift/true) through this property, the transition to the new state appearance is not animated. For animated selected-state transitions, see the [`setSelected(_:animated:)`](uitableviewcell/setselected(_:animated:).md) method.

## See Also

- [var selectionStyle: UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.enum.md)
  The style of selected cells.
- [func setSelected(Bool, animated: Bool)](uitableviewcell/setselected(_:animated:).md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](uitableviewcell/ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](uitableviewcell/sethighlighted(_:animated:).md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/isselected)*