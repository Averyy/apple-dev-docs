# searchBar(_:shouldChangeTextIn:replacementText:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Ask the delegate if text in a specified range should be replaced with given text.

**Availability**:
- iOS 3.0+ - Deprecated in 27.0
- iPadOS 3.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
optional func searchBar(_ searchBar: UISearchBar, shouldChangeTextIn range: NSRange, replacementText text: String) -> Bool
```

```objc
- (BOOL) searchBar:(UISearchBar *) searchBar shouldChangeTextInRange:(NSRange) range replacementText:(NSString *) text;
```

#### Return Value

[`true`](../../Swift/true.md) if text in `range` should be replaced by `text`, otherwise, [`false`](../../Swift/false.md).

## Parameters

- `searchBar`: The search bar that is being edited.
- `range`: The range of the text to be changed.
- `text`: The text to replace existing text in `range`.

## See Also

### Managing the search text
- [func searchBar(UISearchBar, textDidChange: String)](./searchbar%28_,textdidchange%29.md)
  Tells the delegate that the user changed the search text.
- [func searchBarShouldBeginEditing(UISearchBar) -> Bool](./searchbarshouldbeginediting%28_%29.md)
  Asks the delegate if editing should begin in the specified search bar.
- [func searchBarTextDidBeginEditing(UISearchBar)](./searchbartextdidbeginediting%28_%29.md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](./searchbarshouldendediting%28_%29.md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](./searchbartextdidendediting%28_%29.md)
  Tells the delegate that the user finished editing the search text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbar(_:shouldchangetextin:replacementtext:))*