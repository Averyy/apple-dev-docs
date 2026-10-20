# UITableView.ScrollPosition

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The position in the table view (top, middle, bottom) to scroll a specified row to.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum ScrollPosition
```

```c
enum UITableViewScrollPosition : NSInteger;
```

#### Overview

You set the scroll position through a parameter of the [`selectRow(at:animated:scrollPosition:)`](./selectrow%28at,animated,scrollposition%29.md), [`scrollToNearestSelectedRow(at:animated:)`](./scrolltonearestselectedrow%28at,animated%29.md), [`cellForRow(at:)`](./cellforrow%28at%29.md), and [`indexPathForSelectedRow`](./indexpathforselectedrow.md) methods.

## Topics

### Constants
- [UITableView.ScrollPosition.none](./scrollposition/none.md)
  The table view scrolls the row of interest to be fully visible with a minimum of movement.
- [UITableView.ScrollPosition.top](./scrollposition/top.md)
  The table view scrolls the row of interest to the top of the visible table view.
- [UITableView.ScrollPosition.middle](./scrollposition/middle.md)
  The table view scrolls the row of interest to the middle of the visible table view.
- [UITableView.ScrollPosition.bottom](./scrollposition/bottom.md)
  The table view scrolls the row of interest to the bottom of the visible table view.
### Initializers
- [init?(rawValue: Int)](./scrollposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Scrolling the table view
- [func scrollToRow(at: IndexPath, at: UITableView.ScrollPosition, animated: Bool)](./scrolltorow%28at,at,animated%29.md)
  Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.
- [func scrollToNearestSelectedRow(at: UITableView.ScrollPosition, animated: Bool)](./scrolltonearestselectedrow%28at,animated%29.md)
  Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/scrollposition)*