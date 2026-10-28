# indexPathsForVisibleRows

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of index paths, each identifying a visible row in the table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var indexPathsForVisibleRows: [IndexPath]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSIndexPath *> * indexPathsForVisibleRows;
```

## Discussion

The value of this property is an array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects each representing a row index and section index that together identify a visible row in the table view. If no rows are visible, the value is `nil`.

## See Also

### Getting cells and section-based views
- [func cellForRow(at: IndexPath) -> UITableViewCell?](./cellforrow%28at%29.md)
  Returns the table cell at the index path you specify.
- [func headerView(forSection: Int) -> UITableViewHeaderFooterView?](./headerview%28forsection%29.md)
  Returns the header view for the specified section.
- [func footerView(forSection: Int) -> UITableViewHeaderFooterView?](./footerview%28forsection%29.md)
  Returns the footer view for the specified section.
- [func indexPath(for: UITableViewCell) -> IndexPath?](./indexpath%28for%29.md)
  Returns an index path that represents the row and section of a specified table-view cell.
- [func indexPathForRow(at: CGPoint) -> IndexPath?](./indexpathforrow%28at%29.md)
  Returns an index path that identifies the row and section at the specified point.
- [func indexPathsForRows(in: CGRect) -> [IndexPath]?](./indexpathsforrows%28in%29.md)
  Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [var visibleCells: [UITableViewCell]](./visiblecells.md)
  The table cells that are visible in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview/indexpathsforvisiblerows)*