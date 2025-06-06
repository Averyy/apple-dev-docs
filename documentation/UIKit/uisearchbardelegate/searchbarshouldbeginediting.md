# searchBarShouldBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if editing should begin in the specified search bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func searchBarShouldBeginEditing(_ searchBar: UISearchBar) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if an editing session should be initiated, otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `searchBar`: The search bar that is being edited.

## See Also

- [func searchBar(UISearchBar, textDidChange: String)](uisearchbardelegate/searchbar(_:textdidchange:).md)
  Tells the delegate that the user changed the search text.
- [func searchBar(UISearchBar, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](uisearchbardelegate/searchbar(_:shouldchangetextin:replacementtext:).md)
  Ask the delegate if text in a specified range should be replaced with given text.
- [func searchBarTextDidBeginEditing(UISearchBar)](uisearchbardelegate/searchbartextdidbeginediting(_:).md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](uisearchbardelegate/searchbarshouldendediting(_:).md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](uisearchbardelegate/searchbartextdidendediting(_:).md)
  Tells the delegate that the user finished editing the search text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarshouldbeginediting(_:))*