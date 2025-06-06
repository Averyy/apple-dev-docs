# selectedChild

**Framework**: UIKit  
**Kind**: property

The currently selected tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
var selectedChild: UITab? { get set }
```

## See Also

- [var children: [UITab]](uitabgroup/children.md)
  The tabs within a tab group.
- [func tab(forIdentifier: String) -> UITab?](uitabgroup/tab(foridentifier:).md)
  Returns a tab with a matching identifier, if any.
- [var defaultChildIdentifier: String?](uitabgroup/defaultchildidentifier.md)
  The identifier for the default subitem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/selectedchild)*