# UITabBarAppearance

**Framework**: UIKit  
**Kind**: class

An object for customizing the appearance of a tab bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITabBarAppearance
```

#### Overview

After creating a [`UITabBarAppearance`](uitabbarappearance.md) object, use the methods and properties of this class to specify the appearance of items in the tab bar. Use the inherited properties from [`UIBarAppearance`](uibarappearance.md) to configure the background and shadow attributes of the tab bar itself.

## Topics

### Configuring stacked item appearances
- [var stackedLayoutAppearance: UITabBarItemAppearance](uitabbarappearance/stackedlayoutappearance.md)
  The appearance attributes for items with a stacked layout.
- [var stackedItemPositioning: UITabBar.ItemPositioning](uitabbarappearance/stackeditempositioning.md)
  The scheme to use when positioning stacked items within the tab bar.
- [var stackedItemSpacing: CGFloat](uitabbarappearance/stackeditemspacing.md)
  The amount of space to insert between stacked tab bar items.
- [var stackedItemWidth: CGFloat](uitabbarappearance/stackeditemwidth.md)
  The width of stacked items in the tab bar.
### Configuring inline item appearances
- [var inlineLayoutAppearance: UITabBarItemAppearance](uitabbarappearance/inlinelayoutappearance.md)
  The appearance attributes for items displayed with an inline style.
- [var compactInlineLayoutAppearance: UITabBarItemAppearance](uitabbarappearance/compactinlinelayoutappearance.md)
  The appearance attributes for items displayed with an inline style in a compact environment.
### Specifying the selection appearance
- [var selectionIndicatorTintColor: UIColor?](uitabbarappearance/selectionindicatortintcolor.md)
  The tint color to apply to the selection indicator image.
- [var selectionIndicatorImage: UIImage?](uitabbarappearance/selectionindicatorimage.md)
  The image to draw for the selected item.

## Relationships

### Inherits From
- [UIBarAppearance](uibarappearance.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UITabBarItemAppearance](uitabbaritemappearance.md)
  An object for customizing the appearance of tab bar items.
- [class UITabBarItemStateAppearance](uitabbaritemstateappearance.md)
  A data object containing the specific customizations for tab bar items in a particular state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarappearance)*