# isHighlighted

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the cell is highlighted.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isHighlighted: Bool { get set }
```

#### Discussion

The highlighting affects the appearance of labels, image, and background. When the highlighted state of a cell is set to [`true`](https://developer.apple.com/documentation/swift/true), labels are drawn in their highlighted text color (default is white). The default value is [`false`](https://developer.apple.com/documentation/swift/false). If you set the highlighted state to [`true`](https://developer.apple.com/documentation/swift/true) through this property, the transition to the new state appearance is not animated. For animated highlighted-state transitions, see the [`setHighlighted(_:animated:)`](uitableviewcell/sethighlighted(_:animated:).md) method.

Note that for highlighting to work properly, you must fetch the cell’s labels using the [`textLabel`](uitableviewcell/textlabel.md) and [`detailTextLabel`](uitableviewcell/detailtextlabel.md) properties and set each label’s [`highlightedTextColor`](uilabel/highlightedtextcolor.md) property; for images, get the cell’s image using the [`imageView`](uitableviewcell/imageview.md) property and set the [`UIImageView`](uiimageview.md) object’s `highlightedImage` property.

## See Also

- [var selectionStyle: UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](uitableviewcell/isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](uitableviewcell/setselected(_:animated:).md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [func setHighlighted(Bool, animated: Bool)](uitableviewcell/sethighlighted(_:animated:).md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/ishighlighted)*