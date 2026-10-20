# displaysSearchBarInNavigationBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies that the navigation bar contains a search bar.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var displaysSearchBarInNavigationBar: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL displaysSearchBarInNavigationBar;
```

#### Discussion

When you return [`true`](../../Swift/true.md) to display the search bar in a navigation bar, the system uses the search display controller’s [`navigationItem`](./navigationitem.md) property and ignores the navigation item, if set, of the [`searchContentsController`](./searchcontentscontroller.md) view controller. The displayed search field occupies as much width in the navigation bar as possible.

A search bar displayed in a navigation bar cannot have a scope bar.

> ❗ **Important**:  The system raises an exception if you set the [`showsScopeBar`](../uisearchbar/showsscopebar.md) property to [`true`](../../Swift/true.md) in a search bar that is displayed in a navigation bar.

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
- [var navigationItem: UINavigationItem?](./navigationitem.md)
  Represents the search display controller in a navigation controller’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/displayssearchbarinnavigationbar)*