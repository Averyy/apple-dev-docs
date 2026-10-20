# searchBar(_:textDidChange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user changed the search text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String)
```

```objc
- (void) searchBar:(UISearchBar *) searchBar textDidChange:(NSString *) searchText;
```

#### Discussion

This method is also invoked when text is cleared from the search text field.

## Parameters

- `searchBar`: The search bar that is being edited.
- `searchText`: The current text in the search text field.

## See Also

### Managing the search text
- [func searchBarShouldBeginEditing(UISearchBar) -> Bool](./searchbarshouldbeginediting%28_%29.md)
  Asks the delegate if editing should begin in the specified search bar.
- [func searchBarTextDidBeginEditing(UISearchBar)](./searchbartextdidbeginediting%28_%29.md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](./searchbarshouldendediting%28_%29.md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](./searchbartextdidendediting%28_%29.md)
  Tells the delegate that the user finished editing the search text.
- [func searchBar(UISearchBar, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./searchbar%28_,shouldchangetextin,replacementtext%29.md)
  Ask the delegate if text in a specified range should be replaced with given text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:textdidchange:))*