# headerView(forSection:)

**Framework**: UIKit  
**Kind**: method

Returns the header view for the specified section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func headerView(forSection section: Int) -> UITableViewHeaderFooterView?
```

#### Return Value

The header view associated with the section, or `nil` if the section does not have a header view.

## Parameters

- `section`: An index number that identifies a section of the table. Table views in a plain style have a section index of zero.

## See Also

- [func cellForRow(at: IndexPath) -> UITableViewCell?](uitableview/cellforrow(at:).md)
  Returns the table cell at the index path you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/headerview(forsection:))*