# stackedLayoutAppearance

**Framework**: UIKit  
**Kind**: property

The appearance attributes for items with a stacked layout.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var stackedLayoutAppearance: UITabBarItemAppearance { get set }
```

#### Discussion

If you didn’t provide a set of explicit attributes at initialization time, UIKit provides an object with default attributes.

## See Also

- [var stackedItemPositioning: UITabBar.ItemPositioning](uitabbarappearance/stackeditempositioning.md)
  The scheme to use when positioning stacked items within the tab bar.
- [var stackedItemSpacing: CGFloat](uitabbarappearance/stackeditemspacing.md)
  The amount of space to insert between stacked tab bar items.
- [var stackedItemWidth: CGFloat](uitabbarappearance/stackeditemwidth.md)
  The width of stacked items in the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarappearance/stackedlayoutappearance)*