# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The controller’s delegate.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UISearchDisplayController`](../uisearchdisplaycontroller.md).

## Declaration

```swift
unowned(unsafe) var delegate: (any UISearchDisplayDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<UISearchDisplayDelegate> delegate;
```

## See Also

### Configuring a search bar
- [var searchBar: UISearchBar](./searchbar.md)
  The search bar.
- [var searchContentsController: UIViewController](./searchcontentscontroller.md)
  The view controller that manages the contents being searched.
- [var searchResultsTableView: UITableView](./searchresultstableview.md)
  The table view in which the search results are displayed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/delegate)*