# scrollToNearestSelectedRow(at:animated:)

**Framework**: UIKit  
**Kind**: method

Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func scrollToNearestSelectedRow(at scrollPosition: UITableView.ScrollPosition, animated: Bool)
```

## Parameters

- `scrollPosition`: A constant that identifies a relative position in the table view (top, middle, bottom) for the row when scrolling concludes. See   for a descriptions of valid constants.
- `animated`:   if you want to animate the change in position;   if it should be immediate.

## See Also

- [func scrollToRow(at: IndexPath, at: UITableView.ScrollPosition, animated: Bool)](uitableview/scrolltorow(at:at:animated:).md)
  Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.
- [UITableView.ScrollPosition](uitableview/scrollposition.md)
  The position in the table view (top, middle, bottom) to scroll a specified row to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/scrolltonearestselectedrow(at:animated:))*