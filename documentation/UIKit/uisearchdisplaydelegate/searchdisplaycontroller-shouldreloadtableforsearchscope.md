# searchDisplayController(_:shouldReloadTableForSearchScope:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if the table view should be reloaded for a given scope.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearchScope searchOption: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the display controller should reload the data in its table view, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If you don’t implement this method, then the results table is reloaded as soon as the scope button selection changes.

You might implement this method if you want to perform an asynchronous search: you would initiate the search in this method, then return [`false`](https://developer.apple.com/documentation/swift/false), and reload the table when you have results.

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.
- `searchOption`: The index of the selected scope button in the search bar.

## See Also

- [var selectedScopeButtonIndex: Int](uisearchbar/selectedscopebuttonindex.md)
  The index of the selected scope button.
- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearch: String?) -> Bool](uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearch:).md)
  Asks the delegate if the table view should be reloaded for a given search string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:))*