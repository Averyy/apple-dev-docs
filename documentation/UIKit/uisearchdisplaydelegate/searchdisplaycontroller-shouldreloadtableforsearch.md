# searchDisplayController(_:shouldReloadTableForSearch:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the table view should be reloaded for a given search string.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearch searchString: String?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the display controller should reload the data in its table view, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If you don’t implement this method, then the results table is reloaded as soon as the search string changes.

You might implement this method if you want to perform an asynchronous search. You would initiate the search in this method, then return [`false`](https://developer.apple.com/documentation/swift/false). You would reload the table when you have results.

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.
- `searchString`: The string in the search bar.

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
- [func searchDisplayController(UISearchDisplayController, willUnloadSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willunloadsearchresultstableview:).md)
  Tells the delegate that the controller is about to unload its table view.
- [func searchDisplayController(UISearchDisplayController, willShowSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willshowsearchresultstableview:).md)
  Tells the delegate that the controller is about to display its table view.
- [func searchDisplayController(UISearchDisplayController, didShowSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didshowsearchresultstableview:).md)
  Tells the delegate that the controller just displayed its table view.
- [func searchDisplayController(UISearchDisplayController, willHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willhidesearchresultstableview:).md)
  Tells the delegate that the controller is about to hide its table view.
- [func searchDisplayController(UISearchDisplayController, didHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didhidesearchresultstableview:).md)
  Tells the delegate that the controller just hid its table view.
- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearchScope: Int) -> Bool](uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:).md)
  Asks the delegate if the table view should be reloaded for a given scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearch:))*