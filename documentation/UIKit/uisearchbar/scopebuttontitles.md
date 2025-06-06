# scopeButtonTitles

**Framework**: UIKit  
**Kind**: property

An array of strings indicating the titles of the scope buttons.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scopeButtonTitles: [String]? { get set }
```

#### Discussion

The order of the strings in the array indicates the order that the corresponding buttons will be displayed, from left to right. The index in the array corresponds to the index used in [`selectedScopeButtonIndex`](uisearchbar/selectedscopebuttonindex.md).

## See Also

- [var selectedScopeButtonIndex: Int](uisearchbar/selectedscopebuttonindex.md)
  The index of the selected scope button.
- [var showsScopeBar: Bool](uisearchbar/showsscopebar.md)
  Specifies whether the scope bar is displayed.
- [func setShowsScope(Bool, animated: Bool)](uisearchbar/setshowsscope(_:animated:).md)
  Specifies whether the scope bar is displayed, optionally using an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/scopebuttontitles)*