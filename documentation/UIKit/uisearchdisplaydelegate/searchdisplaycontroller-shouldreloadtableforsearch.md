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
@MainActor
optional func searchDisplayController(_ controller: UISearchDisplayController, shouldReloadTableForSearch searchString: String?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the display controller should reload the data in its table view, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If you don’t implement this method, then the results table is reloaded as soon as the search string changes.

You might implement this method if you want to perform an asynchronous search. You would initiate the search in this method, then return [`false`](https://developer.apple.com/documentation/Swift/false). You would reload the table when you have results.

## Parameters

- `controller`: The search display controller for which the receiver is the delegate.
- `searchString`: The string in the search bar.

## See Also

- [func searchDisplayController(UISearchDisplayController, shouldReloadTableForSearchScope: Int) -> Bool](uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearchscope:).md)
  Asks the delegate if the table view should be reloaded for a given scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontroller(_:shouldreloadtableforsearch:))*