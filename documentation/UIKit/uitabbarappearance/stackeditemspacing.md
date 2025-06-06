# stackedItemSpacing

**Framework**: UIKit  
**Kind**: property

The amount of space to insert between stacked tab bar items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var stackedItemSpacing: CGFloat { get set }
```

#### Discussion

When the [`stackedItemPositioning`](uitabbarappearance/stackeditempositioning.md) property is set to [`UITabBar.ItemPositioning.centered`](uitabbar/itempositioning-swift.enum/centered.md), UIKit uses this property to determine how much space to insert between the items. The default value of this property is `0`, which causes UIKit to insert a system-defined default space between items. For any values above `0`, UIKit inserts the specified amount of space, measured in points, between the items. If you try to assign a negative number to this property, UIKit sets the value to `0` instead.

## See Also

- [var stackedLayoutAppearance: UITabBarItemAppearance](uitabbarappearance/stackedlayoutappearance.md)
  The appearance attributes for items with a stacked layout.
- [var stackedItemPositioning: UITabBar.ItemPositioning](uitabbarappearance/stackeditempositioning.md)
  The scheme to use when positioning stacked items within the tab bar.
- [var stackedItemWidth: CGFloat](uitabbarappearance/stackeditemwidth.md)
  The width of stacked items in the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarappearance/stackeditemspacing)*