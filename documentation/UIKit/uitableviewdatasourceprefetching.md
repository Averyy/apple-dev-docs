# UITableViewDataSourcePrefetching

**Framework**: UIKit  
**Kind**: protocol

A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITableViewDataSourcePrefetching : NSObjectProtocol
```

## Mentions

- [Filling a table with data](filling-a-table-with-data.md)

#### Overview

You use a prefetch data source object in conjunction with your table view’s data source to begin loading data for cells before the [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md) data source method is called. The following steps are required to support a prefetch data source to your table view:

- Create the table view and its regular data source.
- Create an object that adopts the [`UITableViewDataSourcePrefetching`](uitableviewdatasourceprefetching.md) protocol, and assign it to the [`prefetchDataSource`](uitableview/prefetchdatasource.md) property on the table view.
- Initiate asynchronous loading of the data required for the cells at the specified index paths in your implementation of [`tableView(_:prefetchRowsAt:)`](uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:).md).
- Prepare the cell for display using the prefetched data in your [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md) data source method.
- Cancel pending data load operations when the table view informs you that the data is no longer required in the [`tableView(_:cancelPrefetchingForRowsAt:)`](uitableviewdatasourceprefetching/tableview(_:cancelprefetchingforrowsat:).md) method.

> **Note**:  The prefetch method isn’t necessarily called for every cell in the table view. For details about a suggested approach to loading data, see [`Load data asynchronously`](uitableviewdatasourceprefetching#Load-data-asynchronously.md).

 The prefetch method isn’t necessarily called for every cell in the table view. For details about a suggested approach to loading data, see [`Load data asynchronously`](uitableviewdatasourceprefetching#Load-data-asynchronously.md).

When configuring the table view object, assign your prefetch data source to its [`prefetchDataSource`](uitableview/prefetchdatasource.md) property. For more information about how a table view works, see [`UITableView`](uitableview.md).

##### Load Data Asynchronously

The [`tableView(_:prefetchRowsAt:)`](uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:).md) method isn’t necessarily called for every cell in the table view. Your implementation of [`tableView(_:cellForRowAt:)`](uitableviewdatasource/tableview(_:cellforrowat:).md) must therefore be able to cope with the following potential situations:

- Data has been loaded via the prefetch request, and is ready to be displayed.
- Data is currently being prefetched, but isn’t yet available.
- Data hasn’t yet been requested.

One approach that handles all of these situations is to use [`Operation`](https://developer.apple.com/documentation/Foundation/Operation) to load the data for each row. You create the [`Operation`](https://developer.apple.com/documentation/Foundation/Operation) object and store it in the prefetch method. The data source method can then either retrieve the operation and the result, or create it if it doesn’t exist. For further information about how you can use asynchronous programming models to achieve this desired behavior, see [`Concurrency Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## Topics

### Fetching the row data
- [func tableView(UITableView, prefetchRowsAt: [IndexPath])](uitableviewdatasourceprefetching/tableview(_:prefetchrowsat:).md)
  Instructs your prefetch data source object to begin preparing data for the cells at the supplied index paths.
- [func tableView(UITableView, cancelPrefetchingForRowsAt: [IndexPath])](uitableviewdatasourceprefetching/tableview(_:cancelprefetchingforrowsat:).md)
  Cancels a previously triggered data prefetch request.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Filling a table with data](filling-a-table-with-data.md)
  Create and configure cells for your table dynamically using a data source object, or provide them statically from your storyboard.
- [Asynchronously loading images into table and collection views](asynchronously-loading-images-into-table-and-collection-views.md)
  Store and fetch images asynchronously to make your app more responsive.
- [protocol UITableViewDataSource](uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [class UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md)
  The object you use to manage data and provide cells for a table view.
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.
- [class UILocalizedIndexedCollation](uilocalizedindexedcollation.md)
  An object that organizes, sorts, and localizes the data for a table view that has a section index.
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdatasourceprefetching)*