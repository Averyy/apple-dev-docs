# UITableViewDiffableDataSource.CellProvider

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that configures and returns a cell for a table view from its diffable data source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
typealias CellProvider = (UITableView, IndexPath, ItemIdentifierType) -> UITableViewCell?
```

## Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the table view.

## Parameters

- `tableView`: The table view to configure this cell for.
- `indexPath`: The index path that specifies the location of the cell in the table view.
- `itemIdentifier`: The identifier of the item for this cell.

## See Also

### Creating a diffable data source
- [init(tableView: UITableView, cellProvider: UITableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)](./init%28tableview,cellprovider%29.md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/cellprovider)*