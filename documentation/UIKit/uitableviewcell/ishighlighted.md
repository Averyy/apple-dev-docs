# isHighlighted

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cell is highlighted.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isHighlighted: Bool { get set }
```

```objc
@property (nonatomic, getter=isHighlighted) BOOL highlighted;
```

## Discussion

The highlighting affects the appearance of labels, image, and background. When the highlighted state of a cell is set to [`true`](../../Swift/true.md), labels are drawn in their highlighted text color (default is white). The default value is [`false`](../../Swift/false.md). If you set the highlighted state to [`true`](../../Swift/true.md) through this property, the transition to the new state appearance is not animated. For animated highlighted-state transitions, see the [`setHighlighted(_:animated:)`](./sethighlighted%28_,animated%29.md) method.

Note that for highlighting to work properly, you must fetch the cell’s labels using the [`textLabel`](./textlabel.md) and [`detailTextLabel`](./detailtextlabel.md) properties and set each label’s [`highlightedTextColor`](../uilabel/highlightedtextcolor.md) property; for images, get the cell’s image using the [`imageView`](./imageview.md) property and set the [`UIImageView`](../uiimageview.md) object’s `highlightedImage` property.

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
- [func setHighlighted(Bool, animated: Bool)](./sethighlighted%28_,animated%29.md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/ishighlighted)*