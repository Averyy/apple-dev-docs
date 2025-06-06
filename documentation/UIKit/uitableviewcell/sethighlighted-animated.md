# setHighlighted(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the highlighted state of the cell, optionally animating the transition between states.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setHighlighted(_ highlighted: Bool, animated: Bool)
```

#### Discussion

Highlights or unhighlights the cell, animating the transition between regular and highlighted state if `animated` is YES.  Highlighting affects the appearance of the cell’s labels, image, and background.

Note that for highlighting to work properly, you must fetch the cell’s label (or labels) using the [`textLabel`](uitableviewcell/textlabel.md) (and [`detailTextLabel`](uitableviewcell/detailtextlabel.md) properties and set the label’s [`highlightedTextColor`](uilabel/highlightedtextcolor.md) property; for images, get the cell’s image using the [`imageView`](uitableviewcell/imageview.md) property and set the [`UIImageView`](uiimageview.md) object’s `highlightedImage` property.

A custom table cell may override this method to make any transitory appearance changes.

## Parameters

- `highlighted`:   to set the cell as highlighted,   to set it as unhighlighted. The default is  .
- `animated`:   to animate the transition between highlighted states,   to make the transition immediate.

## See Also

- [var selectionStyle: UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](uitableviewcell/isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](uitableviewcell/setselected(_:animated:).md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](uitableviewcell/ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/sethighlighted(_:animated:))*