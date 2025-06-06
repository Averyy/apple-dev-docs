# searchResultsDataSource

**Framework**: UIKit  
**Kind**: property

The data source for the table view in which the search results are displayed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var searchResultsDataSource: (any UITableViewDataSource)? { get set }
```

#### Discussion

The default is `nil`.

## See Also

- [var delegate: (any UISearchDisplayDelegate)?](uisearchdisplaycontroller/delegate.md)
  The controller’s delegate.
- [var searchBar: UISearchBar](uisearchdisplaycontroller/searchbar.md)
  The search bar.
- [var searchContentsController: UIViewController](uisearchdisplaycontroller/searchcontentscontroller.md)
  The view controller that manages the contents being searched.
- [var searchResultsTableView: UITableView](uisearchdisplaycontroller/searchresultstableview.md)
  The table view in which the search results are displayed.
- [var searchResultsDelegate: (any UITableViewDelegate)?](uisearchdisplaycontroller/searchresultsdelegate.md)
  The delegate for the table view in which the search results are displayed.
- [var searchResultsTitle: String?](uisearchdisplaycontroller/searchresultstitle.md)
  The title for the search results view.
- [var displaysSearchBarInNavigationBar: Bool](uisearchdisplaycontroller/displayssearchbarinnavigationbar.md)
  Specifies that the navigation bar contains a search bar.
- [var navigationItem: UINavigationItem?](uisearchdisplaycontroller/navigationitem.md)
  Represents the search display controller in a navigation controller’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/searchresultsdatasource)*