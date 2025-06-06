# displaysSearchBarInNavigationBar

**Framework**: UIKit  
**Kind**: property

Specifies that the navigation bar contains a search bar.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var displaysSearchBarInNavigationBar: Bool { get set }
```

#### Discussion

When you return [`true`](https://developer.apple.com/documentation/swift/true) to display the search bar in a navigation bar, the system uses the search display controller’s [`navigationItem`](uisearchdisplaycontroller/navigationitem.md) property and ignores the navigation item, if set, of the [`searchContentsController`](uisearchdisplaycontroller/searchcontentscontroller.md) view controller. The displayed search field occupies as much width in the navigation bar as possible.

A search bar displayed in a navigation bar cannot have a scope bar.

> ❗ **Important**:  The system raises an exception if you set the [`showsScopeBar`](uisearchbar/showsscopebar.md) property to [`true`](https://developer.apple.com/documentation/swift/true) in a search bar that is displayed in a navigation bar.

 The system raises an exception if you set the [`showsScopeBar`](uisearchbar/showsscopebar.md) property to [`true`](https://developer.apple.com/documentation/swift/true) in a search bar that is displayed in a navigation bar.

## See Also

- [var delegate: (any UISearchDisplayDelegate)?](uisearchdisplaycontroller/delegate.md)
  The controller’s delegate.
- [var searchBar: UISearchBar](uisearchdisplaycontroller/searchbar.md)
  The search bar.
- [var searchContentsController: UIViewController](uisearchdisplaycontroller/searchcontentscontroller.md)
  The view controller that manages the contents being searched.
- [var searchResultsTableView: UITableView](uisearchdisplaycontroller/searchresultstableview.md)
  The table view in which the search results are displayed.
- [var searchResultsDataSource: (any UITableViewDataSource)?](uisearchdisplaycontroller/searchresultsdatasource.md)
  The data source for the table view in which the search results are displayed.
- [var searchResultsDelegate: (any UITableViewDelegate)?](uisearchdisplaycontroller/searchresultsdelegate.md)
  The delegate for the table view in which the search results are displayed.
- [var searchResultsTitle: String?](uisearchdisplaycontroller/searchresultstitle.md)
  The title for the search results view.
- [var navigationItem: UINavigationItem?](uisearchdisplaycontroller/navigationitem.md)
  Represents the search display controller in a navigation controller’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/displayssearchbarinnavigationbar)*