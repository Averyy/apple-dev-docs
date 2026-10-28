# UITableView.ScrollPosition.none

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The table view scrolls the row of interest to be fully visible with a minimum of movement.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
case none
```

```c
UITableViewScrollPositionNone
```

## Discussion

If the row is already fully visible, no scrolling occurs. For example, if the row is above the visible area, the behavior is identical to that specified by [`UITableView.ScrollPosition.top`](./top.md). This is the default.

## See Also

### Constants
- [UITableView.ScrollPosition.top](./top.md)
  The table view scrolls the row of interest to the top of the visible table view.
- [UITableView.ScrollPosition.middle](./middle.md)
  The table view scrolls the row of interest to the middle of the visible table view.
- [UITableView.ScrollPosition.bottom](./bottom.md)
  The table view scrolls the row of interest to the bottom of the visible table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/scrollposition/none)*