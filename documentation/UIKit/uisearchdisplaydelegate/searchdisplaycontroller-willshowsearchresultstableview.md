# searchDisplayController(_:willShowSearchResultsTableView:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the controller is about to display its table view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func searchDisplayController(_ controller: UISearchDisplayController, willShowSearchResultsTableView tableView: UITableView)
```

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.
- `tableView`: The search display controller’s table view.

## See Also

- [func searchDisplayController(UISearchDisplayController, didShowSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didshowsearchresultstableview:).md)
  Tells the delegate that the controller just displayed its table view.
- [func searchDisplayController(UISearchDisplayController, willHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:willhidesearchresultstableview:).md)
  Tells the delegate that the controller is about to hide its table view.
- [func searchDisplayController(UISearchDisplayController, didHideSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didhidesearchresultstableview:).md)
  Tells the delegate that the controller just hid its table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willshowsearchresultstableview:))*