# UITableView.ScrollPosition.none

**Framework**: UIKit  
**Kind**: case

The table view scrolls the row of interest to be fully visible with a minimum of movement.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case none
```

#### Discussion

If the row is already fully visible, no scrolling occurs. For example, if the row is above the visible area, the behavior is identical to that specified by [`UITableView.ScrollPosition.top`](uitableview/scrollposition/top.md). This is the default.

## See Also

- [UITableView.ScrollPosition.top](uitableview/scrollposition/top.md)
  The table view scrolls the row of interest to the top of the visible table view.
- [UITableView.ScrollPosition.middle](uitableview/scrollposition/middle.md)
  The table view scrolls the row of interest to the middle of the visible table view.
- [UITableView.ScrollPosition.bottom](uitableview/scrollposition/bottom.md)
  The table view scrolls the row of interest to the bottom of the visible table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/scrollposition/none)*