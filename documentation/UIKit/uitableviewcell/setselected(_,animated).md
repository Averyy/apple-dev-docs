# setSelected(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the selected state of the cell, optionally animating the transition between states.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setSelected(_ selected: Bool, animated: Bool)
```

```objc
- (void) setSelected:(BOOL) selected animated:(BOOL) animated;
```

## Discussion

The selection affects the appearance of labels, image, and background. When the selected state of a cell is [`true`](../../Swift/true.md), it draws the background for selected cells (Reusing cells) with its title in white.

## Parameters

- `selected`: [`true`](../../Swift/true.md) to set the cell as selected, [`false`](../../Swift/false.md) to set it as unselected. The default is [`false`](../../Swift/false.md).
- `animated`: [`true`](../../Swift/true.md) to animate the transition between selected states, [`false`](../../Swift/false.md) to make the transition immediate.

## See Also

### Managing cell selection and highlighting
- [var selectionStyle: UITableViewCell.SelectionStyle](./selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](./selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](./sethighlighted%28_,animated%29.md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/setselected(_:animated:))*