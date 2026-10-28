# isSelected

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cell is selected.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isSelected: Bool { get set }
```

```objc
@property (nonatomic, getter=isSelected) BOOL selected;
```

## Discussion

The selection affects the appearance of labels, image, and background. When the selected state of a cell is set to [`true`](../../Swift/true.md), it draws the background for selected cells with its title in white. The default value is [`false`](../../Swift/false.md). If you set the selection state to [`true`](../../Swift/true.md) through this property, the transition to the new state appearance is not animated. For animated selected-state transitions, see the [`setSelected(_:animated:)`](./setselected%28_,animated%29.md) method.

## See Also

### Managing cell selection and highlighting
- [var selectionStyle: UITableViewCell.SelectionStyle](./selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](./selectionstyle-swift.enum.md)
  The style of selected cells.
- [func setSelected(Bool, animated: Bool)](./setselected%28_,animated%29.md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](./sethighlighted%28_,animated%29.md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/isselected)*