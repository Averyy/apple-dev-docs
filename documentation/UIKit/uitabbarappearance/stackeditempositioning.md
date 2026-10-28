# stackedItemPositioning

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The scheme to use when positioning stacked items within the tab bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var stackedItemPositioning: UITabBar.ItemPositioning { get set }
```

```objc
@property (nonatomic, assign, readwrite) UITabBarItemPositioning stackedItemPositioning;
```

## Discussion

Use this property to specify whether you want the items centered in the available space or distributed across the entire width of the tab bar.

## See Also

### Configuring stacked item appearances
- [var stackedLayoutAppearance: UITabBarItemAppearance](./stackedlayoutappearance.md)
  The appearance attributes for items with a stacked layout.
- [var stackedItemSpacing: CGFloat](./stackeditemspacing.md)
  The amount of space to insert between stacked tab bar items.
- [var stackedItemWidth: CGFloat](./stackeditemwidth.md)
  The width of stacked items in the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarappearance/stackeditempositioning)*