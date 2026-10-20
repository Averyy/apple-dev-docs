# searchDisplayController(_:shouldReloadTableForSearchScope:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the table view should be reloaded for a given scope.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchScope searchOption: Int) -> Bool
```

```objc
- (BOOL) searchDisplayController:(UISearchDisplayController *) controller shouldReloadTableForSearchScope:(NSInteger) searchOption;
```

#### Return Value

[`true`](../../Swift/true.md) if the display controller should reload the data in its table view, otherwise [`false`](../../Swift/false.md).

#### Discussion

If you don’t implement this method, then the results table is reloaded as soon as the scope button selection changes.

You might implement this method if you want to perform an asynchronous search: you would initiate the search in this method, then return [`false`](../../Swift/false.md), and reload the table when you have results.

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.
- `searchOption`: The index of the selected scope button in the search bar.

## See Also

### Related Documentation
- [var selectedScopeButtonIndex: Int](../uisearchbar/selectedscopebuttonindex.md)
  The index of the selected scope button.
### Deprecated methods
- [func searchDisplayControllerWillBeginSearch(UISearchDisplayController)](./searchdisplaycontrollerwillbeginsearch%28_%29.md)
  Tells the delegate that the controller is about to begin searching.
- [func searchDisplayControllerDidBeginSearch(UISearchDisplayController)](./searchdisplaycontrollerdidbeginsearch%28_%29.md)
  Tells the delegate that the controller has started searching.
- [func searchDisplayControllerWillEndSearch(UISearchDisplayController)](./searchdisplaycontrollerwillendsearch%28_%29.md)
  Tells the delegate that the controller is about to end searching.
- [func searchDisplayControllerDidEndSearch(UISearchDisplayController)](./searchdisplaycontrollerdidendsearch%28_%29.md)
  Tells the delegate that the controller has finished searching.
- [func searchDisplayController(UISearchDisplayController, didLoadSearchResultsTableView: UITableView)](./searchdisplaycontroller%28_,didloadsearchresultstableview%29.md)
  Tells the delegate that the controller has loaded its table view.
- [func searchDisplayController(UISearchDisplayController, willUnloadSearchResultsTableView: UITableView)](./searchdisplaycontroller%28_,willunloadsearchresultstableview%29.md)
  Tells the delegate that the controller is about to unload its table view.
- [func searchDisplayController(UISearchDisplayController, willShowSearchResultsTableView: UITableView)](./searchdisplaycontroller%28_,willshowsearchresultstableview%29.md)
  Tells the delegate that the controller is about to display its table view.
- [func searchDisplayController(UISearchDisplayController, didShowSearchResultsTableView: UITableView)](./searchdisplaycontroller%28_,didshowsearchresultstableview%29.md)
  Tells the delegate that the controller just displayed its table view.
- [func searchDisplayController(UISearchDisplayController, willHideSearchResultsTableView: UITableView)](./searchdisplaycontroller%28_,willhidesearchresultstableview%29.md)
  Tells the delegate that the controller is about to hide its table view.
- [func searchDisplayController(UISearchDisplayController, didHideSearchResultsTableView: UITableView)](./searchdisplaycontroller%28_,didhidesearchresultstableview%29.md)
  Tells the delegate that the controller just hid its table view.
- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearch: String?) -> Bool](./searchdisplaycontroller%28_,shouldreloadtableforsearch%29.md)
  Asks the delegate if the table view should be reloaded for a given search string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:))*