# prepareForReuse()

**Framework**: UIKit  
**Kind**: method

Prepares a reusable cell for reuse by the table view’s delegate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareForReuse()
```

## Mentions

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)

#### Discussion

If a [`UITableViewCell`](uitableviewcell.md) object has a reuse identifier, the table view invokes this method just before returning the object from the `UITableView` method [`dequeueReusableCell(withIdentifier:)`](uitableview/dequeuereusablecell(withidentifier:).md). To avoid potential performance issues, you should only reset attributes of the cell that are not related to content, for example, alpha, editing, and selection state. The table view’s delegate in [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md) should  reset all content when reusing a cell.

The table view doesn’t call this method if the cell object doesn’t have an associated reuse identifier, or if you use [`reconfigureRows(at:)`](uitableview/reconfigurerows(at:).md) to update the contents of an existing cell.

If you override this method, you must be sure to invoke the superclass implementation.

## See Also

- [var reuseIdentifier: String?](uitableviewcell/reuseidentifier.md)
  A string for identifying a reusable cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell/prepareforreuse())*