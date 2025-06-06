# searchBarCancelButtonClicked(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the cancel button was tapped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func searchBarCancelButtonClicked(_ searchBar: UISearchBar)
```

#### Discussion

Typically, you implement this method to dismiss the search bar.

## Parameters

- `searchBar`: The search bar that was tapped.

## See Also

- [var showsCancelButton: Bool](uisearchbar/showscancelbutton.md)
  A Boolean value indicating whether the cancel button is displayed.
- [func searchBarBookmarkButtonClicked(UISearchBar)](uisearchbardelegate/searchbarbookmarkbuttonclicked(_:).md)
  Tells the delegate that the bookmark button was tapped.
- [func searchBarSearchButtonClicked(UISearchBar)](uisearchbardelegate/searchbarsearchbuttonclicked(_:).md)
  Tells the delegate that the search button was tapped.
- [func searchBarResultsListButtonClicked(UISearchBar)](uisearchbardelegate/searchbarresultslistbuttonclicked(_:).md)
  Tells the delegate that the search results list button was tapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbardelegate/searchbarcancelbuttonclicked(_:))*