# searchBar(_:shouldChangeTextIn:replacementText:)

**Framework**: UIKit  
**Kind**: method

Ask the delegate if text in a specified range should be replaced with given text.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func searchBar(_ searchBar: UISearchBar, shouldChangeTextIn range: NSRange, replacementText text: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if text in `range` should be replaced by `text`, otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `searchBar`: The search bar that is being edited.
- `range`: The range of the text to be changed.
- `text`: The text to replace existing text in  .

## See Also

- [func searchBar(UISearchBar, textDidChange: String)](uisearchbardelegate/searchbar(_:textdidchange:).md)
  Tells the delegate that the user changed the search text.
- [func searchBarShouldBeginEditing(UISearchBar) -> Bool](uisearchbardelegate/searchbarshouldbeginediting(_:).md)
  Asks the delegate if editing should begin in the specified search bar.
- [func searchBarTextDidBeginEditing(UISearchBar)](uisearchbardelegate/searchbartextdidbeginediting(_:).md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](uisearchbardelegate/searchbarshouldendediting(_:).md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](uisearchbardelegate/searchbartextdidendediting(_:).md)
  Tells the delegate that the user finished editing the search text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:shouldchangetextin:replacementtext:))*