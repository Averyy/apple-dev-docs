# searchDisplayController(_:willUnloadSearchResultsTableView:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the controller is about to unload its table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, willUnloadSearchResultsTableView tableView: UITableView)
```

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.
- `tableView`: The search display controller’s table view.

## See Also

- [func searchDisplayControllerWillBeginSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerwillbeginsearch(_:).md)
  Tells the delegate that the controller is about to begin searching.
- [func searchDisplayControllerDidBeginSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerdidbeginsearch(_:).md)
  Tells the delegate that the controller has started searching.
- [func searchDisplayControllerWillEndSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerwillendsearch(_:).md)
  Tells the delegate that the controller is about to end searching.
- [func searchDisplayControllerDidEndSearch(UISearchDisplayController)](uisearchdisplaydelegate/searchdisplaycontrollerdidendsearch(_:).md)
  Tells the delegate that the controller has finished searching.
- [func searchDisplayController(UISearchDisplayController, didLoadSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didloadsearchresultstableview:).md)
  Tells the delegate that the controller has loaded its table view.
- [func searchDisplayController(UISearchDisplayController, willShowSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willshowsearchresultstableview:).md)
  Tells the delegate that the controller is about to display its table view.
- [func searchDisplayController(UISearchDisplayController, didShowSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didshowsearchresultstableview:).md)
  Tells the delegate that the controller just displayed its table view.
- [func searchDisplayController(UISearchDisplayController, willHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willhidesearchresultstableview:).md)
  Tells the delegate that the controller is about to hide its table view.
- [func searchDisplayController(UISearchDisplayController, didHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didhidesearchresultstableview:).md)
  Tells the delegate that the controller just hid its table view.
- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearch: String?) -> Bool](uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearch:).md)
  Asks the delegate if the table view should be reloaded for a given search string.
- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearchScope: Int) -> Bool](uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:).md)
  Asks the delegate if the table view should be reloaded for a given scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willunloadsearchresultstableview:))*