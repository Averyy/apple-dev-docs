# searchBarResultsListButtonClicked(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the search results list button was tapped.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func searchBarResultsListButtonClicked(_ searchBar: UISearchBar)
```

```objc
- (void) searchBarResultsListButtonClicked:(UISearchBar *) searchBar;
```

## Parameters

- `searchBar`: The search bar that was tapped.

## See Also

### Responding to clicks in search controls
- [func searchBarBookmarkButtonClicked(UISearchBar)](./searchbarbookmarkbuttonclicked%28_%29.md)
  Tells the delegate that the bookmark button was tapped.
- [func searchBarCancelButtonClicked(UISearchBar)](./searchbarcancelbuttonclicked%28_%29.md)
  Tells the delegate that the cancel button was tapped.
- [func searchBarSearchButtonClicked(UISearchBar)](./searchbarsearchbuttonclicked%28_%29.md)
  Tells the delegate that the search button was tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarresultslistbuttonclicked(_:))*