# searchBarBookmarkButtonClicked(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the bookmark button was tapped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func searchBarBookmarkButtonClicked(_ searchBar: UISearchBar)
```

```objc
- (void) searchBarBookmarkButtonClicked:(UISearchBar *) searchBar;
```

## Discussion

There is no automatic bookmark support provided by the search bar. It’s the application’s responsibility to implement this method to perform some action if the bookmark button is tapped by the user.

## Parameters

- `searchBar`: The search bar that was tapped.

## See Also

### Related Documentation
- [var showsBookmarkButton: Bool](../uisearchbar/showsbookmarkbutton.md)
  A Boolean value indicating whether the bookmark button is displayed.
### Responding to clicks in search controls
- [func searchBarCancelButtonClicked(UISearchBar)](./searchbarcancelbuttonclicked%28_%29.md)
  Tells the delegate that the cancel button was tapped.
- [func searchBarSearchButtonClicked(UISearchBar)](./searchbarsearchbuttonclicked%28_%29.md)
  Tells the delegate that the search button was tapped.
- [func searchBarResultsListButtonClicked(UISearchBar)](./searchbarresultslistbuttonclicked%28_%29.md)
  Tells the delegate that the search results list button was tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarbookmarkbuttonclicked(_:))*