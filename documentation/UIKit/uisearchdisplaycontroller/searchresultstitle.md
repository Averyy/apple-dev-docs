# searchResultsTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The title for the search results view.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var searchResultsTitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * searchResultsTitle;
```

## Discussion

The default value is `nil`.

If the value is `nil`, the controller uses the default title string.

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
- [var displaysSearchBarInNavigationBar: Bool](./displayssearchbarinnavigationbar.md)
  Specifies that the navigation bar contains a search bar.
- [var navigationItem: UINavigationItem?](./navigationitem.md)
  Represents the search display controller in a navigation controller’s navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaycontroller/searchresultstitle)*