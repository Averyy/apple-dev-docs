# setShowsCancelButton(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the display state of the cancel button optionally with animation.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setShowsCancelButton(_ showsCancelButton: Bool, animated: Bool)
```

#### Discussion

Cancel buttons are not displayed for apps running on iPad, even when you specify [`true`](https://developer.apple.com/documentation/Swift/true) for the `showsCancelButton` parameter

## Parameters

- `showsCancelButton`:   to display the cancel button, otherwise  .
- `animated`:   to use animation to change the display state of the cancel button, otherwise  .

## See Also

- [var showsBookmarkButton: Bool](uisearchbar/showsbookmarkbutton.md)
  A Boolean value indicating whether the bookmark button is displayed.
- [var showsCancelButton: Bool](uisearchbar/showscancelbutton.md)
  A Boolean value indicating whether the cancel button is displayed.
- [var showsSearchResultsButton: Bool](uisearchbar/showssearchresultsbutton.md)
  A Boolean value indicating whether the search results button is displayed.
- [var isSearchResultsButtonSelected: Bool](uisearchbar/issearchresultsbuttonselected.md)
  A Boolean value indicating whether the search results button is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/setshowscancelbutton(_:animated:))*