# searchBarCancelButtonClicked(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the cancel button was tapped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func searchBarCancelButtonClicked(_ searchBar: UISearchBar)
```

```objc
- (void) searchBarCancelButtonClicked:(UISearchBar *) searchBar;
```

## Discussion

Typically, you implement this method to dismiss the search bar.

## Parameters

- `searchBar`: The search bar that was tapped.

## See Also

### Related Documentation
- [var showsCancelButton: Bool](../uisearchbar/showscancelbutton.md)
  A Boolean value indicating whether the cancel button is displayed.
### Responding to clicks in search controls
- [func searchBarBookmarkButtonClicked(UISearchBar)](./searchbarbookmarkbuttonclicked%28_%29.md)
  Tells the delegate that the bookmark button was tapped.
- [func searchBarSearchButtonClicked(UISearchBar)](./searchbarsearchbuttonclicked%28_%29.md)
  Tells the delegate that the search button was tapped.
- [func searchBarResultsListButtonClicked(UISearchBar)](./searchbarresultslistbuttonclicked%28_%29.md)
  Tells the delegate that the search results list button was tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarcancelbuttonclicked(_:))*