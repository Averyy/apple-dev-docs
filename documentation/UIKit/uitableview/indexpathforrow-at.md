# indexPathForRow(at:)

**Framework**: UIKit  
**Kind**: method

Returns an index path that identifies the row and section at the specified point.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func indexPathForRow(at point: CGPoint) -> IndexPath?
```

#### Return Value

An index path representing the row and section associated with `point`, or `nil` if the point is out of the bounds of any row.

## Parameters

- `point`: A point in the local coordinate system of the table view (the table view’s bounds).

## See Also

- [func cellForRow(at: IndexPath) -> UITableViewCell?](uitableview/cellforrow(at:).md)
  Returns the table cell at the index path you specify.
- [func headerView(forSection: Int) -> UITableViewHeaderFooterView?](uitableview/headerview(forsection:).md)
  Returns the header view for the specified section.
- [func footerView(forSection: Int) -> UITableViewHeaderFooterView?](uitableview/footerview(forsection:).md)
  Returns the footer view for the specified section.
- [func indexPath(for: UITableViewCell) -> IndexPath?](uitableview/indexpath(for:).md)
  Returns an index path that represents the row and section of a specified table-view cell.
- [func indexPathsForRows(in: CGRect) -> [IndexPath]?](uitableview/indexpathsforrows(in:).md)
  Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [var visibleCells: [UITableViewCell]](uitableview/visiblecells.md)
  The table cells that are visible in the table view.
- [var indexPathsForVisibleRows: [IndexPath]?](uitableview/indexpathsforvisiblerows.md)
  An array of index paths, each identifying a visible row in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/indexpathforrow(at:))*