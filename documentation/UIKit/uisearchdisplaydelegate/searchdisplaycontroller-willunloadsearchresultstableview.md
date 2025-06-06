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
@MainActor
optional func searchDisplayController(_ controller: UISearchDisplayController, willUnloadSearchResultsTableView tableView: UITableView)
```

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.
- `tableView`: The search display controller’s table view.

## See Also

- [func searchDisplayController(UISearchDisplayController, didLoadSearchResultsTableView: UITableView)](uisearchdisplaydelegate/searchdisplaycontroller(_:didloadsearchresultstableview:).md)
  Tells the delegate that the controller has loaded its table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:willunloadsearchresultstableview:))*