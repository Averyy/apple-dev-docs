# searchBar(_:textDidChange:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user changed the search text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String)
```

#### Discussion

This method is also invoked when text is cleared from the search text field.

## Parameters

- `searchBar`: The search bar that is being edited.
- `searchText`: The current text in the search text field.

## See Also

- [func searchBar(UISearchBar, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](uisearchbardelegate/searchbar(_:shouldchangetextin:replacementtext:).md)
  Ask the delegate if text in a specified range should be replaced with given text.
- [func searchBarShouldBeginEditing(UISearchBar) -> Bool](uisearchbardelegate/searchbarshouldbeginediting(_:).md)
  Asks the delegate if editing should begin in the specified search bar.
- [func searchBarTextDidBeginEditing(UISearchBar)](uisearchbardelegate/searchbartextdidbeginediting(_:).md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](uisearchbardelegate/searchbarshouldendediting(_:).md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](uisearchbardelegate/searchbartextdidendediting(_:).md)
  Tells the delegate that the user finished editing the search text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:textdidchange:))*