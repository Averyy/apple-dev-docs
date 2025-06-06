# showsScopeBar

**Framework**: UIKit  
**Kind**: property

Specifies whether the scope bar is displayed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var showsScopeBar: Bool { get set }
```

#### Discussion

If the search bar is owned by a [`UISearchController`](uisearchcontroller.md), then setting this property implicitly sets the search controller’s [`automaticallyShowsScopeBar`](uisearchcontroller/automaticallyshowsscopebar.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var scopeButtonTitles: [String]?](uisearchbar/scopebuttontitles.md)
  An array of strings indicating the titles of the scope buttons.
- [var selectedScopeButtonIndex: Int](uisearchbar/selectedscopebuttonindex.md)
  The index of the selected scope button.
- [func setShowsScope(Bool, animated: Bool)](uisearchbar/setshowsscope(_:animated:).md)
  Specifies whether the scope bar is displayed, optionally using an animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchbar/showsscopebar)*