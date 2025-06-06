# cellForRow(at:)

**Framework**: UIKit  
**Kind**: method

Returns the table cell at the index path you specify.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func cellForRow(at indexPath: IndexPath) -> UITableViewCell?
```

#### Return Value

The cell object at the corresponding index path. In versions of iOS earlier than iOS 15, this method returns `nil` if the cell isn’t visible or if `indexPath` is out of range. In iOS 15 and later, this method returns a non-`nil` cell if the table view retains a prepared cell at the specified index path, even if the cell isn’t currently visible.

#### Discussion

In iOS 15 and later, the table view retains a prepared cell in the following situations:

- Cells that the table view prefetches and retains in its cache of prepared cells, but that aren’t visible because the table view hasn’t displayed them yet.
- Cells that the table view finishes displaying and continues to retain in its cache of prepared cells because they remain near the visible region and might scroll back into view.
- The cell that contains the first responder.
- The cell that has focus.

## Parameters

- `indexPath`: The index path locating the row in the table view.

## See Also

- [func headerView(forSection: Int) -> UITableViewHeaderFooterView?](uitableview/headerview(forsection:).md)
  Returns the header view for the specified section.
- [func footerView(forSection: Int) -> UITableViewHeaderFooterView?](uitableview/footerview(forsection:).md)
  Returns the footer view for the specified section.
- [func indexPath(for: UITableViewCell) -> IndexPath?](uitableview/indexpath(for:).md)
  Returns an index path that represents the row and section of a specified table-view cell.
- [func indexPathForRow(at: CGPoint) -> IndexPath?](uitableview/indexpathforrow(at:).md)
  Returns an index path that identifies the row and section at the specified point.
- [func indexPathsForRows(in: CGRect) -> [IndexPath]?](uitableview/indexpathsforrows(in:).md)
  Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [var visibleCells: [UITableViewCell]](uitableview/visiblecells.md)
  The table cells that are visible in the table view.
- [var indexPathsForVisibleRows: [IndexPath]?](uitableview/indexpathsforvisiblerows.md)
  An array of index paths, each identifying a visible row in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/cellforrow(at:))*