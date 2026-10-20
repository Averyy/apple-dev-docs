# searchResultsTableView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The table view in which the search results are displayed.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UISearchDisplayController`](../uisearchdisplaycontroller.md).

## Declaration

```swift
var searchResultsTableView: UITableView { get }
```

```objc
@property (nonatomic, readonly) UITableView * searchResultsTableView;
```

#### Discussion

This method creates a new table view if one does not already exist.

## See Also

### Configuring a search bar
- [var delegate: (any UISearchDisplayDelegate)?](./delegate.md)
  The controller’s delegate.
- [var searchBar: UISearchBar](./searchbar.md)
  The search bar.
- [var searchContentsController: UIViewController](./searchcontentscontroller.md)
  The view controller that manages the contents being searched.
- [var searchResultsDataSource: (any UITableViewDataSource)?](./searchresultsdatasource.md)
  The data source for the table view in which the search results are displayed.
- [var searchResultsDelegate: (any UITableViewDelegate)?](./searchresultsdelegate.md)
  The delegate for the table view in which the search results are displayed.
- [var searchResultsTitle: String?](./searchresultstitle.md)
  The title for the search results view.
- [var displaysSearchBarInNavigationBar: Bool](./displayssearchbarinnavigationbar.md)
  Specifies that the navigation bar contains a search bar.
- [var navigationItem: UINavigationItem?](./navigationitem.md)
  Represents the search display controller in a navigation controller’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/searchresultstableview)*