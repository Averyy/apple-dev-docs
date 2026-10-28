# searchBarShouldBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if editing should begin in the specified search bar.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func searchBarShouldBeginEditing(_ searchBar: UISearchBar) -> Bool
```

```objc
- (BOOL) searchBarShouldBeginEditing:(UISearchBar *) searchBar;
```

## Return Value

[`true`](../../Swift/true.md) if an editing session should be initiated, otherwise, [`false`](../../Swift/false.md).

## Parameters

- `searchBar`: The search bar that is being edited.

## See Also

### Managing the search text
- [func searchBar(UISearchBar, textDidChange: String)](./searchbar%28_,textdidchange%29.md)
  Tells the delegate that the user changed the search text.
- [func searchBarTextDidBeginEditing(UISearchBar)](./searchbartextdidbeginediting%28_%29.md)
  Tells the delegate when the user begins editing the search text.
- [func searchBarShouldEndEditing(UISearchBar) -> Bool](./searchbarshouldendediting%28_%29.md)
  Asks the delegate if editing should stop in the specified search bar.
- [func searchBarTextDidEndEditing(UISearchBar)](./searchbartextdidendediting%28_%29.md)
  Tells the delegate that the user finished editing the search text.
- [func searchBar(UISearchBar, shouldChangeTextIn: NSRange, replacementText: String) -> Bool](./searchbar%28_,shouldchangetextin,replacementtext%29.md)
  Ask the delegate if text in a specified range should be replaced with given text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarshouldbeginediting(_:))*