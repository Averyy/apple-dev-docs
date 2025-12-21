# UITableViewDiffableDataSource

**Framework**: UIKit  
**Kind**: class

The object you use to manage data and provide cells for a table view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class UITableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

#### Overview

A  object is a specialized type of data source that works together with your table view object. It provides the behavior you need to manage updates to your table view’s data and UI in a simple, efficient way. It also conforms to the [`UITableViewDataSource`](uitableviewdatasource.md) protocol and provides implementations for all of the protocol’s methods.

To fill a table view with data:

1. Connect a diffable data source to your table view.
2. Implement a cell provider to configure your table view’s cells.
3. Generate the current state of the data.
4. Display the data in the UI.

To connect a diffable data source to a table view, you create the diffable data source using its [`init(tableView:cellProvider:)`](uitableviewdiffabledatasource-2euir/init(tableview:cellprovider:).md) initializer, passing in the table view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

```swift
dataSource = UITableViewDiffableDataSource<Int, UUID>(tableView: tableView) {
    (tableView: UITableView, indexPath: IndexPath, itemIdentifier: UUID) -> UITableViewCell? in
    // configure and return cell
}
```

Then, you generate the current state of the data and display the data in the UI by constructing and applying a snapshot. For more information, see [`NSDiffableDataSourceSnapshot`](nsdiffabledatasourcesnapshot-swift.struct.md).

> ❗ **Important**:  Do not change the [`dataSource`](uitableview/datasource.md) on the table view after you configure it with a diffable data source. If the table view needs a new data source after you configure it initially, create and configure a new table view and diffable data source.

## Topics

### Creating a diffable data source
- [init(tableView: UITableView, cellProvider: UITableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)](uitableviewdiffabledatasource-2euir/init(tableview:cellprovider:).md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified table view.
- [UITableViewDiffableDataSource.CellProvider](uitableviewdiffabledatasource-2euir/cellprovider.md)
  A closure that configures and returns a cell for a table view from its diffable data source.
### Identifying items
- [func itemIdentifier(for: IndexPath) -> ItemIdentifierType?](uitableviewdiffabledatasource-2euir/itemidentifier(for:).md)
  Returns an identifier for the item at the specified index path in the table view.
- [func indexPath(for: ItemIdentifierType) -> IndexPath?](uitableviewdiffabledatasource-2euir/indexpath(for:).md)
  Returns an index path for the item with the specified identifier in the table view.
### Identifying sections
- [func sectionIdentifier(for: Int) -> SectionIdentifierType?](uitableviewdiffabledatasource-2euir/sectionidentifier(for:).md)
  Returns an identifier for the section at the index you specify in the table view.
- [func index(for: SectionIdentifierType) -> Int?](uitableviewdiffabledatasource-2euir/index(for:).md)
  Returns an index for the section with the identifier you specify in the table view.
### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](uitableviewdiffabledatasource-2euir/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool) async](uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>) async](uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, completion: (() -> Void)?)](uitableviewdiffabledatasource-2euir/applysnapshotusingreloaddata(_:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
- [var defaultRowAnimation: UITableView.RowAnimation](uitableviewdiffabledatasource-2euir/defaultrowanimation.md)
  The default type of animation to use when inserting or deleting rows.
### Supporting bridging
- [class UITableViewDiffableDataSourceReference](uitableviewdiffabledatasourcereference.md)
  The object you use to manage data and provide cells for a table view.
### Debugging a diffable data source
- [func description() -> String](uitableviewdiffabledatasource-2euir/description.md)
  Returns a string with a description of the diffable data source.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UITableViewDataSource](uitableviewdatasource.md)

## See Also

- [Filling a table with data](filling-a-table-with-data.md)
  Create and configure cells for your table dynamically using a data source object, or provide them statically from your storyboard.
- [Asynchronously loading images into table and collection views](asynchronously-loading-images-into-table-and-collection-views.md)
  Store and fetch images asynchronously to make your app more responsive.
- [protocol UITableViewDataSource](uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.
- [class UILocalizedIndexedCollation](uilocalizedindexedcollation.md)
  An object that organizes, sorts, and localizes the data for a table view that has a section index.
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir)*