# UITabBarItemStateAppearance

**Framework**: UIKit  
**Kind**: class

A data object containing the specific customizations for tab bar items in a particular state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITabBarItemStateAppearance
```

#### Overview

Use a [`UITabBarItemStateAppearance`](uitabbaritemstateappearance.md) object to customize the appearance of your tab bar items and the badges they display. Don’t create [`UITabBarItemStateAppearance`](uitabbaritemstateappearance.md) objects yourself. Instead, create a [`UITabBarItemAppearance`](uitabbaritemappearance.md) object and use its properties to fetch the appearance attributes for tab bar items in a particular state. For example, to set the attributes for items in the normal state, configure the object in the [`normal`](uitabbaritemappearance/normal.md) property.

## Topics

### Configuring the item’s title
- [var titleTextAttributes: [NSAttributedString.Key : Any]](uitabbaritemstateappearance/titletextattributes.md)
  String attributes to apply to the text of the tab bar item’s title.
- [var titlePositionAdjustment: UIOffset](uitabbaritemstateappearance/titlepositionadjustment.md)
  The additional amount by which to offset the title horizontally and vertically.
### Tinting the item’s icon
- [var iconColor: UIColor?](uitabbaritemstateappearance/iconcolor.md)
  The color of item icons.
### Configuring the badge appearance
- [var badgeTextAttributes: [NSAttributedString.Key : Any]](uitabbaritemstateappearance/badgetextattributes.md)
  String attributes to apply to the text of the item’s badge.
- [var badgeBackgroundColor: UIColor?](uitabbaritemstateappearance/badgebackgroundcolor.md)
  The background color of the badge.
- [var badgeTitlePositionAdjustment: UIOffset](uitabbaritemstateappearance/badgetitlepositionadjustment.md)
  The additional amount by which to offset the badge’s title horizontally and vertically.
- [var badgePositionAdjustment: UIOffset](uitabbaritemstateappearance/badgepositionadjustment.md)
  The additional amount by which to offset the badge horizontally and vertically.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UITabBarAppearance](uitabbarappearance.md)
  An object for customizing the appearance of a tab bar.
- [class UITabBarItemAppearance](uitabbaritemappearance.md)
  An object for customizing the appearance of tab bar items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbaritemstateappearance)*