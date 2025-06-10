# init(tableView:cellProvider:)

**Framework**: UIKit  
**Kind**: init

Creates a diffable data source with the specified cell provider, and connects it to the specified table view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(tableView: UITableView, cellProvider: @escaping UITableViewDiffableDataSourceReferenceCellProvider)
```

## Parameters

- `tableView`: The initialized table view object to connect to the diffable data source.
- `cellProvider`: A closure that creates and returns each of the cells for the table view from the data the diffable data source provides.

## See Also

- [typealias UITableViewDiffableDataSourceReferenceCellProvider](uitableviewdiffabledatasourcereferencecellprovider.md)
  A closure that configures and returns a cell for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasourcereference/init(tableview:cellprovider:))*