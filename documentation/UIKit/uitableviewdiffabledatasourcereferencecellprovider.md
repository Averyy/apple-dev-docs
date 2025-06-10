# UITableViewDiffableDataSourceReferenceCellProvider

**Framework**: UIKit  
**Kind**: typealias

A closure that configures and returns a cell for a table view from its diffable data source.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias UITableViewDiffableDataSourceReferenceCellProvider = (UITableView, IndexPath, Any) -> UITableViewCell?
```

#### Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the table view.

## Parameters

- `tableView`: The table view to configure this cell for.
- `indexPath`: The index path that specifies the location of the cell in the table view.
- `itemIdentifier`: The identifier of the item for this cell.

## See Also

- [init(tableView: UITableView, cellProvider: UITableViewDiffableDataSourceReferenceCellProvider)](uitableviewdiffabledatasourcereference/init(tableview:cellprovider:).md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereferencecellprovider)*