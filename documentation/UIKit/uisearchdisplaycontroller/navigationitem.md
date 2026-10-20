# navigationItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Represents the search display controller in a navigation controller’s navigation bar.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var navigationItem: UINavigationItem? { get }
```

```objc
@property (nonatomic, readonly, nullable) UINavigationItem * navigationItem;
```

#### Discussion

You can configure the navigation item as described in the [`UINavigationItem`](../uinavigationitem.md), with the exception of configuring the title view.

> ❗ **Important**:  The system raises an exception if you attempt to set the [`titleView`](../uinavigationitem/titleview.md) property for a search display controller’s navigation item.

## See Also

### Configuring a search bar
- [var delegate: (any UISearchDisplayDelegate)?](./delegate.md)
  The controller’s delegate.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/navigationitem)*