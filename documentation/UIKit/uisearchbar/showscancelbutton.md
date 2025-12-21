# showsCancelButton

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the cancel button is displayed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsCancelButton: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the cancel button is displayed if the app is running on iPhone. The value of this property is ignored, and no cancel button is displayed, for apps running on iPad. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var showsBookmarkButton: Bool](uisearchbar/showsbookmarkbutton.md)
  A Boolean value indicating whether the bookmark button is displayed.
- [func setShowsCancelButton(Bool, animated: Bool)](uisearchbar/setshowscancelbutton(_:animated:).md)
  Sets the display state of the cancel button optionally with animation.
- [var showsSearchResultsButton: Bool](uisearchbar/showssearchresultsbutton.md)
  A Boolean value indicating whether the search results button is displayed.
- [var isSearchResultsButtonSelected: Bool](uisearchbar/issearchresultsbuttonselected.md)
  A Boolean value indicating whether the search results button is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/showscancelbutton)*