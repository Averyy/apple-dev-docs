# selectedScopeButtonIndex

**Framework**: UIKit  
**Kind**: property

The index of the selected scope button.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectedScopeButtonIndex: Int { get set }
```

#### Discussion

The indexes of the scope buttons are determined by the indexes of the strings in [`scopeButtonTitles`](uisearchbar/scopebuttontitles.md).

## See Also

- [var scopeButtonTitles: [String]?](uisearchbar/scopebuttontitles.md)
  An array of strings indicating the titles of the scope buttons.
- [var showsScopeBar: Bool](uisearchbar/showsscopebar.md)
  Specifies whether the scope bar is displayed.
- [func setShowsScope(Bool, animated: Bool)](uisearchbar/setshowsscope(_:animated:).md)
  Specifies whether the scope bar is displayed, optionally using an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/selectedscopebuttonindex)*