# UITableView.ScrollPosition

**Framework**: UIKit  
**Kind**: enum

The position in the table view (top, middle, bottom) to scroll a specified row to.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum ScrollPosition
```

#### Overview

You set the scroll position through a parameter of the [`selectRow(at:animated:scrollPosition:)`](uitableview/selectrow(at:animated:scrollposition:).md), [`scrollToNearestSelectedRow(at:animated:)`](uitableview/scrolltonearestselectedrow(at:animated:).md), [`cellForRow(at:)`](uitableview/cellforrow(at:).md), and [`indexPathForSelectedRow`](uitableview/indexpathforselectedrow.md) methods.

## Topics

### Constants
- [UITableView.ScrollPosition.none](uitableview/scrollposition/none.md)
  The table view scrolls the row of interest to be fully visible with a minimum of movement.
- [UITableView.ScrollPosition.top](uitableview/scrollposition/top.md)
  The table view scrolls the row of interest to the top of the visible table view.
- [UITableView.ScrollPosition.middle](uitableview/scrollposition/middle.md)
  The table view scrolls the row of interest to the middle of the visible table view.
- [UITableView.ScrollPosition.bottom](uitableview/scrollposition/bottom.md)
  The table view scrolls the row of interest to the bottom of the visible table view.
### Initializers
- [init?(rawValue: Int)](uitableview/scrollposition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func scrollToRow(at: IndexPath, at: UITableView.ScrollPosition, animated: Bool)](uitableview/scrolltorow(at:at:animated:).md)
  Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.
- [func scrollToNearestSelectedRow(at: UITableView.ScrollPosition, animated: Bool)](uitableview/scrolltonearestselectedrow(at:animated:).md)
  Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/scrollposition)*