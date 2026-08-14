# setSelected(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the selected state of the cell, optionally animating the transition between states.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setSelected(_ selected: Bool, animated: Bool)
```

#### Discussion

The selection affects the appearance of labels, image, and background. When the selected state of a cell is [`true`](https://developer.apple.com/documentation/swift/true), it draws the background for selected cells (Reusing cells) with its title in white.

## Parameters

- `selected`: [`true`](https://developer.apple.com/documentation/swift/true) to set the cell as selected, [`false`](https://developer.apple.com/documentation/swift/false) to set it as unselected. The default is [`false`](https://developer.apple.com/documentation/swift/false).
- `animated`: [`true`](https://developer.apple.com/documentation/swift/true) to animate the transition between selected states, [`false`](https://developer.apple.com/documentation/swift/false) to make the transition immediate.

## See Also

- [var selectionStyle: UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](uitableviewcell/isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [var isHighlighted: Bool](uitableviewcell/ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](uitableviewcell/sethighlighted(_:animated:).md)
  Sets the highlighted state of the cell, optionally animating the transition between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/setselected(_:animated:))*