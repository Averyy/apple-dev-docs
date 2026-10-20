# searchBarSearchButtonClicked(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the search button was tapped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func searchBarSearchButtonClicked(_ searchBar: UISearchBar)
```

```objc
- (void) searchBarSearchButtonClicked:(UISearchBar *) searchBar;
```

#### Discussion

You should implement this method to begin the search. Use the [`text`](../uisearchbar/text.md) property of the search bar to get the text. You can also send [`becomeFirstResponder()`](../uiresponder/becomefirstresponder%28%29.md) to the search bar to begin editing programmatically.

## Parameters

- `searchBar`: The search bar that was tapped.

## See Also

### Responding to clicks in search controls
- [func searchBarBookmarkButtonClicked(UISearchBar)](./searchbarbookmarkbuttonclicked%28_%29.md)
  Tells the delegate that the bookmark button was tapped.
- [func searchBarCancelButtonClicked(UISearchBar)](./searchbarcancelbuttonclicked%28_%29.md)
  Tells the delegate that the cancel button was tapped.
- [func searchBarResultsListButtonClicked(UISearchBar)](./searchbarresultslistbuttonclicked%28_%29.md)
  Tells the delegate that the search results list button was tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarsearchbuttonclicked(_:))*