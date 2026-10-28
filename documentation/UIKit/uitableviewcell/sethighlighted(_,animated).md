# setHighlighted(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the highlighted state of the cell, optionally animating the transition between states.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setHighlighted(_ highlighted: Bool, animated: Bool)
```

```objc
- (void) setHighlighted:(BOOL) highlighted animated:(BOOL) animated;
```

## Discussion

Highlights or unhighlights the cell, animating the transition between regular and highlighted state if `animated` is YES.  Highlighting affects the appearance of the cell’s labels, image, and background.

Note that for highlighting to work properly, you must fetch the cell’s label (or labels) using the [`textLabel`](./textlabel.md) (and [`detailTextLabel`](./detailtextlabel.md) properties and set the label’s [`highlightedTextColor`](../uilabel/highlightedtextcolor.md) property; for images, get the cell’s image using the [`imageView`](./imageview.md) property and set the [`UIImageView`](../uiimageview.md) object’s `highlightedImage` property.

A custom table cell may override this method to make any transitory appearance changes.

## Parameters

- `highlighted`: [`true`](../../Swift/true.md) to set the cell as highlighted, [`false`](../../Swift/false.md) to set it as unhighlighted. The default is [`false`](../../Swift/false.md).
- `animated`: [`true`](../../Swift/true.md) to animate the transition between highlighted states, [`false`](../../Swift/false.md) to make the transition immediate.

## See Also

### Managing cell selection and highlighting
- [var selectionStyle: UITableViewCell.SelectionStyle](./selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](./selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](./setselected%28_,animated%29.md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/sethighlighted(_:animated:))*